"""Module m1: matrix powers versus brute-force walk enumeration.
Plain Python, no libraries. Run: python3 m1_walks.py"""
from itertools import product

def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]

def power(A, k):
    n = len(A)
    R = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = matmul(R, A)
    return R

def walks(A, i, j, k):
    """All vertex sequences (i=u0,...,uk=j) with A[u_{t-1}][u_t]=1 (1-based names)."""
    n = len(A)
    out = []
    for mid in product(range(n), repeat=k - 1):
        seq = (i,) + mid + (j,)
        if all(A[seq[t - 1]][seq[t]] == 1 for t in range(1, k + 1)):
            out.append(tuple(v + 1 for v in seq))
    return out

def is_path(seq):
    return len(set(seq)) == len(seq)

def show(M):
    return "\n".join("  " + " ".join(str(x) for x in row) for row in M)

graphs = {
    "Board matrix (edges 1-2, 2-3)": [[0,1,0],[1,0,1],[0,1,0]],
    "Triangle (edges 1-2, 1-3, 2-3; what the drawing shows)": [[0,1,1],[1,0,1],[1,1,0]],
}
for name, A in graphs.items():
    n = len(A)
    print("=" * 60); print(name)
    print("A ="); print(show(A))
    print("symmetric:", all(A[i][j] == A[j][i] for i in range(n) for j in range(n)),
          "| zero diagonal:", all(A[i][i] == 0 for i in range(n)),
          "| row sums (degrees):", [sum(r) for r in A])
    for k in (1, 2, 3, 4):
        P = power(A, k)
        print(f"A^{k} ="); print(show(P))
        ok = all(P[i][j] == len(walks(A, i, j, k)) for i in range(n) for j in range(n))
        print(f"  entry == brute-force walk count for all i,j: {ok}")
    # walk lists for A^2 and A^3 entries
    for k in (2, 3):
        P = power(A, k)
        for i in range(n):
            for j in range(i, n):
                W = walks(A, i, j, k)
                paths = [w for w in W if is_path(w)]
                print(f"  k={k} (n{i+1},n{j+1}): count {P[i][j]}; walks {W}; of which paths {paths}")
    # symmetry and diagonal of A^2 = degrees
    P2 = power(A, 2)
    print("diag(A^2):", [P2[i][i] for i in range(n)], "degrees:", [sum(r) for r in A])
    print("A^2 symmetric:", all(P2[i][j] == P2[j][i] for i in range(n) for j in range(n)))
