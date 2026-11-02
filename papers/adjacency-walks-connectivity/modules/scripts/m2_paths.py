"""Module m2: checks of the walk / trail / path / cycle facts. Plain Python.
Run: python3 m2_paths.py"""
from itertools import combinations, product

def adj_from_edges(n, edges):
    A = [[0]*n for _ in range(n)]
    for a, b in edges:
        A[a-1][b-1] = A[b-1][a-1] = 1
    return A

def is_walk(A, s):
    return all(A[s[t-1]-1][s[t]-1] == 1 for t in range(1, len(s)))

def edges_of(s):
    return [frozenset((s[t-1], s[t])) for t in range(1, len(s))]

def is_trail(A, s):                      # book Def 1.2.12
    e = edges_of(s)
    return is_walk(A, s) and len(set(e)) == len(e)

def is_path(A, s):                       # book Def 1.2.13 = course "path"
    return is_walk(A, s) and len(set(s)) == len(s)

def is_closed(s):
    return s[0] == s[-1]

def is_simple_cycle(A, s):               # book Def 1.2.14 + 1.2.15
    return is_trail(A, s) and is_closed(s) and len(set(s[:-1])) == len(s) - 1 and len(set(s[1:])) == len(s) - 1

def cut(s):
    """One shortcut step from the proof of Lemma M2.1: remove the part between a repeated vertex."""
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return s[:i+1] + s[j+1:]
    return None

def reduce_to_path(s):
    while True:
        t = cut(s)
        if t is None:
            return s
        s = t

print("PART 1: textbook Fig. 1.2.5, graph G (edges read from the figure on printed p. 21)")
E = [(1,2),(1,3),(1,5),(2,3),(2,4),(3,4),(3,5),(4,5)]
A = adj_from_edges(5, E)
print("edges:", E)
checks = [
 ("walk   v1,v3,v2,v4,v3,v2,v4,v3,v5", (1,3,2,4,3,2,4,3,5), is_walk, True),
 ("walk?  v3,v1,v4,v2,v3,v5", (3,1,4,2,3,5), is_walk, False),
 ("trail  v1,v3,v2,v4,v3,v5", (1,3,2,4,3,5), is_trail, True),
 ("trail? v1,v3,v2,v4,v3,v2,v4,v3,v5", (1,3,2,4,3,2,4,3,5), is_trail, False),
 ("path   v1,v3,v4,v5", (1,3,4,5), is_path, True),
 ("path?  v1,v3,v2,v4,v3,v5", (1,3,2,4,3,5), is_path, False),
 ("simple cycle  v1,v3,v4,v2,v1", (1,3,4,2,1), lambda A,s: is_simple_cycle(A,s), True),
 ("simple cycle? v3,v2,v1,v3,v5,v4,v3", (3,2,1,3,5,4,3), lambda A,s: is_simple_cycle(A,s), False),
 ("closed trail  v3,v2,v1,v3,v5,v4,v3", (3,2,1,3,5,4,3), lambda A,s: is_trail(A,s) and is_closed(s), True),
]
for name, s, f, want in checks:
    got = f(A, s)
    print(f"{name:42s} length {len(s)-1}: {got} (expected {want})", "OK" if got == want else "MISMATCH")
used = set()
for s in [(1,3,2,4,3,2,4,3,5),(1,3,2,4,3,5),(1,3,4,5),(1,3,4,2,1),(3,2,1,3,5,4,3)]:
    used |= set(edges_of(s))
print("distinct edges used by the book's positive examples:", len(used), "of", len(E))
print("edges not used:", [tuple(sorted(e)) for e in map(frozenset, E) if e not in used])
w = (1,3,2,4,3,2,4,3,5)
print("cutting the walk", w, "->", reduce_to_path(w), "(a path from v1 to v5)")

print()
print("PART 2: board graph (edges 1-2, 2-3), all walks of length 2 and what they contain")
A3 = adj_from_edges(3, [(1,2),(2,3)])
for s in product([1,2,3], repeat=3):
    if is_walk(A3, s):
        print(s, "closed" if is_closed(s) else "open", "path" if is_path(A3, s) else "not a path",
              "-> reduces to", reduce_to_path(s))

print()
print("PART 3: exhaustive check on every labelled simple graph with N <= 5 vertices")
bad = 0; graphs = 0; pairs = 0; walks_checked = 0
for N in range(1, 6):
    allpairs = list(combinations(range(1, N+1), 2))
    for mask in range(1 << len(allpairs)):
        E_ = [allpairs[t] for t in range(len(allpairs)) if mask >> t & 1]
        A_ = adj_from_edges(N, E_)
        graphs += 1
        verts = range(1, N+1)
        # all walks up to length 6, grouped by endpoints
        best_walk = {}; best_trail = {}; best_path = {}
        frontier = [(v,) for v in verts]
        for L in range(0, 7):
            for s in frontier:
                key = (s[0], s[-1])
                best_walk.setdefault(key, L)
                if is_trail(A_, s): best_trail.setdefault(key, L)
                if is_path(A_, s):
                    best_path.setdefault(key, L)
                    if L > N - 1: bad += 1             # path length bound
                r = reduce_to_path(s)                  # Lemma M2.1
                walks_checked += 1
                if not (is_path(A_, r) and r[0] == s[0] and r[-1] == s[-1] and len(r)-1 <= L): bad += 1
            frontier = [s + (v,) for s in frontier for v in verts if A_[s[-1]-1][v-1]]
        for u in verts:
            for v in verts:
                pairs += 1
                a, b, c = ((u,v) in best_walk), ((u,v) in best_trail), ((u,v) in best_path)
                if not (a == b == c): bad += 1         # equivalence of three readings
                if a and not (best_walk[(u,v)] == best_trail[(u,v)] == best_path[(u,v)]): bad += 1  # distance
                if a and best_path[(u,v)] > N - 1: bad += 1
                # cycles in a simple graph have length >= 3
print("graphs:", graphs, "ordered vertex pairs:", pairs, "walks reduced:", walks_checked, "violations:", bad)

cyc_bad = 0
for N in range(1, 6):
    allpairs = list(combinations(range(1, N+1), 2))
    for mask in range(1 << len(allpairs)):
        A_ = adj_from_edges(N, [allpairs[t] for t in range(len(allpairs)) if mask >> t & 1])
        frontier = [(v,) for v in range(1, N+1)]
        for L in range(0, 6):
            for s in frontier:
                if L in (1, 2) and is_trail(A_, s) and is_closed(s): cyc_bad += 1
            frontier = [s + (v,) for s in frontier for v in range(1, N+1) if A_[s[-1]-1][v-1]]
print("closed trails of length 1 or 2 found in simple graphs (must be 0):", cyc_bad)
