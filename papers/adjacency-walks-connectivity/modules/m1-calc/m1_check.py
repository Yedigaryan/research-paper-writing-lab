"""Module m1 checks. Pure Python, no packages. Run: python3 m1_check.py"""
import itertools, random

def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]

def power(A, k):
    n = len(A)
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(k):
        P = mul(P, A)
    return P

def show(name, M):
    print(name)
    for row in M:
        print("  ", " ".join(str(x) for x in row))

def adj(n, edges):
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u][v] = A[v][u] = 1
    return A

def walks(A, k, i, j):
    """All walks of length k from i to j, by explicit enumeration."""
    n = len(A)
    out = []
    def go(seq):
        if len(seq) == k + 1:
            if seq[-1] == j:
                out.append(tuple(seq))
            return
        for r in range(n):
            if A[seq[-1]][r]:
                go(seq + [r])
    go([i])
    return out

def is_path(w):
    return len(set(w)) == len(w)

def is_trail(w):
    es = [frozenset(p) for p in zip(w, w[1:])]
    return len(set(es)) == len(es)

# 1. Board graph, vertices 0,1,2 stand for n1,n2,n3; edges n1n2, n2n3
A = adj(3, [(0, 1), (1, 2)])
show("A (board)", A)
print("symmetric:", all(A[i][j] == A[j][i] for i in range(3) for j in range(3)))
print("zero diagonal:", all(A[i][i] == 0 for i in range(3)))
print("row sums:", [sum(r) for r in A], " degrees by counting edges:",
      [sum(1 for e in [(0, 1), (1, 2)] if i in e) for i in range(3)])
for k in (2, 3):
    show(f"A^{k}", power(A, k))

# 2. Counterexample C7: diagonal of A^2, with the walks listed
print("\nWalks of length 2 from n_i to n_i and paths among them")
for i in range(3):
    ws = walks(A, 2, i, i)
    print(f" n{i+1}: (A^2)_{i+1}{i+1} = {power(A,2)[i][i]}; walks:",
          [tuple(x + 1 for x in w) for w in ws],
          "; paths (distinct vertices):", [w for w in ws if is_path(w)])
print("Length-0 convention: A^0 = I, one walk (n_i) and it is a path:", power(A, 0))

# 3. Walks vs paths off the diagonal: A^3 entry (1,2) on the board graph
ws = walks(A, 3, 0, 1)
print("\nlength-3 walks n1 -> n2:", [tuple(x + 1 for x in w) for w in ws],
      "paths among them:", [w for w in ws if is_path(w)],
      "trails among them:", [w for w in ws if is_trail(w)])
ws = walks(A, 2, 0, 0)
print("length-2 closed walk n1 n2 n1 is a trail?", is_trail(ws[0]),
      "(edge n1n2 used twice, so not a trail either)")

# 4. Triangle with a pendant vertex: n1n2, n2n3, n1n3, n3n4  -> row sums = degrees = diag(A^2)
B = adj(4, [(0, 1), (1, 2), (0, 2), (2, 3)])
show("\nB (triangle n1n2n3 plus pendant n3n4)", B)
show("B^2", power(B, 2))
print("row sums:", [sum(r) for r in B], " diag(B^2):", [power(B, 2)[i][i] for i in range(4)])
show("B^3", power(B, 3))
print("B^3 (1,1) =", power(B, 3)[0][0], "; closed walks length 3 from n1:",
      [tuple(x + 1 for x in w) for w in walks(B, 3, 0, 0)])

# 5. Brute-force check of the theorem and of row sums on random simple graphs
random.seed(1)
bad = 0; cases = 0
for _ in range(300):
    n = random.randint(1, 6)
    E = [e for e in itertools.combinations(range(n), 2) if random.random() < 0.4]
    A_ = adj(n, E)
    deg = [sum(1 for e in E if i in e) for i in range(n)]
    if [sum(r) for r in A_] != deg or any(A_[i][i] for i in range(n)) or A_ != [list(c) for c in zip(*A_)]:
        bad += 1
    for k in range(0, 5):
        P = power(A_, k)
        for i in range(n):
            for j in range(n):
                cases += 1
                if P[i][j] != len(walks(A_, k, i, j)):
                    bad += 1
    if any(power(A_, 2)[i][i] != deg[i] for i in range(n)):
        bad += 1
print(f"\nrandom check: {cases} entries compared with enumerated walks, failures = {bad}")
