"""m2: matrices, sums, walk lists and the sum test for the worked examples.
Vertices are numbered 1..N as n_1..n_N. Run: python3 -I m2_connectivity_test.py"""
from itertools import product

def mm(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]

def madd(X, Y):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]

def powers(A, K):
    P = [A]
    for _ in range(K - 1):
        P.append(mm(P[-1], A))
    return P  # P[k-1] = A^k

def show(name, M):
    print(name)
    for r in M:
        print("  " + " ".join(f"{x:2d}" for x in r))

def walks(A, k, i, j):
    n = len(A)
    out = []
    for mid in product(range(n), repeat=k - 1):
        seq = (i,) + mid + (j,)
        if all(A[seq[t]][seq[t + 1]] for t in range(k)):
            out.append(seq)
    return out

def is_path(seq):
    return len(set(seq)) == len(seq)

def fmt(seq):
    return " ".join(f"n{v+1}" for v in seq)

def test(A, label):
    N = len(A)
    print("=" * 60); print(label, "N =", N)
    show("A", A)
    P = powers(A, N - 1)
    S = [[0] * N for _ in range(N)]
    for k, Pk in enumerate(P, 1):
        show(f"A^{k}", Pk)
        S = madd(S, Pk)
    show(f"S = A + ... + A^{N-1}", S)
    off = [(i + 1, j + 1, S[i][j]) for i in range(N) for j in range(N) if i != j]
    verdict = all(v > 0 for _, _, v in off)
    print("off-diagonal entries (i, j, S_ij):", off)
    print("test verdict: connected =", verdict)
    # brute-force cross-check: pairs joined by a path (a walk with no repeated vertex, any length 0..N-1)
    from_walks = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ok = any(is_path(w) for k in range(1, N) for w in walks(A, k, i, j))
            from_walks = from_walks and ok
    print("brute force (every pair joined by a path):", from_walks)
    assert verdict == from_walks
    # check S_ij equals the number of walks of length 1..N-1
    for i in range(N):
        for j in range(N):
            assert S[i][j] == sum(len(walks(A, k, i, j)) for k in range(1, N))
    print("check: each S_ij equals the number of walks of length 1..N-1 from n_i to n_j: ok")
    return P, S

board = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
P, S = test(board, "BOARD GRAPH (edges n1n2, n2n3)")
print("walks named:")
for (i, j, k) in [(1, 1, 2), (2, 2, 2), (1, 3, 2), (1, 2, 1), (1, 2, 2), (2, 3, 1), (1, 2, 3), (1, 1, 1)]:
    ws = walks(board, k, i - 1, j - 1)
    print(f"  (A^{k})_{i}{j} = {len(ws)}:", "; ".join(fmt(w) + (" [path]" if is_path(w) else " [not a path]") for w in ws) or "none")
A3 = mm(P[-1], board)
show("A^3 (board graph, not used by the test for N = 3)", A3)
print("S_22 = 2 counts walks:", "; ".join(fmt(w) for k in (1, 2) for w in walks(board, k, 1, 1)),
      "| paths from n2 to n2:", [fmt(w) for k in (0,) for w in [(1,)]])

disc = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
test(disc, "DISCONNECTED GRAPH (edge n1n2 only, n3 isolated)")
for (i, j) in [(1, 3), (2, 3)]:
    print(f"  walks n{i} to n{j} of length 1 or 2:", [fmt(w) for k in (1, 2) for w in walks(disc, k, i - 1, j - 1)])

# N9: path graph P4, S_12 counts walks, only one path joins n1 to n2
p4 = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
P4, S4 = test(p4, "PATH GRAPH on 4 vertices (edges n1n2, n2n3, n3n4)")
ws = [(k, w) for k in (1, 2, 3) for w in walks(p4, k, 0, 1)]
print("walks n1 to n2 of length 1..3:", [(k, fmt(w), "path" if is_path(w) else "not path") for k, w in ws])
# N = 2 and N = 3 single-power remark: A^(N-1) alone is not a test
print("single power: board A^2 entry (1,2) =", P[1][0][1], " while n1n2 is an edge (A_12 =", board[0][1], ")")

# O1 (optional): (I + A)^(N-1) on the board graph and the disconnected graph
def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
for name, A in (("board", board), ("disconnected", disc)):
    N = len(A); IA = madd(eye(N), A); R = eye(N)
    for _ in range(N - 1): R = mm(R, IA)
    show(f"(I + A)^{N-1}, {name} graph", R)
    print("  all entries positive:", all(x > 0 for r in R for x in r))
