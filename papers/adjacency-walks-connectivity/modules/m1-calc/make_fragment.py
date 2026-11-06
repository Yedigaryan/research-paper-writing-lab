import json, sys
paper = sys.argv[1]
ev = json.load(open(f"{paper}/evidence/evidence.json"))
claims = {c["id"]: c for c in ev["claims"]}
def sup(cid, idx=0):
    return dict(claims[cid]["support"][idx])
def sup_loc(cid, idx, loc):
    s = sup(cid, idx); s["locator"] = loc; return s
D = "modules/m1.md"
frag = {"sources": [], "contradictions": [], "claims": [
 {"id": "M1-1", "text": "Row i of A sums to the degree of n_i: the row sum counts the entries equal to 1 in row i, i.e. the vertices adjacent to n_i, i.e. the edges at n_i in a simple graph. Consequently the sum of all entries of A is 2|E|. Supersedes base claim C4.",
  "kind": "derived", "module": "m1",
  "support": [sup("C1"), sup_loc("C3", 0, "p. 16, Definition 1.2.1"), sup_loc("C3", 1, "p. 16, Theorem 1.2.1 (Euler)")],
  "derivation": D + ", section 5.1 (proof), script modules/m1-calc/m1_check.py (row sums checked on the board graph, a 4-vertex graph and 300 random graphs)",
  "confidence": "high", "status": "supported", "used_in": [], "contradicted_by": []},
 {"id": "M1-2", "text": "(A^2)_ii equals the degree of n_i, so it is positive for every non-isolated vertex, while no path (distinct vertices) of length 2 starts and ends at n_i. On the board graph (A^2)_11 = 1, (A^2)_22 = 2, (A^2)_33 = 1; the only length-2 closed walks are n1 n2 n1, n2 n1 n2, n2 n3 n2, n3 n2 n3. Supersedes base claim C7.",
  "kind": "derived", "module": "m1",
  "support": [sup("C7"), sup("C12")],
  "derivation": D + ", section 5.2 (proof and product), script modules/m1-calc/m1_check.py, output modules/m1-calc/m1_check.out",
  "confidence": "high", "status": "supported", "used_in": [], "contradicted_by": []},
 {"id": "M1-3", "text": "Walk counting for a simple graph: for k >= 1, (A^k)_ij is the number of walks of length k from n_i to n_j. The paper proves it by induction on k, with base case k = 1 and step (A^(k+1))_ij = sum_r (A^k)_ir A_rj, grouping walks by their last-but-one vertex n_r. The textbook contains no such theorem (C8).",
  "kind": "derived", "module": "m1",
  "support": [sup("C5", 0), sup("C5", 1), sup("C5", 2)],
  "derivation": D + ", section 5.3 (full induction proof); brute-force check in modules/m1-calc/m1_check.py (24255 entries, 0 failures)",
  "confidence": "high", "status": "supported", "used_in": [], "contradicted_by": []},
 {"id": "M1-4", "text": "A^k counts walks, not paths, off the diagonal as well: on the board graph (A^3)_12 = 2, counted by the walks n1 n2 n1 n2 and n1 n2 n3 n2, and neither is a path nor a trail, and no path of length 3 joins n1 to n2 because a path in a 3-vertex graph has length at most 2.",
  "kind": "derived", "module": "m1",
  "support": [sup("C6"), sup("C21")],
  "derivation": D + ", section 5.4, script modules/m1-calc/m1_check.py",
  "confidence": "high", "status": "supported", "used_in": [], "contradicted_by": []},
 {"id": "M1-5", "text": "Convention of this paper: a walk of length 0 (a single vertex) is allowed, so A^0 = I counts it and the theorem holds for k >= 0; the textbook is silent on length 0 and Grinberg allows it. This is the paper's own convention, not the textbook's.",
  "kind": "interpretation", "module": "m1",
  "support": [sup("C17", 0)],
  "derivation": None,
  "confidence": "medium", "status": "qualified", "used_in": [], "contradicted_by": []},
 {"id": "M1-6", "text": "A^k is symmetric for every k >= 0 when G is undirected: reversing a walk from n_i to n_j gives a walk from n_j to n_i of the same length, and this is a bijection. (Equivalently, the transpose of a product reverses the factors and A equals its transpose.)",
  "kind": "derived", "module": "m1",
  "support": [sup("C2", 0)],
  "derivation": D + ", section 5.5",
  "confidence": "high", "status": "supported", "used_in": [], "contradicted_by": []}
]}
json.dump(frag, open(f"{paper}/evidence/modules/m1.json", "w"), indent=2, ensure_ascii=False)
print("ok")
