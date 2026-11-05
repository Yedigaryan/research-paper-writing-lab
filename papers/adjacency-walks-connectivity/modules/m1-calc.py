"""Module m1 calculations: powers of A and brute-force walk counts (pure Python, exact integers)."""
import itertools, random

def mul(X, Y):
    n = len(X)
    return [[sum(X[i][t] * Y[t][j] for t in range(n)) for j in range(n)] for i in range(n)]

def power(A, k):
    n = len(A)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mul(R, A)
    return R

def walks(A, k, i, j):
    """Count sequences (u0..uk), u0=i, uk=j, A[u_{t-1}][u_t]=1, by direct enumeration."""
    n = len(A)
    c = 0
    for mid in itertools.product(range(n), repeat=max(k - 1, 0)):
        seq = (i,) + mid + (j,) if k >= 1 else (i,)
        if k == 0:
            c += 1 if i == j else 0
            break
        if all(A[seq[t]][seq[t + 1]] == 1 for t in range(k)):
            c += 1
    return c

def show(name, M):
    print(name)
    for r in M:
        print("  ", r)

board = [[0,1,0],[1,0,1],[0,1,0]]       # board matrix: edges n1n2, n2n3
tri   = [[0,1,1],[1,0,1],[1,1,0]]       # triangle (drawing's three edges)
for nm, A in (("board path graph", board), ("triangle", tri)):
    print("==", nm)
    print("symmetric:", all(A[i][j] == A[j][i] for i in range(3) for j in range(3)),
          " zero diagonal:", all(A[i][i] == 0 for i in range(3)),
          " row sums (degrees):", [sum(r) for r in A])
    for k in (0, 1, 2, 3, 4):
        show(f"A^{k}", power(A, k))
    print("A^2 diagonal equals degrees:", [power(A,2)[i][i] for i in range(3)])

# Brute-force check of the theorem on the two graphs and on random simple graphs
ok = True
for A in (board, tri):
    for k in range(0, 6):
        P = power(A, k)
        ok &= all(P[i][j] == walks(A, k, i, j) for i in range(3) for j in range(3))
random.seed(1)
cnt = 0
for _ in range(200):
    n = random.randint(1, 6)
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < 0.5:
                A[i][j] = A[j][i] = 1
    for k in range(0, 5):
        P = power(A, k)
        ok &= all(P[i][j] == walks(A, k, i, j) for i in range(n) for j in range(n))
        cnt += 1
print("walk-count theorem agrees with enumeration on 2 fixed + 200 random graphs, all k<=5/4:", ok, "(random cases:", cnt, ")")

# Walks listed explicitly for the board graph
def list_walks(A, k, i, j):
    n = len(A); out = []
    for mid in itertools.product(range(n), repeat=k - 1):
        seq = (i,) + mid + (j,)
        if all(A[seq[t]][seq[t+1]] for t in range(k)):
            out.append(tuple(v + 1 for v in seq))
    return out
print("board walks length 2 n1->n1:", list_walks(board, 2, 0, 0))
print("board walks length 2 n1->n3:", list_walks(board, 2, 0, 2))
print("board walks length 3 n1->n2:", list_walks(board, 3, 0, 1))
print("board walks length 3 n1->n1:", list_walks(board, 3, 0, 0))
print("triangle walks length 3 n1->n1:", list_walks(tri, 3, 0, 0))
# paths (distinct vertices) of length 2 from n1 to n1 in the board graph: none
print("paths of length 2 n1->n1 (distinct vertices):",
      [w for w in list_walks(board, 2, 0, 0) if len(set(w)) == len(w)])
