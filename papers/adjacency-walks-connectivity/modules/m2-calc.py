"""m2 checks: classification of walks, trails, paths, cycles; board graph counts;
brute-force check of the walk-to-path lemma. Run: python3 m2-calc.py"""
import itertools


def is_walk(E, seq):
    return all(frozenset((a, b)) in E for a, b in zip(seq, seq[1:]))

def edges_of(seq):
    return [frozenset((a, b)) for a, b in zip(seq, seq[1:])]

def is_trail(E, seq):
    es = edges_of(seq)
    return is_walk(E, seq) and len(set(es)) == len(es)

def is_path(E, seq):  # course convention: no repeated vertex
    return is_walk(E, seq) and len(set(seq)) == len(seq)

def is_closed(seq):
    return seq[0] == seq[-1]

def is_simple_cycle(E, seq):  # book 1.2.15: closed trail, only first=last repeat
    return (is_trail(E, seq) and is_closed(seq) and len(seq) > 1
            and len(set(seq[:-1])) == len(seq) - 1)

# ---- Part 1: textbook Fig. 1.2.5 (edge list is my reading of the figure)
def e(*pairs): return {frozenset(p) for p in pairs}
G = e((1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(1,5))
print("PART 1: textbook examples on Fig. 1.2.5 (edges read from the figure:", sorted(tuple(sorted(x)) for x in G), ")")
tests = [
 ("walk? 1,3,2,4,3,2,4,3,5", [1,3,2,4,3,2,4,3,5], "walk"),
 ("walk? 3,1,4,2,3,5", [3,1,4,2,3,5], "walk"),
 ("trail (book path)? 1,3,2,4,3,5", [1,3,2,4,3,5], "trail"),
 ("trail (book path)? 1,3,2,4,3,2,4,3,5", [1,3,2,4,3,2,4,3,5], "trail"),
 ("course path? 1,3,2,4,3,5", [1,3,2,4,3,5], "path"),
 ("course path? 1,3,4,5", [1,3,4,5], "path"),
 ("simple cycle? 3,2,1,3,5,4,3", [3,2,1,3,5,4,3], "cycle"),
 ("simple cycle? 1,3,4,2,1", [1,3,4,2,1], "cycle"),
]
f = dict(walk=is_walk, trail=is_trail, path=is_path, cycle=is_simple_cycle)
for label, seq, kind in tests:
    print(" ", label, "->", f[kind](G, seq))
print("  closed trail 3,2,1,3,5,4,3 (book's cycle, Def 1.2.14)?", is_trail(G,[3,2,1,3,5,4,3]) and is_closed([3,2,1,3,5,4,3]))

# ---- Part 2: board graph, edges n1n2 and n2n3
B = e((1,2),(2,3))
def all_walks(E, V, k):
    out = [[v] for v in V]
    for _ in range(k):
        out = [w+[x] for w in out for x in V if frozenset((w[-1], x)) in E]
    return out
print("\nPART 2: board graph, edges n1n2, n2n3. Counts by length k, pair (start,end)")
V = [1,2,3]
print(" k pair  walks trails paths")
for pair in [(1,1),(2,2),(1,3),(1,2)]:
    for k in range(0,5):
        W = [w for w in all_walks(B, V, k) if (w[0], w[-1]) == pair]
        print(f" {k} {pair}  {len(W):5d} {sum(is_trail(B,w) for w in W):6d} {sum(is_path(B,w) for w in W):5d}")

# ---- Part 3: brute force on all labelled simple graphs, N <= 5
def paths_between(E, V, u, v, trail=False):
    res = []
    def dfs(seq, used):
        if seq[-1] == v:
            res.append(list(seq))
            if not trail: return
        for x in V:
            ed = frozenset((seq[-1], x))
            if ed not in E: continue
            if trail:
                if ed in used: continue
                dfs(seq+[x], used | {ed})
            elif x not in seq:
                dfs(seq+[x], used)
    dfs([u], frozenset())
    return res

def walk_lengths_exist(E, V, u, K):
    cur = {u}; lens = {}
    for k in range(K+1):
        for v in cur: lens.setdefault(v, []).append(k)
        cur = {x for y in cur for x in V if frozenset((y,x)) in E}
    return lens

checked = bad = 0
for N in range(1, 6):
    V = list(range(N))
    pairs = list(itertools.combinations(V, 2))
    for mask in range(1 << len(pairs)):
        E = {frozenset(p) for i, p in enumerate(pairs) if mask >> i & 1}
        for u in V:
            wl = walk_lengths_exist(E, V, u, 7)
            for v in V:
                P = paths_between(E, V, u, v)
                T = paths_between(E, V, u, v, trail=True)
                minP = min((len(p)-1 for p in P), default=None)
                minT = min((len(t)-1 for t in T), default=None)
                minW = min(wl.get(v, [None]))
                if v not in wl: minW = None
                checked += 1
                ok = (minP == minT == minW)
                for k in wl.get(v, []):
                    ok = ok and minP is not None and minP <= k
                for p in P:
                    ok = ok and is_trail(E, p) and len(p)-1 <= N-1
                if not ok: bad += 1
print("\nPART 3: brute force, all labelled simple graphs with N=1..5 (ordered pairs u,v incl. u=v)")
print(" pairs checked:", checked, " failures:", bad)
print(" checks: walk of length k<=7 exists => path of length <=k exists; min walk = min trail = min path; every path is a trail; path length <= N-1")
