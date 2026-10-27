"""Module m1 calculations: adjacency matrix of the board graph, powers, walk
enumeration, and a brute-force check of the walk-counting theorem.
Pure Python (integers only). Run: python3 modules/m1_walks.py
"""
from itertools import product, combinations

def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]

def matpow(A, k):
    n = len(A)
    R = [[int(i == j) for j in range(n)] for i in range(n)]  # identity = A^0
    for _ in range(k):
        R = matmul(R, A)
    return R

def show(name, M):
    print(name)
    for row in M:
        print("  ", " ".join(str(x) for x in row))

def walks(A, k, i, j):
    """All vertex sequences (w0,...,wk) with w0=i, wk=j, A[w_{t-1}][w_t]=1."""
    n = len(A)
    out = []
    def go(seq):
        if len(seq) == k + 1:
            if seq[-1] == j:
                out.append(tuple(seq))
            return
        for nxt in range(n):
            if A[seq[-1]][nxt] == 1:
                go(seq + [nxt])
    go([i])
    return out

def is_path(seq):      # distinct vertices (course convention, Def. 1.2.13)
    return len(set(seq)) == len(seq)

def is_trail(seq):     # distinct edges (textbook Def. 1.2.12)
    edges = [frozenset(p) for p in zip(seq, seq[1:])]
    return len(set(edges)) == len(edges)

# ---- board matrix (vertices 1,2,3 -> indices 0,1,2) ----
A = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
n = len(A)
print("== Board matrix ==")
show("A", A)
print("symmetric:", all(A[i][j] == A[j][i] for i in range(n) for j in range(n)))
print("zero diagonal:", all(A[i][i] == 0 for i in range(n)))
print("row sums (degrees):", [sum(r) for r in A])
print("column sums:", [sum(A[i][j] for i in range(n)) for j in range(n)])
A2, A3 = matpow(A, 2), matpow(A, 3)
show("A^2", A2)
show("A^3", A3)
print("A^3 == 2*A:", A3 == [[2 * x for x in r] for r in A])
print("trace(A^2) =", sum(A2[i][i] for i in range(n)), " 2|E| =", sum(sum(r) for r in A))
print("diag(A^2) == degrees:", [A2[i][i] for i in range(n)] == [sum(r) for r in A])
for p in (4, 5):
    show(f"A^{p}", matpow(A, p))

print("\n== Explicit walks, labels 1..3 ==")
lab = lambda s: "-".join(str(v + 1) for v in s)
for k in (1, 2, 3):
    Ak = matpow(A, k)
    for i in range(n):
        for j in range(i, n):
            W = walks(A, k, i, j)
            assert len(W) == Ak[i][j], (k, i, j)
            if W:
                flags = [("path" if is_path(w) else "not-path") + "/" + ("trail" if is_trail(w) else "not-trail") for w in W]
                print(f"k={k} from {i+1} to {j+1}: entry={Ak[i][j]}  walks=" +
                      ", ".join(f"{lab(w)} [{f}]" for w, f in zip(W, flags)))

print("\n== Hand-checkable sums (induction step: sum over last-but-one vertex r) ==")
def step_terms(k, i, j):
    Akm1 = matpow(A, k - 1)
    terms = [(r + 1, Akm1[i][r], A[r][j], Akm1[i][r] * A[r][j]) for r in range(n)]
    print(f"(A^{k})_{i+1}{j+1} = sum_r (A^{k-1})_{i+1}r * A_r{j+1}:")
    for r, a, b, c in terms:
        print(f"   r={r}: {a} * {b} = {c}")
    print("   total =", sum(t[3] for t in terms), " (matrix says", matpow(A, k)[i][j], ")")
step_terms(2, 1, 1)   # (A^2)_22
step_terms(3, 0, 1)   # (A^3)_12
step_terms(2, 0, 0)   # (A^2)_11

print("\n== Walks vs paths from 1 to 2 and from 1 to 1 on the board graph ==")
for k in range(0, 6):
    Wk = walks(A, k, 0, 1)
    print(f"k={k}: walks 1->2 = {len(Wk)}, of which paths = {sum(is_path(w) for w in Wk)}, trails = {sum(is_trail(w) for w in Wk)}")
for k in range(1, 5):
    Wk = walks(A, k, 0, 0)
    print(f"k={k}: closed walks 1->1 = {len(Wk)}, of which paths = {sum(is_path(w) for w in Wk)}, trails = {sum(is_trail(w) for w in Wk)}")
# A^k symmetric and nonnegative on all powers up to 6
print("A^k symmetric for k=1..6:", all(matpow(A,k)==[list(r) for r in zip(*matpow(A,k))] for k in range(1,7)))
# odd/even pattern: A^(k+2) = 2 A^k for k>=1
print("A^(k+2) == 2*A^k for k=1..5:", all(matpow(A,k+2)==[[2*x for x in r] for r in matpow(A,k)] for k in range(1,6)))

# ---- brute-force check of the theorem on every simple graph with 2..5 vertices ----
print("\n== Brute-force check of (A^k)_ij = number of walks, all labelled simple graphs ==")
for N in range(2, 6):
    pairs = list(combinations(range(N), 2))
    checked = 0
    for bits in product((0, 1), repeat=len(pairs)):
        B = [[0] * N for _ in range(N)]
        for (a, b), x in zip(pairs, bits):
            B[a][b] = B[b][a] = x
        for k in range(1, 6 if N <= 4 else 4):
            P = matpow(B, k)
            for i in range(N):
                for j in range(N):
                    assert len(walks(B, k, i, j)) == P[i][j]
                    checked += 1
    print(f"N={N}: {2**len(pairs)} graphs, {checked} (k,i,j) entries all agree")
print("done")
