#!/usr/bin/env python3
"""
Test harness for mef_export.py.

Serializes synthetic models and checks the OUTPUT with an independent parser
(xml.etree, not the script's own validator), so the tests genuinely exercise
the serializer rather than trusting its self-checks. Run:

    python3 tests/test_mef_export.py

Exits 0 if all checks pass, 1 otherwise.
"""
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import mef_export as mef  # noqa: E402

NS = "http://www.opengroup.org/xsd/archimate/3.0/"
XSI = "http://www.w3.org/2001/XMLSchema-instance"
CANON_ORDER = ["name", "documentation", "elements", "relationships", "propertyDefinitions", "views"]

_results = []


def check(cond, msg):
    _results.append((bool(cond), msg))


def local(tag):
    return tag.split("}", 1)[1] if "}" in tag else tag


def parse(xml_text):
    return ET.fromstring(xml_text)


# --- a full-coverage synthetic model: every layer, all relationship types,
#     properties, provenance markers, and awkward characters.
FULL = {
    "name": "Synthetic Coverage Model <& \"test\">",
    "elements": [
        {"id": "g1", "name": "Grow revenue", "type": "Goal"},
        {"id": "d1", "name": "Market pressure & risk", "type": "Driver",
         "confidence": "confirmed", "source_reference": "para 1"},
        {"id": "cap1", "name": "Fulfilment", "type": "Capability"},
        {"id": "ba1", "name": "Sales Dept", "type": "BusinessActor"},
        {"id": "bp1", "name": "Order Processing", "type": "BusinessProcess",
         "temporal_perspective": "current", "properties": {"Owner": "Ops"}},
        {"id": "bs1", "name": "Ordering Service", "type": "BusinessService"},
        {"id": "bo1", "name": "Order", "type": "BusinessObject"},
        {"id": "ac1", "name": "Order Management System", "type": "ApplicationComponent"},
        {"id": "as1", "name": "Order API", "type": "ApplicationService"},
        {"id": "do1", "name": "Order Record", "type": "DataObject"},
        {"id": "nd1", "name": "App Server", "type": "Node"},
        {"id": "ss1", "name": "PostgreSQL", "type": "SystemSoftware"},
        {"id": "wp1", "name": "Migration Project", "type": "WorkPackage"},
        {"id": "pl1", "name": "To-Be 2027", "type": "Plateau"},
    ],
    "relationships": [
        {"id": "x1", "source": "d1", "target": "g1", "type": "Influence"},
        {"id": "x2", "source": "cap1", "target": "g1", "type": "Realization"},
        {"id": "x3", "source": "ba1", "target": "bp1", "type": "Assignment"},
        {"id": "x4", "source": "bp1", "target": "bs1", "type": "Realization"},
        {"id": "x5", "source": "bp1", "target": "bo1", "type": "Access"},
        {"id": "x6", "source": "ac1", "target": "bp1", "type": "Serving"},
        {"id": "x7", "source": "ac1", "target": "as1", "type": "Realization"},
        {"id": "x8", "source": "ac1", "target": "do1", "type": "Access"},
        {"id": "x9", "source": "nd1", "target": "ac1", "type": "Serving"},
        {"id": "x10", "source": "ss1", "target": "nd1", "type": "Association"},
        {"id": "x11", "source": "bo1", "target": "do1", "type": "Composition"},
        {"id": "x12", "source": "cap1", "target": "bp1", "type": "Aggregation"},
        {"id": "x13", "source": "bp1", "target": "bs1", "type": "Triggering"},
        {"id": "x14", "source": "do1", "target": "as1", "type": "Flow"},
        {"id": "x15", "source": "wp1", "target": "pl1", "type": "Specialization"},
    ],
}


def test_full_coverage():
    xml_text, flags, elem_rows, rel_rows, propdefs = mef.build(FULL)
    root = parse(xml_text)
    check(local(root.tag) == "model", "root element is <model>")

    # child order matches the canonical MEF sequence
    order = [local(c.tag) for c in root]
    positions = [CANON_ORDER.index(o) for o in order if o in CANON_ORDER]
    check(positions == sorted(positions), "model children in schema-required order: {}".format(order))

    elems = root.findall("{{{}}}elements/{{{}}}element".format(NS, NS))
    rels = root.findall("{{{}}}relationships/{{{}}}relationship".format(NS, NS))
    check(len(elems) == len(FULL["elements"]), "all {} elements serialized".format(len(FULL["elements"])))
    check(len(rels) == len(FULL["relationships"]), "all {} relationships serialized".format(len(FULL["relationships"])))

    # every element identifier unique; every xsi:type valid
    ids = [e.get("identifier") for e in elems]
    check(len(ids) == len(set(ids)), "element identifiers unique")
    bad_types = [e.get("{{{}}}type".format(XSI)) for e in elems
                 if e.get("{{{}}}type".format(XSI)) not in mef.ELEMENT_TYPES]
    check(not bad_types, "all element xsi:type values valid (bad: {})".format(bad_types))

    # every relationship endpoint resolves to a declared element; every type valid
    elem_id_set = set(ids)
    dangling = [(r.get("source"), r.get("target")) for r in rels
                if r.get("source") not in elem_id_set or r.get("target") not in elem_id_set]
    check(not dangling, "every relationship endpoint resolves (dangling: {})".format(dangling))
    bad_rel = [r.get("{{{}}}type".format(XSI)) for r in rels
               if r.get("{{{}}}type".format(XSI)) not in mef.RELATIONSHIP_TYPES]
    check(not bad_rel, "all relationship xsi:type values valid (bad: {})".format(bad_rel))

    # all 11 relationship types exercised at least once
    used = {r.get("{{{}}}type".format(XSI)) for r in rels}
    check(mef.RELATIONSHIP_TYPES <= used, "all relationship types exercised (missing: {})".format(
        mef.RELATIONSHIP_TYPES - used))

    # every propertyDefinitionRef resolves to a declared propertyDefinition
    declared = {pd.get("identifier") for pd in root.findall(
        "{{{}}}propertyDefinitions/{{{}}}propertyDefinition".format(NS, NS))}
    refs = [p.get("propertyDefinitionRef") for p in root.iter("{{{}}}property".format(NS))]
    unresolved = [r for r in refs if r not in declared]
    check(not unresolved, "all property refs resolve (unresolved: {})".format(unresolved))
    check(len(declared) == len(propdefs), "property definitions declared once each")

    check(not flags, "no flags on clean input (got: {})".format(flags))


def test_escaping_and_unicode():
    model = {"name": "M", "elements": [
        {"id": "a", "name": 'Tom & Jerry <b> "q" — café', "type": "Node",
         "documentation": "1 < 2 & 3 > 0"},
    ], "relationships": []}
    xml_text, *_ = mef.build(model)
    root = parse(xml_text)  # would raise if escaping were wrong
    name_el = root.find("{{{}}}elements/{{{}}}element/{{{}}}name".format(NS, NS, NS))
    check(name_el.text == 'Tom & Jerry <b> "q" — café',
          "special chars & unicode round-trip through escaping: {!r}".format(name_el.text))


def test_determinism():
    a, *_ = mef.build(FULL)
    b, *_ = mef.build(FULL)
    check(a == b, "same input -> byte-identical output")


def test_edge_cases():
    # empty model still well-formed with required containers
    xml_text, *_ = mef.build({"name": "Empty", "elements": [], "relationships": []})
    root = parse(xml_text)
    check(root.find("{{{}}}elements".format(NS)) is not None, "empty model has <elements>")
    check(root.find("{{{}}}relationships".format(NS)) is not None, "empty model has <relationships>")

    # unknown element type defaults + flags; dangling relationship dropped + flags
    model = {"name": "Edge", "elements": [
        {"id": "e1", "name": "Widget", "type": "Frobnicator"},
        {"id": "e2", "name": "Thing", "type": "Node"},
    ], "relationships": [
        {"id": "r1", "source": "e1", "target": "e2", "type": "Serving"},
        {"id": "r2", "source": "e2", "target": "ghost", "type": "Flow"},
    ]}
    xml_text, flags, elem_rows, rel_rows, propdefs = mef.build(model)
    root = parse(xml_text)
    types = [e.get("{{{}}}type".format(XSI)) for e in root.iter("{{{}}}element".format(NS))]
    check("ApplicationComponent" in types, "unknown type defaulted to ApplicationComponent")
    check(any("Frobnicator" in f for f in flags), "unknown type flagged")
    rels = root.findall("{{{}}}relationships/{{{}}}relationship".format(NS, NS))
    check(len(rels) == 1, "dangling relationship dropped (kept {} of 2)".format(len(rels)))
    check(any("ghost" in f for f in flags), "dangling relationship flagged")


def main():
    for fn in (test_full_coverage, test_escaping_and_unicode, test_determinism, test_edge_cases):
        fn()
    passed = sum(1 for ok, _ in _results if ok)
    for ok, msg in _results:
        print(("PASS  " if ok else "FAIL  ") + msg)
    print("\n{}/{} checks passed".format(passed, len(_results)))
    sys.exit(0 if passed == len(_results) else 1)


if __name__ == "__main__":
    main()
