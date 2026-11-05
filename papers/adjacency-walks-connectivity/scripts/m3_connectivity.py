"""Module m3: every matrix and count in the connectivity module.

Pure Python, integer arithmetic, no third-party packages.
Run:  python3 scripts/m3_connectivity.py
"""
from itertools import combinations
from math import comb


def zeros(n):
    return [[0] * n for _ in range(n)]


def ident(n):
    m = zeros(n)
    for i in range(n):
        m[i][i] = 1
    return m


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mul(a, b):
    n = len(a)
    return [[sum(a[i][t] * b[t][j] for t in range(n)) for j in range(n)] for i in range(n)]


def power(a, k):
    r = ident(len(a))
    for _ in range(k):
        r = mul(r, a)
    return r


def show(name, m):
    print(name + " =")
    for r in m:
        print("   " + " ".join(f"{x:2d}" for x in r))


def power_sum(a):
    """S = A + A^2 + ... + A^(N-1)."""
    n = len(a)
    s = zeros(n)
    for k in range(1, n):
        s = add(s, power(a, k))
    return s


def test_sum(a):
    n = len(a)
    if n == 1:
        return True
    s = power_sum(a)
    return all(s[i][j] > 0 for i in range(n) for j in range(n) if i != j)


def test_ipa(a):
    n = len(a)
    m = power(add(ident(n), a), n - 1)
    return all(x > 0 for r in m for x in r)


def bfs_connected(a):
    n = len(a)
    seen, queue, order = {0}, [0], [0]
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if a[u][v] == 1 and v not in seen:
                seen.add(v)
                queue.append(v)
                order.append(v)
    return len(seen) == n, [x + 1 for x in order]


def from_edges(n, edges):
    a = zeros(n)
    for i, j in edges:
        a[i - 1][j - 1] = a[j - 1][i - 1] = 1
    return a


def example(title, a):
    n = len(a)
    print("=" * 60)
    print(title, "  N =", n)
    show("A", a)
    for k in range(2, n):
        show(f"A^{k}", power(a, k))
    s = power_sum(a)
    show("S = A + ... + A^(N-1)", s)
    show("I + A", add(ident(n), a))
    show(f"(I+A)^(N-1) = (I+A)^{n-1}", power(add(ident(n), a), n - 1))
    print("off-diagonal entries of S all positive:", test_sum(a))
    print("(I+A)^(N-1) has no zero entry:        ", test_ipa(a))
    ok, order = bfs_connected(a)
    print("BFS from n_1 reaches all vertices:     ", ok, " visit order:", order)
    zero_pairs = [(i + 1, j + 1) for i in range(n) for j in range(i + 1, n) if s[i][j] == 0]
    print("pairs (i<j) with S_ij = 0:", zero_pairs)


# 1. Board example (matrix, edges 1-2 and 2-3): connected
board = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
assert board == from_edges(3, [(1, 2), (2, 3)])
example("Example 1: board matrix (path n1-n2-n3)", board)

# 2. Disconnected: only edge 1-2, n3 isolated
disc = from_edges(3, [(1, 2)])
example("Example 2: disconnected (edge n1-n2, n3 isolated)", disc)

# 3. The graph the board drawing seems to show (three edges)
tri = from_edges(3, [(1, 2), (1, 3), (2, 3)])
example("Example 3 (remark): drawing read as three edges, triangle", tri)

# 4. Distance reading: least k with (A^k)_ij > 0 on the board graph
print("=" * 60)
print("Distance from least k with (A^k)_ij > 0, board graph:")
for i, j in combinations(range(3), 2):
    for k in range(1, 3):
        if power(board, k)[i][j] > 0:
            print(f"  d(n{i+1}, n{j+1}) = {k}")
            break

# 5. Why A^(N-1) alone is not enough, and why N-1 powers are needed
print("=" * 60)
print("A^2 alone on the board graph (connected), entry (1,2):", power(board, 2)[0][1])
for n in (3, 4, 5, 6):
    p = from_edges(n, [(i, i + 1) for i in range(1, n)])
    first = min(k for k in range(1, n + 1) if power(p, k)[0][n - 1] > 0)
    print(f"path graph on N={n}: least k with (A^k)_(1,N) > 0 is {first} = N-1:", first == n - 1)

# 6. Binomial expansion check on the board graph
n = 3
lhs = power(add(ident(n), board), n - 1)
rhs = zeros(n)
for k in range(n):
    c = comb(n - 1, k)
    rhs = add(rhs, [[c * x for x in r] for r in power(board, k)])
print("=" * 60)
print("(I+A)^2 equals sum C(2,k) A^k for k=0..2 on board graph:", lhs == rhs)
print("binomial coefficients C(2,k):", [comb(2, k) for k in range(3)])

# 7. Exhaustive check on all labelled simple graphs, N = 1..6
print("=" * 60)
for n in range(1, 7):
    pairs = list(combinations(range(n), 2))
    total = conn = bad = 0
    for mask in range(1 << len(pairs)):
        edges = [(pairs[b][0] + 1, pairs[b][1] + 1) for b in range(len(pairs)) if mask >> b & 1]
        a = from_edges(n, edges)
        truth = bfs_connected(a)[0]
        total += 1
        conn += truth
        if not (test_sum(a) == truth and test_ipa(a) == truth):
            bad += 1
    print(f"N={n}: labelled graphs {total}, connected {conn}, test disagrees with BFS: {bad}")
