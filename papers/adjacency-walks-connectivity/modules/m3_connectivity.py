"""Module m3 calculations: the matrix connectivity test, its equivalent form,
the two three-vertex examples, sharpness of the bound N-1, an exhaustive
cross-check against breadth-first search, and operation counts for the cost
remark. Pure Python, integers only (no numpy needed).

Run from the paper folder:  python3 modules/m3_connectivity.py
Vertices are 1..N in the text and 0..N-1 in the code (index = vertex - 1).
"""
from itertools import combinations
from math import comb, ceil, log2
from collections import deque


# ---------------------------------------------------------------- matrices
def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)]
            for i in range(n)]


def matadd(X, Y):
    return [[x + y for x, y in zip(rx, ry)] for rx, ry in zip(X, Y)]


def matpow(A, k):
    R = identity(len(A))
    for _ in range(k):
        R = matmul(R, A)
    return R


def adjacency(n, edges):
    """edges: pairs of 1-based vertices; returns the adjacency matrix."""
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u - 1][v - 1] = A[v - 1][u - 1] = 1
    return A


def show(name, M):
    print(name)
    for row in M:
        print("   ", " ".join(f"{x:2d}" for x in row))


def power_sum(A, last):
    """A + A^2 + ... + A^last (zero matrix if last < 1)."""
    n = len(A)
    S = [[0] * n for _ in range(n)]
    P = identity(n)
    for _ in range(last):
        P = matmul(P, A)
        S = matadd(S, P)
    return S


# ------------------------------------------------------------------- tests
def offdiag_positive(M):
    n = len(M)
    return all(M[i][j] > 0 for i in range(n) for j in range(n) if i != j)


def test_sum(A):
    """Test (b): every off-diagonal entry of A + ... + A^(N-1) is positive."""
    return offdiag_positive(power_sum(A, len(A) - 1))


def test_binomial(A):
    """Test (c): every entry of (I + A)^(N-1) is positive."""
    n = len(A)
    M = matpow(matadd(identity(n), A), n - 1)
    return all(M[i][j] > 0 for i in range(n) for j in range(n))


def bfs_component(A, s):
    """Independent check: set of vertices reached from s by breadth-first search."""
    n = len(A)
    seen = {s}
    q = deque([s])
    while q:
        v = q.popleft()
        for w in range(n):
            if A[v][w] and w not in seen:
                seen.add(w)
                q.append(w)
    return seen


def bfs_connected(A):
    return len(bfs_component(A, 0)) == len(A)


def components(A):
    left, out = set(range(len(A))), []
    while left:
        c = bfs_component(A, min(left))
        out.append(sorted(v + 1 for v in c))
        left -= c
    return out


# ------------------------------------------------------------ the examples
def worked_example(title, n, edges):
    print("=" * 66)
    print(title, " N =", n, " edges:", edges)
    A = adjacency(n, edges)
    I = identity(n)
    A2 = matpow(A, 2)
    S = power_sum(A, n - 1)
    B = matpow(matadd(I, A), n - 1)
    show("A", A)
    show("A^2", A2)
    show("S = A + A^2   (N - 1 = %d)" % (n - 1), S)
    show("(I + A)^2     (N - 1 = %d)" % (n - 1), B)
    print("off-diagonal zeros of S      :",
          [(i + 1, j + 1) for i in range(n) for j in range(n)
           if i != j and S[i][j] == 0])
    print("zero entries of (I+A)^(N-1)  :",
          [(i + 1, j + 1) for i in range(n) for j in range(n) if B[i][j] == 0])
    print("sum test says connected      :", test_sum(A))
    print("(I+A)^(N-1) test says        :", test_binomial(A))
    print("BFS says connected           :", bfs_connected(A))
    print("components (BFS)             :", components(A))
    # binomial identity (I+A)^2 = I + 2A + A^2 checked entry by entry
    rhs = matadd(matadd(I, [[2 * x for x in r] for r in A]), A2)
    print("(I+A)^2 == I + 2A + A^2      :", B == rhs)
    return A, S, B


A_conn, S_conn, B_conn = worked_example(
    "EXAMPLE 1 (connected, the board matrix)", 3, [(1, 2), (2, 3)])
A_disc, S_disc, B_disc = worked_example(
    "EXAMPLE 2 (disconnected, edge 1-2 only)", 3, [(1, 2)])

# the same disconnected graph: higher powers never reach vertex 3
print("-" * 66)
print("Example 2, higher powers: column 3 of A^k for k = 1..6 is zero off the diagonal:",
      all(matpow(A_disc, k)[i][2] == 0 for k in range(1, 7) for i in (0, 1)))

# ---------------------------------------------- N = 2: why the diagonal is skipped
print("=" * 66)
print("N = 2, one edge 1-2 (connected): the sum is just A")
A_k2 = adjacency(2, [(1, 2)])
show("A = S", A_k2)
print("diagonal of S is zero although G is connected; off-diagonal entries are 1:",
      power_sum(A_k2, 1)[0][0] == 0 and offdiag_positive(power_sum(A_k2, 1)))
print("Connected graphs with 3 vertices: diagonal of S positive? path 1-2-3:",
      [S_conn[i][i] for i in range(3)])

# -------------------------------------------- sharpness: N-1 cannot be N-2
print("=" * 66)
print("Path graph 1-2-...-N: entry (1,N) of A^k first becomes nonzero at k = N-1")
print("   N | smallest k with (A^k)_{1N} > 0 | (1,N) of A+..+A^(N-2) | (1,N) of A+..+A^(N-1)")
for N in range(3, 9):
    A = adjacency(N, [(i, i + 1) for i in range(1, N)])
    first = next(k for k in range(1, N + 3) if matpow(A, k)[0][N - 1] > 0)
    s_short = power_sum(A, N - 2)[0][N - 1]
    s_full = power_sum(A, N - 1)[0][N - 1]
    print(f"  {N:2d} | {first:30d} | {s_short:22d} | {s_full:22d}")
    assert first == N - 1 and s_short == 0 and s_full > 0

print("-" * 66)
print("N = 4, path 1-2-3-4: A, A^2, A^3, A+A^2, A+A^2+A^3")
A4 = adjacency(4, [(1, 2), (2, 3), (3, 4)])
show("A", A4)
show("A^2", matpow(A4, 2))
show("A^3", matpow(A4, 3))
show("A + A^2  (N-2 powers: NOT enough)", power_sum(A4, 2))
show("A + A^2 + A^3  (N-1 powers: enough)", power_sum(A4, 3))
print("test with N-2 powers says connected:", offdiag_positive(power_sum(A4, 2)),
      "  test with N-1 powers says connected:", offdiag_positive(power_sum(A4, 3)))

# ------------------------------- exhaustive cross-check against BFS, N <= 6
print("=" * 66)
print("Exhaustive check over ALL labelled simple graphs, N = 2..6")
print("   N | graphs | connected | sum test = BFS | (I+A)^(N-1) test = BFS |"
      " S_ij>0 <=> same component | pattern of (I+A)^m for m = 2^t >= N-1 = BFS |"
      " N-2 powers wrong on")
for N in range(2, 7):
    pairs = list(combinations(range(N), 2))
    total = conn = ok_sum = ok_bin = ok_comp = ok_sq = short_wrong = 0
    for mask in range(1 << len(pairs)):
        A = [[0] * N for _ in range(N)]
        for b, (u, v) in enumerate(pairs):
            if mask >> b & 1:
                A[u][v] = A[v][u] = 1
        total += 1
        truth = bfs_connected(A)
        conn += truth
        S = power_sum(A, N - 1)
        ok_sum += (test_sum(A) == truth)
        ok_bin += (test_binomial(A) == truth)
        # corollary: off-diagonal S_ij > 0 iff same component
        same = all((S[i][j] > 0) == (j in bfs_component(A, i))
                   for i in range(N) for j in range(N) if i != j)
        ok_comp += same
        # repeated squaring: M = (I+A), square t times with 2^t >= N-1
        t = max(1, ceil(log2(N - 1))) if N > 2 else 1
        M = matadd(identity(N), A)
        for _ in range(t):
            M = matmul(M, M)
        ok_sq += ((all(x > 0 for r in M for x in r)) == truth)
        # sum with only N-2 powers: wrong on some connected graphs
        if offdiag_positive(power_sum(A, N - 2)) != truth:
            short_wrong += 1
    print(f"  {N:2d} | {total:6d} | {conn:9d} | {ok_sum:14d} | {ok_bin:22d} |"
          f" {ok_comp:26d} | {ok_sq:41d} | {short_wrong}")
    assert ok_sum == ok_bin == ok_comp == ok_sq == total

# ------------------------------------------------------------- cost counts
print("=" * 66)
print("Cost remark: scalar multiplications, schoolbook product of two N x N matrices = N^3")
print("   N | (I+A)^(N-1) by N-2 products | by repeated squaring | BFS row scans of A (N^2)")
for N in (10, 100, 1000):
    prods = N - 2
    t = ceil(log2(N - 1))
    print(f"{N:5d} | {prods * N**3:27,d} | {t * N**3:20,d} | {N * N:,d}")
    print(f"      number of squarings t = {t}, 2^t = {2**t} >= N-1 = {N-1}")

# entries grow fast: largest entry of A^(N-1) for the complete graph K_N
for N in (5, 10, 20):
    K = adjacency(N, [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)])
    top = max(max(r) for r in matpow(K, N - 1))
    print(f"complete graph K_{N}: largest entry of A^(N-1) = {top:,d}")
