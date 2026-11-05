"""Recomputes every number, matrix and example written in the paper.

Run from the paper folder:  python3 -I appendices/computations.py
Output is saved in appendices/computations.out.txt.
Pure Python, exact integers. Graphs are simple and undirected, so a walk
is its vertex sequence.
"""
from itertools import combinations, product


def adjacency(n, edges):
    a = [[0] * n for _ in range(n)]
    for u, v in edges:
        a[u - 1][v - 1] = a[v - 1][u - 1] = 1
    return a


def mul(x, y):
    n = len(x)
    return [[sum(x[i][t] * y[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def power(a, k):
    r = ident(len(a))
    for _ in range(k):
        r = mul(r, a)
    return r


def add(x, y):
    return [[p + q for p, q in zip(r, s)] for r, s in zip(x, y)]


def show(name, m):
    print(name + " =")
    for r in m:
        print("   ", " ".join(f"{v:3d}" for v in r))


def s_matrix(a):
    n = len(a)
    s = [[0] * n for _ in range(n)]
    for k in range(1, n):
        s = add(s, power(a, k))
    return s


def walks(a, k):
    n = len(a)
    ws = [(v,) for v in range(n)]
    for _ in range(k):
        ws = [w + (x,) for w in ws for x in range(n) if a[w[-1]][x]]
    return ws


def is_trail(w):
    es = [frozenset(p) for p in zip(w, w[1:])]
    return len(set(es)) == len(es)


def is_path(w):
    return len(set(w)) == len(w)


def bfs_connected(a):
    seen, todo = {0}, [0]
    while todo:
        u = todo.pop(0)
        for v in range(len(a)):
            if a[u][v] and v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == len(a)


def examples():
    for title, n, edges in (
            ("Board graph (edges n1n2, n2n3)", 3, [(1, 2), (2, 3)]),
            ("Disconnected graph (edge n1n2, n3 alone)", 3, [(1, 2)]),
            ("Triangle (the drawing read as three edges)", 3,
             [(1, 2), (1, 3), (2, 3)])):
        a = adjacency(n, edges)
        print("=" * 60)
        print(title)
        show("A", a)
        print("row sums (degrees):", [sum(r) for r in a])
        for k in (2, 3):
            show(f"A^{k}", power(a, k))
        s = s_matrix(a)
        show("S = A + ... + A^(N-1)", s)
        ia = add(ident(n), a)
        show("I + A", ia)
        show("(I+A)^(N-1)", power(ia, n - 1))
        zeros = [(i + 1, j + 1) for i in range(n) for j in range(n)
                 if i < j and s[i][j] == 0]
        print("pairs i<j with S_ij = 0:", zeros)
        print("BFS says connected:", bfs_connected(a))
    a = adjacency(3, [(1, 2), (2, 3)])
    print("=" * 60)
    print("Board graph, walks written out (towns numbered 1..3)")
    for k, i, j in ((2, 0, 0), (2, 0, 2), (3, 0, 1), (2, 0, 1)):
        ws = [tuple(x + 1 for x in w) for w in walks(a, k)
              if w[0] == i and w[-1] == j]
        print(f"walks of length {k} from n{i+1} to n{j+1}:", ws,
              " trails:", [w for w in ws if is_trail(w)],
              " paths:", [w for w in ws if is_path(w)])
    tri = adjacency(3, [(1, 2), (1, 3), (2, 3)])
    ws = [tuple(x + 1 for x in w) for w in walks(tri, 3)
          if w[0] == 0 and w[-1] == 0]
    print("triangle, walks of length 3 from n1 to n1:", ws)


def five_town():
    edges = [(1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
    a = adjacency(5, edges)
    print("=" * 60)
    print("Five-town map, edges", edges)
    show("A", a)
    print("degrees:", [sum(r) for r in a])

    def is_walk(w):
        return all(a[p - 1][q - 1] for p, q in zip(w, w[1:]))
    cases = {
        "walk 1,3,2,4,3,2,4,3,5": (1, 3, 2, 4, 3, 2, 4, 3, 5),
        "sequence 3,1,4,2,3,5": (3, 1, 4, 2, 3, 5),
        "1,3,2,4,3,5": (1, 3, 2, 4, 3, 5),
        "1,3,4,5": (1, 3, 4, 5),
        "3,2,1,3,5,4,3": (3, 2, 1, 3, 5, 4, 3),
        "1,3,4,2,1": (1, 3, 4, 2, 1),
        "1,3,2": (1, 3, 2),
    }
    for name, w in cases.items():
        z = tuple(x - 1 for x in w)
        print(f"{name}: walk={is_walk(w)} length={len(w)-1}",
              f"trail={is_walk(w) and is_trail(z)}",
              f"path={is_walk(w) and is_path(z)}",
              f"closed={w[0] == w[-1]}")
    print("distance n1 to n5: 1 (edge n1n5);  distance n2 to n5:",
          min(k for k in range(1, 5) if power(a, k)[1][4] > 0))
    print("longest path length:",
          max(len(w) - 1 for k in range(5) for w in walks(a, k)
              if is_path(w)))
    print("length  walks  trails  paths  (A^k)_15")
    for k in range(1, 9):
        ws = [w for w in walks(a, k) if w[0] == 0 and w[-1] == 4]
        print(f"{k:5d} {len(ws):6d} {sum(map(is_trail, ws)):7d} "
              f"{sum(map(is_path, ws)):6d} {power(a, k)[0][4]:9d}")
    print("5-town map connected by BFS:", bfs_connected(a))


def exhaustive():
    print("=" * 60)
    print("Exhaustive check: S-test, (I+A)^(N-1) test, BFS")
    for n in range(1, 7):
        pairs = list(combinations(range(1, n + 1), 2))
        total = conn = bad = 0
        for mask in range(2 ** len(pairs)):
            edges = [p for b, p in enumerate(pairs) if mask >> b & 1]
            a = adjacency(n, edges)
            truth = bfs_connected(a)
            s = s_matrix(a)
            t1 = all(s[i][j] > 0 for i in range(n) for j in range(n) if i != j)
            m = power(add(ident(n), a), n - 1)
            t2 = all(v > 0 for r in m for v in r)
            total += 1
            conn += truth
            bad += (t1 != truth) or (t2 != truth)
        print(f"N={n}: graphs {total}, connected {conn}, disagreements {bad}")
    print("Path graphs: first k with (A^k)_(1,N) > 0")
    for n in range(3, 7):
        a = adjacency(n, [(i, i + 1) for i in range(1, n)])
        k = next(k for k in range(1, n + 1) if power(a, k)[0][n - 1] > 0)
        print(f"  N={n}: k={k}, N-1={n-1}")


def binomial_check():
    a = adjacency(3, [(1, 2), (2, 3)])
    lhs = power(add(ident(3), a), 2)
    rhs = add(add(ident(3), [[2 * v for v in r] for r in a]), power(a, 2))
    print("=" * 60)
    print("(I+A)^2 = I + 2A + A^2 on the board graph:", lhs == rhs)


def lemma_check():
    """Cut out the loop between a repeated vertex; compare with the lemma."""
    print("=" * 60)
    a = adjacency(5, [(1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 4),
                      (3, 5), (4, 5)])
    count = 0
    for k in range(0, 8):
        for w in walks(a, k):
            x = list(w)
            while len(set(x)) < len(x):
                seen = {}
                for idx, v in enumerate(x):
                    if v in seen:
                        x = x[:seen[v]] + x[idx:]
                        break
                    seen[v] = idx
            assert x[0] == w[0] and x[-1] == w[-1] and len(x) - 1 <= k
            count += 1
    print(f"lemma check: {count} walks of length <= 7 in the five-town map "
          "shortened to a path with the same ends and length at most k")
    w = (1, 3, 2, 4, 3, 2, 4, 3, 5)
    print("example walk", w, "contains the path (1, 3, 5)")


if __name__ == "__main__":
    examples()
    five_town()
    binomial_check()
    lemma_check()
    exhaustive()
