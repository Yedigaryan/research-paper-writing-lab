"""Generate the LaTeX macros that carry every matrix and table of numbers in
the paper, so that no matrix is retyped by hand.

What it does
  1. Reads the saved outputs of the three module scripts (m1_walks_output.txt,
     m2_walks_output.txt, m3_connectivity.out.txt) in this folder.
  2. Recomputes every matrix and every count with independent code
     (pure Python integers, no libraries) and asserts that the recomputed
     values equal the saved outputs.
  3. Writes ../generated_numbers.tex, which defines one macro per matrix and
     per table body. main.tex inputs that file; the sections use the macros.

Run from the paper folder:
    python3 -I appendices/scripts/generate_paper_numbers.py
Exit status 0 means every assertion passed.
"""
import re
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "generated_numbers.tex"


# ------------------------------------------------------------- matrix code
def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)]
            for i in range(n)]


def add(X, Y):
    return [[a + b for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def power(A, k):
    R = identity(len(A))
    for _ in range(k):
        R = mul(R, A)
    return R


def adjacency(n, edges):
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u - 1][v - 1] = A[v - 1][u - 1] = 1
    return A


def power_sum(A, last):
    n = len(A)
    S = [[0] * n for _ in range(n)]
    for k in range(1, last + 1):
        S = add(S, power(A, k))
    return S


# ------------------------------------------------------- parse saved output
ROW = re.compile(r"^\s*(\d+(?:\s+\d+)*)\s*$")


def blocks(path):
    """Return the list of (header line, matrix) in the order of appearance.
    A matrix is a run of lines that contain only integers."""
    result, header, rows = [], None, []
    for line in path.read_text().splitlines():
        m = ROW.match(line)
        if m:
            rows.append([int(x) for x in m.group(1).split()])
            continue
        if rows:
            result.append((header, rows))
            rows = []
        header = line.strip()
    if rows:
        result.append((header, rows))
    return result


def check(label, got, saved):
    if got != saved:
        sys.exit(f"MISMATCH {label}: recomputed {got} saved {saved}")


def pm(M):
    body = r" \\ ".join(" & ".join(str(x) for x in row) for row in M)
    return r"\begin{pmatrix}" + body + r"\end{pmatrix}"


macros = {}

# ----------------------------------------------- board graph B, module m1
m1 = blocks(HERE / "m1_walks_output.txt")
B = adjacency(3, [(1, 2), (2, 3)])
names_m1 = ["A", "A^2", "A^3", "A^4", "A^5"]
for idx, k in enumerate(range(1, 6)):
    hdr, saved = m1[idx]
    assert hdr == names_m1[idx], (hdr, names_m1[idx])
    check(f"m1 board A^{k}", power(B, k), saved)
macros["MBoardA"] = pm(power(B, 1))
macros["MBoardAsq"] = pm(power(B, 2))
macros["MBoardAcube"] = pm(power(B, 3))
macros["MBoardAfour"] = pm(power(B, 4))
macros["MBoardAfive"] = pm(power(B, 5))
# A^3 = 2A and A^(k+2) = 2 A^k for k = 1..5 (stated in the paper)
twoA = [[2 * x for x in row] for row in B]
check("A^3 = 2A", power(B, 3), twoA)
for k in range(1, 6):
    check(f"A^({k}+2) = 2 A^{k}", power(B, k + 2),
          [[2 * x for x in row] for row in power(B, k)])
macros["MTwoA"] = pm(twoA)

# ------------------------------------------------ module m3, three graphs
m3 = blocks(HERE / "m3_connectivity.out.txt")
I3 = identity(3)
D = adjacency(3, [(1, 2)])


def example(offset, A, label):
    exp = [("A", A), ("A^2", power(A, 2)),
           ("S = A + A^2", power_sum(A, 2)),
           ("(I + A)^2", power(add(identity(3), A), 2))]
    for off, (prefix, M) in enumerate(exp):
        hdr, saved = m3[offset + off]
        assert hdr.startswith(prefix), (hdr, prefix)
        check(f"m3 {label} {prefix}", M, saved)
    return exp


exB = example(0, B, "board")
exD = example(4, D, "one-edge")
for (_, M), name in zip(exB, ["MBoardA", "MBoardAsq", "MBoardS", "MBoardIAsq"]):
    if name in ("MBoardA", "MBoardAsq"):
        assert pm(M) == macros[name]
    else:
        macros[name] = pm(M)
for (_, M), name in zip(exD, ["MOneA", "MOneAsq", "MOneS", "MOneIAsq"]):
    macros[name] = pm(M)
# the binomial identity (I + A)^2 = I + 2A + A^2 on both graphs
for A in (B, D):
    check("(I+A)^2 = I + 2A + A^2", power(add(identity(3), A), 2),
          add(add(identity(3), [[2 * x for x in r] for r in A]), power(A, 2)))
# higher powers of the one-edge graph: entries (1,3) and (2,3) are 0 for k=1..6
for k in range(1, 7):
    P = power(D, k)
    assert P[0][2] == 0 and P[1][2] == 0 and P[2][0] == 0 and P[2][1] == 0
macros["MOneAcube"] = pm(power(D, 3))

# N = 2: S = A has a zero diagonal although the graph is connected
A2 = adjacency(2, [(1, 2)])
hdr, saved = m3[8]
assert hdr.startswith("A = S"), hdr
check("N=2 S = A", A2, saved)
macros["MTwoVertexA"] = pm(A2)

# N = 4 path graph 1-2-3-4
P4 = adjacency(4, [(1, 2), (2, 3), (3, 4)])
exP = [("A", P4), ("A^2", power(P4, 2)), ("A^3", power(P4, 3)),
       ("A + A^2", power_sum(P4, 2)), ("A + A^2 + A^3", power_sum(P4, 3))]
for off, (prefix, M) in enumerate(exP):
    hdr, saved = m3[9 + off]
    assert hdr.startswith(prefix), (hdr, prefix)
    check(f"m3 path4 {prefix}", M, saved)
for (_, M), name in zip(exP, ["MPathA", "MPathAsq", "MPathAcube",
                              "MPathSshort", "MPathSfull"]):
    macros[name] = pm(M)
assert exP[3][1][0][3] == 0 and exP[3][1][3][0] == 0     # (1,4) and (4,1) zero
assert all(x > 0 for row in exP[4][1] for x in row)       # N-1 powers: all positive

# --------------------------------- table: walks, trails, paths, closed walks
# independent enumeration on the board graph B (vertices 1..3)
adj = {1: [2], 2: [1, 3], 3: [2]}


def all_walks(k):
    seqs = [(v,) for v in adj]
    for _ in range(k):
        seqs = [s + (w,) for s in seqs for w in adj[s[-1]]]
    return seqs


def is_trail(s):
    es = [frozenset(p) for p in zip(s, s[1:])]
    return len(es) == len(set(es))


def is_path(s):
    return len(s) == len(set(s))


rows_m2 = {}
for line in (HERE / "m2_walks_output.txt").read_text().splitlines():
    m = re.match(r"\s*k=(\d+): walks=(\d+)\s+trails=(\d+)\s+paths=(\d+)\s+closed walks=(\d+)", line)
    if m:
        rows_m2[int(m.group(1))] = tuple(int(x) for x in m.groups()[1:])
assert sorted(rows_m2) == [0, 1, 2, 3, 4]
tbody = []
for k in range(5):
    W = all_walks(k)
    mine = (len(W), sum(map(is_trail, W)), sum(map(is_path, W)),
            sum(1 for s in W if s[0] == s[-1]))
    check(f"m2 counts k={k}", mine, rows_m2[k])
    tbody.append(f"{k} & {mine[0]} & {mine[1]} & {mine[2]} & {mine[3]} \\\\")
macros["TabWalkCountsBody"] = "\n".join(tbody)
# the total number of walks of length k equals the sum of the entries of A^k
for k in range(1, 5):
    assert sum(map(sum, power(B, k))) == rows_m2[k][0]

# ------------------- table: walks from 1 to 2 and how many are paths (m1)
rows_m1 = {}
for line in (HERE / "m1_walks_output.txt").read_text().splitlines():
    m = re.match(r"k=(\d+): walks 1->2 = (\d+), of which paths = (\d+), trails = (\d+)", line)
    if m:
        rows_m1[int(m.group(1))] = tuple(int(x) for x in m.groups()[1:])
tbody = []
for k in range(1, 6):
    W = [s for s in all_walks(k) if s[0] == 1 and s[-1] == 2]
    mine = (len(W), sum(map(is_path, W)), sum(map(is_trail, W)))
    check(f"m1 walks 1->2 k={k}", mine, rows_m1[k])
    assert mine[0] == power(B, k)[0][1]
    tbody.append(f"{k} & {mine[0]} & {mine[1]} & {mine[2]} \\\\")
macros["TabWalksVsPathsBody"] = "\n".join(tbody)

# closed walks from 1 to 1 on B: 0, 1, 0, 2 for k = 1..4, none a path or trail (appendix A.2)
closed = {}
for line in (HERE / "m1_walks_output.txt").read_text().splitlines():
    m = re.match(r"k=(\d+): closed walks 1->1 = (\d+), of which paths = (\d+), trails = (\d+)", line)
    if m:
        closed[int(m.group(1))] = tuple(int(x) for x in m.groups()[1:])
for k, exp in zip(range(1, 5), (0, 1, 0, 2)):
    W = [s for s in all_walks(k) if s[0] == 1 and s[-1] == 1]
    check(f"closed walks 1->1 k={k}", (len(W), sum(map(is_path, W)), sum(map(is_trail, W))), closed[k])
    assert len(W) == exp == power(B, k)[0][0]
assert sorted(s for s in all_walks(4) if s[0] == 1 and s[-1] == 1) == [(1, 2, 1, 2, 1), (1, 2, 3, 2, 1)]

# graph H (triangle 1,2,3 with vertex 4 joined to 3) and the triangle T: the examples in Section 2
def is_walk_in(edges, seq):
    es = {frozenset(e) for e in edges}
    return all(frozenset(p) in es for p in zip(seq, seq[1:]))

H_edges = [(1, 2), (1, 3), (2, 3), (3, 4)]
assert is_walk_in(H_edges, (4, 3, 1, 2, 3)) and is_trail((4, 3, 1, 2, 3)) and not is_path((4, 3, 1, 2, 3))
assert is_walk_in(H_edges, (4, 3, 1, 2)) and is_path((4, 3, 1, 2))
assert is_walk_in(H_edges, (1, 2, 3, 2)) and not is_trail((1, 2, 3, 2))
assert is_walk_in(H_edges, (4, 3, 4)) and not is_trail((4, 3, 4))
assert is_walk_in(H_edges, (1, 2, 3, 1)) and is_trail((1, 2, 3, 1)) and len(set((1, 2, 3, 1)[:-1])) == 3
# in H, a closed trail of positive length must avoid edge 34 (it would be used twice) and so is the triangle
# the triangle T: S = A + A^2 has every entry equal to 2 (so modulo 2 it is zero)
T = adjacency(3, [(1, 2), (1, 3), (2, 3)])
assert power_sum(T, 2) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
# hand-check cases quoted in Appendix A.7
assert power(B, 2)[0][2] == 1 and power(B, 3)[0][1] == 2
assert [a + b for a, b in zip(D[0], power(D, 2)[0])] == [1, 1, 0] and power_sum(D, 2)[2] == [0, 0, 0]

# ---- table: path graph 1-2-...-N, first power with a nonzero (1,N) entry
text3 = (HERE / "m3_connectivity.out.txt").read_text()
rows_m3 = {}
for line in text3.splitlines():
    m = re.match(r"\s*(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+)\s*$", line)
    if m and int(m.group(2)) < 10 and int(m.group(1)) <= 8:
        rows_m3[int(m.group(1))] = tuple(int(x) for x in m.groups()[1:])
tbody = []
for N in range(3, 9):
    PN = adjacency(N, [(i, i + 1) for i in range(1, N)])
    first = next(k for k in range(1, 3 * N) if power(PN, k)[0][N - 1] > 0)
    short = power_sum(PN, N - 2)[0][N - 1]
    full = power_sum(PN, N - 1)[0][N - 1]
    mine = (first, short, full)
    check(f"m3 path graph N={N}", mine, rows_m3[N])
    assert first == N - 1
    tbody.append(f"{N} & {first} & {short} & {full} \\\\")
macros["TabPathSharpBody"] = "\n".join(tbody)

# ------------------------------------- table: exhaustive check (m3 output)
ex_rows = {}
for line in text3.splitlines():
    m = re.match(r"\s*(\d) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+)\s*$", line)
    if m:
        ex_rows[int(m.group(1))] = tuple(int(x) for x in m.groups()[1:])
assert sorted(ex_rows) == [2, 3, 4, 5, 6]


def bfs_connected(n, edges):
    seen, stack = {1}, [1]
    while stack:
        u = stack.pop()
        for a, b in edges:
            for x, y in ((a, b), (b, a)):
                if x == u and y not in seen:
                    seen.add(y)
                    stack.append(y)
    return len(seen) == n


tbody = []
for N in range(2, 7):
    pairs = [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)]
    total = conn = test_ok = short_wrong = 0
    for mask in range(2 ** len(pairs)):
        edges = [p for t, p in enumerate(pairs) if mask >> t & 1]
        A = adjacency(N, edges)
        truth = bfs_connected(N, edges)
        S = power_sum(A, N - 1)
        sum_says = all(S[i][j] > 0 for i in range(N) for j in range(N) if i != j)
        Sshort = power_sum(A, N - 2)
        short_says = all(Sshort[i][j] > 0 for i in range(N) for j in range(N) if i != j)
        total += 1
        conn += truth
        test_ok += (sum_says == truth)
        short_wrong += (short_says != truth)
    mine = (total, conn, test_ok, short_wrong)
    saved = (ex_rows[N][0], ex_rows[N][1], ex_rows[N][2], ex_rows[N][6])
    check(f"exhaustive N={N}", mine, saved)
    assert test_ok == total
    tbody.append(f"{N} & {total:,} & {conn:,} & {test_ok:,} & {short_wrong} \\\\".replace(",", "{,}"))
macros["TabExhaustiveBody"] = "\n".join(tbody)

# ------------------------------------------------------ cost remark (m3)
cost_rows = {}
for line in text3.splitlines():
    m = re.match(r"\s*(\d+) \|\s+([\d,]+) \|\s+([\d,]+) \|\s+([\d,]+)\s*$", line)
    if m and int(m.group(1)) in (10, 100, 1000):
        cost_rows[int(m.group(1))] = tuple(int(x.replace(",", "")) for x in m.groups()[1:])
tbody = []
for N in (10, 100, 1000):
    mine = ((N - 2) * N ** 3, ((N - 1 - 1).bit_length()) * N ** 3, N * N)
    # squarings t = ceil(log2(N-1)); (N-2).bit_length() equals that for N-1 >= 2
    t = 0
    while 2 ** t < N - 1:
        t += 1
    mine = ((N - 2) * N ** 3, t * N ** 3, N * N)
    check(f"cost N={N}", mine, cost_rows[N])
    fmt = lambda x: f"{x:,}".replace(",", "{,}")
    tbody.append(f"{N} & {fmt(mine[0])} & {t} & {fmt(mine[1])} & {fmt(mine[2])} \\\\")
macros["TabCostBody"] = "\n".join(tbody)

# largest entry of A^(N-1) for the complete graphs K_5, K_10 (m3 output)
for n, saved_max in ((5, 52), (10, 38742049)):
    K = [[int(i != j) for j in range(n)] for i in range(n)]
    got = max(max(row) for row in power(K, n - 1))
    check(f"K_{n}", got, saved_max)
    assert f"K_{n}: largest entry of A^(N-1) = {saved_max:,}" in text3 or n == 5 and "= 52" in text3

# ---------------------------------------- quoted counts from the outputs
text1 = (HERE / "m1_walks_output.txt").read_text()
for s in ("N=2: 2 graphs, 40 (k,i,j)", "N=3: 8 graphs, 360 (k,i,j)",
          "N=4: 64 graphs, 5120 (k,i,j)", "N=5: 1024 graphs, 76800 (k,i,j)"):
    assert s in text1, s
text2 = (HERE / "m2_walks_output.txt").read_text()
for s in ("73 walks, failures 0", "381 walks, failures 0", "4695 walks, failures 0",
          "'graphs': 300, 'walks': 192696"):
    assert s in text2, s

# --------------------------------------------------------------- write
lines = ["% Generated by appendices/scripts/generate_paper_numbers.py. Do not edit by hand."]
for name, body in macros.items():
    lines.append(f"\\newcommand{{\\{name}}}{{{body}}}")
OUT.write_text("\n".join(lines) + "\n")
print(f"wrote {OUT} with {len(macros)} macros; all assertions passed")
