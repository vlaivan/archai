#!/usr/bin/env python3
"""
Test harness for drawio_export.py.

Serializes synthetic models and checks the OUTPUT with an independent parser
(xml.etree), so it genuinely exercises the serializer. Run:

    python3 tests/test_drawio_export.py

Exits 0 if all checks pass, 1 otherwise.
"""
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import drawio_export as dio  # noqa: E402

_results = []


def check(cond, msg):
    _results.append((bool(cond), msg))


def cells(xml_text):
    root = ET.fromstring(xml_text)
    model = root.find("diagram/mxGraphModel/root")
    return root, model, model.findall("mxCell")


MODEL = {
    "name": "Diagram Test <& \"x\">",
    "elements": [
        {"id": "e{}".format(i), "name": "Element {} & <b>".format(i), "type": "Node"}
        for i in range(1, 10)
    ],
    "relationships": [
        {"id": "r1", "source": "e1", "target": "e2", "type": "Serving"},
        {"id": "r2", "source": "e2", "target": "e3", "type": "Flow", "name": "sends"},
        {"id": "r3", "source": "e3", "target": "ghost", "type": "Access"},  # dangling
    ],
}


def test_structure_and_counts():
    xml_text, flags, nodes, edges = dio.build(MODEL)
    root, model, cs = cells(xml_text)
    check(root.tag == "mxfile", "root element is <mxfile>")
    ids = [c.get("id") for c in cs]
    check("0" in ids and "1" in ids, "layer cells id 0 and 1 present")
    verts = [c for c in cs if c.get("vertex") == "1"]
    edgs = [c for c in cs if c.get("edge") == "1"]
    check(len(verts) == 9, "all 9 elements became nodes (got {})".format(len(verts)))
    check(len(edgs) == 2, "dangling edge dropped: 2 of 3 edges (got {})".format(len(edgs)))
    check(any("ghost" in f for f in flags), "dangling edge flagged")


def test_geometry_present():
    xml_text, *_ = dio.build(MODEL)
    _, _, cs = cells(xml_text)
    verts = [c for c in cs if c.get("vertex") == "1"]
    ok = True
    coords = []
    for v in verts:
        g = v.find("mxGeometry")
        if g is None or None in (g.get("x"), g.get("y"), g.get("width"), g.get("height")):
            ok = False
        else:
            coords.append((g.get("x"), g.get("y")))
    check(ok, "every node has mxGeometry with x/y/width/height")
    check(len(set(coords)) == len(coords), "no two nodes share the same position (grid spreads them)")


def test_edge_endpoints_resolve():
    xml_text, *_ = dio.build(MODEL)
    _, _, cs = cells(xml_text)
    vert_ids = {c.get("id") for c in cs if c.get("vertex") == "1"}
    edgs = [c for c in cs if c.get("edge") == "1"]
    bad = [(e.get("source"), e.get("target")) for e in edgs
           if e.get("source") not in vert_ids or e.get("target") not in vert_ids]
    check(not bad, "every edge source/target references a node (bad: {})".format(bad))
    allids = [c.get("id") for c in cs if c.get("id") not in ("0", "1")]
    check(len(allids) == len(set(allids)), "cell ids unique")


def test_escaping():
    xml_text, *_ = dio.build(MODEL)
    _, _, cs = cells(xml_text)  # parses — would raise on bad escaping
    v = next(c for c in cs if c.get("vertex") == "1")
    check("&" in v.get("value") and "<" in v.get("value"),
          "special chars survive escaping in node label: {!r}".format(v.get("value")))


def test_determinism():
    a, *_ = dio.build(MODEL)
    b, *_ = dio.build(MODEL)
    check(a == b, "same input -> byte-identical output")


def test_empty():
    xml_text, flags, nodes, edges = dio.build({"name": "Empty", "elements": [], "relationships": []})
    root, model, cs = cells(xml_text)  # still well-formed
    check(model is not None, "empty model still produces a valid mxGraphModel")


def test_stereotype():
    m = {"name": "S", "elements": [
        {"id": "t", "name": "Typed", "type": "ApplicationComponent"},
        {"id": "u", "name": "Untyped"},
    ], "relationships": []}
    xml_text, *_ = dio.build(m)
    _, _, cs = cells(xml_text)
    vals = [c.get("value") for c in cs if c.get("vertex") == "1"]
    typed = next(v for v in vals if "Typed" in v)
    untyped = next(v for v in vals if v == "Untyped" or v.endswith("Untyped"))
    check("«ApplicationComponent»" in typed,
          "typed element shows a «Type» stereotype: {!r}".format(typed))
    check("«" not in untyped and untyped == "Untyped",
          "untyped element stays a plain box (no stereotype): {!r}".format(untyped))


def main():
    for fn in (test_structure_and_counts, test_geometry_present, test_edge_endpoints_resolve, test_stereotype,
               test_escaping, test_determinism, test_empty):
        fn()
    passed = sum(1 for ok, _ in _results if ok)
    for ok, msg in _results:
        print(("PASS  " if ok else "FAIL  ") + msg)
    print("\n{}/{} checks passed".format(passed, len(_results)))
    sys.exit(0 if passed == len(_results) else 1)


if __name__ == "__main__":
    main()
