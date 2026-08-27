#!/usr/bin/env python3
"""
drawio_export.py — deterministic Draw.io (diagrams.net) serializer.

Reads a structured model (JSON) and emits a valid .drawio (mxGraphModel) XML
file: one plain rectangle per element, one plain edge per relationship, placed
on a simple grid so every node is separable and the user can rearrange them.

There is deliberately NO semantic layout — a grid is the minimum that a diagram
format requires (Draw.io has no "unplaced" state; nodes need coordinates or they
stack at the origin). Grid-by-layer, swimlanes, and dependency-aware layout are
backlog, shared with the ArchiMate view layout.

Part of architect-exporter-drawio. Consumes the same neutral model contract as
the other serializers (elements + relationships with ids). Types are optional
here — Draw.io draws a box regardless of type.

Usage:
    python3 drawio_export.py INPUT.json [-o OUTPUT.drawio] [--name NAME]
    cat INPUT.json | python3 drawio_export.py - -o OUTPUT.drawio

Exit 0 on a valid diagram (flags to stderr); exit 1 on a fatal error.
"""
import sys
import json
import argparse
import hashlib
import math
from xml.sax.saxutils import quoteattr
from xml.dom import minidom

# grid geometry
W, H = 160, 60      # node width / height
GX, GY = 60, 60     # horizontal / vertical gap
MARGIN = 40         # top-left margin

NODE_STYLE = "rounded=0;whiteSpace=wrap;html=1;"
EDGE_STYLE = "endArrow=classic;html=1;rounded=0;"


def hash6(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:6]


def cell_id(prefix, key):
    return "{}-{}".format(prefix, hash6(prefix + ":" + str(key)))


def read_model(model):
    """Return (nodes, edges, flags). nodes: [(cell_id, name, type_or_None)]. edges: [(cell_id, src, tgt, label)]."""
    elements = model.get("elements") or []
    relationships = model.get("relationships") or []
    flags = []
    used = set()
    id_map = {}
    nodes = []
    for e in elements:
        in_id = str(e.get("id") if e.get("id") is not None else e.get("name"))
        name = e.get("name") or in_id
        cid = cell_id("node", in_id)
        while cid in used:
            cid += "x"
        used.add(cid)
        id_map[in_id] = cid
        typ = e.get("type") or e.get("archimate_type")
        nodes.append((cid, str(name), str(typ) if typ else None))

    edges = []
    for r in relationships:
        s_in = str(r.get("source") if r.get("source") is not None else r.get("source_element_id"))
        t_in = str(r.get("target") if r.get("target") is not None else r.get("target_element_id"))
        if s_in not in id_map or t_in not in id_map:
            flags.append("relationship {}: endpoint not found ({} -> {}) — skipped".format(
                r.get("id"), s_in, t_in))
            continue
        rid = cell_id("edge", str(r.get("id") if r.get("id") is not None else "{}-{}".format(s_in, t_in)))
        while rid in used:
            rid += "x"
        used.add(rid)
        label = (r.get("name") or r.get("label") or r.get("type")
                 or r.get("archimate_relationship_type") or "")
        edges.append((rid, id_map[s_in], id_map[t_in], str(label)))
    return nodes, edges, flags


def node_label(name, typ):
    """A «Type» stereotype line above the name when the element carries a type; just the name otherwise.

    The type string is rendered verbatim — no metamodel lookup — so any typed graph gets stereotypes and
    an untyped ("boxes and arrows") graph stays plain. The <br> is Draw.io's HTML line break (html=1)."""
    if typ:
        return "«{}»<br>{}".format(typ, name)
    return name


def assemble(name, nodes, edges):
    n = len(nodes)
    cols = max(1, int(math.ceil(math.sqrt(n)))) if n else 1
    o = ['<?xml version="1.0" encoding="UTF-8"?>\n']
    o.append('<mxfile host="app.diagrams.net">\n')
    o.append('  <diagram id={did} name={nm}>\n'.format(
        did=quoteattr("d-" + hash6(name or "model")), nm=quoteattr(name or "Model")))
    o.append('    <mxGraphModel dx="1000" dy="700" grid="1" gridSize="10" guides="1" '
             'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
             'pageWidth="1100" pageHeight="850" math="0" shadow="0">\n')
    o.append('      <root>\n')
    o.append('        <mxCell id="0" />\n')
    o.append('        <mxCell id="1" parent="0" />\n')
    for i, (cid, name, typ) in enumerate(nodes):
        col, row = i % cols, i // cols
        x = MARGIN + col * (W + GX)
        y = MARGIN + row * (H + GY)
        o.append('        <mxCell id={cid} value={v} style="{st}" vertex="1" parent="1">\n'.format(
            cid=quoteattr(cid), v=quoteattr(node_label(name, typ)), st=NODE_STYLE))
        o.append('          <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />\n'.format(
            x=x, y=y, w=W, h=H))
        o.append('        </mxCell>\n')
    for rid, s, t, label in edges:
        o.append('        <mxCell id={rid} value={v} style="{st}" edge="1" parent="1" '
                 'source={s} target={t}>\n'.format(
                     rid=quoteattr(rid), v=quoteattr(label), st=EDGE_STYLE,
                     s=quoteattr(s), t=quoteattr(t)))
        o.append('          <mxGeometry relative="1" as="geometry" />\n')
        o.append('        </mxCell>\n')
    o.append('      </root>\n')
    o.append('    </mxGraphModel>\n')
    o.append('  </diagram>\n')
    o.append('</mxfile>\n')
    return "".join(o)


def validate(xml_text, nodes, edges):
    errors = []
    try:
        minidom.parseString(xml_text)
    except Exception as ex:
        return ["output is not well-formed XML: {}".format(ex)]
    node_ids = {n[0] for n in nodes}
    for rid, s, t, _ in edges:
        if s not in node_ids:
            errors.append("edge {}: source {} is not a node".format(rid, s))
        if t not in node_ids:
            errors.append("edge {}: target {} is not a node".format(rid, t))
    seen = set()
    for i in [n[0] for n in nodes] + [e[0] for e in edges]:
        if i in seen:
            errors.append("duplicate cell id {}".format(i))
        seen.add(i)
    return errors


def build(model):
    nodes, edges, flags = read_model(model)
    xml_text = assemble(model.get("name") or (model.get("extraction_metadata") or {}).get("source_description"),
                        nodes, edges)
    return xml_text, flags, nodes, edges


def main():
    ap = argparse.ArgumentParser(description="Serialize a structured model to a Draw.io diagram.")
    ap.add_argument("input", help="input JSON file, or - for stdin")
    ap.add_argument("-o", "--output", help="output .drawio file (default: stdout)")
    ap.add_argument("--name", help="diagram name (overrides input)")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    try:
        model = json.loads(raw)
    except Exception as ex:
        sys.exit("FATAL: input is not valid JSON: {}".format(ex))
    if args.name:
        model["name"] = args.name

    xml_text, flags, nodes, edges = build(model)
    errors = validate(xml_text, nodes, edges)
    if errors:
        sys.stderr.write("VALIDATION FAILED:\n" + "\n".join("  - " + e for e in errors) + "\n")
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(xml_text)
        sys.stderr.write("Wrote {}\n".format(args.output))
    else:
        sys.stdout.write(xml_text)

    sys.stderr.write("OK: {} nodes, {} edges (grid layout).\n".format(len(nodes), len(edges)))
    for f in flags:
        sys.stderr.write("  flag: {}\n".format(f))


if __name__ == "__main__":
    main()
