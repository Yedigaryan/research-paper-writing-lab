"""Worked-example numbers for the sections on walks and walk counting.

Pure Python integers. Run from the paper folder: python3 -I scripts/walks_check.py
Vertices are 1-based in every printout, as in the paper (n_1, ..., n_N).
Everything printed here is quoted in the paper: matrices, walk lists, the
classification of the example sequences, the path graph on four vertices,
and the brute-force check of the walk-counting theorem.
"""
from itertools import combinations


def adjacency(n, edges):
    A = [[0] * n for _ in range(n)]
    for i, j in edges:
        A[i - 1][j - 1] = A[j - 1][i - 1] = 1
    return A


def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def power(A, k):
    n = len(A)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mul(R, A)
    return R


def show(name, M):
    print(name + " =")
    for row in M:
        print("  " + " ".join(f"{v:2d}" for v in row))


def walks(A, i, j, k):
    """All vertex sequences of length k from i to j (1-based)."""
    n = len(A)
    out = []

    def rec(seq):
        if len(seq) == k + 1:
            if seq[-1] == j:
                out.append(tuple(seq))
            return
        for r in range(1, n + 1):
            if A[seq[-1] - 1][r - 1]:
                rec(seq + [r])

    rec([i])
    return out


def name(w):
    return " ".join(f"n{v}" for v in w)


def is_walk(seq, E):
    return all(frozenset(p) in E for p in zip(seq, seq[1:]))


def classify(seq, E):
    if not is_walk(seq, E):
        return "not a walk"
    es = [frozenset(p) for p in zip(seq, seq[1:])]
    closed = seq[0] == seq[-1]
    trail = len(set(es)) == len(es)
    path = len(set(seq)) == len(seq)
    cycle = closed and len(seq) >= 4 and len(set(seq[:-1])) == len(seq) - 1 and trail
    tags = ["walk", f"length {len(seq) - 1}"]
    if closed:
        tags.append("closed")
    if trail:
        tags.append("trail")
    if path:
        tags.append("path")
    if cycle:
        tags.append("cycle")
    return ", ".join(tags)


print("=" * 60)
print("Board graph P3: edges n1n2, n2n3")
P3 = adjacency(3, [(1, 2), (2, 3)])
for k in range(0, 5):
    show(f"A^{k}", power(P3, k))
print("Walks behind selected entries (entry; walks; how many have no repeated vertex)")
for (i, j, k) in [(1, 1, 2), (1, 3, 2), (1, 2, 2), (2, 2, 2), (1, 2, 3), (1, 1, 3), (2, 2, 4)]:
    ws = walks(P3, i, j, k)
    npath = sum(1 for w in ws if len(set(w)) == len(w))
    print(f"(A^{k})_{i}{j} = {power(P3, k)[i - 1][j - 1]}; walks: {'; '.join(name(w) for w in ws) or 'none'}; "
          f"with no repeated vertex: {npath}")
print("Induction step for (A^3)_12 = sum_r (A^2)_1r A_r2")
A2 = power(P3, 2)
tot = 0
for r in (1, 2, 3):
    t = A2[0][r - 1] * P3[r - 1][1]
    tot += t
    print(f"  r={r}: (A^2)_1{r}={A2[0][r - 1]}, A_{r}2={P3[r - 1][1]}, product {t}")
print("  total", tot, "; (A^3)_12 =", power(P3, 3)[0][1])
print("Row sums:", [sum(r) for r in P3], "diag(A^2):", [P3_ for P3_ in (A2[i][i] for i in range(3))],
      "sum of all entries:", sum(map(sum, P3)), "= 2|E| with |E| = 2")
print("Paths from n1 to n1 (all lengths): only the one-vertex path n1 (length 0)")
print("Distances from n1 (least k with (A^k)_1j > 0):",
      {j: next(k for k in range(0, 3) if power(P3, k)[0][j - 1] > 0) for j in (1, 2, 3)})

print("=" * 60)
print("Graph H of the definitions section: edges n1n2, n2n3, n1n3, n3n4, n4n5")
E_H = {frozenset(e) for e in [(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)]}
H = adjacency(5, [(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)])
show("A(H)", H)
print("row sums (degrees):", [sum(r) for r in H])
for seq in [(1, 2, 3, 4, 3, 1), (1, 4), (1, 2, 1), (1, 2, 3, 1), (3, 1, 2, 3, 4), (1, 2, 1, 3),
            (1, 3, 4, 5), (1, 2, 3, 4, 5), (2,), (1, 2, 3, 2, 1)]:
    print(f"{name(seq):22s} -> {classify(seq, E_H)}")
def cut(seq):
    """Remove the first closed block u_i ... u_j (u_i = u_j, i < j) until no vertex repeats."""
    seq = list(seq)
    steps = [tuple(seq)]
    while len(set(seq)) < len(seq):
        i, j = next((i, j) for i in range(len(seq)) for j in range(len(seq) - 1, i, -1) if seq[i] == seq[j])
        seq = seq[:i] + seq[j:]
        steps.append(tuple(seq))
    return steps


print("Cutting the walk n1 n2 n3 n4 n3 n1 (Lemma: every walk contains a path):")
for st in cut((1, 2, 3, 4, 3, 1)):
    print("  ", name(st))
print("Cutting the walk n1 n2 n3 n2 n1 :", " -> ".join(name(st) for st in cut((1, 2, 3, 2, 1))))
print("Cutting the walk n1 n2 n1 n2 n3 :", " -> ".join(name(st) for st in cut((1, 2, 1, 2, 3))))

print("=" * 60)
print("Path graph on four vertices: edges n1n2, n2n3, n3n4")
P4 = adjacency(4, [(1, 2), (2, 3), (3, 4)])
S = [[0] * 4 for _ in range(4)]
for k in (1, 2, 3):
    print(f"(A^{k})_14 = {power(P4, k)[0][3]}")
    S = [[S[i][j] + power(P4, k)[i][j] for j in range(4)] for i in range(4)]
    print(f"  entry (1,4) of A + ... + A^{k} = {S[0][3]}")

print("=" * 60)
print("Two triangles sharing n1: closed trail n1 n2 n3 n1 n4 n5 n1")
E_B = {frozenset(e) for e in [(1, 2), (2, 3), (1, 3), (1, 4), (4, 5), (1, 5)]}
print(classify((1, 2, 3, 1, 4, 5, 1), E_B))

print("=" * 60)
print("Brute-force check of the walk-counting theorem, k = 0..6")
graphs = {
    "P3": (3, [(1, 2), (2, 3)]),
    "K3": (3, [(1, 2), (2, 3), (1, 3)]),
    "C4": (4, [(1, 2), (2, 3), (3, 4), (1, 4)]),
    "K2+K1": (3, [(1, 2)]),
    "star K1,3": (4, [(1, 2), (1, 3), (1, 4)]),
    "H": (5, [(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)]),
}
for nm, (n, ed) in graphs.items():
    A = adjacency(n, ed)
    ok = all(power(A, k)[i - 1][j - 1] == len(walks(A, i, j, k))
             for k in range(0, 7) for i in range(1, n + 1) for j in range(1, n + 1))
    print(f"{nm}: matrix power equals walk count for all i, j, k = 0..6: {ok}")
# every labelled simple graph on 4 vertices, k = 0..5
total = bad = 0
pairs = list(combinations(range(1, 5), 2))
for mask in range(1 << len(pairs)):
    ed = [pairs[b] for b in range(len(pairs)) if mask >> b & 1]
    A = adjacency(4, ed)
    total += 1
    for k in range(0, 6):
        Pk = power(A, k)
        if any(Pk[i - 1][j - 1] != len(walks(A, i, j, k)) for i in range(1, 5) for j in range(1, 5)):
            bad += 1
            break
print(f"all {total} labelled simple graphs on 4 vertices, k = 0..5: graphs with a mismatch = {bad}")
