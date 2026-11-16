"""Checks for module m2 (walks, trails, paths, cycles, distance).

Run: python3 -I modules/m2-check.py   (from the paper folder)
Pure standard library. Every number quoted in modules/m2.md is printed here.
Walks have length >= 0 (the paper's convention); a vertex sequence of length 0 is a walk.
"""
from itertools import combinations, product
from collections import deque


def edge(u, v):
    return frozenset((u, v))


def is_walk(seq, E):
    return len(seq) >= 1 and all(edge(a, b) in E for a, b in zip(seq, seq[1:]))


def edges_of(seq):
    return [edge(a, b) for a, b in zip(seq, seq[1:])]


def is_trail(seq, E):
    es = edges_of(seq)
    return is_walk(seq, E) and len(set(es)) == len(es)


def is_path(seq, E):  # course path = textbook simple path (Def 1.2.13)
    return is_walk(seq, E) and len(set(seq)) == len(seq)


def is_closed(seq, E):
    return is_walk(seq, E) and seq[0] == seq[-1]


def is_simple_cycle(seq, E):  # textbook Def 1.2.14 + 1.2.15, positive length
    if not (is_closed(seq, E) and is_trail(seq, E) and len(seq) >= 2):
        return False
    return len(set(seq[:-1])) == len(seq) - 1  # only first and last repeat


def walks_from(u, k, E, V):
    """All walks of length exactly k starting at u."""
    out = [(u,)]
    for _ in range(k):
        out = [w + (x,) for w in out for x in V if edge(w[-1], x) in E]
    return out


def reduce_to_path(seq):
    """The lemma's procedure: delete the block between the first repeated pair."""
    seq = list(seq)
    while True:
        pos = {}
        for idx, x in enumerate(seq):
            if x in pos:
                i, j = pos[x], idx
                seq = seq[: i + 1] + seq[j + 1:]
                break
            pos[x] = idx
        else:
            return tuple(seq)


def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def matpow(A, k):
    n = len(A)
    R = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = matmul(R, A)
    return R


def bfs_dist(u, E, V):
    d = {u: 0}
    q = deque([u])
    while q:
        x = q.popleft()
        for y in V:
            if edge(x, y) in E and y not in d:
                d[y] = d[x] + 1
                q.append(y)
    return d


def all_trails_from(u, E):
    """Lengths of all trails from u, as dict end vertex -> set of lengths."""
    res = {}

    def rec(x, used, length):
        res.setdefault(x, set()).add(length)
        for e in E:
            if e not in used and x in e:
                (y,) = tuple(e - {x})
                rec(y, used | {e}, length + 1)
    rec(u, frozenset(), 0)
    return res


print("=== 1. Board graph: n1-n2, n2-n3 (the matrix on the board) ===")
V = [1, 2, 3]
E = {edge(1, 2), edge(2, 3)}
A = [[int(edge(i, j) in E) for j in V] for i in V]
print("A =", A)
for k in range(0, 5):
    allw = [w for u in V for w in walks_from(u, k, E, V)]
    nt = sum(is_trail(w, E) for w in allw)
    npth = sum(is_path(w, E) for w in allw)
    ncl = sum(is_closed(w, E) for w in allw)
    cyc = sum(is_simple_cycle(w, E) for w in allw)
    Ak = matpow(A, k)
    ok = all(Ak[i - 1][j - 1] == sum(1 for w in walks_from(i, k, E, V) if w[-1] == j)
             for i in V for j in V)
    print(f"k={k}: walks={len(allw)} (sum of entries of A^{k} = {sum(map(sum, Ak))}), "
          f"closed={ncl}, trails={nt}, paths={npth}, simple cycles={cyc}, A^k matches enumeration={ok}")
print("walks n1 -> n1 of length 2:", [w for w in walks_from(1, 2, E, V) if w[-1] == 1])
print("walks n1 -> n3 of length 2:", [w for w in walks_from(1, 2, E, V) if w[-1] == 3])
print("paths n1 -> n3 (all lengths up to 4):",
      [w for k in range(5) for w in walks_from(1, k, E, V) if w[-1] == 3 and is_path(w, E)])
print("paths n1 -> n1 (all lengths up to 4):",
      [w for k in range(5) for w in walks_from(1, k, E, V) if w[-1] == 1 and is_path(w, E)])
print("distances from n1:", bfs_dist(1, E, V))
V4 = [1, 2, 3, 4]
print("distances from n1 after adding isolated n4:", bfs_dist(1, E, V4),
      "(n4 absent means infinity)")

print()
print("=== 2. Triangle T on n1,n2,n3 (the board drawing read literally) ===")
ET = {edge(1, 2), edge(2, 3), edge(1, 3)}
for s in [(1, 2, 3, 1), (1, 2, 1), (1, 2, 3, 2, 1), (1, 2, 3)]:
    print(s, "walk", is_walk(s, ET), "closed", is_closed(s, ET), "trail", is_trail(s, ET),
          "path", is_path(s, ET), "simple cycle", is_simple_cycle(s, ET))

print()
print("=== 3. Fig. 1.2.5 (printed p. 21): the seven edges the book's examples use ===")
EF = {edge(a, b) for a, b in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]}
book = {
    "walk, length 8: v1 v3 v2 v4 v3 v2 v4 v3 v5": (1, 3, 2, 4, 3, 2, 4, 3, 5),
    "not a walk: v3 v1 v4 v2 v3 v5": (3, 1, 4, 2, 3, 5),
    "trail: v1 v3 v2 v4 v3 v5": (1, 3, 2, 4, 3, 5),
    "simple path: v1 v3 v4 v5": (1, 3, 4, 5),
    "closed trail, not simple cycle: v3 v2 v1 v3 v5 v4 v3": (3, 2, 1, 3, 5, 4, 3),
    "simple cycle: v1 v3 v4 v2 v1": (1, 3, 4, 2, 1),
}
for name, s in book.items():
    print(f"{name}: walk={is_walk(s, EF)} length={len(s) - 1} closed={is_closed(s, EF)} "
          f"trail={is_trail(s, EF)} path(simple)={is_path(s, EF)} simple cycle={is_simple_cycle(s, EF)}")
print("reduction of the length-8 walk:", reduce_to_path((1, 3, 2, 4, 3, 2, 4, 3, 5)))

print()
print("=== 4. Closed trail that is not a simple cycle: two triangles sharing a vertex ===")
EB = {edge(a, b) for a, b in [(1, 2), (2, 3), (1, 3), (1, 4), (4, 5), (1, 5)]}
s = (1, 2, 3, 1, 4, 5, 1)
print(s, "closed trail", is_closed(s, EB) and is_trail(s, EB), "length", len(s) - 1,
      "simple cycle", is_simple_cycle(s, EB))

print()
print("=== 5. Exhaustive checks over all labelled simple graphs ===")


def all_graphs(n):
    pairs = list(combinations(range(1, n + 1), 2))
    for mask in range(1 << len(pairs)):
        yield [edge(*p) for i, p in enumerate(pairs) if mask >> i & 1]


for n, kmax in [(3, 8), (4, 7), (5, 5)]:
    Vn = list(range(1, n + 1))
    graphs = checked = 0
    bad_distinct = bad_lemma = bad_len = bad_dist = 0
    maxpath = 0
    for Eg in all_graphs(n):
        Eg = set(Eg)
        graphs += 1
        # (a) walk with distinct vertices has distinct edges (so it is a textbook simple path)
        # (b) lemma: reduce_to_path gives a path u->v, length <= k, edges among the walk's edges
        for u in Vn:
            for k in range(kmax + 1):
                for w in walks_from(u, k, Eg, Vn):
                    checked += 1
                    if len(set(w)) == len(w) and not is_trail(w, Eg):
                        bad_distinct += 1
                    p = reduce_to_path(w)
                    if not (is_path(p, Eg) and p[0] == w[0] and p[-1] == w[-1]
                            and len(p) - 1 <= k and set(edges_of(p)) <= set(edges_of(w))):
                        bad_lemma += 1
                    if is_path(w, Eg):
                        maxpath = max(maxpath, k)
                        if k > n - 1:
                            bad_len += 1
        # (c) distance: BFS = least trail length = least walk length = least path length
        for u in Vn:
            d = bfs_dist(u, Eg, Vn)
            tr = all_trails_from(u, Eg)
            for v in Vn:
                dt = min(tr[v]) if v in tr else None
                dw = None
                for k in range(0, n + 1):
                    if any(w[-1] == v for w in walks_from(u, k, Eg, Vn)):
                        dw = k
                        break
                dp = None
                for k in range(0, n):
                    if any(w[-1] == v and is_path(w, Eg) for w in walks_from(u, k, Eg, Vn)):
                        dp = k
                        break
                if not (d.get(v) == dt == dw == dp):
                    bad_dist += 1
    print(f"N={n}: graphs={graphs}, walks checked (length 0..{kmax})={checked}, "
          f"distinct-vertex walks with a repeated edge={bad_distinct}, "
          f"lemma failures={bad_lemma}, paths longer than N-1={bad_len}, "
          f"longest path length seen={maxpath}, distance disagreements={bad_dist}")
