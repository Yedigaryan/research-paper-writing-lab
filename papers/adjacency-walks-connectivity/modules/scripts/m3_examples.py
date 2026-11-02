"""Module m3: every matrix in the worked examples, computed with integer arithmetic.

Run:  python3 m3_examples.py
Pure Python, no third-party packages.
"""
from collections import deque


def mat_mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mat_pow(X, k):
    R = identity(len(X))
    for _ in range(k):
        R = mat_mul(R, X)
    return R


def mat_add(X, Y):
    return [[a + b for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def show(name, X):
    print(name)
    for row in X:
        print("   ", " ".join(f"{v:2d}" for v in row))


def bfs_order(A, s):
    """Breadth-first search from index s on the adjacency matrix; returns visit order."""
    n = len(A)
    discovered = [False] * n
    discovered[s] = True
    q = deque([s])
    order = [s]
    while q:
        v = q.popleft()
        for w in range(n):          # scan row v of A
            if A[v][w] == 1 and not discovered[w]:
                discovered[w] = True
                q.append(w)
                order.append(w)
    return order


def analyse(title, A):
    n = len(A)
    print("=" * 60)
    print(title)
    show("A", A)
    powers = {k: mat_pow(A, k) for k in range(1, n)}
    B = [[0] * n for _ in range(n)]
    for k in range(1, n):
        show(f"A^{k}", powers[k])
        B = mat_add(B, powers[k])
    show(f"B = A + ... + A^{n-1}", B)
    M = mat_pow(mat_add(identity(n), A), n - 1)
    show(f"(I + A)^{n-1}", M)
    off_pos = all(B[i][j] > 0 for i in range(n) for j in range(n) if i != j)
    all_pos = all(M[i][j] > 0 for i in range(n) for j in range(n))
    print("every off-diagonal entry of B positive:", off_pos)
    print("every entry of (I+A)^(N-1) positive:  ", all_pos)
    order = bfs_order(A, 0)
    print("BFS from n_1 visits (1-based):", [v + 1 for v in order],
          "-> all visited:", len(order) == n)
    # smallest k with (A^k)_ij > 0 for i != j  (equals distance when it exists)
    print("smallest k in 1..N-1 with (A^k)_ij > 0, per pair i<j:")
    for i in range(n):
        for j in range(i + 1, n):
            ks = [k for k in range(1, n) if powers[k][i][j] > 0]
            print(f"   (n_{i+1}, n_{j+1}):", ks[0] if ks else "none")
    return off_pos, all_pos, len(order) == n


# Connected example: the board matrix (edges n1n2 and n2n3).
A_conn = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
# Disconnected example: edge n1n2, vertex n3 isolated.
A_disc = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
# Extra: the board drawing's graph with the extra edge n1n3 (triangle).
A_tri = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

r1 = analyse("Example 1: connected (board matrix)", A_conn)
r2 = analyse("Example 2: disconnected (n3 isolated)", A_disc)
r3 = analyse("Extra: triangle (board drawing with the edge n1n3)", A_tri)
assert r1 == (True, True, True)
assert r2 == (False, False, False)
assert r3 == (True, True, True)

print("=" * 60)
print("Why the exponent N-1 is needed and the sum (or I+A) is needed")
A = A_conn
print("connected example, A alone: (A)_13 =", A[0][2], "so exponent 1 misses the pair n1,n3")
A2 = mat_pow(A, 2)
print("A^2 alone: (A^2)_12 =", A2[0][1], "so A^(N-1) alone misses the pair n1,n2 (parity)")
print("diagonal of A^2 =", [A2[i][i] for i in range(3)], "= degrees", [sum(r) for r in A])
