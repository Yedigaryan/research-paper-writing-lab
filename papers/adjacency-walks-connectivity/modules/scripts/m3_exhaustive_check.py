"""Module m3: exhaustive check of the connectivity test on all labelled simple graphs, N = 2..6.

For each graph the following are computed independently and compared:
  S  : every off-diagonal entry of A + ... + A^(N-1) is positive
  P  : every entry of (I + A)^(N-1) is positive
  U  : union-find on the edge list gives one class (independent of matrices)
  W  : walk counts by explicit enumeration of walks of length 1..N-1 (independent of matrix powers)
Also checks the distance claim: smallest k with (A^k)_ij > 0 equals BFS distance.
Run:  python3 -I m3_exhaustive_check.py
"""
from itertools import combinations
from collections import deque


def mat_mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def uf_components(n, edges):
    p = list(range(n))

    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for a, b in edges:
        p[f(a)] = f(b)
    return len({f(x) for x in range(n)})


def walk_counts(n, adj, k):
    """cnt[i][j] = number of walks of length k, by explicit enumeration of vertex sequences."""
    cnt = [[0] * n for _ in range(n)]

    def rec(start, v, left):
        if left == 0:
            cnt[start][v] += 1
            return
        for w in adj[v]:
            rec(start, w, left - 1)
    for s in range(n):
        rec(s, s, k)
    return cnt


def bfs_dist(n, adj, s):
    d = [None] * n
    d[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] is None:
                d[w] = d[v] + 1
                q.append(w)
    return d


total_bad = 0
for n in range(2, 7):
    pairs = list(combinations(range(n), 2))
    connected_count = 0
    for mask in range(1 << len(pairs)):
        edges = [pairs[t] for t in range(len(pairs)) if mask >> t & 1]
        A = [[0] * n for _ in range(n)]
        adj = [[] for _ in range(n)]
        for a, b in edges:
            A[a][b] = A[b][a] = 1
            adj[a].append(b)
            adj[b].append(a)
        powers = [ident(n)]
        for _ in range(n - 1):
            powers.append(mat_mul(powers[-1], A))
        S = all(sum(powers[k][i][j] for k in range(1, n)) > 0
                for i in range(n) for j in range(n) if i != j)
        IA = [[A[i][j] + int(i == j) for j in range(n)] for i in range(n)]
        M = ident(n)
        for _ in range(n - 1):
            M = mat_mul(M, IA)
        P = all(M[i][j] > 0 for i in range(n) for j in range(n))
        U = uf_components(n, edges) == 1
        W = None
        if n <= 5:  # explicit walk enumeration only for n <= 5 (cost)
            wc = [None] + [walk_counts(n, adj, k) for k in range(1, n)]
            for k in range(1, n):
                if wc[k] != powers[k]:
                    total_bad += 1
            W = all(sum(wc[k][i][j] for k in range(1, n)) > 0
                    for i in range(n) for j in range(n) if i != j)
        ok = (S == P == U) and (W is None or W == U)
        for s in range(n):
            d = bfs_dist(n, adj, s)
            for t in range(n):
                if t == s:
                    continue
                ks = [k for k in range(1, n) if powers[k][s][t] > 0]
                kmin = ks[0] if ks else None
                if kmin != d[t]:
                    ok = False
        if not ok:
            total_bad += 1
        connected_count += U
    print(f"N = {n}: graphs checked = {1 << len(pairs)}, connected = {connected_count}")
print("disagreements found:", total_bad)

for n in range(2, 8):
    A = [[int(abs(i - j) == 1) for j in range(n)] for i in range(n)]
    P = ident(n)
    first = None
    for k in range(1, n):
        P = mat_mul(P, A)
        if P[0][n - 1] > 0 and first is None:
            first = k
    print(f"path graph N = {n}: smallest k with (A^k)_(1,N) > 0 is {first}")
