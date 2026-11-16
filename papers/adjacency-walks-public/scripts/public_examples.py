"""Numbers for the examples of the paper. Run: python3 -I scripts/public_examples.py"""
def adj(n, edges):
    A = [[0]*n for _ in range(n)]
    for i, j in edges:
        A[i-1][j-1] = A[j-1][i-1] = 1
    return A
def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r]*Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]
def powers(A, m):
    P = [A]
    for _ in range(m-1):
        P.append(mul(P[-1], A))
    return P
def add(Ms):
    n = len(Ms[0])
    return [[sum(M[i][j] for M in Ms) for j in range(n)] for i in range(n)]
for name, n, edges in [("G1 path v1v2v3", 3, [(1,2),(2,3)]),
                       ("G2 edge v1v2 + isolated v3", 3, [(1,2)]),
                       ("G3 path v1v2v3v4", 4, [(1,2),(2,3),(3,4)])]:
    P = powers(adj(n, edges), n-1 if n > 3 else 3)
    print(name)
    for k, M in enumerate(P, 1):
        print(" A^%d =" % k, M)
    print(" B =", add(P[:n-1]))
