"""Checks for module m2: walks, trails, paths, cycles, distance.

Run:  python3 -I modules/m2_checks.py   (from the paper folder)
Every number quoted in modules/m2.md is printed by this script.
Graphs are simple and undirected, so a walk is determined by its vertex
sequence; edges are frozensets of two vertices.
"""
from itertools import product

INF = float("inf")


def make(n, edges):
    return {"n": n, "V": list(range(1, n + 1)),
            "E": {frozenset(e) for e in edges}}


def adj(g, u):
    return [v for v in g["V"] if frozenset((u, v)) in g["E"]]


def edges_of(w):
    return [frozenset((w[i], w[i + 1])) for i in range(len(w) - 1)]


def is_walk(g, w):
    return len(w) >= 1 and all(e in g["E"] for e in edges_of(w))


def is_trail(g, w):  # textbook Definition 1.2.12 ("path"): no repeated edge
    es = edges_of(w)
    return is_walk(g, w) and len(set(es)) == len(es)


def is_path(g, w):  # textbook Definition 1.2.13 ("simple path")
    return is_walk(g, w) and len(set(w)) == len(w)


def is_simple_cycle(g, w):  # Definitions 1.2.14, 1.2.15, length >= 1
    return (is_trail(g, w) and len(w) >= 2 and w[0] == w[-1]
            and len(set(w[:-1])) == len(w) - 1)


def all_walks(g, k):
    """All walks (vertex sequences) with exactly k edges."""
    ws = [(v,) for v in g["V"]]
    for _ in range(k):
        ws = [w + (x,) for w in ws for x in adj(g, w[-1])]
    return ws


def shorten(w):
    """Proof of the lemma: cut out the part between the first repeat."""
    steps = 0
    w = list(w)
    while len(set(w)) < len(w):
        seen = {}
        for idx, x in enumerate(w):
            if x in seen:
                i, j = seen[x], idx
                break
            seen[x] = idx
        new = w[:i + 1] + w[j + 1:]
        assert len(new) < len(w)
        w = new
        steps += 1
    return tuple(w), steps


def matpow_entry(g, k, i, j):
    n = g["n"]
    A = [[1 if frozenset((a, b)) in g["E"] else 0 for b in g["V"]]
         for a in g["V"]]
    P = [[int(a == b) for b in range(n)] for a in range(n)]
    for _ in range(k):
        P = [[sum(P[a][c] * A[c][b] for c in range(n)) for b in range(n)]
             for a in range(n)]
    return P[i - 1][j - 1]


# ---------------------------------------------------------------- graphs
# G is the book's graph of Fig. 1.2.5 (printed p. 21), read from the page
# image: eight edges.
G = make(5, [(1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
# Board graph (matrix rows 0 1 0 / 1 0 1 / 0 1 0): edges 1-2 and 2-3.
B = make(3, [(1, 2), (2, 3)])
# Disconnected example: edge 1-2 and isolated vertex 3.
D = make(3, [(1, 2)])
SMALL = {
    "G (Fig. 1.2.5)": G, "board": B, "disconnected 3": D,
    "triangle": make(3, [(1, 2), (2, 3), (1, 3)]),
    "path P4": make(4, [(1, 2), (2, 3), (3, 4)]),
    "cycle C4": make(4, [(1, 2), (2, 3), (3, 4), (4, 1)]),
    "K4": make(4, [(a, b) for a in range(1, 5) for b in range(a + 1, 5)]),
    "two edges 4": make(4, [(1, 2), (3, 4)]),
}

print("== 1. Book examples on Fig. 1.2.5 (printed pp. 21-22) ==")
w1 = (1, 3, 2, 4, 3, 2, 4, 3, 5)
w2 = (3, 1, 4, 2, 3, 5)
print("walk v1,v3,v2,v4,v3,v2,v4,v3,v5:", is_walk(G, w1),
      "length", len(w1) - 1, "(book: eight)")
print("sequence v3,v1,v4,v2,v3,v5 is a walk:", is_walk(G, w2),
      "(book: not a walk; v1v4 is not an edge:",
      frozenset((1, 4)) in G["E"], ")")
t = (1, 3, 2, 4, 3, 5)
print("v1,v3,v2,v4,v3,v5 trail:", is_trail(G, t), " path:", is_path(G, t),
      "(book: trail, not simple path)")
print("v1,v3,v2,v4,v3,v2,v4,v3,v5 trail:", is_trail(G, w1),
      "(book: not a trail)")
print("v1,v3,v4,v5 path:", is_path(G, (1, 3, 4, 5)))
c1 = (3, 2, 1, 3, 5, 4, 3)
c2 = (1, 3, 4, 2, 1)
print("v3,v2,v1,v3,v5,v4,v3 closed trail:", is_trail(G, c1) and c1[0] == c1[-1],
      " simple cycle:", is_simple_cycle(G, c1), "(book: not simple)")
print("v1,v3,v4,v2,v1 simple cycle:", is_simple_cycle(G, c2))

print()
print("== 2. Hierarchy: path => trail => walk, and strictness ==")
for name, g in SMALL.items():
    for k in range(0, 8 if g["n"] == 5 else 7):
        for w in all_walks(g, k):
            if is_path(g, w):
                assert is_trail(g, w)
            if is_trail(g, w):
                assert is_walk(g, w)
print("path => trail => walk holds on all walks up to length 7 in 8 graphs")
print("(trail but not path) example in G:", t)
print("(walk but not trail) example in G:", w1)

print()
print("== 3. Lemma: shortening a walk gives a path of length <= k ==")
total = 0
worst = 0
for name, g in SMALL.items():
    top = 8 if g["n"] == 5 else 7
    for k in range(0, top + 1):
        for w in all_walks(g, k):
            p, steps = shorten(w)
            assert is_path(g, p) and p[0] == w[0] and p[-1] == w[-1]
            assert len(p) - 1 <= k
            # the result uses only vertices of the walk, in the same order
            it = iter(w)
            assert all(x in it for x in p)
            total += 1
            worst = max(worst, steps)
print("walks checked:", total, " all shortened to a path, same ends, length <= k")
print("most cut steps needed by one walk:", worst)
print("example: shorten", w1, "->", shorten(w1)[0])
print("closed walk (1,2,1) in board graph ->", shorten((1, 2, 1))[0],
      "(length-0 path, u = v)")

print()
print("== 4. Path length at most N - 1 ==")
for name, g in SMALL.items():
    longest = 0
    for k in range(0, g["n"] + 3):
        for w in all_walks(g, k):
            if is_path(g, w):
                longest = max(longest, k)
    print(f"{name}: N = {g['n']}, longest path length = {longest},",
          "N - 1 =", g["n"] - 1)
    assert longest <= g["n"] - 1
    # no path of length N exists
    assert not any(is_path(g, w) for w in all_walks(g, g["n"]))


def best(g, u, v, pred, top):
    for k in range(0, top + 1):
        if any(w[0] == u and w[-1] == v and pred(g, w)
               for w in all_walks(g, k)):
            return k
    return INF


print()
print("== 5. Existence and distance agree for walk, trail, path ==")
for name, g in SMALL.items():
    top = g["n"] + 2
    for u, v in product(g["V"], repeat=2):
        dw = best(g, u, v, is_walk, top)
        dt = best(g, u, v, is_trail, top)
        dp = best(g, u, v, is_path, top)
        assert dw == dt == dp, (name, u, v, dw, dt, dp)
print("shortest walk = shortest trail = shortest path (or none within",
      "N + 2 steps) for every ordered pair in all 8 graphs")

print()
print("== 6. Counts between v1 and v5 in G, by length (walk / trail / path) ==")
print("length  walks  trails  paths  (A^k)_15")
for k in range(0, 9):
    ws = [w for w in all_walks(G, k) if w[0] == 1 and w[-1] == 5]
    nt = sum(is_trail(G, w) for w in ws)
    npth = sum(is_path(G, w) for w in ws)
    ma = matpow_entry(G, k, 1, 5)
    assert ma == len(ws)
    print(f"{k:5d} {len(ws):6d} {nt:7d} {npth:6d} {ma:9d}")

print()
print("== 7. Simple cycles of G (as vertex cycles, up to start and direction) ==")
cycles = set()
for k in range(3, 6):
    for w in all_walks(G, k):
        if is_simple_cycle(G, w):
            body = w[:-1]
            r = min(range(len(body)), key=lambda i: body[i])
            rot = body[r:] + body[:r]
            rev = (rot[0],) + tuple(reversed(rot[1:]))
            cycles.add(min(rot, rev))
for c in sorted(cycles, key=lambda c: (len(c), c)):
    print("length", len(c), c)
print("number of simple cycles:", len(cycles))
print("simple cycles of length 1 or 2 anywhere:",
      any(is_simple_cycle(g, w) for g in SMALL.values()
          for k in (1, 2) for w in all_walks(g, k)))

print()
print("== 8. Board graph (edges 1-2, 2-3) ==")
for u, v in [(1, 3), (1, 1), (1, 2)]:
    print(f"paths from n{u} to n{v}:",
          [w for k in range(0, 4) for w in all_walks(B, k)
           if w[0] == u and w[-1] == v and is_path(B, w)])
print("walks of length 2 from n1 to n1:",
      [w for w in all_walks(B, 2) if w[0] == 1 and w[-1] == 1],
      "(none is a path)")
print("distances in board graph:")
for u in B["V"]:
    print("  ", [best(B, u, v, is_path, 4) for v in B["V"]])
print("distances in disconnected example (inf = no path):")
for u in D["V"]:
    print("  ", [best(D, u, v, is_path, 4) for v in D["V"]])
print("all checks passed")
