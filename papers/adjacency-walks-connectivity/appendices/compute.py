"""Reproduces every matrix, product, sum and count printed in the paper.
Run: python3 -I compute.py   (pure Python, no packages)"""
import itertools


def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def add(X, Y):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]

def power(A, k):
    P = ident(len(A))
    for _ in range(k):
        P = mul(P, A)
    return P

def adj(n, edges):
    A = [[0] * n for _ in range(n)]
    for a, b in edges:
        A[a - 1][b - 1] = A[b - 1][a - 1] = 1
    return A

def S_of(A):
    n = len(A)
    S = [[0] * n for _ in range(n)]
    for k in range(1, n):
        S = add(S, power(A, k))
    return S

def show(name, M):
    print(name)
    for r in M:
        print("   " + " ".join(str(x) for x in r))

def walks(A, i, j, k):
    n = len(A)
    out = []
    for seq in itertools.product(range(n), repeat=k + 1):
        if seq[0] == i and seq[-1] == j and all(A[a][b] for a, b in zip(seq, seq[1:])):
            out.append(tuple(x + 1 for x in seq))
    return out

def is_path(seq):
    return len(set(seq)) == len(seq)

def is_trail(seq):
    es = [frozenset(p) for p in zip(seq, seq[1:])]
    return len(set(es)) == len(es)

def connected_bfs(A):
    n = len(A)
    seen, queue = {0}, [0]
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if A[u][v] and v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen) == n

def sum_test(A):
    S = S_of(A)
    n = len(A)
    return all(S[i][j] > 0 for i in range(n) for j in range(n) if i != j)

def power_test(A):
    n = len(A)
    I_A = add(ident(n), A)
    P = power(I_A, n - 1)
    return all(x > 0 for r in P for x in r)

print("=== Board graph: edges n1n2, n2n3")
A = adj(3, [(1, 2), (2, 3)])
show("A", A)
print("row sums:", [sum(r) for r in A], " symmetric:", A == [list(c) for c in zip(*A)], " diagonal:", [A[i][i] for i in range(3)])
for k in (2, 3):
    show(f"A^{k}", power(A, k))
S = S_of(A)
show("S = A + A^2", S)
show("(I+A)^2", power(add(ident(3), A), 2))
print("B = A + A^2: B_22 =", S[1][1], "; R = (I+A)^2: R_11 =", power(add(ident(3), A), 2)[0][0])
for (i, j, k) in [(0, 0, 2), (1, 1, 2), (2, 2, 2), (0, 1, 3), (0, 1, 2), (0, 2, 2), (0, 2, 4), (0, 1, 1), (0, 2, 1)]:
    W = walks(A, i, j, k)
    print(f"n{i+1} to n{j+1}, length {k}: entry {power(A, k)[i][j]}, walks {W}, "
          f"trails {[w for w in W if is_trail(w)]}, paths {[w for w in W if is_path(w)]}")

print("\n=== Disconnected: edge n1n2, n3 isolated")
D = adj(3, [(1, 2)])
show("A", D)
show("A^2", power(D, 2))
show("S = A + A^2", S_of(D))
show("(I+A)^2", power(add(ident(3), D), 2))
print("sum test:", sum_test(D), " power test:", power_test(D), " BFS:", connected_bfs(D))

print("\n=== Board drawing read as a triangle")
T = adj(3, [(1, 2), (1, 3), (2, 3)])
show("A", T)
show("A^2", power(T, 2))
show("S", S_of(T))
show("(I+A)^2", power(add(ident(3), T), 2))
print("sum test:", sum_test(T), " power test:", power_test(T), " BFS:", connected_bfs(T))

print("\n=== Two connected graphs, diagonal of S: K2 and board graph")
K2 = adj(2, [(1, 2)])
show("S of K2", S_of(K2))
print("diagonal of S, board graph:", [S_of(A)[i][i] for i in range(3)], " disconnected graph:", [S_of(D)[i][i] for i in range(3)])

print("\n=== Triangle with a pendant edge (n1n2, n2n3, n1n3, n3n4)")
Bm = adj(4, [(1, 2), (2, 3), (1, 3), (3, 4)])
print("A^2 diagonal:", [power(Bm, 2)[i][i] for i in range(4)], " degrees:", [sum(r) for r in Bm])
print("(A^3)_11 =", power(Bm, 3)[0][0], " closed walks:", walks(Bm, 0, 0, 3))

print("\n=== Four-vertex path n1-n2-n3-n4: why N-1 powers are needed")
P4 = adj(4, [(1, 2), (2, 3), (3, 4)])
for k in (1, 2, 3):
    print(f"(A^{k})_14 =", power(P4, k)[0][3])

print("\n=== Exhaustive check over all labelled simple graphs, N = 1..6")
for n in range(1, 7):
    pairs = list(itertools.combinations(range(n), 2))
    total = conn = bad = 0
    for mask in range(2 ** len(pairs)):
        M = [[0] * n for _ in range(n)]
        for b, (a, c) in enumerate(pairs):
            if mask >> b & 1:
                M[a][c] = M[c][a] = 1
        t = connected_bfs(M)
        total += 1
        conn += t
        if not (sum_test(M) == t == power_test(M)):
            bad += 1
    print(f"N={n}: graphs {total}, connected {conn}, disagreements {bad}")

print("\n=== Walk-count theorem against enumeration, all graphs N = 1..4, k = 0..4")
cnt = bad = 0
for n in range(1, 5):
    pairs = list(itertools.combinations(range(n), 2))
    for mask in range(2 ** len(pairs)):
        M = [[0] * n for _ in range(n)]
        for b, (a, c) in enumerate(pairs):
            if mask >> b & 1:
                M[a][c] = M[c][a] = 1
        for k in range(5):
            P = power(M, k)
            for i in range(n):
                for j in range(n):
                    cnt += 1
                    bad += P[i][j] != len(walks(M, i, j, k))
print("entries compared:", cnt, " failures:", bad)
