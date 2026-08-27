#!/usr/bin/env python3
"""
mef_export.py — deterministic ArchiMate Model Exchange Format (MEF) serializer.

Reads a structured model (JSON) and emits valid ArchiMate 3.x MEF XML,
importable into Archi, BiZZdesign, and Sparx EA. Base model only: elements,
relationships, properties, and documentation — no views or layout.

Part of the architect-exporter-archimate skill. The MEF *encoding* lives here
(the serializer). The *metamodel* it encodes — what the element and
relationship types mean — is defined in architect-foundation-archimate.

INPUT CONTRACT — a neutral model, not any one producer's schema. See
`references/model-input.md`. In brief:

    {
      "name": "Model name",                 # optional
      "documentation": "...",               # optional
      "elements": [
        {"id": "E1", "name": "...", "type": "ApplicationComponent",
         "documentation": "...", "properties": {"Key": "Value"}}
      ],
      "relationships": [
        {"id": "R1", "source": "E1", "target": "E2", "type": "Serving",
         "name": "...", "documentation": "..."}
      ]
    }

The extractor's structured-output maps directly: element `archimate_type`,
`description`; relationship `source_element_id`, `target_element_id`,
`archimate_relationship_type` are accepted as aliases, and its `confidence`,
`temporal_perspective`, `source_reference` are carried through as properties.
Other producers are normalised onto this contract by the skill before the
script runs.

VALIDATION — the script always runs structural checks (well-formedness,
referential integrity, valid types, unique ids). When lxml is available AND a
MEF XSD is present (in ../schema/ or via --xsd), it additionally validates
against the official schema. The summary states which level ran; the schema is
not bundled (it is not redistributable and the host is offline for it) — drop
`archimate3_Model.xsd` into a `schema/` folder beside the skill to enable it.

Usage:
    python3 mef_export.py INPUT.json [-o OUTPUT.xml] [--name NAME] [--xsd PATH]
    cat INPUT.json | python3 mef_export.py - -o OUTPUT.xml

Exit 0 on a valid model (flags, if any, to stderr); exit 1 on a fatal error
(malformed input, failed structural check, or failed XSD validation).
"""
import sys
import os
import json
import argparse
import hashlib
import re
from xml.sax.saxutils import escape, quoteattr
from xml.dom import minidom

MEF_NS = "http://www.opengroup.org/xsd/archimate/3.0/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
SCHEMA_LOC = ("http://www.opengroup.org/xsd/archimate/3.0/ "
              "http://www.opengroup.org/xsd/archimate/3.1/archimate3_Model.xsd")

# --- The MEF xsi:type spellings: the serializer's own knowledge.
# The metamodel (what these types are) is defined in architect-foundation-archimate.
ELEMENT_TYPES = {
    "Stakeholder", "Driver", "Assessment", "Goal", "Outcome", "Principle",
    "Requirement", "Constraint", "Value", "Meaning",
    "Resource", "Capability", "ValueStream", "CourseOfAction",
    "BusinessActor", "BusinessRole", "BusinessCollaboration", "BusinessProcess",
    "BusinessFunction", "BusinessInteraction", "BusinessEvent", "BusinessService",
    "BusinessObject", "Contract", "Representation", "Product",
    "ApplicationComponent", "ApplicationCollaboration", "ApplicationFunction",
    "ApplicationInteraction", "ApplicationProcess", "ApplicationEvent",
    "ApplicationService", "DataObject",
    "Node", "Device", "SystemSoftware", "TechnologyCollaboration",
    "TechnologyFunction", "TechnologyProcess", "TechnologyService",
    "TechnologyInteraction", "TechnologyEvent", "Artifact",
    "CommunicationNetwork", "Path",
    "Equipment", "Facility", "DistributionNetwork", "Material",
    "WorkPackage", "Deliverable", "ImplementationEvent", "Plateau", "Gap",
    "Location", "Grouping", "Junction",
}
RELATIONSHIP_TYPES = {
    "Composition", "Aggregation", "Assignment", "Realization", "Serving",
    "Access", "Influence", "Association", "Triggering", "Flow", "Specialization",
}
REL_ALIASES = {"realisation": "Realization", "specialisation": "Specialization"}

ELEMENT_DEFAULT = "ApplicationComponent"
RELATIONSHIP_DEFAULT = "Association"

PROVENANCE = {  # extractor markers carried through as MEF properties
    "confidence": "Confidence",
    "temporal_perspective": "Temporal",
    "source_reference": "Source",
}


def _camel(raw):
    parts = re.split(r"[\s_\-]+", str(raw).strip())
    if len(parts) == 1:
        return parts[0]
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def norm_element_type(raw):
    if not raw:
        return ELEMENT_DEFAULT, True
    if str(raw).strip() in ELEMENT_TYPES:
        return str(raw).strip(), False
    c = _camel(raw)
    if c in ELEMENT_TYPES:
        return c, False
    return ELEMENT_DEFAULT, True


def norm_relationship_type(raw):
    if not raw:
        return RELATIONSHIP_DEFAULT, True
    s = str(raw).strip()
    key = s.lower().replace("relationship", "").strip()
    if key in REL_ALIASES:
        return REL_ALIASES[key], False
    c = _camel(s.replace("Relationship", "").replace("relationship", ""))
    c = c[:1].upper() + c[1:] if c else c
    if c in RELATIONSHIP_TYPES:
        return c, False
    return RELATIONSHIP_DEFAULT, True


def sanitise(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", str(s).strip().lower()).strip("-")
    return s[:30] or "x"


def hash4(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:4]


def mef_id(prefix, name, key):
    return "id-{p}-{n}-{h}".format(p=prefix, n=sanitise(name), h=hash4(prefix + ":" + str(key)))


def build(model):
    """Return (xml_text, flags, elem_rows, rel_rows, propdefs)."""
    elements = model.get("elements") or []
    relationships = model.get("relationships") or []
    meta = model.get("extraction_metadata") or {}
    flags = []
    used_ids = set()

    id_map = {}      # input element id -> MEF identifier
    elem_rows = []   # (mef_id, xsi_type, name, documentation, {prop_key: value})
    propdefs = {}    # property key -> propdef MEF identifier (insertion-ordered)

    for e in elements:
        in_id = str(e.get("id") if e.get("id") is not None else e.get("name"))
        name = e.get("name") or in_id
        raw_type = e.get("type") or e.get("archimate_type")
        etype, defaulted = norm_element_type(raw_type)
        if defaulted:
            flags.append("element {!r}: type {!r} not recognised -> {}".format(
                name, raw_type, ELEMENT_DEFAULT))
        mid = mef_id("elem", name, in_id)
        while mid in used_ids:
            mid += "x"
        used_ids.add(mid)
        id_map[in_id] = mid

        props = dict(e.get("properties") or {})
        for src_key, pretty in PROVENANCE.items():
            v = e.get(src_key)
            if v:
                props.setdefault(pretty, v)
        for k in props:
            propdefs.setdefault(k, None)
        elem_rows.append((mid, etype, name, e.get("documentation") or e.get("description"), props))

    for k in list(propdefs):
        propdefs[k] = mef_id("propdef", k, k)

    rel_rows = []  # (mef_id, xsi_type, source, target, name, documentation)
    for r in relationships:
        s_in = str(r.get("source") if r.get("source") is not None else r.get("source_element_id"))
        t_in = str(r.get("target") if r.get("target") is not None else r.get("target_element_id"))
        if s_in not in id_map or t_in not in id_map:
            flags.append("relationship {}: endpoint not found ({} -> {}) — skipped".format(
                r.get("id"), s_in, t_in))
            continue
        raw_rtype = r.get("type") or r.get("archimate_relationship_type")
        rtype, defaulted = norm_relationship_type(raw_rtype)
        if defaulted:
            flags.append("relationship {}: type {!r} not recognised -> {}".format(
                r.get("id"), raw_rtype, RELATIONSHIP_DEFAULT))
        rid = mef_id("rel", "{}-{}".format(s_in, t_in),
                     str(r.get("id") if r.get("id") is not None else "{}-{}".format(s_in, t_in)))
        while rid in used_ids:
            rid += "x"
        used_ids.add(rid)
        rel_rows.append((rid, rtype, id_map[s_in], id_map[t_in],
                         r.get("name") or r.get("label"), r.get("documentation") or r.get("description")))

    name = model.get("name") or meta.get("source_description") or "Exported Architecture Model"
    documentation = meta.get("source_description") if model.get("name") else None

    xml_text = assemble(name, documentation, elem_rows, rel_rows, propdefs)
    return xml_text, flags, elem_rows, rel_rows, propdefs


def _name(indent, text):
    return '{i}<name xml:lang="en">{t}</name>\n'.format(i=indent, t=escape(str(text)))


def assemble(name, documentation, elem_rows, rel_rows, propdefs):
    o = ['<?xml version="1.0" encoding="UTF-8"?>\n']
    o.append('<model xmlns={ns} xmlns:xsi={xsi} xsi:schemaLocation={loc} '
             'identifier={mid} version="1.1">\n'.format(
                 ns=quoteattr(MEF_NS), xsi=quoteattr(XSI_NS), loc=quoteattr(SCHEMA_LOC),
                 mid=quoteattr(mef_id("model", name, name))))
    o.append(_name("  ", name))
    if documentation:
        o.append('  <documentation xml:lang="en">{}</documentation>\n'.format(escape(str(documentation))))

    o.append("  <elements>\n")
    for mid, etype, ename, edoc, props in elem_rows:
        o.append('    <element identifier={i} xsi:type={t}>\n'.format(i=quoteattr(mid), t=quoteattr(etype)))
        o.append(_name("      ", ename))
        if edoc:
            o.append('      <documentation xml:lang="en">{}</documentation>\n'.format(escape(str(edoc))))
        if props:
            o.append("      <properties>\n")
            for k, v in props.items():
                o.append('        <property propertyDefinitionRef={r}>\n'.format(r=quoteattr(propdefs[k])))
                o.append('          <value xml:lang="en">{}</value>\n'.format(escape(str(v))))
                o.append("        </property>\n")
            o.append("      </properties>\n")
        o.append("    </element>\n")
    o.append("  </elements>\n")

    o.append("  <relationships>\n")
    for rid, rtype, s, t, rname, rdoc in rel_rows:
        o.append('    <relationship identifier={i} xsi:type={t} source={s} target={g}>\n'.format(
            i=quoteattr(rid), t=quoteattr(rtype), s=quoteattr(s), g=quoteattr(t)))
        if rname:
            o.append(_name("      ", rname))
        if rdoc:
            o.append('      <documentation xml:lang="en">{}</documentation>\n'.format(escape(str(rdoc))))
        o.append("    </relationship>\n")
    o.append("  </relationships>\n")

    if propdefs:
        o.append("  <propertyDefinitions>\n")
        for k, pid in propdefs.items():
            o.append('    <propertyDefinition identifier={i} type="string">\n'.format(i=quoteattr(pid)))
            o.append(_name("      ", k))
            o.append("    </propertyDefinition>\n")
        o.append("  </propertyDefinitions>\n")

    o.append("</model>\n")
    return "".join(o)


def validate_structural(xml_text, elem_rows, rel_rows, propdefs):
    """Always-on checks: well-formedness, referential integrity, valid types, unique ids."""
    errors = []
    try:
        minidom.parseString(xml_text)
    except Exception as ex:
        return ["output is not well-formed XML: {}".format(ex)]
    elem_ids = {r[0] for r in elem_rows}
    for rid, rtype, s, t, *_ in rel_rows:
        if s not in elem_ids:
            errors.append("relationship {}: source {} is not a declared element".format(rid, s))
        if t not in elem_ids:
            errors.append("relationship {}: target {} is not a declared element".format(rid, t))
    for mid, etype, *_ in elem_rows:
        if etype not in ELEMENT_TYPES:
            errors.append("element {}: invalid xsi:type {}".format(mid, etype))
    for rid, rtype, *_ in rel_rows:
        if rtype not in RELATIONSHIP_TYPES:
            errors.append("relationship {}: invalid xsi:type {}".format(rid, rtype))
    seen = set()
    for i in [r[0] for r in elem_rows] + [r[0] for r in rel_rows] + list(propdefs.values()):
        if i in seen:
            errors.append("duplicate identifier {}".format(i))
        seen.add(i)
    return errors


def find_xsd(explicit):
    if explicit:
        return explicit if os.path.isfile(explicit) else None
    schema_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "schema")
    if os.path.isdir(schema_dir):
        for preferred in ("archimate3_Model.xsd", "archimate3_Diagram.xsd"):
            p = os.path.join(schema_dir, preferred)
            if os.path.isfile(p):
                return p
        for fn in sorted(os.listdir(schema_dir)):
            if fn.endswith(".xsd"):
                return os.path.join(schema_dir, fn)
    return None


def validate_xsd(xml_text, xsd_path):
    """Authoritative XSD validation. Returns (ok_or_None, errors). ok=None means it could not run."""
    try:
        from lxml import etree
    except ImportError:
        return None, ["lxml not available"]
    try:
        schema = etree.XMLSchema(etree.parse(xsd_path))
        doc = etree.fromstring(xml_text.encode("utf-8"))
    except Exception as ex:
        return None, ["could not load/parse for XSD validation: {}".format(ex)]
    if schema.validate(doc):
        return True, []
    return False, [str(e) for e in schema.error_log]


def main():
    ap = argparse.ArgumentParser(description="Serialize a structured model to ArchiMate MEF XML.")
    ap.add_argument("input", help="input JSON file, or - for stdin")
    ap.add_argument("-o", "--output", help="output .xml file (default: stdout)")
    ap.add_argument("--name", help="model name (overrides input)")
    ap.add_argument("--xsd", help="path to a MEF XSD for authoritative validation")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    try:
        model = json.loads(raw)
    except Exception as ex:
        sys.exit("FATAL: input is not valid JSON: {}".format(ex))
    if args.name:
        model["name"] = args.name

    xml_text, flags, elem_rows, rel_rows, propdefs = build(model)

    errors = validate_structural(xml_text, elem_rows, rel_rows, propdefs)
    if errors:
        sys.stderr.write("STRUCTURAL VALIDATION FAILED:\n" + "\n".join("  - " + e for e in errors) + "\n")
        sys.exit(1)

    xsd_path = find_xsd(args.xsd)
    validation_level = "structural checks only (no XSD schema present)"
    if xsd_path:
        ok, xerrs = validate_xsd(xml_text, xsd_path)
        if ok is None:
            validation_level = "structural checks only ({})".format(xerrs[0])
        elif not ok:
            sys.stderr.write("XSD VALIDATION FAILED against {}:\n".format(xsd_path)
                             + "\n".join("  - " + e for e in xerrs[:20]) + "\n")
            sys.exit(1)
        else:
            validation_level = "schema-valid against {}".format(os.path.basename(xsd_path))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(xml_text)
        sys.stderr.write("Wrote {}\n".format(args.output))
    else:
        sys.stdout.write(xml_text)

    sys.stderr.write("OK: {} elements, {} relationships, {} property definitions — {}.\n".format(
        len(elem_rows), len(rel_rows), len(propdefs), validation_level))
    for f in flags:
        sys.stderr.write("  flag: {}\n".format(f))


if __name__ == "__main__":
    main()
