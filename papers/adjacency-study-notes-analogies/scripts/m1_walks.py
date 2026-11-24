"""m1: walk counting checks. Brute-force enumeration of walks vs matrix powers."""
import itertools, random
import numpy as np

def walks(A, k):
    """All vertex sequences (v0..vk), 0-based, consecutive entries adjacent."""
    N = len(A)
    out = []
    for seq in itertools.product(range(N), repeat=k + 1):
        if all(A[seq[t]][seq[t + 1]] == 1 for t in range(k)):
            out.append(seq)
    return out

def is_path(seq):
    return len(set(seq)) == len(seq)

def lab(seq):  # 1-based names n_1..n_N
    return ",".join(f"n{v+1}" for v in seq)

A = np.array([[0,1,0],[1,0,1],[0,1,0]])   # board matrix
print("A =\n", A)
P = np.eye(3, dtype=int)
for k in range(0, 5):
    if k > 0:
        P = P @ A
    cnt = np.zeros((3,3), dtype=int)
    for s in walks(A, k):
        cnt[s[0]][s[-1]] += 1
    assert (cnt == P).all()
    print(f"A^{k} =\n", P, " (equals brute-force walk count)")

print("\nWalks of length 2 from n1 to n1:")
for s in walks(A, 2):
    if s[0] == 0 and s[-1] == 0:
        print("  ", lab(s), "path?", is_path(s))
print("Walks of length 2 from n1 to n3:")
for s in walks(A, 2):
    if s[0] == 0 and s[-1] == 2:
        print("  ", lab(s), "path?", is_path(s))
print("Walks of length 2 from n2 to n2:")
for s in walks(A, 2):
    if s[0] == 1 and s[-1] == 1:
        print("  ", lab(s), "path?", is_path(s))

# random simple graphs, N = 2..6, k = 0..4
random.seed(1)
checked = 0
for _ in range(200):
    N = random.randint(2, 6)
    M = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < 0.5:
                M[i][j] = M[j][i] = 1
    P = np.eye(N, dtype=int)
    for k in range(0, 5):
        if k > 0:
            P = P @ M
        cnt = np.zeros((N, N), dtype=int)
        for s in walks(M.tolist(), k):
            cnt[s[0]][s[-1]] += 1
        assert (cnt == P).all()
        checked += 1
print("\nRandom graphs: theorem verified in", checked, "(graph, k) cases, no failure")

# trail/path check: in simple graphs a walk with distinct vertices has distinct edges
bad = 0
for _ in range(100):
    N = random.randint(2, 6)
    M = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if random.random() < 0.6:
                M[i][j] = M[j][i] = 1
    for k in range(0, N):
        for s in walks(M, k):
            if is_path(s):
                edges = [frozenset((s[t], s[t+1])) for t in range(k)]
                if len(set(edges)) != len(edges):
                    bad += 1
print("Paths with a repeated edge found:", bad)
