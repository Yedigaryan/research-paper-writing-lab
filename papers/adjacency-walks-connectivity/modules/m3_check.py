"""m3 check: every matrix in module m3, plus an exhaustive test on small graphs.
Pure Python integers, no libraries beyond itertools. Run: python3 m3_check.py"""
from itertools import combinations, product
from math import comb

def mat(n, edges):
    A = [[0]*n for _ in range(n)]
    for i, j in edges:
        A[i-1][j-1] = A[j-1][i-1] = 1
    return A

def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r]*Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def power(A, k):
    P = ident(len(A))
    for _ in range(k):
        P = mul(P, A)
    return P

def add(X, Y):
    return [[a+b for a, b in zip(r, s)] for r, s in zip(X, Y)]

def S_sum(A):                      # A + A^2 + ... + A^(N-1)
    n = len(A)
    S = [[0]*n for _ in range(n)]
    for k in range(1, n):
        S = add(S, power(A, k))
    return S

def I_plus_A_pow(A):               # (I + A)^(N-1)
    return power(add(ident(len(A)), A), len(A)-1)

def walks(A, i, j, k):             # brute-force count of walks of length k, vertices 0-based
    n = len(A)
    def go(v, left):
        if left == 0:
            return int(v == j)
        return sum(go(w, left-1) for w in range(n) if A[v][w])
    return go(i, k)

def show(name, M):
    print(name)
    for r in M:
        print("  ", " ".join(str(x) for x in r))

def test_sum(A):
    n = len(A); S = S_sum(A)
    return all(S[i][j] > 0 for i in range(n) for j in range(n) if i != j)

def test_pow(A):
    return all(x > 0 for r in I_plus_A_pow(A) for x in r)

def connected_bfs(A):
    n = len(A); seen = {0}; queue = [0]
    while queue:
        v = queue.pop(0)
        for w in range(n):
            if A[v][w] and w not in seen:
                seen.add(w); queue.append(w)
    return len(seen) == n

def example(title, A):
    print("=" * 60); print(title)
    n = len(A)
    show("A", A)
    for k in range(2, n):
        show(f"A^{k}", power(A, k))
    show(f"S = A + ... + A^{n-1}", S_sum(A))
    show(f"(I+A)^{n-1}", I_plus_A_pow(A))
    print("sum test says connected:", test_sum(A), "| power test:", test_pow(A),
          "| BFS:", connected_bfs(A))
    # cross-check A^k against brute-force walk enumeration
    for k in range(1, n+2):
        P = power(A, k)
        assert all(P[i][j] == walks(A, i, j, k) for i in range(n) for j in range(n))
    print("A^k equals brute-force walk count for k = 1 ..", n+1)

example("Example 1, connected: edges n1n2, n2n3 (the board matrix)", mat(3, [(1, 2), (2, 3)]))
example("Example 2, disconnected: edge n1n2 only, n3 isolated", mat(3, [(1, 2)]))
example("Extra, the board drawing read as three edges: triangle", mat(3, [(1, 2), (2, 3), (1, 3)]))

print("=" * 60)
A = mat(3, [(1, 2), (2, 3)])
print("Counterexamples on the board graph")
B = add(A, power(A, 2)); print("B = A + A^2, B_22 =", B[1][1])
R = power(add(ident(3), A), 2); print("R = (I+A)^2, R_11 =", R[0][0])
print("(A^2)_11 =", power(A, 2)[0][0], " (A^2)_22 =", power(A, 2)[1][1])
print("A^(N-1) = A^2 alone: (A^2)_12 =", power(A, 2)[0][1], "although n1n2 is an edge")
print("(A^1)_13 =", A[0][2], " (A^2)_13 =", power(A, 2)[0][2], " -> both A and A^2 are needed")

print("=" * 60)
print("Diagonal of S carries no connectivity information")
K2 = mat(2, [(1, 2)]); print("K2 (connected): S =", S_sum(K2), " diagonal zero, still connected:", test_sum(K2))
print("board graph (connected) diagonal of S:", [S_sum(A)[i][i] for i in range(3)])
print("edge n1n2 + isolated n3 (disconnected) diagonal of S:", [S_sum(mat(3, [(1, 2)]))[i][i] for i in range(3)])

print("=" * 60)
print("Binomial identity check, (I+A)^(N-1) = sum_k C(N-1,k) A^k, board graph")
n = 3; T = [[0]*n for _ in range(n)]
for k in range(n):
    T = add(T, [[comb(n-1, k)*x for x in r] for r in power(A, k)])
print("equal:", T == I_plus_A_pow(A)); show("sum", T)

print("=" * 60)
print("Exhaustive check: all labelled simple graphs on N = 1..6 vertices")
for n in range(1, 7):
    pairs = list(combinations(range(1, n+1), 2))
    total = bad = conn = 0
    for bits in product([0, 1], repeat=len(pairs)):
        Ag = mat(n, [p for p, b in zip(pairs, bits) if b])
        c = connected_bfs(Ag)
        total += 1; conn += c
        if not (test_sum(Ag) == c == test_pow(Ag)):
            bad += 1
    print(f"N={n}: graphs={total}, connected={conn}, disagreements={bad}")
