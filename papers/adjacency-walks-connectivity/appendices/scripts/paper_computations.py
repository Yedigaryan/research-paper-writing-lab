"""Every number, matrix and classification printed in the paper.

Run from the paper folder:
    python3 -I appendices/scripts/paper_computations.py > appendices/scripts/paper_computations_output.txt
It also writes appendices/generated-matrices.tex, which the paper inputs, so
that no matrix in the text is typed by hand. Pure Python, integer arithmetic.
"""
from collections import deque
from itertools import product
from pathlib import Path


def mul(X, Y):
    n = len(X)
    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def power(X, k):
    R = ident(len(X))
    for _ in range(k):
        R = mul(R, X)
    return R


def add(X, Y):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]


def adjacency(n, edges):
    A = [[0] * n for _ in range(n)]
    for (a, b) in edges:
        A[a - 1][b - 1] = A[b - 1][a - 1] = 1
    return A


def adjacent(edges, a, b):
    return (a, b) in edges or (b, a) in edges


def is_walk(seq, edges):
    return all(adjacent(edges, a, b) for a, b in zip(seq, seq[1:]))


def edge_list(seq):
    return [frozenset(p) for p in zip(seq, seq[1:])]


def is_trail(seq, edges):
    e = edge_list(seq)
    return is_walk(seq, edges) and len(set(e)) == len(e)


def is_path(seq, edges):
    return is_walk(seq, edges) and len(set(seq)) == len(seq)


def walks(n, edges, k, i, j):
    out = []
    for mid in product(range(1, n + 1), repeat=k - 1):
        seq = (i,) + mid + (j,)
        if is_walk(seq, edges):
            out.append(seq)
    return out


def cut(seq):
    """The reduction in the proof of the walk-to-path lemma: remove a loop."""
    seq = list(seq)
    while len(set(seq)) < len(seq):
        for a in range(len(seq)):
            b = next((b for b in range(a + 1, len(seq)) if seq[b] == seq[a]), None)
            if b is not None:
                seq = seq[:a + 1] + seq[b + 1:]
                break
    return tuple(seq)


def bfs(A, s):
    n = len(A)
    seen, q, order = {s}, deque([s]), [s]
    while q:
        v = q.popleft()
        for w in range(n):
            if A[v][w] == 1 and w not in seen:
                seen.add(w)
                q.append(w)
                order.append(w)
    return order


def show(name, M):
    print(name)
    for r in M:
        print("   ", " ".join(f"{x:2d}" for x in r))


GRAPHS = {
    "Board": (3, [(1, 2), (2, 3)]),
    "Tri": (3, [(1, 2), (1, 3), (2, 3)]),
    "Disc": (3, [(1, 2)]),
    "H": (4, [(1, 2), (1, 3), (2, 3), (3, 4)]),
}
WORDS = {1: "one", 2: "two", 3: "three", 4: "four"}
macros = {}


def tex(M):
    return r"\begin{pmatrix}" + r" \\ ".join(" & ".join(map(str, r)) for r in M) + r"\end{pmatrix}"


for name, (n, edges) in GRAPHS.items():
    A = adjacency(n, edges)
    print("=" * 60)
    print(name, "N =", n, "edges", edges)
    show("A", A)
    print("symmetric:", all(A[i][j] == A[j][i] for i in range(n) for j in range(n)),
          "zero diagonal:", all(A[i][i] == 0 for i in range(n)),
          "row sums:", [sum(r) for r in A], "sum of entries:", sum(map(sum, A)), "2|E| =", 2 * len(edges))
    macros[f"mat{name}A"] = A
    ok = True
    for k in range(1, 5):
        P = power(A, k)
        for i in range(n):
            for j in range(n):
                if P[i][j] != len(walks(n, edges, k, i + 1, j + 1)):
                    ok = False
        show(f"A^{k}", P)
        if name != "H" or k <= 2:
            macros[f"mat{name}A{WORDS[k]}"] = P
    print("entry == brute-force walk count for all i, j, k = 1..4:", ok)
    print("diag of A^2:", [power(A, 2)[i][i] for i in range(n)])
    B = [[0] * n for _ in range(n)]
    for k in range(1, n):
        B = add(B, power(A, k))
    R = power(add(ident(n), A), n - 1)
    show(f"B = A + ... + A^{n-1}", B)
    show(f"R = (I + A)^{n-1}", R)
    macros[f"mat{name}B"] = B
    macros[f"mat{name}R"] = R
    offB = all(B[i][j] > 0 for i in range(n) for j in range(n) if i != j)
    allR = all(R[i][j] > 0 for i in range(n) for j in range(n))
    print("off-diagonal of B all positive:", offB, "| R all positive:", allR)
    print("BFS from n_1 visits:", [v + 1 for v in bfs(A, 0)])
    print("least k in 1..N-1 with (A^k)_ij > 0 per pair:")
    for i in range(n):
        for j in range(i + 1, n):
            ks = [k for k in range(1, n) if power(A, k)[i][j] > 0]
            print(f"   (n_{i+1}, n_{j+1}):", ks[0] if ks else "none")

print("=" * 60)
print("Walks behind the entries of the board graph")
n, E = GRAPHS["Board"]
for k, i, j in [(2, 1, 1), (2, 1, 3), (2, 2, 2), (2, 1, 2), (3, 1, 2), (3, 2, 3), (1, 1, 2)]:
    w = walks(n, E, k, i, j)
    print(f"k={k} (n_{i}, n_{j}): count {len(w)} walks {w} paths among them {[s for s in w if is_path(s, E)]}")
print("A^4 is the zero matrix:", all(x == 0 for r in power(adjacency(n, E), 4) for x in r), "N - 1 =", n - 1)
print("paths from n_1 to n_2 of any length:", [s for k in range(1, 4) for s in walks(n, E, k, 1, 2) if is_path(s, E)])

print("=" * 60)
print("Triangle: walks behind (A^3)_11 and (A^3)_12")
n, E = GRAPHS["Tri"]
print(walks(n, E, 3, 1, 1))
print(walks(n, E, 3, 1, 2))

print("=" * 60)
print("Classification of the examples used in the definitions (graph H)")
n, E = GRAPHS["H"]
tests = [
    ("walk", (1, 2, 3, 1, 3, 4)), ("walk", (4, 3, 4)), ("walk", (2,)), ("not a walk", (1, 4)),
    ("not a walk", (1, 2, 4)),
    ("closed walk", (1, 2, 1)), ("closed walk", (3, 4, 3)), ("not closed", (1, 2, 3)),
    ("trail", (4, 3, 1, 2, 3)), ("trail", (1, 2, 3, 1)), ("not a trail", (1, 2, 1)),
    ("not a trail", (1, 2, 3, 1, 3, 4)),
    ("path", (1, 3, 4)), ("path", (4, 3, 2, 1)), ("not a path", (4, 3, 1, 2, 3)), ("not a path", (1, 2, 3, 1)),
]
for label, s in tests:
    print(f"{label:12s} {s}  walk={is_walk(s, E)} closed={s[0] == s[-1]} trail={is_trail(s, E)} path={is_path(s, E)}")
print("cut of (1,2,3,1,3,4):", cut((1, 2, 3, 1, 3, 4)))
print("cut of (4,3,1,2,3,4):", cut((4, 3, 1, 2, 3, 4)))
nb, Eb = GRAPHS["Board"]
print("board graph: walk (1,2,1,2,3) -> cut", cut((1, 2, 1, 2, 3)), " is_walk", is_walk((1, 2, 1, 2, 3), Eb))
print("board graph: (1,3) is a walk:", is_walk((1, 3), Eb), "; (1,2,3) path:", is_path((1, 2, 3), Eb),
      "; (1,2,1,2,3) path:", is_path((1, 2, 1, 2, 3), Eb))
print("H: simple cycles found as closed trails of length 3:",
      [s for s in product(range(1, 5), repeat=4) if is_trail(s, E) and s[0] == s[-1] and len(set(s[:-1])) == 3])
print("distances in H from n_4:", {v: min(k for k in range(0, 4) if (k == 0 and v == 4) or (k > 0 and power(adjacency(4, E), k)[3][v - 1] > 0)) for v in range(1, 5)})
print("degrees in H:", [sum(r) for r in adjacency(4, E)])

print("=" * 60)
print("Path graph on N vertices: least k with (A^k)_(1,N) > 0")
for N in range(2, 8):
    A = adjacency(N, [(i, i + 1) for i in range(1, N)])
    print(N, next(k for k in range(1, N + 1) if power(A, k)[0][N - 1] > 0))

print("=" * 60)
print("Boundary: two-vertex-road example, B of connected board graph uses A + A^2; A^2 alone, (A^2)_12 =",
      power(adjacency(3, GRAPHS['Board'][1]), 2)[0][1])

out = ["% Generated by appendices/scripts/paper_computations.py. Do not edit by hand."]
for k, M in macros.items():
    out.append(r"\newcommand{\%s}{%s}" % (k, tex(M)))
Path("appendices/generated-matrices.tex").write_text("\n".join(out) + "\n")
print("wrote appendices/generated-matrices.tex with", len(macros), "matrices")
