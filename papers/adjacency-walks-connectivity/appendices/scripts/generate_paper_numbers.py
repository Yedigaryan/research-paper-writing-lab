"""Generate every number printed in the paper's examples and tables.

Run from the paper folder:
    python3 -I appendices/scripts/generate_paper_numbers.py

It writes appendices/scripts/numbers.tex, a file of LaTeX macros that the
paper inputs, so that no matrix or count in the text is typed by hand.
It also prints the same numbers and asserts the facts the text states.
Pure Python integers; no libraries. About 15 seconds (N = 6 loop).
"""
from itertools import combinations, product
from pathlib import Path


# ---------- basic matrix tools ----------
def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def add(X, Y):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]


def power(A, k):
    R = ident(len(A))
    for _ in range(k):
        R = mul(R, A)
    return R


def from_edges(n, edges):
    A = [[0] * n for _ in range(n)]
    for u, v in edges:
        A[u - 1][v - 1] = A[v - 1][u - 1] = 1
    return A


def sum_powers(A, top):
    S = [[0] * len(A) for _ in A]
    for k in range(1, top + 1):
        S = add(S, power(A, k))
    return S


def pmatrix(M):
    return (r"\begin{pmatrix}" + r" \\ ".join(" & ".join(str(x) for x in row) for row in M)
            + r"\end{pmatrix}")


def bfs_components(A):
    n = len(A)
    seen, comps = set(), []
    for s in range(n):
        if s in seen:
            continue
        comp, queue = [s], [s]
        seen.add(s)
        while queue:
            u = queue.pop(0)
            for v in range(n):
                if A[u][v] and v not in seen:
                    seen.add(v)
                    comp.append(v)
                    queue.append(v)
        comps.append(sorted(comp))
    return comps


def off_diag_positive(S):
    n = len(S)
    return all(S[i][j] > 0 for i in range(n) for j in range(n) if i != j)


def no_zero(M):
    return all(x > 0 for r in M for x in r)


# ---------- walk enumeration ----------
def walks(A, k, i, j):
    n = len(A)
    out = []

    def go(seq):
        if len(seq) == k + 1:
            if seq[-1] == j:
                out.append(tuple(seq))
            return
        for v in range(n):
            if A[seq[-1]][v]:
                go(seq + [v])

    go([i])
    return out


def all_walks(A, k):
    n = len(A)
    out = []
    for i in range(n):
        for j in range(n):
            out += walks(A, k, i, j)
    return out


def is_path(w):
    return len(set(w)) == len(w)


def is_trail(w):
    edges = [frozenset(p) for p in zip(w, w[1:])]
    return len(set(edges)) == len(edges)


macros = {}


def macro(name, body):
    macros[name] = body


# ---------- board matrix (edges 1-2, 2-3) ----------
A = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
assert A == from_edges(3, [(1, 2), (2, 3)])
P = {k: power(A, k) for k in range(1, 6)}
for name, k in (("One", 1), ("Two", 2), ("Three", 3), ("Four", 4), ("Five", 5)):
    macro("MBoardA" + name, pmatrix(P[k]))
assert P[2] == [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
assert P[3] == [[2 * x for x in r] for r in A]
for k in range(1, 6):
    assert power(A, k + 2) == [[2 * x for x in r] for r in power(A, k)]
S_B = sum_powers(A, 2)
IA_B = power(add(ident(3), A), 2)
macro("MBoardS", pmatrix(S_B))
macro("MBoardIA", pmatrix(IA_B))
macro("MBoardId", pmatrix(ident(3)))
macro("MBoardTwoA", pmatrix([[2 * x for x in r] for r in A]))
assert IA_B == add(add(ident(3), [[2 * x for x in r] for r in A]), P[2])
assert off_diag_positive(S_B) and no_zero(IA_B)
assert bfs_components(A) == [[0, 1, 2]]
degrees = [sum(r) for r in A]
assert degrees == [1, 2, 1] and sum(map(sum, A)) == 4
assert [P[2][i][i] for i in range(3)] == degrees

# the board drawing (triangle) for comparison
T = from_edges(3, [(1, 2), (1, 3), (2, 3)])
macro("MDrawT", pmatrix(T))
macro("MDiffAT", pmatrix([[T[i][j] - A[i][j] for j in range(3)] for i in range(3)]))

# the non-example matrix of the adjacency-matrix definition (not symmetric)
macro("MNonSym", pmatrix([[0, 1, 0], [0, 0, 1], [0, 1, 0]]))

# ---------- disconnected example (edge 1-2 only) ----------
D = from_edges(3, [(1, 2)])
D2 = power(D, 2)
S_D = sum_powers(D, 2)
IA_D = power(add(ident(3), D), 2)
macro("MDiscA", pmatrix(D))
macro("MDiscAtwo", pmatrix(D2))
macro("MDiscS", pmatrix(S_D))
macro("MDiscIA", pmatrix(IA_D))
zeros_S = [(i + 1, j + 1) for i in range(3) for j in range(3) if i != j and S_D[i][j] == 0]
zeros_IA = [(i + 1, j + 1) for i in range(3) for j in range(3) if IA_D[i][j] == 0]
assert zeros_S == zeros_IA == [(1, 3), (2, 3), (3, 1), (3, 2)]
assert bfs_components(D) == [[0, 1], [2]]
for k in range(1, 7):
    Dk = power(D, k)
    assert Dk[0][2] == 0 and Dk[1][2] == 0

# ---------- N = 2 edge case ----------
A2 = from_edges(2, [(1, 2)])
macro("MTwoA", pmatrix(A2))
assert sum_powers(A2, 1) == A2 and A2[0][0] == 0

# ---------- path graph on 4 vertices ----------
Q = from_edges(4, [(1, 2), (2, 3), (3, 4)])
Q2, Q3 = power(Q, 2), power(Q, 3)
macro("MPathA", pmatrix(Q))
macro("MPathAtwo", pmatrix(Q2))
macro("MPathAthree", pmatrix(Q3))
macro("MPathShort", pmatrix(add(Q, Q2)))
macro("MPathFull", pmatrix(add(add(Q, Q2), Q3)))
assert add(Q, Q2)[0][3] == 0 and off_diag_positive(add(add(Q, Q2), Q3))

# ---------- Table: sharpness of N - 1 ----------
rows = []
for N in range(3, 9):
    Pn = from_edges(N, [(i, i + 1) for i in range(1, N)])
    first = next(k for k in range(1, N + 2) if power(Pn, k)[0][N - 1] > 0)
    short = sum_powers(Pn, N - 2)[0][N - 1]
    full = sum_powers(Pn, N - 1)[0][N - 1]
    assert first == N - 1 and short == 0 and full >= 1
    rows.append(rf"{N} & {first} & {short} & {full} \\")
macro("RowsSharp", "\n".join(rows))

# ---------- Table: walks, trails, paths in the board graph, by length ----------
rows = []
for k in range(0, 5):
    if k == 0:
        W = [(i,) for i in range(3)]
    else:
        W = all_walks(A, k)
    nw = len(W)
    nt = sum(is_trail(w) for w in W)
    npth = sum(is_path(w) for w in W)
    nc = sum(w[0] == w[-1] for w in W)
    if k >= 1:
        assert nw == sum(map(sum, power(A, k)))
    rows.append(rf"{k} & {nw} & {nt} & {npth} & {nc} \\")
assert rows[0].startswith("0 & 3 & 3 & 3 & 3") and rows[2].startswith("2 & 6 & 2 & 2 & 4")
assert rows[3].startswith("3 & 8 & 0 & 0 & 0") and rows[4].startswith("4 & 12 & 0 & 0 & 8")
macro("RowsWalkCounts", "\n".join(rows))

# ---------- Table: walks versus paths from 1 to 2 ----------
rows = []
for k in range(1, 6):
    W = walks(A, k, 0, 1)
    assert len(W) == power(A, k)[0][1]
    rows.append(rf"{k} & {len(W)} & {sum(is_trail(w) for w in W)} & {sum(is_path(w) for w in W)} \\")
macro("RowsWalkPath", "\n".join(rows))
assert [len(walks(A, k, 0, 1)) for k in range(1, 6)] == [1, 0, 2, 0, 4]

# ---------- explicit walk lists for the example (labels 1..3) ----------
def fmt(w):
    return r"\text{-}".join(str(v + 1) for v in w)


def wl(k, i, j):
    return ", ".join(fmt(w) for w in walks(A, k, i - 1, j - 1))


macro("WalksTwoOneOne", wl(2, 1, 1))
macro("WalksTwoOneThree", wl(2, 1, 3))
macro("WalksTwoTwoTwo", wl(2, 2, 2))
macro("WalksTwoThreeThree", wl(2, 3, 3))
macro("WalksThreeOneTwo", wl(3, 1, 2))
macro("WalksThreeTwoThree", wl(3, 2, 3))

# ---------- exhaustive check, N = 2..6 ----------
rows = []
for N in range(2, 7):
    pairs = list(combinations(range(N), 2))
    total = conn = ok_sum = ok_ia = ok_pat = wrong_short = 0
    for bits in product((0, 1), repeat=len(pairs)):
        M = [[0] * N for _ in range(N)]
        for b, (u, v) in zip(bits, pairs):
            if b:
                M[u][v] = M[v][u] = 1
        is_conn = len(bfs_components(M)) == 1
        total += 1
        conn += is_conn
        # sum test with N - 1 powers
        ok_sum += off_diag_positive(sum_powers(M, N - 1)) == is_conn
        # (I + A)^(N-1) test
        IA = add(ident(N), M)
        ok_ia += no_zero(power(IA, N - 1)) == is_conn
        # repeated squaring: exponent 2^t >= N - 1
        E = IA
        e = 1
        while e < N - 1:
            E = mul(E, E)
            e *= 2
        ok_pat += no_zero(E) == is_conn
        # N - 2 powers (empty sum for N = 2)
        short = off_diag_positive(sum_powers(M, N - 2)) if N > 2 else (N == 1)
        wrong_short += short != is_conn
    assert ok_sum == ok_ia == ok_pat == total
    rows.append(rf"{N} & {total} & {conn} & {ok_sum} & {ok_ia} & {ok_pat} & {wrong_short} \\")
macro("RowsExhaustive", "\n".join(rows))
assert "3 & 8 & 4 & 8" in rows[1] and rows[1].endswith(r"3 \\")
assert "6 & 32768 & 26704" in rows[4]

# ---------- cost remark ----------
rows = []
for N in (10, 100, 1000):
    direct = (N - 2) * N ** 3
    t = 0
    while 2 ** t < N - 1:
        t += 1
    squar = t * N ** 3
    rows.append(rf"{N} & {N - 2} & {direct:,} & {t} & {squar:,} & {N * N:,} \\".replace(",", r"\,"))
macro("RowsCost", "\n".join(rows))
assert (100 - 2) * 100 ** 3 == 98_000_000 and 7 * 100 ** 3 == 7_000_000

# ---------- write macros ----------
out = ["% Generated by appendices/scripts/generate_paper_numbers.py. Do not edit."]
for name, body in macros.items():
    out.append(r"\newcommand{\%s}{%s}" % (name, body))
path = Path(__file__).resolve().parent / "numbers.tex"
path.write_text("\n".join(out) + "\n")
print("wrote", path.name, "with", len(macros), "macros")
for name, body in macros.items():
    print(name, "=", body.replace("\n", " | "))
