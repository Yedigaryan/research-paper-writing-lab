"""Module m3: matrices for the connectivity test, and an exhaustive check.

Pure Python integers, no libraries. Run: python3 -I m3_connectivity.py
"""
from itertools import combinations
from math import comb


def mat_mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mat_add(X, Y):
    return [[a + b for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def mat_pow(X, k):
    R = identity(len(X))
    for _ in range(k):
        R = mat_mul(R, X)
    return R


def show(name, M):
    print(name + " =")
    for row in M:
        print("  " + " ".join(f"{v:2d}" for v in row))


def adjacency(n, edges):
    A = [[0] * n for _ in range(n)]
    for (i, j) in edges:  # 0-based vertex indices
        A[i][j] = A[j][i] = 1
    return A


def sum_powers(A, top):
    n = len(A)
    S = [[0] * n for _ in range(n)]
    for k in range(1, top + 1):
        S = mat_add(S, mat_pow(A, k))
    return S


def sum_test(A):
    n = len(A)
    S = sum_powers(A, n - 1)
    return all(S[i][j] > 0 for i in range(n) for j in range(n) if i != j)


def ipa_test(A):
    n = len(A)
    P = mat_pow(mat_add(identity(n), A), n - 1)
    return all(P[i][j] > 0 for i in range(n) for j in range(n))


def bfs_test(A):
    n = len(A)
    seen = {0}
    frontier = [0]
    while frontier:
        nxt = []
        for u in frontier:
            for v in range(n):
                if A[u][v] and v not in seen:
                    seen.add(v)
                    nxt.append(v)
        frontier = nxt
    return len(seen) == n


def example(title, edges, n=3):
    print("=" * 60)
    print(title, " edges (1-based):", [(i + 1, j + 1) for i, j in edges])
    A = adjacency(n, edges)
    show("A", A)
    for k in range(2, n):
        show(f"A^{k}", mat_pow(A, k))
    show("B = A + ... + A^(N-1)", sum_powers(A, n - 1))
    show("(I + A)^(N-1)", mat_pow(mat_add(identity(n), A), n - 1))
    print("sum test:", sum_test(A), " (I+A)^(N-1) test:", ipa_test(A), " BFS:", bfs_test(A))
    return A


# Connected: the board graph, edges n1n2 and n2n3.
example("Connected example (board matrix)", [(0, 1), (1, 2)])
# Disconnected: edge n1n2, vertex n3 isolated.
example("Disconnected example", [(0, 1)])
# Triangle, for the single-power remark and a second connected graph.
example("Triangle (extra)", [(0, 1), (1, 2), (0, 2)])

print("=" * 60)
print("Single power is not a test (path n1-n2-n3): A^2 entry (1,2) =",
      mat_pow(adjacency(3, [(0, 1), (1, 2)]), 2)[0][1], "although n1n2 is an edge")

# Binomial identity: (I+A)^(N-1) = sum_k C(N-1,k) A^k, checked on the path n1-n2-n3.
A = adjacency(3, [(0, 1), (1, 2)])
lhs = mat_pow(mat_add(identity(3), A), 2)
rhs = [[0] * 3 for _ in range(3)]
for k in range(0, 3):
    term = mat_pow(A, k)
    rhs = [[rhs[i][j] + comb(2, k) * term[i][j] for j in range(3)] for i in range(3)]
print("binomial identity holds on path n1-n2-n3:", lhs == rhs)

# Exhaustive check on all labelled simple graphs, N = 1..6.
print("=" * 60)
print("Exhaustive check: sum test == (I+A)^(N-1) test == BFS test")
for N in range(1, 7):
    pairs = list(combinations(range(N), 2))
    total = connected = bad = 0
    for mask in range(1 << len(pairs)):
        edges = [pairs[b] for b in range(len(pairs)) if mask >> b & 1]
        A = adjacency(N, edges)
        s, p, b = sum_test(A), ipa_test(A), bfs_test(A)
        total += 1
        connected += b
        if not (s == p == b):
            bad += 1
    print(f"N={N}: graphs={total}, connected={connected}, disagreements={bad}")
