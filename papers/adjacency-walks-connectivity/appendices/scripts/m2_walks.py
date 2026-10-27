#!/usr/bin/env python3
"""Module m2 checks: walks, trails, paths, cycles, distance, and the lemma
that every u-v walk contains a u-v path.

Run:  python3 modules/m2_walks.py > modules/m2_walks_output.txt
Pure standard library. Every number quoted in modules/m2.md comes from here.

Naming used in the code (textbook / English):
  walk                      Def 1.2.10   walk
  closed walk               Def 1.2.11   closed walk
  trail  (book: "path")     Def 1.2.12   distinct edges
  path   (book: "simple path") Def 1.2.13 distinct vertices
  cycle  (book: "cycle")    Def 1.2.14   closed trail
  simple cycle              Def 1.2.15   closed trail, only first = last vertex repeats
"""
import itertools
import random
from collections import deque


# ---------- graph helpers ------------------------------------------------
def make_graph(vertices, edges):
    """Simple undirected graph: edges are frozensets of two distinct vertices."""
    return {"V": list(vertices), "E": {frozenset(e) for e in edges}}


def adj(g):
    nb = {v: set() for v in g["V"]}
    for e in g["E"]:
        a, b = tuple(e)
        nb[a].add(b)
        nb[b].add(a)
    return nb


def edges_of(seq):
    return [frozenset((seq[i], seq[i + 1])) for i in range(len(seq) - 1)]


# ---------- the definitions, written exactly as stated -------------------
def is_walk(g, seq):                      # Def 1.2.10 (k >= 0)
    return len(seq) >= 1 and all(e in g["E"] for e in edges_of(seq))


def length(seq):                          # number of edges, with multiplicity
    return len(seq) - 1


def is_closed(seq):                       # Def 1.2.11
    return seq[0] == seq[-1]


def is_trail(g, seq):                     # Def 1.2.12 (textbook "path")
    es = edges_of(seq)
    return is_walk(g, seq) and len(set(es)) == len(es)


def is_path(g, seq):                      # Def 1.2.13 (textbook "simple path")
    return is_walk(g, seq) and len(set(seq)) == len(seq)


def is_cycle(g, seq):                     # Def 1.2.14 (closed trail)
    return is_trail(g, seq) and is_closed(seq)


def is_simple_cycle(g, seq):              # Def 1.2.15 (+ k >= 3 from C_n, n >= 3)
    return (is_cycle(g, seq) and length(seq) >= 3
            and len(set(seq[:-1])) == len(seq) - 1)


def classify(g, seq):
    tags = []
    if is_walk(g, seq):
        tags.append("walk")
        if is_closed(seq):
            tags.append("closed")
        if is_trail(g, seq):
            tags.append("trail=book-path")
        if is_path(g, seq):
            tags.append("path=book-simple-path")
        if is_cycle(g, seq) and length(seq) > 0:
            tags.append("book-cycle")
        if is_simple_cycle(g, seq):
            tags.append("simple-cycle")
    else:
        tags.append("NOT a walk")
    return tags


def all_walks(g, k):
    nb = adj(g)
    out = [(v,) for v in g["V"]]
    for _ in range(k):
        out = [w + (x,) for w in out for x in sorted(nb[w[-1]])]
    return out


# ---------- the lemma: cut out a loop ------------------------------------
def cut_once(seq):
    """Find the smallest i < j with seq[i] == seq[j] (smallest j for that i)
    and return seq[0..i] + seq[j+1..], as in Prop 2.9.5 / Lemma 1.2.1.
    Returns None if no vertex repeats."""
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j]:
                return seq[: i + 1] + seq[j + 1:], (i, j)
    return None


def reduce_to_path(seq, trace=None):
    while True:
        r = cut_once(seq)
        if r is None:
            return seq
        new, ij = r
        if trace is not None:
            trace.append((seq, ij, new))
        assert len(new) < len(seq)
        seq = new


def bfs_dist(g, s):
    nb = adj(g)
    d = {s: 0}
    q = deque([s])
    while q:
        x = q.popleft()
        for y in nb[x]:
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)
    return d


def mat_mult(X, Y):
    n = len(X)
    return [[sum(X[i][t] * Y[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]


def main():
    print("=== 1. Board graph B: V = {1,2,3}, E = {12, 23} (from the matrix) ===")
    B = make_graph([1, 2, 3], [(1, 2), (2, 3)])
    examples = [
        (1, 2, 3), (3, 2, 1), (1, 2, 1, 2, 3), (2, 1, 2), (2, 3, 2, 1, 2),
        (1, 2, 1), (2,), (1, 2), (1, 3), (1, 2, 3, 2),
    ]
    for s in examples:
        print(f"  {s!s:<16} length {length(s):<2} {', '.join(classify(B, s))}")

    print("\n  Walks by length in B (all start/end pairs), counted by enumeration:")
    for k in range(0, 5):
        ws = all_walks(B, k)
        n_trail = sum(is_trail(B, w) for w in ws)
        n_path = sum(is_path(B, w) for w in ws)
        print(f"   k={k}: walks={len(ws):<3} trails={n_trail:<3} paths={n_path:<3}"
              f" closed walks={sum(is_closed(w) for w in ws)}")

    print("\n  Walks from 1 to 3 of length <= 4 in B, with type:")
    for k in range(0, 5):
        for w in all_walks(B, k):
            if w[0] == 1 and w[-1] == 3:
                print(f"   {w!s:<18} length {k}  {', '.join(classify(B, w))}")

    print("\n  Check: B has no cycle (every closed walk of length 1..6 repeats an edge):")
    cyc = [w for k in range(1, 7) for w in all_walks(B, k) if is_cycle(B, w)]
    print("   cycles of positive length found:", cyc)

    print("\n  Consistency with m1 (A^k entry = number of walks); A =")
    A = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    P = [[int(i == j) for j in range(3)] for i in range(3)]
    ok = True
    for k in range(1, 6):
        P = mat_mult(P, A)
        ws = all_walks(B, k)
        for i in range(3):
            for j in range(3):
                cnt = sum(1 for w in ws if w[0] == i + 1 and w[-1] == j + 1)
                ok &= (cnt == P[i][j])
    print("   enumeration equals A^k for k=1..5, all i,j:", ok)

    print("\n=== 2. Triangle T (the board DRAWING): V={1,2,3}, E={12,13,23} ===")
    T = make_graph([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
    for s in [(1, 2, 3, 1), (1, 2, 1), (1, 2, 3), (1, 2, 3, 2, 1)]:
        print(f"  {s!s:<16} length {length(s):<2} {', '.join(classify(T, s))}")

    print("\n=== 3. Textbook example graph (edges forced by the textbook examples) ===")
    G = make_graph([1, 2, 3, 4, 5],
                   [(1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (1, 2), (4, 5)])
    tb = [
        (1, 3, 2, 4, 3, 2, 4, 3, 5),   # walk, not a trail (Def 1.2.10/1.2.12)
        (3, 1, 4, 2, 3, 5),            # not a walk (31? 14 not an edge here)
        (1, 3, 2, 4, 3, 5),            # trail (book "path"), not a path
        (1, 3, 4, 5),                  # simple path
        (3, 2, 1, 3, 5, 4, 3),         # book cycle, not simple
        (1, 3, 4, 2, 1),               # simple cycle
    ]
    for s in tb:
        print(f"  {s!s:<28} length {length(s):<2} {', '.join(classify(G, s))}")
    print("  (the second sequence is the textbook's 'v3,v1,v4,v2,v3,v5' on p. 22; it is a")
    print("   non-walk only if v1v4 is not an edge: the textbook says it is not a walk.)")

    print("\n=== 4. The lemma: trace on the textbook walk (Lemma 1.2.1) ===")
    s = (1, 3, 2, 4, 3, 2, 4, 3, 5)
    tr = []
    p = reduce_to_path(s, tr)
    for old, (i, j), new in tr:
        print(f"  {old}  (len {length(old)}): u_{i} = u_{j} = {old[i]}; cut -> {new} (len {length(new)})")
    print(f"  result {p}: path? {is_path(G, p)}; length {length(p)} <= {length(s)}")

    print("\n  Trace on a board-graph walk and a closed walk:")
    for s in [(1, 2, 1, 2, 3), (2, 1, 2), (1, 2, 3, 2, 1)]:
        tr = []
        p = reduce_to_path(s, tr)
        for old, (i, j), new in tr:
            print(f"   {old}: u_{i} = u_{j} = {old[i]}; cut -> {new}")
        print(f"   {s} -> {p}, path? {is_path(B, p)}, endpoints kept: "
              f"{p[0] == s[0] and p[-1] == s[-1]}, length {length(p)} <= {length(s)}")

    print("\n=== 5. Exhaustive and random checks of the claims ===")
    # 5a. lemma on all walks of length <= 6 in B, T, G
    for name, g in [("B", B), ("T", T), ("G", G)]:
        n = 0
        bad = 0
        for k in range(0, 7):
            for w in all_walks(g, k):
                p = reduce_to_path(w)
                n += 1
                good = (is_path(g, p) and p[0] == w[0] and p[-1] == w[-1]
                        and length(p) <= length(w)
                        and set(p) <= set(w))
                bad += (not good)
        print(f"  lemma on all walks of length 0..6 in {name}: {n} walks, failures {bad}")

    # 5b. random graphs: lemma, distinct vertices => distinct edges, path <= N-1,
    #     shortest walk = distance = shortest path = shortest trail
    random.seed(20261027)
    stats = dict(graphs=0, walks=0, lemma_fail=0, edge_fail=0, len_fail=0,
                 dist_fail=0, trail_fail=0)
    for _ in range(300):
        N = random.randint(2, 7)
        V = list(range(1, N + 1))
        E = [e for e in itertools.combinations(V, 2) if random.random() < 0.4]
        g = make_graph(V, E)
        stats["graphs"] += 1
        for k in range(0, 6):
            for w in all_walks(g, k):
                stats["walks"] += 1
                p = reduce_to_path(w)
                if not (is_path(g, p) and p[0] == w[0] and p[-1] == w[-1]
                        and length(p) <= length(w)):
                    stats["lemma_fail"] += 1
        # every path has distinct edges and length <= N-1
        for k in range(0, N + 1):
            for w in all_walks(g, k):
                if is_path(g, w):
                    if not is_trail(g, w):
                        stats["edge_fail"] += 1
                    if length(w) > N - 1:
                        stats["len_fail"] += 1
        # distance: shortest walk / trail / path lengths agree with BFS
        for s_ in V:
            d = bfs_dist(g, s_)
            for t_ in V:
                best = {"walk": None, "trail": None, "path": None}
                for k in range(0, N + 1):
                    for w in all_walks(g, k):
                        if w[0] == s_ and w[-1] == t_:
                            for nm, f in (("walk", is_walk), ("trail", is_trail),
                                          ("path", is_path)):
                                if best[nm] is None and f(g, w):
                                    best[nm] = k
                    if all(v is not None for v in best.values()):
                        break
                exp = d.get(t_)
                if not (best["walk"] == best["trail"] == best["path"] == exp):
                    stats["dist_fail"] += 1
    print("  random graphs (300 seeds, N=2..7):", stats)

    print("\n=== 6. Distance in B and in a disconnected graph D ===")
    for s_ in B["V"]:
        d = bfs_dist(B, s_)
        print(f"  B: d({s_}, .) =", {t: d.get(t, float('inf')) for t in B["V"]})
    D = make_graph([1, 2, 3], [(1, 2)])
    for s_ in D["V"]:
        d = bfs_dist(D, s_)
        print(f"  D (only edge 12): d({s_}, .) =", {t: d.get(t, float('inf')) for t in D["V"]})

    print("\n=== 7. Path length bound: B has N=3, so a path has at most 2 edges ===")
    longest = max(length(w) for k in range(0, 6) for w in all_walks(B, k) if is_path(B, w))
    print("  longest path in B has", longest, "edges; N-1 =", len(B["V"]) - 1)


if __name__ == "__main__":
    main()
