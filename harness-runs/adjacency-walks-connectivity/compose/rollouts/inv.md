# Rollout `inv`: papers/adjacency-walks-connectivity

One run of the research-paper pipeline. Sections, in order: the commits that
built the paper (what changed in each revision round), the reports the agents
returned, the evaluation report with every round's scores and findings, the
technician reader's findings, the author's self-evaluation, and the module
reports. Scores and findings inside the evaluation report are the pipeline's
own evaluator speaking, recorded as it produced them.

# Commits

## Commit 1: 716b7a1 2026-10-31
Probe inv: author-stage rollout of adjacency-walks-connectivity

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01V3X5pws9JeJUCaMoyjTump

```
papers/adjacency-walks-connectivity/appendices/course-terms.tex             |  37 +++
 papers/adjacency-walks-connectivity/appendices/derivations.tex              | 116 +++++++++
 papers/adjacency-walks-connectivity/appendices/photographs.tex              |  34 +++
 papers/adjacency-walks-connectivity/appendices/reproducibility.tex          |  14 +
 papers/adjacency-walks-connectivity/appendices/scripts/author_numbers.py    | 108 ++++++++
 .../appendices/scripts/author_numbers_output.txt                            |  22 ++
 .../adjacency-walks-connectivity/appendices/scripts/generated_numbers.tex   |  17 ++
 papers/adjacency-walks-connectivity/appendices/scripts/m1_walks.py          | 116 +++++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m1_walks_output.txt  |  76 ++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m2_walks.py          | 295 +++++++++++++++++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m2_walks_output.txt  |  75 ++++++
 .../adjacency-walks-connectivity/appendices/scripts/m3_connectivity.out.txt | 116 +++++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.py   | 228 ++++++++++++++++
 papers/adjacency-walks-connectivity/evaluation-report.md                    | 143 ++++++++++
 papers/adjacency-walks-connectivity/evidence/evidence.base.json             |   8 +-
 papers/adjacency-walks-connectivity/evidence/evidence.json                  |  38 +--
 papers/adjacency-walks-connectivity/evidence/modules/m1.json                |  10 +-
 papers/adjacency-walks-connectivity/evidence/modules/m2.json                |  10 +-
 papers/adjacency-walks-connectivity/evidence/modules/m3.json                |  10 +-
 papers/adjacency-walks-connectivity/figures/generated_numbers.tex           |  17 ++
 papers/adjacency-walks-connectivity/main.pdf                                | Bin 0 -> 776560 bytes
 papers/adjacency-walks-connectivity/main.tex                                |  78 ++++++
 papers/adjacency-walks-connectivity/reader-findings.md                      |  84 ++++++
 papers/adjacency-walks-connectivity/references.bib                          |  95 +++++++
 papers/adjacency-walks-connectivity/reports/paper-author-round1.md          |  31 +++
 papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md       |  48 ++++
 papers/adjacency-walks-connectivity/reports/technician-reader-round1.md     |  78 ++++++
 papers/adjacency-walks-connectivity/sections/answer1_walks.tex              | 194 ++++++++++++++
 papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex       | 303 ++++++++++++++++++++++
 papers/adjacency-walks-connectivity/sections/answer3_path.tex               |  48 ++++
 papers/adjacency-walks-connectivity/sections/background.tex                 | 503 ++++++++++++++++++++++++++++++++++++
 papers/adjacency-walks-connectivity/sections/conclusion.tex                 |  21 ++
 papers/adjacency-walks-connectivity/sections/discussion.tex                 |  69 +++++
 papers/adjacency-walks-connectivity/sections/example.tex                    | 166 ++++++++++++
 papers/adjacency-walks-connectivity/sections/introduction.tex               | 142 ++++++++++
 papers/adjacency-walks-connectivity/self-evaluation.md                      | 147 +++++++++++
 36 files changed, 3459 insertions(+), 38 deletions(-)
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/course-terms.tex b/papers/adjacency-walks-connectivity/appendices/course-terms.tex
new file mode 100644
index 0000000..18f4275
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/course-terms.tex
@@ -0,0 +1,37 @@
+\section{The textbook's terms and numbers}\label{app:terms}
+
+\Cref{tab:terms} lists every textbook definition and result used in the paper, with its printed page, so that each can be checked against the book \cite{petrosyan2015grafneri}.
+Page numbers are the printed numbers of the book; the PDF page is the printed page plus one.
+The textbook is in Armenian, and its text layer drops most symbols, so formulas were checked against the page images.
+Only the pages named below were read page by page, and the rest of the book was not read.
+
+\begin{table}[ht]
+\centering
+\caption{Textbook definitions and results used in this paper \cite{petrosyan2015grafneri}.}\label{tab:terms}
+\small
+\begin{tabular}{@{}p{0.22\textwidth}p{0.1\textwidth}p{0.36\textwidth}p{0.2\textwidth}@{}}
+\toprule
+Textbook item & Page & Content (English) & Paper\\
+\midrule
+Definition 1.1.1 & 9 & graph $G=(V,E)$, finite $V$, $E$ a set of unordered pairs of distinct vertices & \cref{def:graph}\\
+Definition 1.1.4 & 11 & adjacent vertices & \cref{def:adjacent}\\
+adjacency matrix (after Definition 1.1.6; number not recorded) & 11--12 & $a_{ij}=1$ if adjacent, else $0$; symmetric, zero diagonal; converse & \cref{def:adjmat}, \cref{prop:rowsums}\\
+Definition 1.2.10 & 21--22 & walk; vertices and edges may repeat; length counts edges with multiplicity & \cref{def:walk}\\
+Definition 1.2.11 & 22 & closed walk & \cref{def:closed}\\
+Definition 1.2.12 & 22 & ``path'': distinct edges (English: trail) & \cref{def:trail}\\
+Definition 1.2.13 & 22 & ``simple path'': distinct vertices (English: path) & \cref{def:path}\\
+Definition 1.2.14 & 22 & ``closed path or cycle'': closed trail & \cref{def:cycle}\\
+Definition 1.2.15 & 22 & ``simple cycle'': only first and last vertex repeat; $C_n$, $n\ge3$ & \cref{def:simplecycle}\\
+Definition 1.2.16 & 22--23 & distance & \cref{def:distance}\\
+Lemma 1.2.1 & 23 & from a walk between different vertices one can extract a simple path & \cref{lem:walkpath}\\
+Definition 2.1.1 & 48 & connected graph & \cref{def:connected}\\
+(no number) & 49 & connected components & \cref{def:component}\\
+Remark 2.1.1 & 49 & connected if and only if one component & \cref{rem:component}\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\paragraph{Board and textbook notation.}
+The board writes $(G,V)$ for the graph, $e_{ij}\in V$ for ``the edge $e_{ij}$ belongs to the edge set'', $|G|=N$ for the number of vertices, and $n_i,n_j$ for vertices \cite{whiteboard1,whiteboard2}.
+The textbook writes $G=(V,E)$, $e\in E$, $n=|V|$, and $v_i$ \cite{petrosyan2015grafneri}.
+The paper uses $G=(V,E)$ and $N$ for the number of vertices, and the board's $n_i$ for vertices (\cref{tab:notation}).
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/derivations.tex b/papers/adjacency-walks-connectivity/appendices/derivations.tex
new file mode 100644
index 0000000..4aa59f4
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/derivations.tex
@@ -0,0 +1,116 @@
+\section{Derivations and checks}\label{app:derivations}
+
+This appendix holds the proofs and computations that the main text only states.
+Every statement here is derived in this paper, except where a citation is given.
+
+\subsection{The distance properties}\label{app:distance}
+
+\begin{proposition}[Shortest walk, trail, and path agree]\label{prop:shortest}
+For vertices $u,v$ of a simple graph, the length of a shortest $(u,v)$-walk, of a shortest $(u,v)$-trail, and of a shortest $(u,v)$-path are equal.
+Each is $+\infty$ when the corresponding set is empty, and the three sets are empty together.
+So $d(u,v)$ of \cref{def:distance} is the same whether ``path'' in that definition is read as trail or as path.
+\end{proposition}
+
+\begin{proof}
+Every path is a trail (\cref{prop:pathtrail}) and every trail is a walk.
+So the lengths of paths are among the lengths of trails, which are among the lengths of walks.
+Hence the minimum over walks is at most the minimum over trails, which is at most the minimum over paths.
+By \cref{lem:walkpath} a shortest walk contains a path of at most the same length, so the minimum over paths is at most the minimum over walks.
+Therefore the three minima are equal.
+If there is no walk, there is no trail and no path.
+If there is a walk, \cref{lem:walkpath} gives a path, so the three sets are empty together.
+\end{proof}
+
+Another text makes the same remark in prose: a shortest walk from $u$ to $v$, if it exists, is also a shortest path \cite[Section 2.9.4]{grinberg2025graph}.
+
+\begin{proposition}[The distance properties]\label{prop:distprops}
+The three properties of \cref{def:distance} follow from the definition.
+\end{proposition}
+
+\begin{proof}
+Use \cref{prop:shortest} to compute $d$ by shortest walks.
+(1) Lengths are $0,1,2,\dots$ or $+\infty$, so $d\ge0$.
+The walk consisting of $u$ alone has length $0$, so $d(u,u)=0$.
+If $d(u,v)=0$ there is a walk of length $0$ from $u$ to $v$; it is the single vertex, so $v=u$.
+(2) If $u_0,\dots,u_k$ is a $(u,v)$-walk, then $u_k,\dots,u_0$ is a $(v,u)$-walk of the same length, since each step is an edge and edges are unordered.
+So the sets of walk lengths from $u$ to $v$ and from $v$ to $u$ are equal, and so are their minima.
+(3) If $d(u,w)$ or $d(w,v)$ is $+\infty$, the right side is $+\infty$ and the inequality holds.
+Otherwise take a shortest $(u,w)$-walk and a shortest $(w,v)$-walk and join them at $w$.
+The result is a $(u,v)$-walk of length $d(u,w)+d(w,v)$, and the shortest $(u,v)$-walk is no longer than this.
+\end{proof}
+
+\subsection{The counterexample to ``entries count paths''}\label{app:counterexample}
+
+For the board graph the script \texttt{m1\_walks.py} lists, for each $k$ from $1$ to $5$, all walks from $n_1$ to $n_2$ and tests each for distinct vertices (path) and distinct edges (trail).
+Its output is saved in \texttt{appendices/scripts/m1\_walks\_output.txt}.
+\Cref{tab:counterex} repeats the numbers; the author script \texttt{author\_numbers.py} recomputes them independently and agrees.
+
+\begin{table}[ht]
+\centering
+\caption{Walks from $n_1$ to $n_2$ in the board graph, and how many of them are paths (they are also the trails).}\label{tab:counterex}
+\begin{tabular}{@{}cccccc@{}}
+\toprule
+$k$ & 1 & 2 & 3 & 4 & 5\\
+\midrule
+$(A^k)_{12}$ = walks & 1 & 0 & 2 & 0 & 4\\
+paths among them & 1 & 0 & 0 & 0 & 0\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+For closed walks at $n_1$ the numbers of walks of length $1,\dots,4$ are $0,1,0,2$, and none of them is a path or a trail (script \texttt{m1\_walks.py}).
+The general fact is \cref{prop:warning}.
+
+\subsection{The chain of premises for the connectivity test}\label{app:testproof}
+
+The proof of \cref{thm:test} rests on the premises below, each marked with where it comes from.
+\begin{enumerate}
+\item \emph{Walk counting} (\cref{thm:walks}): the entry $(A^k)_{ij}$ counts walks of length $k$ \cite{quinlan_matrices_graphs,grinberg2025graph}; proved in \cref{sec:walks}.
+\item \emph{Non-negativity} (\cref{cor:counts}): every entry of every power is a non-negative whole number; derived from item 1.
+\item \emph{Walk to path} (\cref{lem:walkpath}): a walk contains a path of at most its length \cite[Corollary 2.9.7]{grinberg2025graph}; the textbook states it for $u\ne v$ \cite[p.~23]{petrosyan2015grafneri}; proved in \cref{sec:background}.
+\item \emph{Length bound} (\cref{cor:bound}): a path has at most $N-1$ edges \cite[Section 2.9.4]{grinberg2025graph}; proved in \cref{sec:background}.
+\item \emph{Path implies trail} (\cref{prop:pathtrail}): proved in \cref{sec:background}.
+\item \emph{Definition of connected} (\cref{def:connected}) \cite[p.~48]{petrosyan2015grafneri}.
+\end{enumerate}
+Forward direction: if $G$ is connected and $i\ne j$, items 6, 3 and 4 give a path of length $k$ with $1\le k\le N-1$, and items 1 and 2 give $(A^k)_{ij}\ge1$ and hence $S_{ij}\ge1$.
+Backward direction: if $S_{ij}>0$, items 1 and 2 give a walk, and items 3 and 5 give a path in either reading, so $G$ is connected.
+These are the steps of \cref{prop:pair}.
+
+\subsection{Proof of the $I+A$ form}\label{app:iplusa}
+
+\begin{proof}[Proof of \cref{prop:iplusa}]
+Put $m\ge N-1$ and expand $(I+A)^m=(I+A)(I+A)\cdots(I+A)$, with $m$ factors.
+Each term of the expansion chooses $I$ or $A$ from each factor and multiplies the choices in order.
+Because $IX=XI=X$ for every matrix $X$, a product with $k$ letters $A$ and $m-k$ letters $I$ equals $A^k$.
+The number of ways to choose which $k$ of the $m$ factors give $A$ is the binomial coefficient $\binom{m}{k}$.
+Therefore
+\[
+(I+A)^m=\binom{m}{0}I+\binom{m}{1}A+\binom{m}{2}A^2+\dots+\binom{m}{m}A^m .
+\]
+Take an entry $(i,j)$ with $i\ne j$.
+The identity has $0$ there, so
+\[
+\big((I+A)^m\big)_{ij}=\binom{m}{1}(A)_{ij}+\binom{m}{2}(A^2)_{ij}+\dots+\binom{m}{m}(A^m)_{ij}.
+\]
+Every coefficient $\binom{m}{k}$ with $1\le k\le m$ is a positive whole number, and every $(A^k)_{ij}$ is a non-negative whole number.
+So the sum is positive if and only if at least one $(A^k)_{ij}$ with $1\le k\le m$ is positive.
+For $m=N-1$ this is exactly $S_{ij}>0$.
+For $m>N-1$, if some $(A^k)_{ij}$ with $k\le m$ is positive, there is a walk from $n_i$ to $n_j$, hence by \cref{cor:bound} a walk of length at most $N-1$, so some $(A^{k'})_{ij}$ with $1\le k'\le N-1$ is positive, that is, $S_{ij}>0$; the converse is immediate because $N-1\le m$.
+On the diagonal the term $\binom{m}{0}I$ contributes $1$ and all other terms are non-negative, so every diagonal entry of $(I+A)^m$ is at least $1$ whatever the graph is.
+\end{proof}
+
+The idea of the $(I+A)^{N-1}$ form appears in lecture notes in a proof sketch \cite{bai2025adjacency}; the expansion above is derived here.
+
+\subsection{Cross-checks by script}\label{app:crosschecks}
+
+All checks are finite tests of statements that are proved in the text.
+\begin{itemize}
+\item \emph{Walk counting.}
+For every labelled simple graph on $N=2,3,4,5$ vertices ($2$, $8$, $64$, $1024$ graphs) the script \texttt{m1\_walks.py} enumerated all walks by depth-first search and compared with $A^k$ for $k=1,\dots,5$ when $N\le4$ and $k=1,\dots,3$ when $N=5$.
+All $40$, $360$, $5120$ and $76800$ tested cases of $(k,i,j)$ agree.
+\item \emph{Lemma and propositions of \cref{sec:background}.}
+The script \texttt{m2\_walks.py} applied the cutting construction of \cref{lem:walkpath} to all $73$ walks of length $0$ to $6$ in the board graph, all $381$ in the triangle and all $4695$ in the textbook graph, with $0$ failures.
+On $300$ random graphs with $N$ from $2$ to $7$ (seed $20261027$) and $192696$ walks of length $0$ to $5$ it found $0$ failures of the lemma, $0$ failures of \cref{prop:pathtrail}, $0$ paths longer than $N-1$ (\cref{cor:bound}), and $0$ disagreements between BFS distance and the shortest walk, trail and path (\cref{prop:shortest}).
+\item \emph{Connectivity test.}
+The script \texttt{m3\_connectivity.py} reports in \cref{tab:exhaustive} the exhaustive agreement with BFS for $N=2,\dots,6$, and for the path graph on $N=3,\dots,8$ vertices that the smallest $k$ with $(A^k)_{1N}>0$ is $N-1$, so that the $(1,N)$ entry of $A+\dots+A^{N-2}$ is $0$ and that of $A+\dots+A^{N-1}$ is $1$ each time.
+\end{itemize}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/photographs.tex b/papers/adjacency-walks-connectivity/appendices/photographs.tex
new file mode 100644
index 0000000..7ed18fa
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/photographs.tex
@@ -0,0 +1,34 @@
+\section{The whiteboard photographs}\label{app:photos}
+
+Two photographs show the same lecture board at slightly different angles \cite{whiteboard1,whiteboard2}.
+They are read together.
+\Cref{fig:board} reproduces both.
+
+\begin{figure}[ht]
+\centering
+\includegraphics[width=0.46\textwidth]{sources/whiteboard-1.jpg}\hfill
+\includegraphics[width=0.46\textwidth]{sources/whiteboard-2.jpg}
+\caption{The two photographs of the lecture board \cite{whiteboard1,whiteboard2}. A reflection of a person is visible on the right.}\label{fig:board}
+\end{figure}
+
+\paragraph{Transcription in reading order.}
+\begin{enumerate}
+\item $A_{ij}=1$ if $e_{ij}\in V$, and $0$ if $e_{ij}\notin V$; the board's $V$ is the edge set \cite{whiteboard1,whiteboard2}.
+\item A drawing with vertices labelled $1,2,3$, and next to it a matrix labelled ``adj.'' with rows $0\,1\,0$ / $1\,0\,1$ / $0\,1\,0$.
+\item ``Problem. Given graph $(G,V)$ with $N$ nodes i.e.\ $|G|=N$ and the graph is represented through it's adj.\ matrix. So you have $A$ matrix.''
+\item ``1) What does $A_{ij}$ represent'', with a small mark above $A$.
+\item ``2) How to know if graph is connected or not.''
+\item ``Def. Graph is called connected if for any $n_i,n_j$ there exists a path between nodes.''
+\end{enumerate}
+
+\paragraph{Clearly visible.}
+All the prose above, the matrix entries, and the vertex labels.
+
+\paragraph{Likely interpretation.}
+The mark above $A$ is an exponent $k$ (interpretation, qualified: the assignment text asks about $A^k$, but in both photographs the mark looks like a small $n$ or a pair of quotation marks).
+The arrowhead on the line $1$--$2$ is a stray mark, because the matrix is symmetric and the problem is about undirected graphs (interpretation).
+
+\paragraph{Unclear or in conflict.}
+The drawing shows a line from $1$ to $2$ with an arrowhead at $2$, a line from $1$ to $3$, and a line from $2$ to $3$, which would be three edges, while the matrix encodes only the edges $1$--$2$ and $2$--$3$ \cite{whiteboard1,whiteboard2}.
+Edge by edge: the edge $1$--$2$ is in both; the edge $2$--$3$ is in both; the edge $1$--$3$ is in the drawing only.
+The paper follows the matrix and reports the mismatch.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/reproducibility.tex b/papers/adjacency-walks-connectivity/appendices/reproducibility.tex
new file mode 100644
index 0000000..d1c8e74
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/reproducibility.tex
@@ -0,0 +1,14 @@
+\section{Reproducibility}\label{app:repro}
+
+Every number in the paper that is a matrix entry, a sum, or a count was computed by one of the scripts below.
+All are pure Python with integer arithmetic, so no rounding occurs.
+Run each one from the paper folder with \texttt{python3 -I}; the saved outputs sit beside the scripts.
+
+\begin{description}
+\item[\texttt{appendices/scripts/author\_numbers.py}] computes the matrices of \cref{sec:examples} and writes them to \texttt{figures/generated\_numbers.tex}, which the paper inputs; it also checks each power against a direct walk enumeration, and computes the walk and path counts of \cref{tab:counterex} and the cost counts of \cref{sec:cost}. Output: \texttt{author\_numbers\_output.txt}.
+\item[\texttt{appendices/scripts/m1\_walks.py}] board graph powers, explicit walks, walks against paths, brute-force check of \cref{thm:walks}. Output: \texttt{m1\_walks\_output.txt}.
+\item[\texttt{appendices/scripts/m2\_walks.py}] classification of sequences as walk, trail, path, cycle; the cutting construction of \cref{lem:walkpath}; \cref{tab:walkcounts}. Output: \texttt{m2\_walks\_output.txt}.
+\item[\texttt{appendices/scripts/m3\_connectivity.py}] the tests of \cref{sec:conn}, the examples, the sharpness table, the exhaustive check of \cref{tab:exhaustive}, and the cost counts. It takes about thirty seconds. Output: \texttt{m3\_connectivity.out.txt}.
+\end{description}
+
+The scripts are copies of the ones in the folder \texttt{modules/}, which are kept as the module records.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/author_numbers.py b/papers/adjacency-walks-connectivity/appendices/scripts/author_numbers.py
new file mode 100644
index 0000000..90aaf37
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/author_numbers.py
@@ -0,0 +1,108 @@
+"""Author script: computes every matrix and count that the paper prints and
+writes them as LaTeX macros to figures/generated_numbers.tex.
+Pure Python integers. Run from the paper folder:
+    python3 -I appendices/scripts/author_numbers.py
+"""
+from itertools import product
+from math import comb, ceil, log2
+
+
+def ident(n):
+    return [[int(i == j) for j in range(n)] for i in range(n)]
+
+
+def mul(X, Y):
+    n = len(X)
+    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]
+
+
+def add(X, Y):
+    return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]
+
+
+def power(A, k):
+    R = ident(len(A))
+    for _ in range(k):
+        R = mul(R, A)
+    return R
+
+
+def adj(n, edges):
+    A = [[0] * n for _ in range(n)]
+    for u, v in edges:
+        A[u - 1][v - 1] = A[v - 1][u - 1] = 1
+    return A
+
+
+def tex(M):
+    return "\\begin{pmatrix}" + " \\\\ ".join(" & ".join(str(x) for x in r) for r in M) + "\\end{pmatrix}"
+
+
+def walks(A, k, i, j):
+    """Number of vertex sequences of length k from i to j (0-based), by search."""
+    n = len(A)
+    def go(v, left):
+        if left == 0:
+            return int(v == j)
+        return sum(go(w, left - 1) for w in range(n) if A[v][w])
+    return go(i, k)
+
+
+out = {}
+# connected example: the board matrix
+B = adj(3, [(1, 2), (2, 3)])
+assert B == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
+Bp = {k: power(B, k) for k in range(1, 6)}
+SB = add(Bp[1], Bp[2])
+IB = power(add(ident(3), B), 2)
+assert IB == add(add(ident(3), [[2 * x for x in r] for r in B]), Bp[2])  # (I+A)^2 = I + 2A + A^2
+for k in range(1, 6):
+    for i, j in product(range(3), repeat=2):
+        assert Bp[k][i][j] == walks(B, k, i, j)
+assert Bp[3] == [[2 * x for x in r] for r in B]
+out.update(matA=B, matAtwo=Bp[2], matAthree=Bp[3], matAfour=Bp[4], matAfive=Bp[5], matSB=SB, matIB=IB)
+# disconnected example
+D = adj(3, [(1, 2)])
+Dp = {k: power(D, k) for k in range(1, 7)}
+SD = add(Dp[1], Dp[2])
+ID = power(add(ident(3), D), 2)
+assert all(Dp[k][i][2] == 0 for k in range(1, 7) for i in range(2))
+out.update(matD=D, matDtwo=Dp[2], matSD=SD, matID=ID)
+# path on four vertices
+P = adj(4, [(1, 2), (2, 3), (3, 4)])
+P2, P3 = power(P, 2), power(P, 3)
+out.update(matP=P, matPtwo=P2, matPthree=P3, matPsmall=add(P, P2), matPfull=add(add(P, P2), P3))
+# degrees and sums for the board matrix
+deg = [sum(r) for r in B]
+total = sum(map(sum, B))
+print("board degrees", deg, "total", total, "diag of A^2", [Bp[2][i][i] for i in range(3)])
+# walks and paths from 1 to 2 for k = 1..5 (vertex sequences, board graph)
+def seqs(k, s, t):
+    res = []
+    def go(w):
+        if len(w) == k + 1:
+            if w[-1] == t:
+                res.append(tuple(w))
+            return
+        for v in range(3):
+            if B[w[-1]][v]:
+                go(w + [v])
+    go([s])
+    return res
+rows = []
+for k in range(1, 6):
+    W = seqs(k, 0, 1)
+    rows.append((k, len(W), sum(len(set(w)) == len(w) for w in W)))
+print("walks 1->2 and paths among them", rows)
+assert [r[1] for r in rows] == [1, 0, 2, 0, 4] and [r[2] for r in rows] == [1, 0, 0, 0, 0]
+# cost counts
+for N in (10, 100, 1000):
+    t = ceil(log2(N - 1))
+    print("cost", N, (N - 2) * N**3, t * N**3, N * N, "squarings", t)
+print("K10 largest entry of A^9:", max(max(r) for r in power([[int(i != j) for j in range(10)] for i in range(10)], 9)))
+with open("figures/generated_numbers.tex", "w") as fh:
+    fh.write("% Generated by appendices/scripts/author_numbers.py. Do not edit.\n")
+    for name, M in out.items():
+        fh.write("\\newcommand{\\%s}{%s}\n" % (name, tex(M)))
+for name, M in out.items():
+    print(name, M)
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/author_numbers_output.txt b/papers/adjacency-walks-connectivity/appendices/scripts/author_numbers_output.txt
new file mode 100644
index 0000000..a20a36a
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/author_numbers_output.txt
@@ -0,0 +1,22 @@
+board degrees [1, 2, 1] total 4 diag of A^2 [1, 2, 1]
+walks 1->2 and paths among them [(1, 1, 1), (2, 0, 0), (3, 2, 0), (4, 0, 0), (5, 4, 0)]
+cost 10 8000 4000 100 squarings 4
+cost 100 98000000 7000000 10000 squarings 7
+cost 1000 998000000000 10000000000 1000000 squarings 10
+K10 largest entry of A^9: 38742049
+matA [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
+matAtwo [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
+matAthree [[0, 2, 0], [2, 0, 2], [0, 2, 0]]
+matAfour [[2, 0, 2], [0, 4, 0], [2, 0, 2]]
+matAfive [[0, 4, 0], [4, 0, 4], [0, 4, 0]]
+matSB [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
+matIB [[2, 2, 1], [2, 3, 2], [1, 2, 2]]
+matD [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
+matDtwo [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
+matSD [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
+matID [[2, 2, 0], [2, 2, 0], [0, 0, 1]]
+matP [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
+matPtwo [[1, 0, 1, 0], [0, 2, 0, 1], [1, 0, 2, 0], [0, 1, 0, 1]]
+matPthree [[0, 2, 0, 1], [2, 0, 3, 0], [0, 3, 0, 2], [1, 0, 2, 0]]
+matPsmall [[1, 1, 1, 0], [1, 2, 1, 1], [1, 1, 2, 1], [0, 1, 1, 1]]
+matPfull [[1, 3, 1, 1], [3, 2, 4, 1], [1, 4, 2, 3], [1, 1, 3, 1]]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/generated_numbers.tex b/papers/adjacency-walks-connectivity/appendices/scripts/generated_numbers.tex
new file mode 100644
index 0000000..67d686e
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/generated_numbers.tex
@@ -0,0 +1,17 @@
+% Generated by appendices/scripts/author_numbers.py. Do not edit.
+\newcommand{\matA}{\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}}
+\newcommand{\matAtwo}{\begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{pmatrix}}
+\newcommand{\matAthree}{\begin{pmatrix}0 & 2 & 0 \\ 2 & 0 & 2 \\ 0 & 2 & 0\end{pmatrix}}
+\newcommand{\matAfour}{\begin{pmatrix}2 & 0 & 2 \\ 0 & 4 & 0 \\ 2 & 0 & 2\end{pmatrix}}
+\newcommand{\matAfive}{\begin{pmatrix}0 & 4 & 0 \\ 4 & 0 & 4 \\ 0 & 4 & 0\end{pmatrix}}
+\newcommand{\matSB}{\begin{pmatrix}1 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 1\end{pmatrix}}
+\newcommand{\matIB}{\begin{pmatrix}2 & 2 & 1 \\ 2 & 3 & 2 \\ 1 & 2 & 2\end{pmatrix}}
+\newcommand{\matD}{\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\matDtwo}{\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\matSD}{\begin{pmatrix}1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\matID}{\begin{pmatrix}2 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 1\end{pmatrix}}
+\newcommand{\matP}{\begin{pmatrix}0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0\end{pmatrix}}
+\newcommand{\matPtwo}{\begin{pmatrix}1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 \\ 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 1\end{pmatrix}}
+\newcommand{\matPthree}{\begin{pmatrix}0 & 2 & 0 & 1 \\ 2 & 0 & 3 & 0 \\ 0 & 3 & 0 & 2 \\ 1 & 0 & 2 & 0\end{pmatrix}}
+\newcommand{\matPsmall}{\begin{pmatrix}1 & 1 & 1 & 0 \\ 1 & 2 & 1 & 1 \\ 1 & 1 & 2 & 1 \\ 0 & 1 & 1 & 1\end{pmatrix}}
+\newcommand{\matPfull}{\begin{pmatrix}1 & 3 & 1 & 1 \\ 3 & 2 & 4 & 1 \\ 1 & 4 & 2 & 3 \\ 1 & 1 & 3 & 1\end{pmatrix}}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/m1_walks.py b/papers/adjacency-walks-connectivity/appendices/scripts/m1_walks.py
new file mode 100644
index 0000000..38a2f02
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/m1_walks.py
@@ -0,0 +1,116 @@
+"""Module m1 calculations: adjacency matrix of the board graph, powers, walk
+enumeration, and a brute-force check of the walk-counting theorem.
+Pure Python (integers only). Run: python3 modules/m1_walks.py
+"""
+from itertools import product, combinations
+
+def matmul(X, Y):
+    n = len(X)
+    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)] for i in range(n)]
+
+def matpow(A, k):
+    n = len(A)
+    R = [[int(i == j) for j in range(n)] for i in range(n)]  # identity = A^0
+    for _ in range(k):
+        R = matmul(R, A)
+    return R
+
+def show(name, M):
+    print(name)
+    for row in M:
+        print("  ", " ".join(str(x) for x in row))
+
+def walks(A, k, i, j):
+    """All vertex sequences (w0,...,wk) with w0=i, wk=j, A[w_{t-1}][w_t]=1."""
+    n = len(A)
+    out = []
+    def go(seq):
+        if len(seq) == k + 1:
+            if seq[-1] == j:
+                out.append(tuple(seq))
+            return
+        for nxt in range(n):
+            if A[seq[-1]][nxt] == 1:
+                go(seq + [nxt])
+    go([i])
+    return out
+
+def is_path(seq):      # distinct vertices (course convention, Def. 1.2.13)
+    return len(set(seq)) == len(seq)
+
+def is_trail(seq):     # distinct edges (textbook Def. 1.2.12)
+    edges = [frozenset(p) for p in zip(seq, seq[1:])]
+    return len(set(edges)) == len(edges)
+
+# ---- board matrix (vertices 1,2,3 -> indices 0,1,2) ----
+A = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
+n = len(A)
+print("== Board matrix ==")
+show("A", A)
+print("symmetric:", all(A[i][j] == A[j][i] for i in range(n) for j in range(n)))
+print("zero diagonal:", all(A[i][i] == 0 for i in range(n)))
+print("row sums (degrees):", [sum(r) for r in A])
+print("column sums:", [sum(A[i][j] for i in range(n)) for j in range(n)])
+A2, A3 = matpow(A, 2), matpow(A, 3)
+show("A^2", A2)
+show("A^3", A3)
+print("A^3 == 2*A:", A3 == [[2 * x for x in r] for r in A])
+print("trace(A^2) =", sum(A2[i][i] for i in range(n)), " 2|E| =", sum(sum(r) for r in A))
+print("diag(A^2) == degrees:", [A2[i][i] for i in range(n)] == [sum(r) for r in A])
+for p in (4, 5):
+    show(f"A^{p}", matpow(A, p))
+
+print("\n== Explicit walks, labels 1..3 ==")
+lab = lambda s: "-".join(str(v + 1) for v in s)
+for k in (1, 2, 3):
+    Ak = matpow(A, k)
+    for i in range(n):
+        for j in range(i, n):
+            W = walks(A, k, i, j)
+            assert len(W) == Ak[i][j], (k, i, j)
+            if W:
+                flags = [("path" if is_path(w) else "not-path") + "/" + ("trail" if is_trail(w) else "not-trail") for w in W]
+                print(f"k={k} from {i+1} to {j+1}: entry={Ak[i][j]}  walks=" +
+                      ", ".join(f"{lab(w)} [{f}]" for w, f in zip(W, flags)))
+
+print("\n== Hand-checkable sums (induction step: sum over last-but-one vertex r) ==")
+def step_terms(k, i, j):
+    Akm1 = matpow(A, k - 1)
+    terms = [(r + 1, Akm1[i][r], A[r][j], Akm1[i][r] * A[r][j]) for r in range(n)]
+    print(f"(A^{k})_{i+1}{j+1} = sum_r (A^{k-1})_{i+1}r * A_r{j+1}:")
+    for r, a, b, c in terms:
+        print(f"   r={r}: {a} * {b} = {c}")
+    print("   total =", sum(t[3] for t in terms), " (matrix says", matpow(A, k)[i][j], ")")
+step_terms(2, 1, 1)   # (A^2)_22
+step_terms(3, 0, 1)   # (A^3)_12
+step_terms(2, 0, 0)   # (A^2)_11
+
+print("\n== Walks vs paths from 1 to 2 and from 1 to 1 on the board graph ==")
+for k in range(0, 6):
+    Wk = walks(A, k, 0, 1)
+    print(f"k={k}: walks 1->2 = {len(Wk)}, of which paths = {sum(is_path(w) for w in Wk)}, trails = {sum(is_trail(w) for w in Wk)}")
+for k in range(1, 5):
+    Wk = walks(A, k, 0, 0)
+    print(f"k={k}: closed walks 1->1 = {len(Wk)}, of which paths = {sum(is_path(w) for w in Wk)}, trails = {sum(is_trail(w) for w in Wk)}")
+# A^k symmetric and nonnegative on all powers up to 6
+print("A^k symmetric for k=1..6:", all(matpow(A,k)==[list(r) for r in zip(*matpow(A,k))] for k in range(1,7)))
+# odd/even pattern: A^(k+2) = 2 A^k for k>=1
+print("A^(k+2) == 2*A^k for k=1..5:", all(matpow(A,k+2)==[[2*x for x in r] for r in matpow(A,k)] for k in range(1,6)))
+
+# ---- brute-force check of the theorem on every simple graph with 2..5 vertices ----
+print("\n== Brute-force check of (A^k)_ij = number of walks, all labelled simple graphs ==")
+for N in range(2, 6):
+    pairs = list(combinations(range(N), 2))
+    checked = 0
+    for bits in product((0, 1), repeat=len(pairs)):
+        B = [[0] * N for _ in range(N)]
+        for (a, b), x in zip(pairs, bits):
+            B[a][b] = B[b][a] = x
+        for k in range(1, 6 if N <= 4 else 4):
+            P = matpow(B, k)
+            for i in range(N):
+                for j in range(N):
+                    assert len(walks(B, k, i, j)) == P[i][j]
+                    checked += 1
+    print(f"N={N}: {2**len(pairs)} graphs, {checked} (k,i,j) entries all agree")
+print("done")
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/m1_walks_output.txt b/papers/adjacency-walks-connectivity/appendices/scripts/m1_walks_output.txt
new file mode 100644
index 0000000..e22ec4f
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/m1_walks_output.txt
@@ -0,0 +1,76 @@
+== Board matrix ==
+A
+   0 1 0
+   1 0 1
+   0 1 0
+symmetric: True
+zero diagonal: True
+row sums (degrees): [1, 2, 1]
+column sums: [1, 2, 1]
+A^2
+   1 0 1
+   0 2 0
+   1 0 1
+A^3
+   0 2 0
+   2 0 2
+   0 2 0
+A^3 == 2*A: True
+trace(A^2) = 4  2|E| = 4
+diag(A^2) == degrees: True
+A^4
+   2 0 2
+   0 4 0
+   2 0 2
+A^5
+   0 4 0
+   4 0 4
+   0 4 0
+
+== Explicit walks, labels 1..3 ==
+k=1 from 1 to 2: entry=1  walks=1-2 [path/trail]
+k=1 from 2 to 3: entry=1  walks=2-3 [path/trail]
+k=2 from 1 to 1: entry=1  walks=1-2-1 [not-path/not-trail]
+k=2 from 1 to 3: entry=1  walks=1-2-3 [path/trail]
+k=2 from 2 to 2: entry=2  walks=2-1-2 [not-path/not-trail], 2-3-2 [not-path/not-trail]
+k=2 from 3 to 3: entry=1  walks=3-2-3 [not-path/not-trail]
+k=3 from 1 to 2: entry=2  walks=1-2-1-2 [not-path/not-trail], 1-2-3-2 [not-path/not-trail]
+k=3 from 2 to 3: entry=2  walks=2-1-2-3 [not-path/not-trail], 2-3-2-3 [not-path/not-trail]
+
+== Hand-checkable sums (induction step: sum over last-but-one vertex r) ==
+(A^2)_22 = sum_r (A^1)_2r * A_r2:
+   r=1: 1 * 1 = 1
+   r=2: 0 * 0 = 0
+   r=3: 1 * 1 = 1
+   total = 2  (matrix says 2 )
+(A^3)_12 = sum_r (A^2)_1r * A_r2:
+   r=1: 1 * 1 = 1
+   r=2: 0 * 0 = 0
+   r=3: 1 * 1 = 1
+   total = 2  (matrix says 2 )
+(A^2)_11 = sum_r (A^1)_1r * A_r1:
+   r=1: 0 * 0 = 0
+   r=2: 1 * 1 = 1
+   r=3: 0 * 0 = 0
+   total = 1  (matrix says 1 )
+
+== Walks vs paths from 1 to 2 and from 1 to 1 on the board graph ==
+k=0: walks 1->2 = 0, of which paths = 0, trails = 0
+k=1: walks 1->2 = 1, of which paths = 1, trails = 1
+k=2: walks 1->2 = 0, of which paths = 0, trails = 0
+k=3: walks 1->2 = 2, of which paths = 0, trails = 0
+k=4: walks 1->2 = 0, of which paths = 0, trails = 0
+k=5: walks 1->2 = 4, of which paths = 0, trails = 0
+k=1: closed walks 1->1 = 0, of which paths = 0, trails = 0
+k=2: closed walks 1->1 = 1, of which paths = 0, trails = 0
+k=3: closed walks 1->1 = 0, of which paths = 0, trails = 0
+k=4: closed walks 1->1 = 2, of which paths = 0, trails = 0
+A^k symmetric for k=1..6: True
+A^(k+2) == 2*A^k for k=1..5: True
+
+== Brute-force check of (A^k)_ij = number of walks, all labelled simple graphs ==
+N=2: 2 graphs, 40 (k,i,j) entries all agree
+N=3: 8 graphs, 360 (k,i,j) entries all agree
+N=4: 64 graphs, 5120 (k,i,j) entries all agree
+N=5: 1024 graphs, 76800 (k,i,j) entries all agree
+done
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/m2_walks.py b/papers/adjacency-walks-connectivity/appendices/scripts/m2_walks.py
new file mode 100644
index 0000000..829dafc
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/m2_walks.py
@@ -0,0 +1,295 @@
+#!/usr/bin/env python3
+"""Module m2 checks: walks, trails, paths, cycles, distance, and the lemma
+that every u-v walk contains a u-v path.
+
+Run:  python3 modules/m2_walks.py > modules/m2_walks_output.txt
+Pure standard library. Every number quoted in modules/m2.md comes from here.
+
+Naming used in the code (textbook / English):
+  walk                      Def 1.2.10   walk
+  closed walk               Def 1.2.11   closed walk
+  trail  (book: "path")     Def 1.2.12   distinct edges
+  path   (book: "simple path") Def 1.2.13 distinct vertices
+  cycle  (book: "cycle")    Def 1.2.14   closed trail
+  simple cycle              Def 1.2.15   closed trail, only first = last vertex repeats
+"""
+import itertools
+import random
+from collections import deque
+
+
+# ---------- graph helpers ------------------------------------------------
+def make_graph(vertices, edges):
+    """Simple undirected graph: edges are frozensets of two distinct vertices."""
+    return {"V": list(vertices), "E": {frozenset(e) for e in edges}}
+
+
+def adj(g):
+    nb = {v: set() for v in g["V"]}
+    for e in g["E"]:
+        a, b = tuple(e)
+        nb[a].add(b)
+        nb[b].add(a)
+    return nb
+
+
+def edges_of(seq):
+    return [frozenset((seq[i], seq[i + 1])) for i in range(len(seq) - 1)]
+
+
+# ---------- the definitions, written exactly as stated -------------------
+def is_walk(g, seq):                      # Def 1.2.10 (k >= 0)
+    return len(seq) >= 1 and all(e in g["E"] for e in edges_of(seq))
+
+
+def length(seq):                          # number of edges, with multiplicity
+    return len(seq) - 1
+
+
+def is_closed(seq):                       # Def 1.2.11
+    return seq[0] == seq[-1]
+
+
+def is_trail(g, seq):                     # Def 1.2.12 (textbook "path")
+    es = edges_of(seq)
+    return is_walk(g, seq) and len(set(es)) == len(es)
+
+
+def is_path(g, seq):                      # Def 1.2.13 (textbook "simple path")
+    return is_walk(g, seq) and len(set(seq)) == len(seq)
+
+
+def is_cycle(g, seq):                     # Def 1.2.14 (closed trail)
+    return is_trail(g, seq) and is_closed(seq)
+
+
+def is_simple_cycle(g, seq):              # Def 1.2.15 (+ k >= 3 from C_n, n >= 3)
+    return (is_cycle(g, seq) and length(seq) >= 3
+            and len(set(seq[:-1])) == len(seq) - 1)
+
+
+def classify(g, seq):
+    tags = []
+    if is_walk(g, seq):
+        tags.append("walk")
+        if is_closed(seq):
+            tags.append("closed")
+        if is_trail(g, seq):
+            tags.append("trail=book-path")
+        if is_path(g, seq):
+            tags.append("path=book-simple-path")
+        if is_cycle(g, seq) and length(seq) > 0:
+            tags.append("book-cycle")
+        if is_simple_cycle(g, seq):
+            tags.append("simple-cycle")
+    else:
+        tags.append("NOT a walk")
+    return tags
+
+
+def all_walks(g, k):
+    nb = adj(g)
+    out = [(v,) for v in g["V"]]
+    for _ in range(k):
+        out = [w + (x,) for w in out for x in sorted(nb[w[-1]])]
+    return out
+
+
+# ---------- the lemma: cut out a loop ------------------------------------
+def cut_once(seq):
+    """Find the smallest i < j with seq[i] == seq[j] (smallest j for that i)
+    and return seq[0..i] + seq[j+1..], as in Prop 2.9.5 / Lemma 1.2.1.
+    Returns None if no vertex repeats."""
+    for i in range(len(seq)):
+        for j in range(i + 1, len(seq)):
+            if seq[i] == seq[j]:
+                return seq[: i + 1] + seq[j + 1:], (i, j)
+    return None
+
+
+def reduce_to_path(seq, trace=None):
+    while True:
+        r = cut_once(seq)
+        if r is None:
+            return seq
+        new, ij = r
+        if trace is not None:
+            trace.append((seq, ij, new))
+        assert len(new) < len(seq)
+        seq = new
+
+
+def bfs_dist(g, s):
+    nb = adj(g)
+    d = {s: 0}
+    q = deque([s])
+    while q:
+        x = q.popleft()
+        for y in nb[x]:
+            if y not in d:
+                d[y] = d[x] + 1
+                q.append(y)
+    return d
+
+
+def mat_mult(X, Y):
+    n = len(X)
+    return [[sum(X[i][t] * Y[t][j] for t in range(n)) for j in range(n)]
+            for i in range(n)]
+
+
+def main():
+    print("=== 1. Board graph B: V = {1,2,3}, E = {12, 23} (from the matrix) ===")
+    B = make_graph([1, 2, 3], [(1, 2), (2, 3)])
+    examples = [
+        (1, 2, 3), (3, 2, 1), (1, 2, 1, 2, 3), (2, 1, 2), (2, 3, 2, 1, 2),
+        (1, 2, 1), (2,), (1, 2), (1, 3), (1, 2, 3, 2),
+    ]
+    for s in examples:
+        print(f"  {s!s:<16} length {length(s):<2} {', '.join(classify(B, s))}")
+
+    print("\n  Walks by length in B (all start/end pairs), counted by enumeration:")
+    for k in range(0, 5):
+        ws = all_walks(B, k)
+        n_trail = sum(is_trail(B, w) for w in ws)
+        n_path = sum(is_path(B, w) for w in ws)
+        print(f"   k={k}: walks={len(ws):<3} trails={n_trail:<3} paths={n_path:<3}"
+              f" closed walks={sum(is_closed(w) for w in ws)}")
+
+    print("\n  Walks from 1 to 3 of length <= 4 in B, with type:")
+    for k in range(0, 5):
+        for w in all_walks(B, k):
+            if w[0] == 1 and w[-1] == 3:
+                print(f"   {w!s:<18} length {k}  {', '.join(classify(B, w))}")
+
+    print("\n  Check: B has no cycle (every closed walk of length 1..6 repeats an edge):")
+    cyc = [w for k in range(1, 7) for w in all_walks(B, k) if is_cycle(B, w)]
+    print("   cycles of positive length found:", cyc)
+
+    print("\n  Consistency with m1 (A^k entry = number of walks); A =")
+    A = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
+    P = [[int(i == j) for j in range(3)] for i in range(3)]
+    ok = True
+    for k in range(1, 6):
+        P = mat_mult(P, A)
+        ws = all_walks(B, k)
+        for i in range(3):
+            for j in range(3):
+                cnt = sum(1 for w in ws if w[0] == i + 1 and w[-1] == j + 1)
+                ok &= (cnt == P[i][j])
+    print("   enumeration equals A^k for k=1..5, all i,j:", ok)
+
+    print("\n=== 2. Triangle T (the board DRAWING): V={1,2,3}, E={12,13,23} ===")
+    T = make_graph([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
+    for s in [(1, 2, 3, 1), (1, 2, 1), (1, 2, 3), (1, 2, 3, 2, 1)]:
+        print(f"  {s!s:<16} length {length(s):<2} {', '.join(classify(T, s))}")
+
+    print("\n=== 3. Textbook example graph (edges forced by the textbook examples) ===")
+    G = make_graph([1, 2, 3, 4, 5],
+                   [(1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (1, 2), (4, 5)])
+    tb = [
+        (1, 3, 2, 4, 3, 2, 4, 3, 5),   # walk, not a trail (Def 1.2.10/1.2.12)
+        (3, 1, 4, 2, 3, 5),            # not a walk (31? 14 not an edge here)
+        (1, 3, 2, 4, 3, 5),            # trail (book "path"), not a path
+        (1, 3, 4, 5),                  # simple path
+        (3, 2, 1, 3, 5, 4, 3),         # book cycle, not simple
+        (1, 3, 4, 2, 1),               # simple cycle
+    ]
+    for s in tb:
+        print(f"  {s!s:<28} length {length(s):<2} {', '.join(classify(G, s))}")
+    print("  (the second sequence is the textbook's 'v3,v1,v4,v2,v3,v5' on p. 22; it is a")
+    print("   non-walk only if v1v4 is not an edge: the textbook says it is not a walk.)")
+
+    print("\n=== 4. The lemma: trace on the textbook walk (Lemma 1.2.1) ===")
+    s = (1, 3, 2, 4, 3, 2, 4, 3, 5)
+    tr = []
+    p = reduce_to_path(s, tr)
+    for old, (i, j), new in tr:
+        print(f"  {old}  (len {length(old)}): u_{i} = u_{j} = {old[i]}; cut -> {new} (len {length(new)})")
+    print(f"  result {p}: path? {is_path(G, p)}; length {length(p)} <= {length(s)}")
+
+    print("\n  Trace on a board-graph walk and a closed walk:")
+    for s in [(1, 2, 1, 2, 3), (2, 1, 2), (1, 2, 3, 2, 1)]:
+        tr = []
+        p = reduce_to_path(s, tr)
+        for old, (i, j), new in tr:
+            print(f"   {old}: u_{i} = u_{j} = {old[i]}; cut -> {new}")
+        print(f"   {s} -> {p}, path? {is_path(B, p)}, endpoints kept: "
+              f"{p[0] == s[0] and p[-1] == s[-1]}, length {length(p)} <= {length(s)}")
+
+    print("\n=== 5. Exhaustive and random checks of the claims ===")
+    # 5a. lemma on all walks of length <= 6 in B, T, G
+    for name, g in [("B", B), ("T", T), ("G", G)]:
+        n = 0
+        bad = 0
+        for k in range(0, 7):
+            for w in all_walks(g, k):
+                p = reduce_to_path(w)
+                n += 1
+                good = (is_path(g, p) and p[0] == w[0] and p[-1] == w[-1]
+                        and length(p) <= length(w)
+                        and set(p) <= set(w))
+                bad += (not good)
+        print(f"  lemma on all walks of length 0..6 in {name}: {n} walks, failures {bad}")
+
+    # 5b. random graphs: lemma, distinct vertices => distinct edges, path <= N-1,
+    #     shortest walk = distance = shortest path = shortest trail
+    random.seed(20261027)
+    stats = dict(graphs=0, walks=0, lemma_fail=0, edge_fail=0, len_fail=0,
+                 dist_fail=0, trail_fail=0)
+    for _ in range(300):
+        N = random.randint(2, 7)
+        V = list(range(1, N + 1))
+        E = [e for e in itertools.combinations(V, 2) if random.random() < 0.4]
+        g = make_graph(V, E)
[... truncated by build_evidence.py: 51 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/m2_walks_output.txt b/papers/adjacency-walks-connectivity/appendices/scripts/m2_walks_output.txt
new file mode 100644
index 0000000..03b2ab6
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/m2_walks_output.txt
@@ -0,0 +1,75 @@
+=== 1. Board graph B: V = {1,2,3}, E = {12, 23} (from the matrix) ===
+  (1, 2, 3)        length 2  walk, trail=book-path, path=book-simple-path
+  (3, 2, 1)        length 2  walk, trail=book-path, path=book-simple-path
+  (1, 2, 1, 2, 3)  length 4  walk
+  (2, 1, 2)        length 2  walk, closed
+  (2, 3, 2, 1, 2)  length 4  walk, closed
+  (1, 2, 1)        length 2  walk, closed
+  (2,)             length 0  walk, closed, trail=book-path, path=book-simple-path
+  (1, 2)           length 1  walk, trail=book-path, path=book-simple-path
+  (1, 3)           length 1  NOT a walk
+  (1, 2, 3, 2)     length 3  walk
+
+  Walks by length in B (all start/end pairs), counted by enumeration:
+   k=0: walks=3   trails=3   paths=3   closed walks=3
+   k=1: walks=4   trails=4   paths=4   closed walks=0
+   k=2: walks=6   trails=2   paths=2   closed walks=4
+   k=3: walks=8   trails=0   paths=0   closed walks=0
+   k=4: walks=12  trails=0   paths=0   closed walks=8
+
+  Walks from 1 to 3 of length <= 4 in B, with type:
+   (1, 2, 3)          length 2  walk, trail=book-path, path=book-simple-path
+   (1, 2, 1, 2, 3)    length 4  walk
+   (1, 2, 3, 2, 3)    length 4  walk
+
+  Check: B has no cycle (every closed walk of length 1..6 repeats an edge):
+   cycles of positive length found: []
+
+  Consistency with m1 (A^k entry = number of walks); A =
+   enumeration equals A^k for k=1..5, all i,j: True
+
+=== 2. Triangle T (the board DRAWING): V={1,2,3}, E={12,13,23} ===
+  (1, 2, 3, 1)     length 3  walk, closed, trail=book-path, book-cycle, simple-cycle
+  (1, 2, 1)        length 2  walk, closed
+  (1, 2, 3)        length 2  walk, trail=book-path, path=book-simple-path
+  (1, 2, 3, 2, 1)  length 4  walk, closed
+
+=== 3. Textbook example graph (edges forced by the textbook examples) ===
+  (1, 3, 2, 4, 3, 2, 4, 3, 5)  length 8  walk
+  (3, 1, 4, 2, 3, 5)           length 5  NOT a walk
+  (1, 3, 2, 4, 3, 5)           length 5  walk, trail=book-path
+  (1, 3, 4, 5)                 length 3  walk, trail=book-path, path=book-simple-path
+  (3, 2, 1, 3, 5, 4, 3)        length 6  walk, closed, trail=book-path, book-cycle
+  (1, 3, 4, 2, 1)              length 4  walk, closed, trail=book-path, book-cycle, simple-cycle
+  (the second sequence is the textbook's 'v3,v1,v4,v2,v3,v5' on p. 22; it is a
+   non-walk only if v1v4 is not an edge: the textbook says it is not a walk.)
+
+=== 4. The lemma: trace on the textbook walk (Lemma 1.2.1) ===
+  (1, 3, 2, 4, 3, 2, 4, 3, 5)  (len 8): u_1 = u_4 = 3; cut -> (1, 3, 2, 4, 3, 5) (len 5)
+  (1, 3, 2, 4, 3, 5)  (len 5): u_1 = u_4 = 3; cut -> (1, 3, 5) (len 2)
+  result (1, 3, 5): path? True; length 2 <= 8
+
+  Trace on a board-graph walk and a closed walk:
+   (1, 2, 1, 2, 3): u_0 = u_2 = 1; cut -> (1, 2, 3)
+   (1, 2, 1, 2, 3) -> (1, 2, 3), path? True, endpoints kept: True, length 2 <= 4
+   (2, 1, 2): u_0 = u_2 = 2; cut -> (2,)
+   (2, 1, 2) -> (2,), path? True, endpoints kept: True, length 0 <= 2
+   (1, 2, 3, 2, 1): u_0 = u_4 = 1; cut -> (1,)
+   (1, 2, 3, 2, 1) -> (1,), path? True, endpoints kept: True, length 0 <= 4
+
+=== 5. Exhaustive and random checks of the claims ===
+  lemma on all walks of length 0..6 in B: 73 walks, failures 0
+  lemma on all walks of length 0..6 in T: 381 walks, failures 0
+  lemma on all walks of length 0..6 in G: 4695 walks, failures 0
+  random graphs (300 seeds, N=2..7): {'graphs': 300, 'walks': 192696, 'lemma_fail': 0, 'edge_fail': 0, 'len_fail': 0, 'dist_fail': 0, 'trail_fail': 0}
+
+=== 6. Distance in B and in a disconnected graph D ===
+  B: d(1, .) = {1: 0, 2: 1, 3: 2}
+  B: d(2, .) = {1: 1, 2: 0, 3: 1}
+  B: d(3, .) = {1: 2, 2: 1, 3: 0}
+  D (only edge 12): d(1, .) = {1: 0, 2: 1, 3: inf}
+  D (only edge 12): d(2, .) = {1: 1, 2: 0, 3: inf}
+  D (only edge 12): d(3, .) = {1: inf, 2: inf, 3: 0}
+
+=== 7. Path length bound: B has N=3, so a path has at most 2 edges ===
+  longest path in B has 2 edges; N-1 = 2
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.out.txt b/papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.out.txt
new file mode 100644
index 0000000..22277ad
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.out.txt
@@ -0,0 +1,116 @@
+==================================================================
+EXAMPLE 1 (connected, the board matrix)  N = 3  edges: [(1, 2), (2, 3)]
+A
+     0  1  0
+     1  0  1
+     0  1  0
+A^2
+     1  0  1
+     0  2  0
+     1  0  1
+S = A + A^2   (N - 1 = 2)
+     1  1  1
+     1  2  1
+     1  1  1
+(I + A)^2     (N - 1 = 2)
+     2  2  1
+     2  3  2
+     1  2  2
+off-diagonal zeros of S      : []
+zero entries of (I+A)^(N-1)  : []
+sum test says connected      : True
+(I+A)^(N-1) test says        : True
+BFS says connected           : True
+components (BFS)             : [[1, 2, 3]]
+(I+A)^2 == I + 2A + A^2      : True
+==================================================================
+EXAMPLE 2 (disconnected, edge 1-2 only)  N = 3  edges: [(1, 2)]
+A
+     0  1  0
+     1  0  0
+     0  0  0
+A^2
+     1  0  0
+     0  1  0
+     0  0  0
+S = A + A^2   (N - 1 = 2)
+     1  1  0
+     1  1  0
+     0  0  0
+(I + A)^2     (N - 1 = 2)
+     2  2  0
+     2  2  0
+     0  0  1
+off-diagonal zeros of S      : [(1, 3), (2, 3), (3, 1), (3, 2)]
+zero entries of (I+A)^(N-1)  : [(1, 3), (2, 3), (3, 1), (3, 2)]
+sum test says connected      : False
+(I+A)^(N-1) test says        : False
+BFS says connected           : False
+components (BFS)             : [[1, 2], [3]]
+(I+A)^2 == I + 2A + A^2      : True
+------------------------------------------------------------------
+Example 2, higher powers: column 3 of A^k for k = 1..6 is zero off the diagonal: True
+==================================================================
+N = 2, one edge 1-2 (connected): the sum is just A
+A = S
+     0  1
+     1  0
+diagonal of S is zero although G is connected; off-diagonal entries are 1: True
+Connected graphs with 3 vertices: diagonal of S positive? path 1-2-3: [1, 2, 1]
+==================================================================
+Path graph 1-2-...-N: entry (1,N) of A^k first becomes nonzero at k = N-1
+   N | smallest k with (A^k)_{1N} > 0 | (1,N) of A+..+A^(N-2) | (1,N) of A+..+A^(N-1)
+   3 |                              2 |                      0 |                      1
+   4 |                              3 |                      0 |                      1
+   5 |                              4 |                      0 |                      1
+   6 |                              5 |                      0 |                      1
+   7 |                              6 |                      0 |                      1
+   8 |                              7 |                      0 |                      1
+------------------------------------------------------------------
+N = 4, path 1-2-3-4: A, A^2, A^3, A+A^2, A+A^2+A^3
+A
+     0  1  0  0
+     1  0  1  0
+     0  1  0  1
+     0  0  1  0
+A^2
+     1  0  1  0
+     0  2  0  1
+     1  0  2  0
+     0  1  0  1
+A^3
+     0  2  0  1
+     2  0  3  0
+     0  3  0  2
+     1  0  2  0
+A + A^2  (N-2 powers: NOT enough)
+     1  1  1  0
+     1  2  1  1
+     1  1  2  1
+     0  1  1  1
+A + A^2 + A^3  (N-1 powers: enough)
+     1  3  1  1
+     3  2  4  1
+     1  4  2  3
+     1  1  3  1
+test with N-2 powers says connected: False   test with N-1 powers says connected: True
+==================================================================
+Exhaustive check over ALL labelled simple graphs, N = 2..6
+   N | graphs | connected | sum test = BFS | (I+A)^(N-1) test = BFS | S_ij>0 <=> same component | pattern of (I+A)^m for m = 2^t >= N-1 = BFS | N-2 powers wrong on
+   2 |      2 |         1 |              2 |                      2 |                          2 |                                         2 | 1
+   3 |      8 |         4 |              8 |                      8 |                          8 |                                         8 | 3
+   4 |     64 |        38 |             64 |                     64 |                         64 |                                        64 | 12
+   5 |   1024 |       728 |           1024 |                   1024 |                       1024 |                                      1024 | 60
+   6 |  32768 |     26704 |          32768 |                  32768 |                      32768 |                                     32768 | 360
+==================================================================
+Cost remark: scalar multiplications, schoolbook product of two N x N matrices = N^3
+   N | (I+A)^(N-1) by N-2 products | by repeated squaring | BFS row scans of A (N^2)
+   10 |                       8,000 |                4,000 | 100
+      number of squarings t = 4, 2^t = 16 >= N-1 = 9
+  100 |                  98,000,000 |            7,000,000 | 10,000
+      number of squarings t = 7, 2^t = 128 >= N-1 = 99
+ 1000 |             998,000,000,000 |       10,000,000,000 | 1,000,000
+      number of squarings t = 10, 2^t = 1024 >= N-1 = 999
+complete graph K_5: largest entry of A^(N-1) = 52
+complete graph K_10: largest entry of A^(N-1) = 38,742,049
+complete graph K_20: largest entry of A^(N-1) = 98,920,982,783,015,679,456,199
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.py b/papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.py
new file mode 100644
index 0000000..9d513ec
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.py
@@ -0,0 +1,228 @@
+"""Module m3 calculations: the matrix connectivity test, its equivalent form,
+the two three-vertex examples, sharpness of the bound N-1, an exhaustive
+cross-check against breadth-first search, and operation counts for the cost
+remark. Pure Python, integers only (no numpy needed).
+
+Run from the paper folder:  python3 modules/m3_connectivity.py
+Vertices are 1..N in the text and 0..N-1 in the code (index = vertex - 1).
+"""
+from itertools import combinations
+from math import comb, ceil, log2
+from collections import deque
+
+
+# ---------------------------------------------------------------- matrices
+def identity(n):
+    return [[int(i == j) for j in range(n)] for i in range(n)]
+
+
+def matmul(X, Y):
+    n = len(X)
+    return [[sum(X[i][r] * Y[r][j] for r in range(n)) for j in range(n)]
+            for i in range(n)]
+
+
+def matadd(X, Y):
+    return [[x + y for x, y in zip(rx, ry)] for rx, ry in zip(X, Y)]
+
+
+def matpow(A, k):
+    R = identity(len(A))
+    for _ in range(k):
+        R = matmul(R, A)
+    return R
+
+
+def adjacency(n, edges):
+    """edges: pairs of 1-based vertices; returns the adjacency matrix."""
+    A = [[0] * n for _ in range(n)]
+    for u, v in edges:
+        A[u - 1][v - 1] = A[v - 1][u - 1] = 1
+    return A
+
+
+def show(name, M):
+    print(name)
+    for row in M:
+        print("   ", " ".join(f"{x:2d}" for x in row))
+
+
+def power_sum(A, last):
+    """A + A^2 + ... + A^last (zero matrix if last < 1)."""
+    n = len(A)
+    S = [[0] * n for _ in range(n)]
+    P = identity(n)
+    for _ in range(last):
+        P = matmul(P, A)
+        S = matadd(S, P)
+    return S
+
+
+# ------------------------------------------------------------------- tests
+def offdiag_positive(M):
+    n = len(M)
+    return all(M[i][j] > 0 for i in range(n) for j in range(n) if i != j)
+
+
+def test_sum(A):
+    """Test (b): every off-diagonal entry of A + ... + A^(N-1) is positive."""
+    return offdiag_positive(power_sum(A, len(A) - 1))
+
+
+def test_binomial(A):
+    """Test (c): every entry of (I + A)^(N-1) is positive."""
+    n = len(A)
+    M = matpow(matadd(identity(n), A), n - 1)
+    return all(M[i][j] > 0 for i in range(n) for j in range(n))
+
+
+def bfs_component(A, s):
+    """Independent check: set of vertices reached from s by breadth-first search."""
+    n = len(A)
+    seen = {s}
+    q = deque([s])
+    while q:
+        v = q.popleft()
+        for w in range(n):
+            if A[v][w] and w not in seen:
+                seen.add(w)
+                q.append(w)
+    return seen
+
+
+def bfs_connected(A):
+    return len(bfs_component(A, 0)) == len(A)
+
+
+def components(A):
+    left, out = set(range(len(A))), []
+    while left:
+        c = bfs_component(A, min(left))
+        out.append(sorted(v + 1 for v in c))
+        left -= c
+    return out
+
+
+# ------------------------------------------------------------ the examples
+def worked_example(title, n, edges):
+    print("=" * 66)
+    print(title, " N =", n, " edges:", edges)
+    A = adjacency(n, edges)
+    I = identity(n)
+    A2 = matpow(A, 2)
+    S = power_sum(A, n - 1)
+    B = matpow(matadd(I, A), n - 1)
+    show("A", A)
+    show("A^2", A2)
+    show("S = A + A^2   (N - 1 = %d)" % (n - 1), S)
+    show("(I + A)^2     (N - 1 = %d)" % (n - 1), B)
+    print("off-diagonal zeros of S      :",
+          [(i + 1, j + 1) for i in range(n) for j in range(n)
+           if i != j and S[i][j] == 0])
+    print("zero entries of (I+A)^(N-1)  :",
+          [(i + 1, j + 1) for i in range(n) for j in range(n) if B[i][j] == 0])
+    print("sum test says connected      :", test_sum(A))
+    print("(I+A)^(N-1) test says        :", test_binomial(A))
+    print("BFS says connected           :", bfs_connected(A))
+    print("components (BFS)             :", components(A))
+    # binomial identity (I+A)^2 = I + 2A + A^2 checked entry by entry
+    rhs = matadd(matadd(I, [[2 * x for x in r] for r in A]), A2)
+    print("(I+A)^2 == I + 2A + A^2      :", B == rhs)
+    return A, S, B
+
+
+A_conn, S_conn, B_conn = worked_example(
+    "EXAMPLE 1 (connected, the board matrix)", 3, [(1, 2), (2, 3)])
+A_disc, S_disc, B_disc = worked_example(
+    "EXAMPLE 2 (disconnected, edge 1-2 only)", 3, [(1, 2)])
+
+# the same disconnected graph: higher powers never reach vertex 3
+print("-" * 66)
+print("Example 2, higher powers: column 3 of A^k for k = 1..6 is zero off the diagonal:",
+      all(matpow(A_disc, k)[i][2] == 0 for k in range(1, 7) for i in (0, 1)))
+
+# ---------------------------------------------- N = 2: why the diagonal is skipped
+print("=" * 66)
+print("N = 2, one edge 1-2 (connected): the sum is just A")
+A_k2 = adjacency(2, [(1, 2)])
+show("A = S", A_k2)
+print("diagonal of S is zero although G is connected; off-diagonal entries are 1:",
+      power_sum(A_k2, 1)[0][0] == 0 and offdiag_positive(power_sum(A_k2, 1)))
+print("Connected graphs with 3 vertices: diagonal of S positive? path 1-2-3:",
+      [S_conn[i][i] for i in range(3)])
+
+# -------------------------------------------- sharpness: N-1 cannot be N-2
+print("=" * 66)
+print("Path graph 1-2-...-N: entry (1,N) of A^k first becomes nonzero at k = N-1")
+print("   N | smallest k with (A^k)_{1N} > 0 | (1,N) of A+..+A^(N-2) | (1,N) of A+..+A^(N-1)")
+for N in range(3, 9):
+    A = adjacency(N, [(i, i + 1) for i in range(1, N)])
+    first = next(k for k in range(1, N + 3) if matpow(A, k)[0][N - 1] > 0)
+    s_short = power_sum(A, N - 2)[0][N - 1]
+    s_full = power_sum(A, N - 1)[0][N - 1]
+    print(f"  {N:2d} | {first:30d} | {s_short:22d} | {s_full:22d}")
+    assert first == N - 1 and s_short == 0 and s_full > 0
+
+print("-" * 66)
+print("N = 4, path 1-2-3-4: A, A^2, A^3, A+A^2, A+A^2+A^3")
+A4 = adjacency(4, [(1, 2), (2, 3), (3, 4)])
+show("A", A4)
+show("A^2", matpow(A4, 2))
+show("A^3", matpow(A4, 3))
+show("A + A^2  (N-2 powers: NOT enough)", power_sum(A4, 2))
+show("A + A^2 + A^3  (N-1 powers: enough)", power_sum(A4, 3))
+print("test with N-2 powers says connected:", offdiag_positive(power_sum(A4, 2)),
+      "  test with N-1 powers says connected:", offdiag_positive(power_sum(A4, 3)))
+
+# ------------------------------- exhaustive cross-check against BFS, N <= 6
+print("=" * 66)
+print("Exhaustive check over ALL labelled simple graphs, N = 2..6")
+print("   N | graphs | connected | sum test = BFS | (I+A)^(N-1) test = BFS |"
+      " S_ij>0 <=> same component | pattern of (I+A)^m for m = 2^t >= N-1 = BFS |"
+      " N-2 powers wrong on")
+for N in range(2, 7):
+    pairs = list(combinations(range(N), 2))
+    total = conn = ok_sum = ok_bin = ok_comp = ok_sq = short_wrong = 0
+    for mask in range(1 << len(pairs)):
+        A = [[0] * N for _ in range(N)]
+        for b, (u, v) in enumerate(pairs):
+            if mask >> b & 1:
+                A[u][v] = A[v][u] = 1
+        total += 1
+        truth = bfs_connected(A)
+        conn += truth
+        S = power_sum(A, N - 1)
+        ok_sum += (test_sum(A) == truth)
+        ok_bin += (test_binomial(A) == truth)
+        # corollary: off-diagonal S_ij > 0 iff same component
+        same = all((S[i][j] > 0) == (j in bfs_component(A, i))
+                   for i in range(N) for j in range(N) if i != j)
+        ok_comp += same
+        # repeated squaring: M = (I+A), square t times with 2^t >= N-1
+        t = max(1, ceil(log2(N - 1))) if N > 2 else 1
+        M = matadd(identity(N), A)
+        for _ in range(t):
+            M = matmul(M, M)
+        ok_sq += ((all(x > 0 for r in M for x in r)) == truth)
+        # sum with only N-2 powers: wrong on some connected graphs
+        if offdiag_positive(power_sum(A, N - 2)) != truth:
+            short_wrong += 1
+    print(f"  {N:2d} | {total:6d} | {conn:9d} | {ok_sum:14d} | {ok_bin:22d} |"
+          f" {ok_comp:26d} | {ok_sq:41d} | {short_wrong}")
+    assert ok_sum == ok_bin == ok_comp == ok_sq == total
+
+# ------------------------------------------------------------- cost counts
+print("=" * 66)
+print("Cost remark: scalar multiplications, schoolbook product of two N x N matrices = N^3")
+print("   N | (I+A)^(N-1) by N-2 products | by repeated squaring | BFS row scans of A (N^2)")
+for N in (10, 100, 1000):
+    prods = N - 2
+    t = ceil(log2(N - 1))
+    print(f"{N:5d} | {prods * N**3:27,d} | {t * N**3:20,d} | {N * N:,d}")
+    print(f"      number of squarings t = {t}, 2^t = {2**t} >= N-1 = {N-1}")
+
+# entries grow fast: largest entry of A^(N-1) for the complete graph K_N
+for N in (5, 10, 20):
+    K = adjacency(N, [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)])
+    top = max(max(r) for r in matpow(K, N - 1))
+    print(f"complete graph K_{N}: largest entry of A^(N-1) = {top:,d}")
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evaluation-report.md b/papers/adjacency-walks-connectivity/evaluation-report.md
new file mode 100644
index 0000000..ed204a6
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/evaluation-report.md
@@ -0,0 +1,143 @@
+# Evaluation report
+
+## Round 1, 2026-10-31
+
+Question: For a simple undirected graph with N vertices given by its
+adjacency matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how
+can one determine from A whether the graph is connected, and (3) what is
+the definition of a path between vertices n_i and n_j? (from `brief.md`)
+
+Scope: Finite simple undirected graphs; walks, trails, paths, cycles and
+distance; connectivity and components; the matrix-power connectivity test
+in both forms (sum of powers and (I + A)^(N-1)) with full proofs; a
+breadth-first search alternative stated for comparison; worked examples on
+the three-vertex board graph, a disconnected three-vertex graph, and the
+four-vertex path. Study-note register with the textbook standard and the
+plain words layer. Directed graphs, multigraphs, weighted graphs,
+eigenvalue methods, and implementation code are out of scope.
+
+Research summary: 11 sources in `evidence/evidence.json` (the course
+textbook as a local file, two whiteboard photos, one preprint, one
+peer-reviewed article, five web sources, one lecture-slide set); 77
+claims (70 supported, 7 qualified, 0 unverified). Three modules (m1
+adjacency matrix and walk counting, m2 walks, trails, paths, cycles, m3
+connectivity from the adjacency matrix). Research and modules were final
+inputs for this run (one round of research, round 0). This probe is the
+author stage only: one draft, one evaluation round, no revision.
+
+Model levels: research 2, modules 2, author 2, reader 2, evaluator 3,
+orchestrator session model (configured claude-fable-5-1, level 4).
+Hierarchy requirement: met (evaluator level 3 exceeds author and module
+level 2). Levels are configured levels taken from `model-levels.md`; a
+runtime fallback is not observable from inside the session and none was
+reported by the harness for the evaluator.
+
+Mechanical checks (run by the orchestrator after the author returned):
+build pass (exit 0, 1 overfull box of 0.36 pt), citations pass (11 cited
+keys, 11 bib entries, 11 evidence sources, 0 errors), claims pass (70
+supported, 7 qualified, 0 unverified, 0 errors), pdf pass (31 pages, 0
+errors, 1 warning), evidence rebuild pass (0 differences), self-evaluation
+pass (13 inputs covered, 0 errors). The gate passed on the first run; no
+failure was sent back to the author.
+
+### Scores
+
+| Dimension | Score | Observation |
+|---|---|---|
+| 1 Correctness | 5 | Evaluator recomputed every number by script (board powers A to A^5, S, (I+A)^2, disconnected matrices, P4 matrices, Tables 4 and 5, case counts 40/360/5120/76800, cost figures, largest entry of A^9 for K10) and all match. Proofs of Theorem 3.5, Lemma 2.45, Propositions 4.13 and 4.14, Theorem 4.15 valid step by step. |
+| 2 Evidence coverage | 4 | All 77 claims cover every cited statement with matching quotes. Exception: Definition 2.9 (`sections/background.tex:69-71`) cites a Quinlan remark for degree and says the textbook definition was not read, although the textbook has Definition 1.2.1 on printed p. 16. |
+| 3 Citation integrity | 4 | Eight sources checked (seven fetched or read locally plus both board photos); all support the attributed statements. `sections/introduction.tex:67` calls the peer-reviewed article [7] a "web source". |
+| 4 Logical validity | 5 | Every conclusion follows; the walk-to-path step skipped by the sources is supplied by Lemma 2.45; the trail and path readings of "connected" are shown to agree; i = j and N = 1 handled in Remark 4.21. |
+| 5 Understandability | 4 | Plain-words layer applied almost everywhere. Unexplained: "metric space" (`background.tex:413`), "reflexive, symmetric and transitive" (`answer2_connectivity.tex:55`), "queue" (`answer2_connectivity.tex:293`), "adjacency lists" (`discussion.tex:49`), binomial coefficient at `example.tex:89` before Appendix A.4. |
+| 6 Completeness | 4 | Every brief objective met. Gaps: textbook number for degree missing (`background.tex:71`); Table 3 lacks the "course" column the text at `background.tex:366` announces. |
+| 7 Methodological rigor | 5 | Every claim tagged as cited, derived, interpretation or open; script checks presented as tests, not proofs (Sections 6.5, 7.1); integer arithmetic assumption stated. |
+| 8 Critical analysis | 5 | Section 7.3 explains the source that says "paths" for walks; drawing-versus-matrix mismatch and the mark above A reported (Sections 1.1, 1.4, 7.5); cost discussed in 7.4; textbook absence claim qualified and independently confirmed by the evaluator. |
+| 9 Internal consistency | 4 | Terms and notation consistent. Table 3 header "This paper" against the text's "course"; [7] called "web source" in the introduction but "published note" in Sections 4.4 and 7.3. |
+| 10 Reproducibility | 5 | Appendix D names a script and saved output for every number; `figures/generated_numbers.tex` agrees with the evaluator's independent computation. |
+| 11 LaTeX and PDF quality | 4 | 31 pages, references resolve, matrices render (page 22 checked as image). One overfull hbox of 0.36 pt at Example 2.29. |
+| 12 Answer relevance | 5 | Sections 3.5, 4.8, 5 and the Conclusion answer Q1, Q2 and Q3 directly; nothing outside the brief is claimed. |
+
+### Findings
+
+Evaluator findings (full text in `reports/paper-evaluator-round1.md`).
+This probe is a single author-stage round with no revision, so every
+finding stays open and is documented here with that reason. None is
+critical or major.
+
+| Id | Severity | Location | Defect | Status |
+|---|---|---|---|---|
+| F1 | minor | `sections/background.tex:69-71` (Definition 2.9) | Degree cited to a Quinlan remark and marked "not read" in the textbook, although the textbook defines it as Definition 1.2.1 on printed p. 16; misses the brief's rule to cite textbook numbers. | documented: open, no revision in this probe |
+| F2 | minor | `sections/introduction.tex:67` | Peer-reviewed article [7] described as "One web source". | documented: open, no revision in this probe |
+| F3 | minor | `sections/background.tex:366-375` (Table 3) | Text announces course, textbook and English columns; table has Textbook, English, This paper. | documented: open, no revision in this probe |
+| F4 | minor | `sections/answer2_connectivity.tex:204` (Corollary 4.19) | No plain-words paragraph before the corollary, against the study-note rule. | documented: open, no revision in this probe |
+| F5 | minor | `sections/background.tex:413` | "metric space" unexplained. | documented: open, no revision in this probe |
+| F6 | minor | `sections/answer2_connectivity.tex:55` | "reflexive, symmetric and transitive" unexplained. | documented: open, no revision in this probe |
+| F7 | minor | `sections/answer2_connectivity.tex:293`; `sections/discussion.tex:49` | "queue" and "adjacency lists" unexplained. | documented: open, no revision in this probe |
+| F8 | minor | `sections/example.tex:89` | Binomial coefficient and expansion of (I+A)^2 used before Appendix A.4 explains them. | documented: open, no revision in this probe |
+| F9 | minor | Example 2.29 (`sections/background.tex`; `build/main.log:828`) | Overfull hbox of 0.36 pt. | documented: open, no revision in this probe |
+
+Technician reader: 37 comprehension findings, recorded verbatim in
+`reader-findings.md` under Round 1 and in
+`reports/technician-reader-round1.md`. The reader's summary paragraph
+states the three questions and the paper's answers correctly (walk count,
+sum-of-powers test with the (I + A)^(N-1) form, path as a walk with no
+repeated vertex, the board mismatch and the mark above A); it matches the
+paper's actual conclusion, so no major finding arises from it. The
+reader's recurring points are that the 31-page length hides which sections
+the main argument needs (its F12, F33, F36, F37), that several terms are
+used before explanation (F13, F15, F19, F27, overlapping evaluator F5 to
+F8), and that some reported counts are not explained (F17, F30). These are
+advisory for the next revision round and are left open for the same
+reason as the evaluator findings.
+
+### Citation and claim coverage
+
+Sources: 11 (1 local-file textbook with partial access, 2 local
+whiteboard photos, 1 preprint with partial access, 1 peer-reviewed article,
+5 web sources, 1 lecture-slide set with partial access). Claims: 70
+supported, 7 qualified, 0 unverified, 0 removed. Evaluator spot checks: 8
+source records checked (quinlan_matrices_graphs, paramadevan2021adjacency,
+bai2025adjacency, weisstein_connectedgraph, grinberg2025graph,
+schost2026bfs fetched; petrosyan2015grafneri and the two whiteboard photos
+read locally), all "supports".
+
+### Unverified claims and access limits
+
+- No unverified claims in the text.
+- Qualified claims, each disclosed in the text: C24 and m2-8 (course
+  meaning of "path", from the assignment text, which is not a file);
+  C29 and m1-9 (the mark above A read as the exponent k); m2-15 (walks of
+  length 0 allowed, a reading of the textbook); C36 (the (I + A)^(N-1)
+  form, whose only source has a proof sketch and was accessed partially);
+  m3-11 (the textbook states neither theorem in the pages checked;
+  confirmed by the evaluator with a full-text search).
+- Access limits: the textbook (petrosyan2015grafneri), the Grinberg
+  preprint, and the Schost slides are recorded as partial access; the
+  Bai page as partial access. The textbook's PDF text layer drops most
+  symbols, so formulas were read from page images.
+- Author's own list of what it could not fully justify (from
+  `reports/paper-author-round1.md`): the textbook's degree definition and
+  the number of its adjacency-matrix definition were not recorded (now
+  evaluator F1); the seven edges of textbook Fig. 1.2.5 are the module's
+  reading; some printed counts come from the module scripts rather than
+  the author script; bibliography years are "n.d." where the evidence has
+  none; Armenian text is given in English gloss and transliteration.
+
+### Known limitations
+
+- Single round: no revision was made and the evaluator's minor findings
+  and the reader's comprehension findings are not resolved.
+- The evaluator did not run `build.sh` itself (it writes build files)
+  and did not observe release condition 9; the orchestrator ran both
+  checks and they pass.
+- The paper is 31 pages for a three-question study note; the reader could
+  not tell which sections carry the main argument.
+- Armenian textbook text is not reproduced in the PDF.
+
+Decision: PASS -- Every dimension scores at least 4, there is no critical
+or major finding, all seven qualified claims are qualified in the text,
+the hierarchy requirement is met, every mechanical check passes, the self
+evaluation covers all 13 input files, and the independent evaluation
+recommends PASS. The nine minor findings are documented above as open
+because this probe is one round with no revision; they should be fixed in
+the next revision before any further release.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/evidence.base.json b/papers/adjacency-walks-connectivity/evidence/evidence.base.json
index 9b7e52d..439bce8 100644
--- a/papers/adjacency-walks-connectivity/evidence/evidence.base.json
+++ b/papers/adjacency-walks-connectivity/evidence/evidence.base.json
@@ -417,7 +417,7 @@
           "quote": "The 0-th power of any n × n-matrix is defined to be the n × n identity matrix In ; thus, C0 = In ."
         }
       ],
-      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walkcount); appendices/derivations.tex, Appendix A.1 (label app:walkcount)",
+      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walks)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -492,7 +492,7 @@
           "quote": "The number of walks of length 2 from a vertex to itself is just the number of edges at that vertex, or the vertex degree."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.10 (label prop:warning); matrix products and counts by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.11 (label prop:warning); matrix products and counts by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1126,7 +1126,7 @@
           "quote": "Then, there is a path from u to v of length ≤ k."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Proposition 4.5 (label prop:pair) and Theorem 4.6 (label thm:test); appendices/derivations.tex, Appendix A.3 (label app:testproof) (chain of premises)",
+      "derivation": "sections/answer2_connectivity.tex, Proposition 4.13 (label prop:pair) and Theorem 4.15 (label thm:test); appendices/derivations.tex, Appendix A.3 (label app:testproof) (chain of premises)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1170,7 +1170,7 @@
           "quote": "Define the modified adjacency matrix A′ = I + A, where the identity matrix I adds self-loops (A′i,i = 1)."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (binomial expansion, proof of Proposition 4.16 (label prop:iplusa))",
+      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (binomial expansion, proof of Proposition 4.14 (label prop:iplusa))",
       "confidence": "high",
       "status": "supported",
       "used_in": [
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/evidence.json b/papers/adjacency-walks-connectivity/evidence/evidence.json
index 65f95bf..9558db4 100644
--- a/papers/adjacency-walks-connectivity/evidence/evidence.json
+++ b/papers/adjacency-walks-connectivity/evidence/evidence.json
@@ -417,7 +417,7 @@
           "quote": "The 0-th power of any n × n-matrix is defined to be the n × n identity matrix In ; thus, C0 = In ."
         }
       ],
-      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walkcount); appendices/derivations.tex, Appendix A.1 (label app:walkcount)",
+      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walks)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -492,7 +492,7 @@
           "quote": "The number of walks of length 2 from a vertex to itself is just the number of edges at that vertex, or the vertex degree."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.10 (label prop:warning); matrix products and counts by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.11 (label prop:warning); matrix products and counts by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1126,7 +1126,7 @@
           "quote": "Then, there is a path from u to v of length ≤ k."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Proposition 4.5 (label prop:pair) and Theorem 4.6 (label thm:test); appendices/derivations.tex, Appendix A.3 (label app:testproof) (chain of premises)",
+      "derivation": "sections/answer2_connectivity.tex, Proposition 4.13 (label prop:pair) and Theorem 4.15 (label thm:test); appendices/derivations.tex, Appendix A.3 (label app:testproof) (chain of premises)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1170,7 +1170,7 @@
           "quote": "Define the modified adjacency matrix A′ = I + A, where the identity matrix I adds self-loops (A′i,i = 1)."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (binomial expansion, proof of Proposition 4.16 (label prop:iplusa))",
+      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (binomial expansion, proof of Proposition 4.14 (label prop:iplusa))",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1253,7 +1253,7 @@
           "quote": "Սահմանում 1.1.4: u և v գագաթները կանվանենք հարևան, եթե uv ∈ E։"
         }
       ],
-      "derivation": "sections/background.tex, Proposition 2.20 (label prop:rowsums); numbers by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "sections/background.tex, Proposition 2.17 (label prop:rowsums); numbers by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1278,7 +1278,7 @@
           "quote": "A walk (in G) means a finite sequence (v0 , v1 , . . . , vk ) of vertices of G (with k ≥ 0) such that all of v0 v1 , v1 v2 , v2 v3 , . . . , vk−1 vk are edges of G."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.1 (label app:walkcount); sections/background.tex, Remark 2.24 (label rem:walk)",
+      "derivation": "sections/background.tex, Remark 2.20 (label rem:vertexlist)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1305,7 +1305,7 @@
           "quote": "Thus the total number of walks of length k from vi to vj is the sum of the expressions (Ak−1 )ir Arj over all vertices vr of G, which is exactly (Ak )ij ."
         }
       ],
-      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walkcount); appendices/derivations.tex, Appendix A.1 (label app:walkcount); finite cross-check by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walks); finite cross-check by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1321,7 +1321,7 @@
       "kind": "derived",
       "module": "m1",
       "support": [],
-      "derivation": "appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt), last section; appendices/derivations.tex, Appendix A.6 (label app:crosschecks)",
+      "derivation": "appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt), last section; appendices/derivations.tex, Appendix A.5 (label app:crosschecks)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1374,7 +1374,7 @@
           "quote": "G գրաֆի (u0, u_k)-ճանապարհը կանվանենք պարզ (u0, u_k)-ճանապարհ, եթե նրա մեջ մտնող բոլոր գագաթները զույգ առ զույգ տարբեր են։"
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.10 (label prop:warning) and Table 5 (label tab:walksvspaths); enumeration by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.11 (label prop:warning) and Table 6 (label tab:counterex); enumeration by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1752,7 +1752,7 @@
           "quote": "Let G be a simple graph. Let w be a path in G. Prove that the edges of w are distinct."
         }
       ],
-      "derivation": "sections/background.tex, Proposition 2.39 (label prop:pathtrail); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
+      "derivation": "sections/background.tex, Proposition 2.35 (label prop:pathtrail); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1799,7 +1799,7 @@
           "quote": "Indeed, Corollary 2.9.7 shows that a shortest walk from u to v (if it exists) must also be a shortest path from u to v."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.5 (label app:distance), Proposition A.1 (label prop:shortest); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
+      "derivation": "appendices/derivations.tex, Appendix A.1 (label app:distance), Proposition A.1 (label prop:shortest); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1820,7 +1820,7 @@
           "quote": "adj. 0 1 0 / 1 0 1 / 0 1 0"
         }
       ],
-      "derivation": "sections/example.tex, Table 8 (label tab:walkcounts); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1 and 6; premise: the matrix of C28 defines B",
+      "derivation": "sections/example.tex, Table 4 (label tab:walkcounts); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1 and 6; premise: the matrix of C28 defines B",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1847,7 +1847,7 @@
           "quote": "G գրաֆի (u0, u_k)-ճանապարհը կանվանենք փակ ճանապարհ կամ ցիկլ, եթե այն փակ շրջանցում է, այսինքն՝ եթե u0 = u_k։"
         }
       ],
-      "derivation": "sections/background.tex, Remark 2.32 (label rem:trail) and Non-example (label nex:cycle); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1, 2 and 3",
+      "derivation": "sections/background.tex, Remark 2.28 (label rem:trail) and Non-example 2.40 (label nex:cycle); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1, 2 and 3",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1896,7 +1896,7 @@
           "quote": "G գրաֆի ցանկացած u, v և w գագաթների համար d_G(u, v) ≤ d_G(u, w) + d_G(w, v)։"
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.5 (label app:distance), Proposition A.2 (label prop:distprops), uses Proposition A.1",
+      "derivation": "appendices/derivations.tex, Appendix A.1 (label app:distance), Proposition A.2 (label prop:distprops), uses Proposition A.1",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1964,7 +1964,7 @@
           "quote": "The number of walks of length 2 from a vertex to itself is just the number of edges at that vertex, or the vertex degree."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Remark 4.11 (label rem:diagonal); sections/background.tex, Remark 2.56 (label rem:connected); script section 'N = 2' of appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "sections/answer2_connectivity.tex, Remark 4.21 (label rem:edge); sections/answer2_connectivity.tex, Remark 4.2 (label rem:connected); script section 'N = 2' of appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -1987,7 +1987,7 @@
           "quote": "Then the entry in the (i, j)-position of the matrix Ak is the number of walks of length k from vi to vj in G."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Proposition 4.17 (label prop:sharp), Example 4.18 (label ex:sharp), Table 6 (label tab:sharp) and Remark 4.19 (label rem:failcount) (the failing graphs are the labelled paths, N!/2); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "sections/answer2_connectivity.tex, Proposition 4.23 (label prop:sharp); sections/example.tex, Example 6.3 (label ex:four) and Table 5 (label tab:exhaustive), last column (the failing graphs are the labelled paths, N!/2); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -2016,7 +2016,7 @@
           "quote": "Then, there is a path from u to v of length ≤ k."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Proposition 4.5 (label prop:pair) and Corollary 4.10 (label cor:components); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "sections/answer2_connectivity.tex, Proposition 4.13 (label prop:pair) and Corollary 4.19 (label cor:components); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -2082,7 +2082,7 @@
           "quote": "Then the entry in the (i, j)-position of the matrix Ak is the number of walks of length k from vi to vj in G."
         }
       ],
-      "derivation": "appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt), section 'Exhaustive check'; sections/example.tex, Table 10 (label tab:exhaustive); appendices/derivations.tex, Appendix A.6 (label app:crosschecks)",
+      "derivation": "appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt), section 'Exhaustive check'; sections/example.tex, Table 5 (label tab:exhaustive); appendices/derivations.tex, Appendix A.5 (label app:crosschecks)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -2110,7 +2110,7 @@
           "quote": "Then, there is a path from u to v of length ≤ k."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (any exponent m >= N - 1), Proposition 4.16 (label prop:iplusa); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (any exponent m >= N - 1), Proposition 4.14 (label prop:iplusa); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/modules/m1.json b/papers/adjacency-walks-connectivity/evidence/modules/m1.json
index b9d4257..af523d7 100644
--- a/papers/adjacency-walks-connectivity/evidence/modules/m1.json
+++ b/papers/adjacency-walks-connectivity/evidence/modules/m1.json
@@ -19,7 +19,7 @@
           "quote": "Սահմանում 1.1.4: u և v գագաթները կանվանենք հարևան, եթե uv ∈ E։"
         }
       ],
-      "derivation": "sections/background.tex, Proposition 2.20 (label prop:rowsums); numbers by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "sections/background.tex, Proposition 2.17 (label prop:rowsums); numbers by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -44,7 +44,7 @@
           "quote": "A walk (in G) means a finite sequence (v0 , v1 , . . . , vk ) of vertices of G (with k ≥ 0) such that all of v0 v1 , v1 v2 , v2 v3 , . . . , vk−1 vk are edges of G."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.1 (label app:walkcount); sections/background.tex, Remark 2.24 (label rem:walk)",
+      "derivation": "sections/background.tex, Remark 2.20 (label rem:vertexlist)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -71,7 +71,7 @@
           "quote": "Thus the total number of walks of length k from vi to vj is the sum of the expressions (Ak−1 )ir Arj over all vertices vr of G, which is exactly (Ak )ij ."
         }
       ],
-      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walkcount); appendices/derivations.tex, Appendix A.1 (label app:walkcount); finite cross-check by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "sections/answer1_walks.tex, proof of Theorem 3.5 (label thm:walks); finite cross-check by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -87,7 +87,7 @@
       "kind": "derived",
       "module": "m1",
       "support": [],
-      "derivation": "appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt), last section; appendices/derivations.tex, Appendix A.6 (label app:crosschecks)",
+      "derivation": "appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt), last section; appendices/derivations.tex, Appendix A.5 (label app:crosschecks)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -140,7 +140,7 @@
           "quote": "G գրաֆի (u0, u_k)-ճանապարհը կանվանենք պարզ (u0, u_k)-ճանապարհ, եթե նրա մեջ մտնող բոլոր գագաթները զույգ առ զույգ տարբեր են։"
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.10 (label prop:warning) and Table 5 (label tab:walksvspaths); enumeration by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
+      "derivation": "appendices/derivations.tex, Appendix A.2 (label app:counterexample); sections/answer1_walks.tex, Proposition 3.11 (label prop:warning) and Table 6 (label tab:counterex); enumeration by appendices/scripts/m1_walks.py (output appendices/scripts/m1_walks_output.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/modules/m2.json b/papers/adjacency-walks-connectivity/evidence/modules/m2.json
index 4f27546..b734ad2 100644
--- a/papers/adjacency-walks-connectivity/evidence/modules/m2.json
+++ b/papers/adjacency-walks-connectivity/evidence/modules/m2.json
@@ -300,7 +300,7 @@
           "quote": "Let G be a simple graph. Let w be a path in G. Prove that the edges of w are distinct."
         }
       ],
-      "derivation": "sections/background.tex, Proposition 2.39 (label prop:pathtrail); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
+      "derivation": "sections/background.tex, Proposition 2.35 (label prop:pathtrail); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -347,7 +347,7 @@
           "quote": "Indeed, Corollary 2.9.7 shows that a shortest walk from u to v (if it exists) must also be a shortest path from u to v."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.5 (label app:distance), Proposition A.1 (label prop:shortest); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
+      "derivation": "appendices/derivations.tex, Appendix A.1 (label app:distance), Proposition A.1 (label prop:shortest); checked by appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), section 5",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -368,7 +368,7 @@
           "quote": "adj. 0 1 0 / 1 0 1 / 0 1 0"
         }
       ],
-      "derivation": "sections/example.tex, Table 8 (label tab:walkcounts); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1 and 6; premise: the matrix of C28 defines B",
+      "derivation": "sections/example.tex, Table 4 (label tab:walkcounts); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1 and 6; premise: the matrix of C28 defines B",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -395,7 +395,7 @@
           "quote": "G գրաֆի (u0, u_k)-ճանապարհը կանվանենք փակ ճանապարհ կամ ցիկլ, եթե այն փակ շրջանցում է, այսինքն՝ եթե u0 = u_k։"
         }
       ],
-      "derivation": "sections/background.tex, Remark 2.32 (label rem:trail) and Non-example (label nex:cycle); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1, 2 and 3",
+      "derivation": "sections/background.tex, Remark 2.28 (label rem:trail) and Non-example 2.40 (label nex:cycle); appendices/scripts/m2_walks.py (output appendices/scripts/m2_walks_output.txt), sections 1, 2 and 3",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -444,7 +444,7 @@
           "quote": "G գրաֆի ցանկացած u, v և w գագաթների համար d_G(u, v) ≤ d_G(u, w) + d_G(w, v)։"
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.5 (label app:distance), Proposition A.2 (label prop:distprops), uses Proposition A.1",
+      "derivation": "appendices/derivations.tex, Appendix A.1 (label app:distance), Proposition A.2 (label prop:distprops), uses Proposition A.1",
       "confidence": "high",
       "status": "supported",
       "used_in": [
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/modules/m3.json b/papers/adjacency-walks-connectivity/evidence/modules/m3.json
index 7bdfc36..620f28d 100644
--- a/papers/adjacency-walks-connectivity/evidence/modules/m3.json
+++ b/papers/adjacency-walks-connectivity/evidence/modules/m3.json
@@ -62,7 +62,7 @@
           "quote": "The number of walks of length 2 from a vertex to itself is just the number of edges at that vertex, or the vertex degree."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Remark 4.11 (label rem:diagonal); sections/background.tex, Remark 2.56 (label rem:connected); script section 'N = 2' of appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "sections/answer2_connectivity.tex, Remark 4.21 (label rem:edge); sections/answer2_connectivity.tex, Remark 4.2 (label rem:connected); script section 'N = 2' of appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -85,7 +85,7 @@
           "quote": "Then the entry in the (i, j)-position of the matrix Ak is the number of walks of length k from vi to vj in G."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Proposition 4.17 (label prop:sharp), Example 4.18 (label ex:sharp), Table 6 (label tab:sharp) and Remark 4.19 (label rem:failcount) (the failing graphs are the labelled paths, N!/2); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "sections/answer2_connectivity.tex, Proposition 4.23 (label prop:sharp); sections/example.tex, Example 6.3 (label ex:four) and Table 5 (label tab:exhaustive), last column (the failing graphs are the labelled paths, N!/2); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -114,7 +114,7 @@
           "quote": "Then, there is a path from u to v of length ≤ k."
         }
       ],
-      "derivation": "sections/answer2_connectivity.tex, Proposition 4.5 (label prop:pair) and Corollary 4.10 (label cor:components); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "sections/answer2_connectivity.tex, Proposition 4.13 (label prop:pair) and Corollary 4.19 (label cor:components); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -180,7 +180,7 @@
           "quote": "Then the entry in the (i, j)-position of the matrix Ak is the number of walks of length k from vi to vj in G."
         }
       ],
-      "derivation": "appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt), section 'Exhaustive check'; sections/example.tex, Table 10 (label tab:exhaustive); appendices/derivations.tex, Appendix A.6 (label app:crosschecks)",
+      "derivation": "appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt), section 'Exhaustive check'; sections/example.tex, Table 5 (label tab:exhaustive); appendices/derivations.tex, Appendix A.5 (label app:crosschecks)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
@@ -208,7 +208,7 @@
           "quote": "Then, there is a path from u to v of length ≤ k."
         }
       ],
-      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (any exponent m >= N - 1), Proposition 4.16 (label prop:iplusa); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
+      "derivation": "appendices/derivations.tex, Appendix A.4 (label app:iplusa) (any exponent m >= N - 1), Proposition 4.14 (label prop:iplusa); appendices/scripts/m3_connectivity.py (output appendices/scripts/m3_connectivity.out.txt)",
       "confidence": "high",
       "status": "supported",
       "used_in": [
```

```diff
diff --git a/papers/adjacency-walks-connectivity/figures/generated_numbers.tex b/papers/adjacency-walks-connectivity/figures/generated_numbers.tex
new file mode 100644
index 0000000..67d686e
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/figures/generated_numbers.tex
@@ -0,0 +1,17 @@
+% Generated by appendices/scripts/author_numbers.py. Do not edit.
+\newcommand{\matA}{\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}}
+\newcommand{\matAtwo}{\begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{pmatrix}}
+\newcommand{\matAthree}{\begin{pmatrix}0 & 2 & 0 \\ 2 & 0 & 2 \\ 0 & 2 & 0\end{pmatrix}}
+\newcommand{\matAfour}{\begin{pmatrix}2 & 0 & 2 \\ 0 & 4 & 0 \\ 2 & 0 & 2\end{pmatrix}}
+\newcommand{\matAfive}{\begin{pmatrix}0 & 4 & 0 \\ 4 & 0 & 4 \\ 0 & 4 & 0\end{pmatrix}}
+\newcommand{\matSB}{\begin{pmatrix}1 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 1\end{pmatrix}}
+\newcommand{\matIB}{\begin{pmatrix}2 & 2 & 1 \\ 2 & 3 & 2 \\ 1 & 2 & 2\end{pmatrix}}
+\newcommand{\matD}{\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\matDtwo}{\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\matSD}{\begin{pmatrix}1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\matID}{\begin{pmatrix}2 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 1\end{pmatrix}}
+\newcommand{\matP}{\begin{pmatrix}0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0\end{pmatrix}}
+\newcommand{\matPtwo}{\begin{pmatrix}1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 \\ 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 1\end{pmatrix}}
+\newcommand{\matPthree}{\begin{pmatrix}0 & 2 & 0 & 1 \\ 2 & 0 & 3 & 0 \\ 0 & 3 & 0 & 2 \\ 1 & 0 & 2 & 0\end{pmatrix}}
+\newcommand{\matPsmall}{\begin{pmatrix}1 & 1 & 1 & 0 \\ 1 & 2 & 1 & 1 \\ 1 & 1 & 2 & 1 \\ 0 & 1 & 1 & 1\end{pmatrix}}
+\newcommand{\matPfull}{\begin{pmatrix}1 & 3 & 1 & 1 \\ 3 & 2 & 4 & 1 \\ 1 & 4 & 2 & 3 \\ 1 & 1 & 3 & 1\end{pmatrix}}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/main.tex b/papers/adjacency-walks-connectivity/main.tex
new file mode 100644
index 0000000..68eaaa3
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/main.tex
@@ -0,0 +1,78 @@
+\documentclass[11pt,a4paper]{article}
+\usepackage[utf8]{inputenc}
+\usepackage[T1]{fontenc}
+\usepackage{lmodern}
+\usepackage[a4paper,margin=2.5cm]{geometry}
+\usepackage{amsmath,amsthm,amssymb}
+\usepackage{graphicx}
+\usepackage{booktabs}
+\usepackage[backend=biber,style=numeric,sorting=nyt,urldate=long]{biblatex}
+\addbibresource{references.bib}
+\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=black]{hyperref}
+\usepackage[capitalise,nameinlink]{cleveref}
+
+% Theorem-like environments, one shared counter inside each section.
+\theoremstyle{definition}
+\newtheorem{definition}{Definition}[section]
+\newtheorem{remark}[definition]{Remark}
+\newtheorem{example}[definition]{Example}
+\newtheorem{nonexample}[definition]{Non-example}
+\theoremstyle{plain}
+\newtheorem{theorem}[definition]{Theorem}
+\newtheorem{lemma}[definition]{Lemma}
+\newtheorem{proposition}[definition]{Proposition}
+\newtheorem{corollary}[definition]{Corollary}
+\newtheorem{test}[definition]{Test}
+\crefname{nonexample}{Non-example}{Non-examples}
+\crefname{test}{Test}{Tests}
+\crefname{appendix}{Appendix}{Appendices}
+\crefname{subappendix}{Appendix}{Appendices}
+
+% The plain-words paragraph that precedes every definition, theorem, test and example.
+\newenvironment{plainwords}{\par\medskip\noindent\textbf{In plain words.}\ \itshape}{\par\medskip}
+
+\newcommand{\n}[1]{n_{#1}}
+\newcommand{\NN}{\mathbb{N}}
+\setlength{\emergencystretch}{2em}
+
+% Matrices computed by appendices/scripts/author_numbers.py
+\input{figures/generated_numbers}
+
+\title{Walks, Paths and Connectivity from the Adjacency Matrix:\\
+A Study Note on $(A^k)_{ij}$ and the Connectivity Test}
+\author{Study note prepared from a lecture whiteboard and the course textbook}
+\date{}
+
+\begin{document}
+\maketitle
+
+\begin{abstract}
+A graph with $N$ vertices can be stored as an $N\times N$ table of zeros and ones, its adjacency matrix $A$.
+This note answers three questions about that table.
+First, the entry in row $i$ and column $j$ of the matrix power $A^k$ is the number of walks of length $k$ from vertex $n_i$ to vertex $n_j$; it counts walks, not paths \cite{quinlan_matrices_graphs,bai2025adjacency}.
+Second, a graph with $N\ge 2$ vertices is connected if and only if every entry off the diagonal of $A+A^2+\dots+A^{N-1}$ is positive, or equivalently if and only if $(I+A)^{N-1}$ has no zero entry.
+Third, a path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ with no repeated vertex, which is the course textbook's simple path.
+Both theorems are proved in full, because the course textbook does not state them in the pages checked \cite{petrosyan2015grafneri}.
+Every matrix in the examples was computed by script.
+\end{abstract}
+
+\tableofcontents
+
+\input{sections/introduction}
+\input{sections/background}
+\input{sections/answer1_walks}
+\input{sections/answer2_connectivity}
+\input{sections/answer3_path}
+\input{sections/example}
+\input{sections/discussion}
+\input{sections/conclusion}
+
+\appendix
+\input{appendices/derivations}
+\input{appendices/course-terms}
+\input{appendices/photographs}
+\input{appendices/reproducibility}
+
+\printbibliography
+
+\end{document}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reader-findings.md b/papers/adjacency-walks-connectivity/reader-findings.md
new file mode 100644
index 0000000..d6777d6
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reader-findings.md
@@ -0,0 +1,84 @@
+# Reader findings
+
+## Round 1, 2026-10-31
+
+Technician reader findings for the draft evaluated in round 1, verbatim from the agent.
+
+FINDINGS
+
+F1 | comprehension | Abstract: "Both theorems are proved in full, because the course textbook does not state them in the pages checked [9]." | The abstract names three questions but then says "both theorems" without saying which two they are. The abstract also uses "walk", "path", "vertex", "off the diagonal" and "(I + A)^(N−1)" with no gloss. "I" is not defined there. | Name the two theorems ("the walk-counting theorem and the connectivity test"). Add a half-sentence defining I as the identity matrix. | 
+
+F2 | comprehension | 1.1: "the board puts a small mark above the letter A... a small n or a pair of quotation marks, not clearly a k [4, 5]." | The reader cannot see the photographs until Appendix C. Sections 1.1 and 1.4 describe the board's drawing in words ("an arrowhead at 2", "an edge 1–3 that the matrix lacks") with no figure. The reader must take these descriptions on faith for 25 pages. | Add a forward pointer ("see Figure 1, Appendix C") at the first mention, or move the figure into Section 1.1.
+
+F3 | comprehension | 1.1 and 1.4: "The assignment text added a third question"; "the assignment states that in the course a path has no repeated vertex." | "The assignment", "the board" and "the course" are never introduced. The reader does not know who wrote the assignment, whether it is available, or why the paper depends on it. The "[4, 5]" citations point to photographs, but the assignment text has no citation at all. | Add one sentence at the start of 1.1 saying what the assignment is and that it is unavailable as a file. Alternatively cite it as a numbered source.
+
+F4 | comprehension | 1.3: "both prove it loosely [7, 1]"; "(derived here)"; "(qualified)"; 1.4 "Kinds of statement". | The labels "derived", "interpretation", "qualified", "estimate" and "open" are defined only in the last paragraph of 1.4. The reader meets "qualified" in 1.1 and the abstract before then. "Qualified" is never defined precisely. It seems to mean "caveated", but this is a guess. | Define "qualified" in one sentence and move the "Kinds of statement" paragraph before first use, or add a forward reference.
+
+F5 | comprehension | 1.2 and 1.4 (Table 1, "Definition 2.18", "Definition 2.31", "Definition 2.13"). | The roles of "plain words" paragraphs versus formal definitions are clear. However, the story fixes "trip" as the word for "walk" and "clean route" for "path", while the paper later says "trail". Trail has no entry in Table 1. The "In plain words" for trail says "Our textbook calls it a path", which clashes with the story's "clean route". | Add "trail" to Table 1 (for example "trip with no repeated road").
+
+F6 | comprehension | 1.4: "The board writes (G, V) for the graph and eij ∈ V in its matrix definition, where its V is the edge set." | This is confusing. The reader has not yet seen what is on the board, and a vertex set V that is secretly the edge set is hard to follow. | Say "the board uses V for the edge set (probably a slip)" and move the details to Appendix C, keeping only the paper's own notation in the main text.
+
+F7 | comprehension | 1.4 and 2.3: "The textbook's Fig. 1.2.5 shows a graph on five vertices... The textbook's own examples force the seven edges..." | The textbook graph is introduced inside a block of walk examples. The reader cannot see the figure and must trust the reconstruction from the edge list. The figure is never reproduced. | Draw the seven-edge textbook graph as a small figure, or list the edges as a labelled example (for example "Example 2.20a") before it is used.
+
+F8 | comprehension | 2.1: "The textbook's own definition of degree was not read, so no textbook number is given." Also Definition 2.13, "The textbook's definition number for this matrix was not recorded." | This is bookkeeping about the author's process, not about the mathematics. It makes the reader wonder whether the definitions were checked. | Drop it from the body and keep it in Appendix B, or state it once in 1.4.
+
+F9 | comprehension | Definition 2.18: "u0, e1, u1, ..., uk−1, ek, uk of vertices and edges with ei = ui−1 ui". | The notation ui−1ui for an edge is explained earlier (Table 2, "uv, eij"), but the symbol "ei" is introduced as an edge and is also the index in "eij" (the board's edge). The two uses of e look alike. | Say "the i-th edge ei joins ui−1 and ui".
+
+F10 | comprehension | Remark 2.19: "The textbook does not say in so many words that k = 0 is allowed. This paper reads k = 0 as allowed, because the textbook's property d(u,u) = 0 of distance needs a path of length 0." | This is a long justification for a small convention. The reader cannot tell why it matters: the length-0 walk is needed only later (Lemma 2.45, Remark 4.2). | Add "needed in Lemma 2.45 and Remark 4.2" to say why the point is raised.
+
+F11 | comprehension | 2.3, Remark 2.28: "In the board graph every trail is also a path... for every length from 0 to 4 ... (derived, checked by script for lengths up to 4)." | The reader is asked to take a claim for lengths 0 to 4 on trust. A short argument is available: the board graph is a path with 3 vertices and no cycle. The text then says the claim is "derived" yet only "checked by script". | Replace with one sentence of reasoning ("the board graph has no cycle, so no trail revisits a vertex"), or label it "checked" only.
+
+F12 | comprehension | 2.4 (Cycles): "Cycles are not needed for the main results; they are given because the textbook's list of definitions includes them." | A full page of definitions, examples and non-examples (Definitions 2.36 and 2.37, Remark 2.38) is not used afterwards. The reader cannot tell whether to retain it. Likewise for Table 3 and the trail material, which is needed only for Remark 4.2. | Mark 2.4 as skippable at its start, or move it to an appendix.
+
+F13 | comprehension | Definition 2.41 and the text after it: "The textbook's 'path' here is its Definition 1.2.12, a trail. The definition does not depend on whether one reads trail or path..." | The reader is told that "the pair (V,d) is a metric space" with no explanation of "metric space". Distance is used later only in Remark 4.20. | Delete the metric-space sentence or gloss it ("d behaves like an ordinary distance").
+
+F14 | comprehension | Lemma 2.45 proof: "Form the sequence W′ = u0, ..., ui, uj+1, ..., uk; if j = k nothing follows ui." | This is the hardest step to follow and I had to read it three times. The index juggling hides the idea of cutting out the loop between ui and uj. The edge case j = k is stated inside a sentence about the sequence. The trace example appears only after the proof. | Add one sentence before the formal construction ("delete everything after the first ui up to and including uj, so the walk goes from ui straight on to uj+1"), or put the trace first.
+
+F15 | comprehension | Definition 3.1: "(XY)ij = Σ_{r=1}^N Xir Yrj" and the following remark that "A^0 = I... corresponds to one walk of length 0". | The pdf text of the formula is garbled in my reading, but the intent is clear. A technician who has not met matrix products will rely on the "plain words". The identity matrix I appears in Table 2 and in the abstract without a display of an example. | Show I once for N = 3. Show one numeric row-times-column product before Theorem 3.5.
+
+F16 | comprehension | Proof of Theorem 3.5: "Wk(i, j) is the sum over r = 1, ..., N of the number of walks of length k from ni to nj whose second-last vertex is nr. Fix r. We claim that the number in class r is Wk−1(i, r) · Arj." | The reader is not told in advance why the sum is organised by the second-last vertex. The proof is correct in form but long. The two bullet cases are clear. The "Why the argument is valid" paragraph then repeats it. | Open the proof with a roadmap sentence ("a walk of length k is a walk of length k−1 plus one final step; that final step is allowed exactly when Arj = 1").
+
+F17 | comprehension | 3.2, end: "A computer check supports the theorem but is not a proof: ... all 40, 360, 5120 and 76800 tested cases of (k, i, j) agreed." | The numbers 40, 360, 5120 and 76800 are not explained. The reader cannot tell how they arise (A.5 says k runs to 4 for N ≤ 4 and to 3 for N = 5, so the count depends on k, N, and the graph count). | Give the formula, for example "graphs × N² pairs × values of k", or drop the counts.
+
+F18 | comprehension | Proposition 3.11: "If ni has at least one neighbour, then (A²)ii = deg(ni) &gt; 0, but no path, and no trail, of length 2 from ni to ni exists." | "The first inequality" in the proof refers to "&gt; 0", but the statement has no inequality symbol sign besides "&gt;". The claim "no trail" is explained only by the edge being used twice, which is fine. The final sentence "Hence (A^k)ij is in general not the number of paths" does not follow from a single diagonal example unless one adds that k = 2 is a specific case. | Say "so the entry (A²)ii counts a walk that is not a path; hence the entries are not path counts".
+
+F19 | comprehension | Definition 4.5 (Connected component): "On the vertex set V write u ∼ v if G has a (u, v)-path. This relation is reflexive, symmetric and transitive, so V splits into classes." | Reflexive, symmetric, transitive and "classes" (equivalence relation) are used without explanation. The claim that the relation has these properties is not shown. | State "equivalence relation" with a one-line gloss and a pointer to why transitivity holds (join two walks).
+
+F20 | comprehension | Definition 4.9 (new notation S) and Remark 4.10. | S is defined as a sum of N−1 powers, but the reader does not see why N−1 is the right stopping point until Section 4.4. The "plain words" tell the reader to stop at "one step short" without a reason. | Add "(the reason is Corollary 2.46)" to the definition.
+
+F21 | comprehension | Proposition 4.14: "(I + A)^m ij &gt; 0 if and only if Sij &gt; 0. Every diagonal entry of (I + A)^m is at least 1." | The purpose of this second form is never stated in the main text: why would one prefer (I + A)^(N−1)? The reason appears only in 7.4 (repeated squaring). Its proof is deferred to Appendix A.4 although it is a half-page argument. | At first mention, add one sentence on motivation ("it can be computed by repeated squaring, Section 7.4").
+
+F22 | comprehension | Proposition 4.13, statement (i): "There is an (ni, nj)-path in G (in the sense of textbook Definition 2.1.1)." | The parenthetical is confusing. Definition 2.1.1 is about "connected", and the text calls the textbook "path" a trail. The reader does not know which meaning of "path" statement (i) uses. | Replace with "a path (Definition 2.31) from ni to nj" and refer to Remark 4.2 for the trail reading.
+
+F23 | comprehension | Proof of Theorem 4.15: "Together with the diagonal entries, which are always positive by Proposition 4.14, this is (c)." | The step from positivity of off-diagonal entries of (I+A)^(N−1) to (b) uses Proposition 4.14 with Sij, and the diagonal remark is easy to miss. Statement (a) also requires u = v pairs, which the proof dismisses by Remark 4.2. The chain is correct but spread over four references. | Add a three-line outline of the proof: (a) iff each pair joined, (b) via Prop 4.13, (c) via Prop 4.14.
+
+F24 | comprehension | Remark 4.21: "For N = 2 and one edge, S = A has zeros on the diagonal although the graph is connected. ... For N = 1 ... S is an empty sum." | This sits in a remark in the middle of the proof area and mixes three cases. The sentence "For N ≥ 3 and a connected graph the diagonal of S is positive anyway" is an unproved claim, said to be unneeded. | Split into short bullets, or cut the N ≥ 3 claim since the test does not need it.
+
+F25 | comprehension | 4.6: "Enough: Proposition 4.13 shows that if a trip between two different vertices exists at all, a trip of length at most N − 1 exists... Not fewer: the next statement shows that N − 1 cannot be lowered." | The heading says "N − 2 are not", but the argument for "not fewer" is a single counterexample family. The text says "the next statement shows" but a "plain words" paragraph sits between. The term "trip" is used while the formal statement uses "walk". | Use "walk" in this paragraph, or state that the claim is shown by Proposition 4.23 for a path graph.
+
+F26 | comprehension | Proposition 4.23 and Example 6.3. | The example prints A + A² as "(N − 2 powers)" with the (1,4) entry 0. The reader must locate the entry in a 4×4 matrix with no highlight. | Mark the (1,4) entry (for example boldface) and say "top-right entry".
+
+F27 | comprehension | 4.7, Remark 4.24: "Its correctness statement in the source is that for every vertex v there is a walk from s to v if and only if v is discovered when the search ends [10]." | BFS, "queue" and "discovered" are used before being defined. The plain-words version helps. The claim "agree on all 32768 labelled graphs with 6 vertices" is taken on faith from a script. | State briefly that the BFS comparison is only a sanity check, with a pointer to Table 5.
+
+F28 | comprehension | 6.1: "Also A³ = 2A and A^(k+2) = 2A^k for k = 1, ..., 5 (script)." | The reader is told this pattern without any reason or relevance to the questions. It does not return afterwards. | Delete it, or say why it matters (it shows that the entries grow).
+
+F29 | comprehension | Table 4 (6.1). | The columns "trails" and "paths" are equal in every row, and the table includes k = 0 with a "closed walks" count of 3 but k = 1 with 0. The reader cannot tell what the table is meant to show. The caption does not say. The reported "walks" for k = 4 (12) is not tied to the matrix entries shown (the sum of A⁴ is 12). | Add one sentence on the point of the table ("walks multiply while paths stop at length 2"). State that the walk column equals the sum of the entries of A^k.
+
+F30 | comprehension | Table 5: "wrong with N − 2 powers" column: 1, 3, 12, 60, 360. | The numbers are not explained. The text covers N = 3 (3 graphs) and N = 4 (12 graphs) only. The reader cannot check the 60 and 360, or see why they are the numbers of labelled graphs on which the shortened test fails. | State the rule (for example, the shortened test errs exactly on graphs of diameter N−1, that is, labelled paths, which number N!/2), or say that no pattern is claimed.
+
+F31 | comprehension | 7.4: "Reaching A^(N−1) from A takes N − 2 products, so the matrix test costs about (N − 2)N³ multiplications: 98,000,000 for N = 100 ... t squarings, 7 for N = 100, costing 7,000,000 multiplications." | "t squarings" and "2^t ≥ N − 1" are given without a derivation (log2 99 is about 6.6, so 7). The "BFS reads each row once... N² = 10,000" claim is derived with no argument. The conclusion "useful because its answer is a clean statement ..., not because it is fast" is an opinion. | Show the arithmetic in one line, or say these are illustrative estimates.
+
+F32 | comprehension | 7.3: "As written, Theorem 1 is false for any definition of path that forbids repeated vertices or repeated edges... so their explanation is wrong although their statements of the test are correct." | The reader is told that published sources are wrong. The only evidence given is Proposition 3.11, and the sources are not quoted. The reader has to take the claim about [7] and [1] on faith. | Quote the sentence from [7] in the body, or soften to "as we read it".
+
+F33 | comprehension | Sections 1.3, 7.1, 7.5: repeated statements ("the rest of the book was not read page by page", "qualified") at three places, plus Appendix B. | The same caveat is repeated at least four times, which hides the main results. The reader needs it once, in 1.4. | State it once in 1.4 and refer to it.
+
+F34 | comprehension | Section 7.5, "Open: whether the lecturer's intended answer to the board's question 2 was the sum test, the (I+A)^(N−1) test, or BFS... Only the user can settle these." | "The user" is not a reader of a paper. The sentence addresses the person who gave the task, so the paper's frame (study note versus a reply to a request) is unclear. | Replace "Only the user can settle these" with "These can be settled only by the lecturer".
+
+F35 | comprehension | Appendix D: "The scripts are copies of the ones in the folder modules/, which are kept as the module records." | The reader has no access to "modules/" or "figures/generated_numbers.tex" and cannot tell whether the scripts are shipped with the paper. The text also names script names (m1_walks.py and so on) throughout the body. | State where the scripts can be obtained, or remove the internal folder names from the paper.
+
+F36 | comprehension | Section 5 (Q3), whole section. | Section 5 repeats Definition 2.31 almost word for word. After the long treatment in Section 2, I could not say what Section 5 adds beyond the endpoint notation and the claim that both readings of "path" agree. | Fold Section 5 into Section 2.3, or state at its head that it only restates Definition 2.31 for the question Q3.
+
+F37 | comprehension | Whole paper, structure. | The paper is 31 pages for three short questions. The answers appear in the abstract and Section 1.3, but the main chain of reasoning (walk counting, then walk-to-path, then the test) is spread over Sections 2 to 4, with side topics (cycles, metric space, naming conventions, BFS, cost) in between. The reader cannot easily tell what is essential and what is context. | Add a "reading path" line in 1.5 listing the sections needed for the proofs (2.3, 2.7, 3.1-3.2, 4.1-4.4) and the optional ones.
+
+READER SUMMARY
+The paper starts from a lecture-board photograph that shows a small graph and its table of zeros and ones (the adjacency matrix A). It asks three things. First, what does entry (i,j) of the k-th power of A mean? Second, how can one tell from A alone whether the graph is connected? Third, what is a "path" between two vertices? Its answers are as follows. Entry (i,j) of A^k counts the walks of length k from vertex i to vertex j. A walk may revisit vertices and reuse edges, so the entry does not count paths. It is proved by induction on k, by sorting walks by their second-last vertex. A graph with at least two vertices is connected exactly when every off-diagonal entry of A + A² + … + A^(N−1) is positive. The same holds when (I + A)^(N−1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path, and that a path on N vertices has at most N−1 edges. So longer walks add nothing, and stopping at N−2 can fail, as the four-house row shows. A path is defined as a walk with no repeated vertex. The paper notes that its textbook calls this a "simple path" and uses "path" for a walk with no repeated edge (which the paper calls a "trail"). It also notes that the board's drawing and matrix disagree, and that the mark above A on the board is read as an exponent k. The results are checked by script against breadth-first search on all graphs with up to six vertices. The paper says the matrix test is neat but not fast, compared with breadth-first search. I can state this, but I cannot say why the study note needed 31 pages, or which parts the main argument needs and which are context.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/references.bib b/papers/adjacency-walks-connectivity/references.bib
new file mode 100644
index 0000000..1abab0f
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/references.bib
@@ -0,0 +1,95 @@
+@misc{petrosyan2015grafneri,
+  author       = {Petrosyan, P. A. and Mkrtchyan, V. V. and Kamalyan, R. R.},
+  title        = {Grafneri tesutyun (Graph Theory: a study guide)},
+  year         = {2015},
+  howpublished = {File \texttt{Grafneri\_tesutyun.pdf}, course textbook in Armenian},
+  note         = {Supplied by the user. Yerevan State University Press, Yerevan. ISBN 978-5-8084-1995-7. Locators are printed page numbers.},
+}
+
+@misc{whiteboard1,
+  title        = {Lecture whiteboard photo 1},
+  howpublished = {File \texttt{sources/whiteboard-1.jpg}},
+  year         = {n.d.},
+  note         = {Supplied by the user. Photograph of a lecture board; author and date unknown. Accessed 2026-10-27.},
+}
+
+@misc{whiteboard2,
+  title        = {Lecture whiteboard photo 2},
+  howpublished = {File \texttt{sources/whiteboard-2.jpg}},
+  year         = {n.d.},
+  note         = {Supplied by the user. Second photograph of the same board; author and date of the board unknown. Accessed 2026-10-27.},
+}
+
+@online{grinberg2025graph,
+  author  = {Grinberg, Darij},
+  title   = {An introduction to graph theory (Text for Math 530 in Spring 2022 at Drexel University)},
+  year    = {2025},
+  note    = {arXiv:2308.04512v3 [math.HO], Spring 2025 edition, 7 June 2025; lecture-note text, 454 pp.; page locators are the document's own},
+  url     = {https://arxiv.org/abs/2308.04512},
+  urldate = {2026-10-27},
+}
+
+@online{quinlan_matrices_graphs,
+  title   = {Chapter 1 Matrices and Graphs, 1.1 The Adjacency Matrix (linear algebra course notes, NUI Galway)},
+  year    = {n.d.},
+  note    = {Lecture notes, School of Mathematical and Statistical Sciences, University of Galway; author and date do not appear in the file},
+  url     = {https://maths.nuigalway.ie/~rquinlan/linearalgebra/section1-1.pdf},
+  urldate = {2026-10-27},
+}
+
+@online{lehman_mcs_adjacency,
+  author  = {Lehman, Eric and Leighton, F. Thomson and Meyer, Albert R.},
+  title   = {9.3: Adjacency Matrices (Mathematics for Computer Science; MIT OpenCourseWare), Engineering LibreTexts},
+  year    = {n.d.},
+  note    = {Engineering LibreTexts, CC BY-NC-SA; page last modified 2021-07-02; publication year of the underlying book is not on the page},
+  url     = {https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Mathematics_for_Computer_Science_(Lehman_Leighton_and_Meyer)/02%3A_Structures/09%3A_Directed_graphs_and_Partial_Orders/9.03%3A_Adjacency_Matrices},
+  urldate = {2026-10-27},
+}
+
+@article{paramadevan2021adjacency,
+  author  = {Paramadevan, P. and Sotheeswaran, S.},
+  title   = {Properties of Adjacency Matrix of a Graph and It's Construction},
+  journal = {JSc EUSL (Journal of Science, Eastern University, Sri Lanka)},
+  year    = {2021},
+  volume  = {12},
+  number  = {1},
+  pages   = {13--21},
+  doi     = {10.4038/jsc.v12i1.29},
+  url     = {https://www.fsc.esn.ac.lk/jsc/archive/12.1.2.pdf},
+  urldate = {2026-10-27},
+}
+
+@online{bai2025adjacency,
+  author  = {Bai, Shuliang},
+  title   = {Important Properties and Applications of the Adjacency Matrix (20250310)},
+  year    = {2025},
+  note    = {Lecture notes, BIMSA, dated 2025-03-10 in the title},
+  url     = {https://bimsa.net/doc/notes/48535.pdf?id=0.3935315718408674},
+  urldate = {2026-10-27},
+}
+
+@online{weisstein_connectedgraph,
+  author  = {Weisstein, Eric W.},
+  title   = {Connected Graph},
+  year    = {n.d.},
+  note    = {Wolfram MathWorld; no publication date on the page},
+  url     = {https://mathworld.wolfram.com/ConnectedGraph.html},
+  urldate = {2026-10-27},
+}
+
+@online{wikipedia_path_graph_theory,
+  title   = {Path (graph theory)},
+  year    = {n.d.},
+  note    = {Wikipedia, English edition, revision of 5 June 2026 (oldid 1357845833) as fetched},
+  url     = {https://en.wikipedia.org/wiki/Path_(graph_theory)},
+  urldate = {2026-10-27},
+}
+
+@online{schost2026bfs,
+  author  = {Schost, {\'E}ric},
+  title   = {CS 341: Algorithms, Lecture 10: Graphs, breadth first search},
+  year    = {2026},
+  note    = {Lecture slides, David R. Cheriton School of Computer Science, University of Waterloo, Winter 2026},
+  url     = {https://www.student.cs.uwaterloo.ca/~cs341/lectures/lecture10.pdf},
+  urldate = {2026-10-27},
+}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reports/paper-author-round1.md b/papers/adjacency-walks-connectivity/reports/paper-author-round1.md
new file mode 100644
index 0000000..9e35912
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reports/paper-author-round1.md
@@ -0,0 +1,31 @@
+The paper is written and builds cleanly. I did not run or hand-verify the textbook pages again; the evidence file is final and I used it as given.
+
+**Files created in `papers/adjacency-walks-connectivity/`**
+- `main.tex`, `references.bib` (11 entries, keys equal the evidence source ids), `self-evaluation.md`, and the compiled `main.pdf` (31 pages).
+- `sections/`: `introduction`, `background`, `answer1_walks`, `answer2_connectivity`, `answer3_path`, `example`, `discussion`, `conclusion`.
+- `appendices/`: `derivations`, `course-terms`, `photographs`, `reproducibility`.
+- `appendices/scripts/`: copies of the three module scripts and their outputs, plus a new `author_numbers.py` and its output.
+- `figures/generated_numbers.tex`: the matrices in the paper, written by `author_numbers.py`.
+
+**Edits to existing files.** I did not edit `evidence/evidence.json` by hand. In `evidence.base.json` and `modules/m1.json`, `m2.json` and `m3.json` I changed only the `derivation` locator strings, so they name the paper's real proposition, table and appendix numbers. Then I rebuilt the merged file with `merge_evidence.py`. No claim was added, so there is no `author.json`.
+
+**Mechanical checks**
+- `build.sh`: exit 0, no LaTeX errors, undefined references or undefined citations.
+- `check_citations.py`: cited keys 11, bib entries 11, evidence sources 11, errors 0, warnings 0.
+- `check_claims.py`: 11 sources, 70 supported, 7 qualified, 0 unverified, 0 removed, errors 0, warnings 0.
+- `check_evidence_rebuild.py`: rebuild from base plus 3 fragments, 0 differences.
+- `inspect_pdf.py`: 31 pages, errors 0, warnings 1. The warning is one overfull box of 0.36 pt, which I left.
+- `check_self_evaluation.py`: inputs 13, errors 0, warnings 0.
+- Re-running `m1_walks.py`, `m2_walks.py` and `m3_connectivity.py` reproduces their saved outputs exactly.
+- I read `build/main.txt` from start to end and fixed what it showed. One real fix: the Theorem 4.15 paragraph had confused which source gave which proof.
+
+**Unverified claims in the text:** none.
+
+**Qualified claims, each disclosed in the text:** C24 and m2-8 (the course meaning of "path"), C29 and m1-9 (the mark above A), m2-15 (length-0 walks), C36 (the second form of the test, whose only source has a proof sketch), and m3-11 (the textbook's silence on both theorems).
+
+**Not fully justified**
+- **Textbook references.** The textbook's own definition of degree and its number for the adjacency-matrix definition were never recorded, so `background.tex` gives the matrix only a page (p. 11) and cites degree to a lecture-note remark.
+- **Textbook graph.** The seven edges I use for the textbook's Fig. 1.2.5 are the ones its own examples force. That reading is the module's, and no claim of its own covers it.
+- **Walk and trail counts.** Some counts printed in the paper come from the module scripts, not from `author_numbers.py`: the walk, trail and path table, the exhaustive-check table, and the random-graph counts. Those outputs match the saved files.
+- **Bibliography years.** Years are `n.d.` where the evidence has none, because the citation checker requires a year field.
+- **Armenian text.** The textbook's Armenian is not reproduced, since pdflatex has no Armenian support configured. I used English glosses and a transliterated title.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md b/papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md
new file mode 100644
index 0000000..04b82b1
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md
@@ -0,0 +1,48 @@
+SCORES
+1 Correctness: 5 -- I recomputed every number I could with my own script, and all match the paper: the board powers A to A^5, S, (I+A)^2 and the disconnected matrices (sections/example.tex, Examples 6.1 and 6.2), the P4 matrices (Example 6.3), Table 4, Table 5 (graphs 2/8/64/1024/32768; connected 1/4/38/728/26704; N-2 failures 1/3/12/60/360), the walk-test case counts 40/360/5120/76800 (Section 3.2), the costs 98,000,000 and 7,000,000, and the largest entry 38,742,049 of A^9 for K10 (Section 7.4). The proofs of Theorem 3.5, Lemma 2.45, Proposition 4.13, Proposition 4.14 (Appendix A.4) and Theorem 4.15 are valid step by step.
+2 Evidence coverage: 4 -- The 77 claims in evidence.json cover every cited statement, and the quotes match. One exception: Definition 2.9 (sections/background.tex:69-71) cites Quinlan's remark about walks of length 2 as the definition of degree and says the textbook definition "was not read". The textbook defines degree as Definition 1.2.1 on printed p. 16.
+3 Citation integrity: 4 -- Eight sources checked (seven fetched or read locally, plus both board photos), and all support the attributed statements, including the paper's accurate criticism of Paramadevan's Theorem 1 and its proof of Theorem 2. One description is wrong: sections/introduction.tex:67 calls the peer-reviewed journal article [7] a "web source".
+4 Logical validity: 5 -- Every conclusion follows. The walk-to-path step in the proof of Proposition 4.13 that the cited sources skip is supplied by Lemma 2.45. The trail and path readings of "connected" are shown to agree (Remark 4.2, Section 5). The case i = j and N = 1 is handled (Remark 4.21).
+5 Understandability: 4 -- The plain-words layer and the story of houses and roads are applied almost everywhere. A few terms are used without explanation: "metric space" (background.tex:413), "reflexive, symmetric and transitive" (answer2_connectivity.tex:55), "queue" (answer2_connectivity.tex:293), "adjacency lists" (discussion.tex:49), and the binomial coefficient in example.tex:89, which appears before Appendix A.4 explains it.
+6 Completeness: 4 -- Every objective in the brief is met. Two small gaps: the textbook number for degree is missing (background.tex:71), and Table 3 has no explicit "course" column although the brief and the text at background.tex:366 say it does.
+7 Methodological rigor: 5 -- Every claim is tagged as cited, derived, interpretation or open. The script checks are presented as tests, not proofs (Sections 6.5 and 7.1), and the integer arithmetic assumption is stated (Section 7.1).
+8 Critical analysis: 5 -- Section 7.3 identifies and explains the source that says "paths" where it means walks. The drawing-versus-matrix mismatch and the mark above A are reported, not hidden (Sections 1.1, 1.4 and 7.5). Section 7.4 discusses cost. The textbook absence claim is qualified (Sections 1.3 and 7.5), and I confirmed it: the book's only later use of the adjacency matrix is Kirchhoff's theorem on printed p. 60.
+9 Internal consistency: 4 -- Terms (walk, trail, path) and notation (n_i, N, S) are consistent throughout. Two small inconsistencies: Table 3's header "This paper" against the text's "course" (background.tex:366-375), and [7] called a "web source" in introduction.tex:67 but a "published note" in Sections 4.4 and 7.3.
+10 Reproducibility: 5 -- Appendix D names a script and saved output for every number. figures/generated_numbers.tex holds the matrices, and they agree with my independent computation.
+11 LaTeX and PDF quality: 4 -- 31 pages, references resolve, and the matrices render (page 22 checked as an image). inspect_pdf reports 0 errors and 1 warning: an overfull hbox of 0.36pt at Example 2.29.
+12 Answer relevance: 5 -- Sections 3.5, 4.8 and 5 and the Conclusion (Section 8) answer Q1, Q2 and Q3 directly, and nothing outside the brief is claimed.
+
+FINDINGS
+F1 | minor | sections/background.tex:69-71 (Definition 2.9) | Says the textbook's definition of degree "was not read" and cites a Quinlan remark about walks as the definition, but the textbook defines degree as Definition 1.2.1 on printed p. 16 (PDF p. 17), as the number of edges incident to the vertex; this misses the brief's requirement to cite textbook numbers. | Title Definition 2.9 "textbook Definition 1.2.1", cite [9, p. 16], delete the "not read" sentence, add an evidence claim with the p. 16 quote, and add the row to Table 7.
+F2 | minor | sections/introduction.tex:67 | "One web source states the theorem with the word 'paths'" describes [7], which is a peer-reviewed journal article (JSc EUSL 12(1), DOI 10.4038/jsc.v12i1.29) and is called a "published note" elsewhere. | Replace "One web source" with "One published note".
+F3 | minor | sections/background.tex:366-375 (Table 3) | The text says the table lists "the course, textbook, and English names", but the columns are Textbook, English, This paper. | Rename the last column "Course / this paper", or reword line 366 to match the columns.
+F4 | minor | sections/answer2_connectivity.tex:204 (Corollary 4.19) | No plain-words paragraph comes before this corollary, against the study-note rule in the brief that every theorem-like statement has one. | Add one, e.g. "If the running total for two houses is positive, they are in the same piece of the village; if it is zero, they are in different pieces."
+F5 | minor | sections/background.tex:413 | "the pair (V,d) is a metric space" is not explained for a first-time reader. | Add: "that is, d behaves like an ordinary distance: properties 1 to 3 above are exactly the rules a distance must obey."
+F6 | minor | sections/answer2_connectivity.tex:55 | "reflexive, symmetric and transitive" is used without explanation. | Add one clause per word: "every vertex is related to itself, u ~ v gives v ~ u, and u ~ v with v ~ w gives u ~ w."
+F7 | minor | sections/answer2_connectivity.tex:293; sections/discussion.tex:49 | "queue" and "adjacency lists" are not explained. | Add "a queue is a list served first-in, first-out" and "an adjacency list stores, for each vertex, the list of its neighbours."
+F8 | minor | sections/example.tex:89 | The binomial coefficient binom(2,2) and the expansion (I+A)^2 = I + 2A + A^2 are used before Appendix A.4 explains them. | Add "(binomial expansion, Appendix A.4)" or write the product out: (I+A)(I+A) = I + A + A + A^2.
+F9 | minor | Example 2.29 (sections/background.tex; build/main.log:828) | Overfull hbox of 0.36pt. | Allow a line break in the vertex sequence, or reword the sentence slightly.
+
+CITATION SPOT CHECKS
+quinlan_matrices_graphs | fetched | supports | Definition 1.1.1, Notes 1-2, Theorem 1.1.3 and its proof (sum of (A^{k-1})_{ir}A_{rj} sorted by second-last vertex), and "the number of edges at that vertex, or the vertex degree" all appear verbatim. No author or date in the file, as the bib entry says.
+paramadevan2021adjacency | fetched | supports | Metadata matches (JSc EUSL 12(1) pp. 13-21, DOI 10.4038/jsc.v12i1.29). Properties 7-9, Theorem 1 ("different paths"), Theorem 2 (sum test with i != j) and Theorem 3 are verbatim. The paper's criticism that the proof says "paths" and goes from b_ij != 0 to a path without a lemma is accurate.
+bai2025adjacency | fetched | supports | Title, author and date match. Theorem 1 says walks, followed by "counts walks — not paths". Theorem 2 is the (I+A)^{n-1} criterion, with a proof sketch that says "paths", as the paper states.
+weisstein_connectedgraph | fetched | supports | States that a graph on n&gt;1 vertices is connected iff the sum of A^k for k=1..n-1 has no zero off-diagonal entries, with no proof, as the paper states.
+grinberg2025graph | fetched | supports | arXiv v3, "Spring 2025 edition, June 7, 2025", 454 pp. Exercise 2.9, Corollary 2.9.7, Section 2.9.4 ("vertices to spare"), Proposition 2.9.10, Definitions 2.9.12, 2.10.1 and 3.4.5, and Theorem 4.5.10 (proof by induction from C^0 = I_n) are all present.
+schost2026bfs | fetched | supports | Winter 2026 slides by Éric Schost. Correctness: "there is a walk s ; v in G if and only if discovered[v]"; "testing if G is connected"; adjacency lists; "Total: O(n + m)".
+petrosyan2015grafneri | fetched (local file, PDF pp. 12-13, 17, 22-24, 49-50) | supports | The wording of Definitions 1.1.4, 1.2.10-1.2.16, Lemma 1.2.1 (u != v, induction on length), the distance properties, Definition 2.1.1, the components paragraph and Remark 2.1.1 matches the paper's rendering and page locators. The degree definition (Definition 1.2.1, p. 16) exists but is not cited (F1).
+whiteboard1 / whiteboard2 | fetched (local images viewed) | supports | The transcription is accurate: matrix 010/101/010, arrowhead at 2, lines 1-2, 1-3 and 2-3, and a mark above A that looks like quotation marks or a small n, as the paper says.
+
+UNVERIFIED CLAIMS IN TEXT
+C24 | Definition 2.31 note and Definition 5.1 note (course meaning of "path", from the assignment text) | qualified
+C29 | Section 1.1 "Reading of the board"; Appendix C (mark above A read as k) | qualified
+C36 | Section 4.4 after Theorem 4.15 ((I+A)^{N-1} form, Bai accessed partially) | qualified
+m1-9 | Section 7.2, item on the mark above A | qualified
+m2-8 | Section 5, note after Definition 5.1 | qualified
+m2-15 | Remark 2.19 (length-0 walks allowed) | qualified
+m3-11 | Sections 1.3 and 7.5 (textbook states neither theorem; independently confirmed by full-text search) | qualified
+
+Mechanical checks: check_citations: 11 keys, 11 bib entries, 11 sources, 0 errors, 0 warnings. check_claims: 70 supported, 7 qualified, 0 unverified, 0 errors. inspect_pdf: 31 pages, 0 errors, 1 warning (F9). I did not run build.sh because it writes build files; main.pdf is present and current. I did not observe release condition 9 (self-evaluation coverage), as instructed.
+
+RECOMMENDATION
+PASS -- There are no critical or major findings, every dimension scores at least 4, every observable release condition holds, and the nine minor findings should be fixed or documented before release.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reports/technician-reader-round1.md b/papers/adjacency-walks-connectivity/reports/technician-reader-round1.md
new file mode 100644
index 0000000..580e0d5
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reports/technician-reader-round1.md
@@ -0,0 +1,78 @@
+FINDINGS
+
+F1 | comprehension | Abstract: "Both theorems are proved in full, because the course textbook does not state them in the pages checked [9]." | The abstract names three questions but then says "both theorems" without saying which two they are. The abstract also uses "walk", "path", "vertex", "off the diagonal" and "(I + A)^(N−1)" with no gloss. "I" is not defined there. | Name the two theorems ("the walk-counting theorem and the connectivity test"). Add a half-sentence defining I as the identity matrix. | 
+
+F2 | comprehension | 1.1: "the board puts a small mark above the letter A... a small n or a pair of quotation marks, not clearly a k [4, 5]." | The reader cannot see the photographs until Appendix C. Sections 1.1 and 1.4 describe the board's drawing in words ("an arrowhead at 2", "an edge 1–3 that the matrix lacks") with no figure. The reader must take these descriptions on faith for 25 pages. | Add a forward pointer ("see Figure 1, Appendix C") at the first mention, or move the figure into Section 1.1.
+
+F3 | comprehension | 1.1 and 1.4: "The assignment text added a third question"; "the assignment states that in the course a path has no repeated vertex." | "The assignment", "the board" and "the course" are never introduced. The reader does not know who wrote the assignment, whether it is available, or why the paper depends on it. The "[4, 5]" citations point to photographs, but the assignment text has no citation at all. | Add one sentence at the start of 1.1 saying what the assignment is and that it is unavailable as a file. Alternatively cite it as a numbered source.
+
+F4 | comprehension | 1.3: "both prove it loosely [7, 1]"; "(derived here)"; "(qualified)"; 1.4 "Kinds of statement". | The labels "derived", "interpretation", "qualified", "estimate" and "open" are defined only in the last paragraph of 1.4. The reader meets "qualified" in 1.1 and the abstract before then. "Qualified" is never defined precisely. It seems to mean "caveated", but this is a guess. | Define "qualified" in one sentence and move the "Kinds of statement" paragraph before first use, or add a forward reference.
+
+F5 | comprehension | 1.2 and 1.4 (Table 1, "Definition 2.18", "Definition 2.31", "Definition 2.13"). | The roles of "plain words" paragraphs versus formal definitions are clear. However, the story fixes "trip" as the word for "walk" and "clean route" for "path", while the paper later says "trail". Trail has no entry in Table 1. The "In plain words" for trail says "Our textbook calls it a path", which clashes with the story's "clean route". | Add "trail" to Table 1 (for example "trip with no repeated road").
+
+F6 | comprehension | 1.4: "The board writes (G, V) for the graph and eij ∈ V in its matrix definition, where its V is the edge set." | This is confusing. The reader has not yet seen what is on the board, and a vertex set V that is secretly the edge set is hard to follow. | Say "the board uses V for the edge set (probably a slip)" and move the details to Appendix C, keeping only the paper's own notation in the main text.
+
+F7 | comprehension | 1.4 and 2.3: "The textbook's Fig. 1.2.5 shows a graph on five vertices... The textbook's own examples force the seven edges..." | The textbook graph is introduced inside a block of walk examples. The reader cannot see the figure and must trust the reconstruction from the edge list. The figure is never reproduced. | Draw the seven-edge textbook graph as a small figure, or list the edges as a labelled example (for example "Example 2.20a") before it is used.
+
+F8 | comprehension | 2.1: "The textbook's own definition of degree was not read, so no textbook number is given." Also Definition 2.13, "The textbook's definition number for this matrix was not recorded." | This is bookkeeping about the author's process, not about the mathematics. It makes the reader wonder whether the definitions were checked. | Drop it from the body and keep it in Appendix B, or state it once in 1.4.
+
+F9 | comprehension | Definition 2.18: "u0, e1, u1, ..., uk−1, ek, uk of vertices and edges with ei = ui−1 ui". | The notation ui−1ui for an edge is explained earlier (Table 2, "uv, eij"), but the symbol "ei" is introduced as an edge and is also the index in "eij" (the board's edge). The two uses of e look alike. | Say "the i-th edge ei joins ui−1 and ui".
+
+F10 | comprehension | Remark 2.19: "The textbook does not say in so many words that k = 0 is allowed. This paper reads k = 0 as allowed, because the textbook's property d(u,u) = 0 of distance needs a path of length 0." | This is a long justification for a small convention. The reader cannot tell why it matters: the length-0 walk is needed only later (Lemma 2.45, Remark 4.2). | Add "needed in Lemma 2.45 and Remark 4.2" to say why the point is raised.
+
+F11 | comprehension | 2.3, Remark 2.28: "In the board graph every trail is also a path... for every length from 0 to 4 ... (derived, checked by script for lengths up to 4)." | The reader is asked to take a claim for lengths 0 to 4 on trust. A short argument is available: the board graph is a path with 3 vertices and no cycle. The text then says the claim is "derived" yet only "checked by script". | Replace with one sentence of reasoning ("the board graph has no cycle, so no trail revisits a vertex"), or label it "checked" only.
+
+F12 | comprehension | 2.4 (Cycles): "Cycles are not needed for the main results; they are given because the textbook's list of definitions includes them." | A full page of definitions, examples and non-examples (Definitions 2.36 and 2.37, Remark 2.38) is not used afterwards. The reader cannot tell whether to retain it. Likewise for Table 3 and the trail material, which is needed only for Remark 4.2. | Mark 2.4 as skippable at its start, or move it to an appendix.
+
+F13 | comprehension | Definition 2.41 and the text after it: "The textbook's 'path' here is its Definition 1.2.12, a trail. The definition does not depend on whether one reads trail or path..." | The reader is told that "the pair (V,d) is a metric space" with no explanation of "metric space". Distance is used later only in Remark 4.20. | Delete the metric-space sentence or gloss it ("d behaves like an ordinary distance").
+
+F14 | comprehension | Lemma 2.45 proof: "Form the sequence W′ = u0, ..., ui, uj+1, ..., uk; if j = k nothing follows ui." | This is the hardest step to follow and I had to read it three times. The index juggling hides the idea of cutting out the loop between ui and uj. The edge case j = k is stated inside a sentence about the sequence. The trace example appears only after the proof. | Add one sentence before the formal construction ("delete everything after the first ui up to and including uj, so the walk goes from ui straight on to uj+1"), or put the trace first.
+
+F15 | comprehension | Definition 3.1: "(XY)ij = Σ_{r=1}^N Xir Yrj" and the following remark that "A^0 = I... corresponds to one walk of length 0". | The pdf text of the formula is garbled in my reading, but the intent is clear. A technician who has not met matrix products will rely on the "plain words". The identity matrix I appears in Table 2 and in the abstract without a display of an example. | Show I once for N = 3. Show one numeric row-times-column product before Theorem 3.5.
+
+F16 | comprehension | Proof of Theorem 3.5: "Wk(i, j) is the sum over r = 1, ..., N of the number of walks of length k from ni to nj whose second-last vertex is nr. Fix r. We claim that the number in class r is Wk−1(i, r) · Arj." | The reader is not told in advance why the sum is organised by the second-last vertex. The proof is correct in form but long. The two bullet cases are clear. The "Why the argument is valid" paragraph then repeats it. | Open the proof with a roadmap sentence ("a walk of length k is a walk of length k−1 plus one final step; that final step is allowed exactly when Arj = 1").
+
+F17 | comprehension | 3.2, end: "A computer check supports the theorem but is not a proof: ... all 40, 360, 5120 and 76800 tested cases of (k, i, j) agreed." | The numbers 40, 360, 5120 and 76800 are not explained. The reader cannot tell how they arise (A.5 says k runs to 4 for N ≤ 4 and to 3 for N = 5, so the count depends on k, N, and the graph count). | Give the formula, for example "graphs × N² pairs × values of k", or drop the counts.
+
+F18 | comprehension | Proposition 3.11: "If ni has at least one neighbour, then (A²)ii = deg(ni) &gt; 0, but no path, and no trail, of length 2 from ni to ni exists." | "The first inequality" in the proof refers to "&gt; 0", but the statement has no inequality symbol sign besides "&gt;". The claim "no trail" is explained only by the edge being used twice, which is fine. The final sentence "Hence (A^k)ij is in general not the number of paths" does not follow from a single diagonal example unless one adds that k = 2 is a specific case. | Say "so the entry (A²)ii counts a walk that is not a path; hence the entries are not path counts".
+
+F19 | comprehension | Definition 4.5 (Connected component): "On the vertex set V write u ∼ v if G has a (u, v)-path. This relation is reflexive, symmetric and transitive, so V splits into classes." | Reflexive, symmetric, transitive and "classes" (equivalence relation) are used without explanation. The claim that the relation has these properties is not shown. | State "equivalence relation" with a one-line gloss and a pointer to why transitivity holds (join two walks).
+
+F20 | comprehension | Definition 4.9 (new notation S) and Remark 4.10. | S is defined as a sum of N−1 powers, but the reader does not see why N−1 is the right stopping point until Section 4.4. The "plain words" tell the reader to stop at "one step short" without a reason. | Add "(the reason is Corollary 2.46)" to the definition.
+
+F21 | comprehension | Proposition 4.14: "(I + A)^m ij &gt; 0 if and only if Sij &gt; 0. Every diagonal entry of (I + A)^m is at least 1." | The purpose of this second form is never stated in the main text: why would one prefer (I + A)^(N−1)? The reason appears only in 7.4 (repeated squaring). Its proof is deferred to Appendix A.4 although it is a half-page argument. | At first mention, add one sentence on motivation ("it can be computed by repeated squaring, Section 7.4").
+
+F22 | comprehension | Proposition 4.13, statement (i): "There is an (ni, nj)-path in G (in the sense of textbook Definition 2.1.1)." | The parenthetical is confusing. Definition 2.1.1 is about "connected", and the text calls the textbook "path" a trail. The reader does not know which meaning of "path" statement (i) uses. | Replace with "a path (Definition 2.31) from ni to nj" and refer to Remark 4.2 for the trail reading.
+
+F23 | comprehension | Proof of Theorem 4.15: "Together with the diagonal entries, which are always positive by Proposition 4.14, this is (c)." | The step from positivity of off-diagonal entries of (I+A)^(N−1) to (b) uses Proposition 4.14 with Sij, and the diagonal remark is easy to miss. Statement (a) also requires u = v pairs, which the proof dismisses by Remark 4.2. The chain is correct but spread over four references. | Add a three-line outline of the proof: (a) iff each pair joined, (b) via Prop 4.13, (c) via Prop 4.14.
+
+F24 | comprehension | Remark 4.21: "For N = 2 and one edge, S = A has zeros on the diagonal although the graph is connected. ... For N = 1 ... S is an empty sum." | This sits in a remark in the middle of the proof area and mixes three cases. The sentence "For N ≥ 3 and a connected graph the diagonal of S is positive anyway" is an unproved claim, said to be unneeded. | Split into short bullets, or cut the N ≥ 3 claim since the test does not need it.
+
+F25 | comprehension | 4.6: "Enough: Proposition 4.13 shows that if a trip between two different vertices exists at all, a trip of length at most N − 1 exists... Not fewer: the next statement shows that N − 1 cannot be lowered." | The heading says "N − 2 are not", but the argument for "not fewer" is a single counterexample family. The text says "the next statement shows" but a "plain words" paragraph sits between. The term "trip" is used while the formal statement uses "walk". | Use "walk" in this paragraph, or state that the claim is shown by Proposition 4.23 for a path graph.
+
+F26 | comprehension | Proposition 4.23 and Example 6.3. | The example prints A + A² as "(N − 2 powers)" with the (1,4) entry 0. The reader must locate the entry in a 4×4 matrix with no highlight. | Mark the (1,4) entry (for example boldface) and say "top-right entry".
+
+F27 | comprehension | 4.7, Remark 4.24: "Its correctness statement in the source is that for every vertex v there is a walk from s to v if and only if v is discovered when the search ends [10]." | BFS, "queue" and "discovered" are used before being defined. The plain-words version helps. The claim "agree on all 32768 labelled graphs with 6 vertices" is taken on faith from a script. | State briefly that the BFS comparison is only a sanity check, with a pointer to Table 5.
+
+F28 | comprehension | 6.1: "Also A³ = 2A and A^(k+2) = 2A^k for k = 1, ..., 5 (script)." | The reader is told this pattern without any reason or relevance to the questions. It does not return afterwards. | Delete it, or say why it matters (it shows that the entries grow).
+
+F29 | comprehension | Table 4 (6.1). | The columns "trails" and "paths" are equal in every row, and the table includes k = 0 with a "closed walks" count of 3 but k = 1 with 0. The reader cannot tell what the table is meant to show. The caption does not say. The reported "walks" for k = 4 (12) is not tied to the matrix entries shown (the sum of A⁴ is 12). | Add one sentence on the point of the table ("walks multiply while paths stop at length 2"). State that the walk column equals the sum of the entries of A^k.
+
+F30 | comprehension | Table 5: "wrong with N − 2 powers" column: 1, 3, 12, 60, 360. | The numbers are not explained. The text covers N = 3 (3 graphs) and N = 4 (12 graphs) only. The reader cannot check the 60 and 360, or see why they are the numbers of labelled graphs on which the shortened test fails. | State the rule (for example, the shortened test errs exactly on graphs of diameter N−1, that is, labelled paths, which number N!/2), or say that no pattern is claimed.
+
+F31 | comprehension | 7.4: "Reaching A^(N−1) from A takes N − 2 products, so the matrix test costs about (N − 2)N³ multiplications: 98,000,000 for N = 100 ... t squarings, 7 for N = 100, costing 7,000,000 multiplications." | "t squarings" and "2^t ≥ N − 1" are given without a derivation (log2 99 is about 6.6, so 7). The "BFS reads each row once... N² = 10,000" claim is derived with no argument. The conclusion "useful because its answer is a clean statement ..., not because it is fast" is an opinion. | Show the arithmetic in one line, or say these are illustrative estimates.
+
+F32 | comprehension | 7.3: "As written, Theorem 1 is false for any definition of path that forbids repeated vertices or repeated edges... so their explanation is wrong although their statements of the test are correct." | The reader is told that published sources are wrong. The only evidence given is Proposition 3.11, and the sources are not quoted. The reader has to take the claim about [7] and [1] on faith. | Quote the sentence from [7] in the body, or soften to "as we read it".
+
+F33 | comprehension | Sections 1.3, 7.1, 7.5: repeated statements ("the rest of the book was not read page by page", "qualified") at three places, plus Appendix B. | The same caveat is repeated at least four times, which hides the main results. The reader needs it once, in 1.4. | State it once in 1.4 and refer to it.
+
+F34 | comprehension | Section 7.5, "Open: whether the lecturer's intended answer to the board's question 2 was the sum test, the (I+A)^(N−1) test, or BFS... Only the user can settle these." | "The user" is not a reader of a paper. The sentence addresses the person who gave the task, so the paper's frame (study note versus a reply to a request) is unclear. | Replace "Only the user can settle these" with "These can be settled only by the lecturer".
+
+F35 | comprehension | Appendix D: "The scripts are copies of the ones in the folder modules/, which are kept as the module records." | The reader has no access to "modules/" or "figures/generated_numbers.tex" and cannot tell whether the scripts are shipped with the paper. The text also names script names (m1_walks.py and so on) throughout the body. | State where the scripts can be obtained, or remove the internal folder names from the paper.
+
+F36 | comprehension | Section 5 (Q3), whole section. | Section 5 repeats Definition 2.31 almost word for word. After the long treatment in Section 2, I could not say what Section 5 adds beyond the endpoint notation and the claim that both readings of "path" agree. | Fold Section 5 into Section 2.3, or state at its head that it only restates Definition 2.31 for the question Q3.
+
+F37 | comprehension | Whole paper, structure. | The paper is 31 pages for three short questions. The answers appear in the abstract and Section 1.3, but the main chain of reasoning (walk counting, then walk-to-path, then the test) is spread over Sections 2 to 4, with side topics (cycles, metric space, naming conventions, BFS, cost) in between. The reader cannot easily tell what is essential and what is context. | Add a "reading path" line in 1.5 listing the sections needed for the proofs (2.3, 2.7, 3.1-3.2, 4.1-4.4) and the optional ones.
+
+READER SUMMARY
+The paper starts from a lecture-board photograph that shows a small graph and its table of zeros and ones (the adjacency matrix A). It asks three things. First, what does entry (i,j) of the k-th power of A mean? Second, how can one tell from A alone whether the graph is connected? Third, what is a "path" between two vertices? Its answers are as follows. Entry (i,j) of A^k counts the walks of length k from vertex i to vertex j. A walk may revisit vertices and reuse edges, so the entry does not count paths. It is proved by induction on k, by sorting walks by their second-last vertex. A graph with at least two vertices is connected exactly when every off-diagonal entry of A + A² + … + A^(N−1) is positive. The same holds when (I + A)^(N−1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path, and that a path on N vertices has at most N−1 edges. So longer walks add nothing, and stopping at N−2 can fail, as the four-house row shows. A path is defined as a walk with no repeated vertex. The paper notes that its textbook calls this a "simple path" and uses "path" for a walk with no repeated edge (which the paper calls a "trail"). It also notes that the board's drawing and matrix disagree, and that the mark above A on the board is read as an exponent k. The results are checked by script against breadth-first search on all graphs with up to six vertices. The paper says the matrix test is neat but not fast, compared with breadth-first search. I can state this, but I cannot say why the study note needed 31 pages, or which parts the main argument needs and which are context.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/answer1_walks.tex b/papers/adjacency-walks-connectivity/sections/answer1_walks.tex
new file mode 100644
index 0000000..2e8a39d
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/answer1_walks.tex
@@ -0,0 +1,194 @@
+\section{Q1: what the entry of a power of $A$ counts}\label{sec:walks}
+
+\subsection{Matrix products and powers}
+
+\begin{plainwords}
+To multiply two tables of the same size, take a row of the first and a column of the second.
+Multiply them place by place, then add.
+That gives one number of the new table.
+To raise a table to a power, multiply it by itself again and again.
+\end{plainwords}
+
+\begin{definition}[Matrix product and power]\label{def:product}
+The \emph{product} of two $N\times N$ matrices $X$ and $Y$ is the matrix $XY$ with $(XY)_{ij}=\sum_{r=1}^{N}X_{ir}Y_{rj}$.
+The powers of $A$ are $A^1=A$ and $A^k=A^{k-1}A$ for $k\ge2$.
+\end{definition}
+
+The exponent $0$ is not used for $A$ in this section; by the usual convention $A^0=I$, the identity matrix, which corresponds to one walk of length $0$ from a vertex to itself \cite{grinberg2025graph}.
+It appears only in \cref{sec:conn}, in $(I+A)^{N-1}$.
+
+\begin{remark}
+The definition allows a sum over all $N$ vertices $r$, whether or not $r$ is a neighbour.
+It forbids multiplying entry by entry: the product is not the table of products of matching entries.
+\end{remark}
+
+\begin{example}
+For the board matrix $A=\matA$ the entry $(A^2)_{11}=A_{11}A_{11}+A_{12}A_{21}+A_{13}A_{31}=0\cdot0+1\cdot1+0\cdot0=1$ (script).
+\end{example}
+
+\begin{nonexample}
+Squaring every entry of $A$ separately gives back $A$, since the entries are $0$ and $1$.
+That is not $A^2$: the matrix product has $(A^2)_{22}=1\cdot1+0\cdot0+1\cdot1=2$ (script), where entry-wise squaring gives $A_{22}^2=0$.
+\end{nonexample}
+
+\subsection{The walk-counting theorem}
+
+\begin{plainwords}
+Take the table of roads and multiply it by itself.
+Each number in the new table counts trips of two roads.
+The trips run from the row house to the column house.
+Multiply again, and you count trips of three roads.
+The count includes trips that turn back.
+So the table counts trips, not clean routes.
+\end{plainwords}
+
+\begin{theorem}[Walk counting]\label{thm:walks}
+Let $A$ be the adjacency matrix of a simple undirected graph with vertices $n_1,\dots,n_N$ and let $k\ge1$ be a whole number.
+Then $(A^k)_{ij}$ is the number of walks of length $k$ from $n_i$ to $n_j$, for all $i,j$.
+\end{theorem}
+
+The theorem is a standard one.
+It is stated and proved for simple undirected graphs in lecture notes \cite[Theorem 1.1.3]{quinlan_matrices_graphs}, and for digraphs and multidigraphs, of which the simple undirected graph is the symmetric case, in two other texts \cite[Theorem 4.5.10]{grinberg2025graph}, \cite[Corollary 9.3.3]{lehman_mcs_adjacency}; a fourth set of notes states it too \cite[Theorem 1]{bai2025adjacency}.
+The course textbook does not state it in the pages checked, so it is proved here (qualified, as said in \cref{sec:intro}).
+The proof below follows the route that the standard notes use: induction on $k$, sorting the walks by their second-last vertex \cite{quinlan_matrices_graphs,grinberg2025graph}.
+
+\begin{remark}
+The theorem allows $i=j$ (closed walks), and it counts every walk once, with repeats of vertices and edges permitted.
+It forbids reading the number as a count of paths (\cref{prop:warning}).
+\end{remark}
+
+\begin{example}
+For the board graph, $(A^2)_{13}=1$, the walk $1,2,3$ (\cref{sec:examples}).
+\end{example}
+
+\begin{nonexample}
+$(A^2)_{12}=0$ in the board graph.
+This does not say that $n_1$ and $n_2$ are unconnected.
+It says that no walk of length exactly $2$ joins them; walks of length $1$ and $3$ do exist.
+\end{nonexample}
+
+\begin{proof}[Proof (derived; induction on $k$)]
+Write $W_k(i,j)$ for the number of walks of length $k$ from $n_i$ to $n_j$.
+We prove $W_k(i,j)=(A^k)_{ij}$ for all $i,j$, for each $k\ge1$.
+By \cref{rem:vertexlist} we count sequences of vertices.
+
+\emph{Base case, $k=1$.}
+A walk of length $1$ from $n_i$ to $n_j$ is a sequence $(n_i,n_j)$ with $n_i,n_j$ adjacent.
+There is exactly one such sequence if $n_i$ and $n_j$ are adjacent, and none otherwise.
+So $W_1(i,j)=A_{ij}=(A^1)_{ij}$.
+
+\emph{Induction hypothesis.}
+Let $k\ge2$ and suppose $W_{k-1}(i,j)=(A^{k-1})_{ij}$ for all $i,j$.
+
+\emph{Inductive step.}
+Fix $i$ and $j$.
+Every walk $(w_0,\dots,w_k)$ of length $k$ from $n_i$ to $n_j$ has a second-last vertex $w_{k-1}$.
+Because $k\ge2$, deleting the last vertex leaves $w_0,\dots,w_{k-1}$, a sequence with consecutive vertices adjacent and length $k-1\ge1$, so the induction hypothesis speaks about walks of that length.
+Let $w_{k-1}=n_r$, where $r$ is one of $1,\dots,N$.
+Sort the walks into $N$ classes by the value of $r$.
+The classes are disjoint, because each walk has exactly one second-last vertex, and together they contain every walk.
+So $W_k(i,j)$ is the sum over $r=1,\dots,N$ of the number of walks of length $k$ from $n_i$ to $n_j$ whose second-last vertex is $n_r$.
+
+Fix $r$.
+We claim that the number in class $r$ is $W_{k-1}(i,r)\cdot A_{rj}$.
+\begin{itemize}
+\item If $n_r$ and $n_j$ are not adjacent ($A_{rj}=0$), no walk can have $n_r$ followed by $n_j$, so class $r$ is empty and the count is $0=W_{k-1}(i,r)\cdot0$.
+\item If $n_r$ and $n_j$ are adjacent ($A_{rj}=1$), delete the last vertex of a walk in class $r$.
+What remains is a sequence $w_0,\dots,w_{k-1}$ with $w_0=n_i$, $w_{k-1}=n_r$ and consecutive vertices adjacent, that is, a walk of length $k-1$ from $n_i$ to $n_r$.
+Conversely, any walk of length $k-1$ from $n_i$ to $n_r$, followed by $n_j$, is a sequence of $k+1$ vertices whose consecutive pairs are adjacent, because the new pair $n_r,n_j$ is adjacent.
+So it is a walk of length $k$ from $n_i$ to $n_j$ with second-last vertex $n_r$.
+Deleting and appending undo each other, so they match the walks of class $r$ one to one with the walks of length $k-1$ from $n_i$ to $n_r$, and the count is $W_{k-1}(i,r)=W_{k-1}(i,r)\cdot1$.
+\end{itemize}
+
+Therefore $W_k(i,j)=\sum_{r=1}^{N}W_{k-1}(i,r)A_{rj}$.
+By the induction hypothesis $W_{k-1}(i,r)=(A^{k-1})_{ir}$, so $W_k(i,j)=\sum_{r}(A^{k-1})_{ir}A_{rj}$, which is the $(i,j)$ entry of $A^{k-1}A=A^k$ by \cref{def:product}.
+This proves the statement for $k$, and by induction for all $k\ge1$.
+\end{proof}
+
+\emph{Why the argument is valid.}
+Two facts are the only places where the counting could go wrong: the sum over the second-last vertex covers each walk exactly once, and the matching in the case $A_{rj}=1$ is one to one.
+Simplicity is used twice: to identify a walk with its vertex sequence (\cref{rem:vertexlist}), and so that $A_{rj}$, the number of edges between $n_r$ and $n_j$, is $0$ or $1$.
+Undirectedness is not used in the induction; it only gives the symmetry of $A$ (interpretation; the versions for digraphs in the cited texts agree \cite{grinberg2025graph,lehman_mcs_adjacency}).
+For a graph with repeated edges the same proof counts walks with multiplicity if $A_{rj}$ is the number of edges, but then the properties of \cref{prop:rowsums} change (interpretation).
+A computer check supports the theorem but is not a proof: for all labelled simple graphs on $N=2,3,4,5$ vertices ($2$, $8$, $64$, $1024$ graphs) a brute-force enumeration of walks agreed with the matrix entries in all $40$, $360$, $5120$ and $76800$ tested cases of $(k,i,j)$ (\cref{app:crosschecks}).
+
+\subsection{Consequences}
+
+\begin{plainwords}
+A count is never negative, and it is always a whole number.
+A positive count means that at least one such trip exists.
+Reverse a trip and you get a trip back.
+So the table of trip counts also looks the same when flipped over its diagonal.
+\end{plainwords}
+
+\begin{corollary}\label{cor:counts}
+For a simple undirected graph and $k\ge1$:
+(a) every entry of $A^k$ is a non-negative whole number, so a sum of powers of $A$ has a positive $(i,j)$ entry if and only if some summand does;
+(b) $(A^k)_{ij}>0$ if and only if there is a walk of length exactly $k$ from $n_i$ to $n_j$;
+(c) $A^k$ is symmetric.
+\end{corollary}
+
+\begin{proof}
+Parts (a) and (b) hold because by \cref{thm:walks} the entry is a count.
+For (c), $(A^k)^{T}=(A^{T})^{k}=A^{k}$ because $A$ is symmetric.
+Alternatively, reversing the sequence of a walk matches the walks from $n_i$ to $n_j$ with the walks from $n_j$ to $n_i$.
+\end{proof}
+
+\begin{plainwords}
+Take the trips of two roads that start and end at the same house.
+Each one goes out along a road and comes straight back.
+So there is one such trip for each neighbour.
+That is the number of roads at the house.
+\end{plainwords}
+
+\begin{proposition}[Diagonal of $A^2$]\label{prop:diag}
+$(A^2)_{ii}=\deg(n_i)$ for every $i$.
+Hence the sum of the diagonal entries of $A^2$ is $2|E|$.
+\end{proposition}
+
+The first statement is made in lecture notes \cite{quinlan_matrices_graphs}; the proof below and the second statement are derived here.
+
+\begin{proof}
+By \cref{thm:walks}, $(A^2)_{ii}$ counts the walks $n_i,n_r,n_i$ of length $2$ from $n_i$ to $n_i$.
+Such a walk exists exactly when $n_r$ is a neighbour of $n_i$, so there is one for each neighbour, and the number of neighbours is $\deg(n_i)$ (\cref{def:degree}).
+Summing over $i$ and using \cref{prop:rowsums}, item 5, gives $2|E|$.
+\end{proof}
+
+For the board graph the diagonal of $A^2$ is $(1,2,1)$, the degrees, and the sum $4$ equals $2|E|$ (script).
+
+\subsection{Walks are not paths}\label{sec:warning}
+
+\begin{plainwords}
+A trip may turn back and visit the same house twice.
+A clean route never visits a house twice.
+The table counts trips, so it counts turn-back trips too.
+A house with at least one neighbour always has a two-road trip that goes out and comes back.
+So the table does not count clean routes.
+\end{plainwords}
+
+\begin{proposition}[Walks are not paths]\label{prop:warning}
+If $n_i$ has at least one neighbour, then $(A^2)_{ii}=\deg(n_i)>0$, but no path, and no trail, of length $2$ from $n_i$ to $n_i$ exists.
+Hence $(A^k)_{ij}$ is in general not the number of paths, or of trails, of length $k$ from $n_i$ to $n_j$.
+\end{proposition}
+
+\begin{proof}
+The first inequality is \cref{prop:diag}.
+A path from $n_i$ to $n_i$ has its first and last vertices equal, so it can only be the single vertex, of length $0$.
+A closed walk of length $2$ has the form $n_i,n_r,n_i$ and uses the edge $n_in_r$ twice, so it is not a trail.
+\end{proof}
+
+The warning holds under both of the textbook's readings of ``path'': distinct vertices (Definition 1.2.13) and distinct edges (Definition 1.2.12) \cite[p.~22]{petrosyan2015grafneri}.
+The general fact that the theorem counts walks and not paths is also made in the notes cited above \cite{bai2025adjacency,grinberg2025graph}.
+
+For the board graph this is concrete: $(A^2)_{11}=1>0$, and the one walk is $1,2,1$, which repeats the vertex $n_1$ and the edge $n_1n_2$.
+Also $(A^3)_{12}=2$, the walks $1,2,1,2$ and $1,2,3,2$, and neither is a path or a trail, yet the only path from $n_1$ to $n_2$ has length $1$.
+The enumeration for $k=1,\dots,5$ finds $1,0,2,0,4$ walks from $n_1$ to $n_2$, of which $1,0,0,0,0$ are paths (script, \cref{app:counterexample}).
+So the entries grow with $k$ while the number of paths does not.
+
+What a positive entry does guarantee is a walk of length $k$, and \cref{lem:walkpath} then gives a path of length at most $k$ (derived).
+This is the fact that \cref{sec:conn} uses.
+
+\subsection{The answer to Q1}
+
+For a simple undirected graph with adjacency matrix $A$ and any whole number $k\ge1$, the entry in row $i$ and column $j$ of $A^k$ is the number of walks of length $k$ from $n_i$ to $n_j$.
+Walks may repeat vertices and edges, so the entry is not a count of paths.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex b/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex
new file mode 100644
index 0000000..41effd6
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex
@@ -0,0 +1,303 @@
+\section{Q2: deciding connectivity from the matrix}\label{sec:conn}
+
+\subsection{Connected graphs}
+
+\begin{plainwords}
+Look at a village.
+Sometimes you can reach every house from every other house.
+You may pass the same house twice on the way.
+Then the village is called connected.
+If one house is cut off, the village is not connected.
+\end{plainwords}
+
+\begin{definition}[Connected graph; textbook Definition 2.1.1]\label{def:connected}
+A graph $G=(V,E)$ is \emph{connected} if for any two vertices $u$ and $v$ of $G$ there is a $(u,v)$-path in $G$ \cite[p.~48]{petrosyan2015grafneri}.
+\end{definition}
+
+The board states the same definition: a graph is called connected if for any $n_i,n_j$ there exists a path between the nodes \cite{whiteboard1,whiteboard2}.
+
+\begin{remark}\label{rem:connected}
+\begin{enumerate}
+\item In the textbook the word ``path'' here is Definition 1.2.12, a trail.
+The board does not say which meaning it uses, and the course convention is ``no repeated vertex''.
+The definition does not depend on the choice: a walk between two different vertices contains a path with distinct vertices (\cref{lem:walkpath}), and a path has distinct edges (\cref{prop:pathtrail}), so both readings accept exactly the same graphs (derived; compare the cited lemma in other notes \cite{grinberg2025graph}).
+\item ``Any two vertices'' includes $u=v$.
+For $u=v$ the walk with one vertex and no edges is a $(u,u)$-path, so these pairs are always satisfied, and reading the definition as ``any two different vertices'' changes nothing (interpretation; the textbook does not discuss $u=v$).
+\item The definition forbids exactly one thing: a pair of vertices with no trip between them.
+\end{enumerate}
+\end{remark}
+
+\begin{example}\label{ex:connected}
+The board graph is connected.
+The pair $n_1,n_3$ is joined by the path $1,2,3$, and the pairs $n_1,n_2$ and $n_2,n_3$ are joined by one edge.
+The textbook's own examples of connected graphs are the complete graphs, the complete bipartite graphs, and the three graphs of its Fig.~2.1.1 \cite[p.~48]{petrosyan2015grafneri}.
+\end{example}
+
+\begin{nonexample}\label{nex:connected}
+Three vertices $n_1,n_2,n_3$ with only the edge $n_1n_2$.
+No walk leaves $n_3$, so the pair $n_1,n_3$ has no path.
+The textbook's Fig.~2.1.2 shows a graph that is not connected and has four components \cite[p.~49]{petrosyan2015grafneri}.
+\end{nonexample}
+
+\subsection{Components}
+
+\begin{plainwords}
+Look at a village that is not connected.
+It falls into pieces.
+Inside one piece every house can reach every other house.
+No road joins two different pieces.
+Each piece is called a component.
+A connected village has exactly one piece.
+\end{plainwords}
+
+\begin{definition}[Connected component; textbook, printed p.~49, no number]\label{def:component}
+On the vertex set $V$ write $u\sim v$ if $G$ has a $(u,v)$-path.
+This relation is reflexive, symmetric and transitive, so $V$ splits into classes $V_1,\dots,V_p$.
+The subgraphs $G_j=G[V_j]$ that these classes induce are the \emph{connected components} of $G$ \cite[p.~49]{petrosyan2015grafneri}.
+\end{definition}
+
+The textbook gives this in a paragraph after Definition 2.1.1 without a number; the notation $G[V_j]$ means the graph on $V_j$ with all the edges of $G$ that join two vertices of $V_j$.
+Another text defines a connected graph as one with exactly one component, and shows that being joined by a walk and being joined by a path are the same relation \cite[Definition 2.9.12, Proposition 2.9.10]{grinberg2025graph}.
+
+\begin{remark}\label{rem:component}
+A component cannot be enlarged: a vertex reachable from a vertex of $V_j$ lies in $V_j$.
+The textbook's Remark 2.1.1 says that $G$ is connected if and only if it has exactly one component \cite[p.~49]{petrosyan2015grafneri}.
+\end{remark}
+
+\begin{example}
+The graph with only the edge $n_1n_2$ has the two components $G[\{n_1,n_2\}]$ and $G[\{n_3\}]$.
+The board graph has the single component $G[\{n_1,n_2,n_3\}]$ (derived; \cref{sec:examples}).
+\end{example}
+
+\begin{nonexample}
+$G[\{n_1\}]$ is not a component of the graph with the edge $n_1n_2$ only, although it is a connected graph: $n_2$ can be reached from $n_1$, so it belongs to the same class.
+A component is a whole class, not any connected piece.
+\end{nonexample}
+
+\subsection{The sum used by the test}
+
+\begin{plainwords}
+We need a name for a running total.
+It adds the counts of trips with one road, with two roads, and so on.
+We stop one step short of the number of houses.
+The whole check uses this one total.
+\end{plainwords}
+
+\begin{definition}[The sum $S$; new notation, not from the textbook]\label{def:S}
+For a graph with $N\ge2$ vertices let $S=A+A^2+\dots+A^{N-1}$, the sum of the first $N-1$ powers of $A$, added entry by entry.
+\end{definition}
+
+\begin{remark}\label{rem:S}
+By \cref{thm:walks}, $S_{ij}$ is the number of walks from $n_i$ to $n_j$ whose length is between $1$ and $N-1$.
+Hence every entry of $S$ is a non-negative whole number (derived).
+The diagonal of $S$ counts closed walks and plays no role in the test (\cref{rem:edge}).
+\end{remark}
+
+\begin{example}
+For the board graph $S=A+A^2=\matSB$ (script; \cref{sec:examples}).
+\end{example}
+
+\begin{nonexample}
+$A^2$ alone is not $S$ for $N=3$, where $S=A+A^2$.
+Either one alone gives a wrong answer for the board graph: $A^2$ has the zero entry $(1,2)$ although $n_1$ and $n_2$ are joined by an edge, and $A$ has the zero entry $(1,3)$ although $n_1$ and $n_3$ are connected (script).
+\end{nonexample}
+
+\subsection{The test and its proof}
+
+\begin{plainwords}
+We want a quick check for a village.
+We only have the table that says which houses share a road.
+From the table we can count trips.
+Count the trips with one road, with two roads, and so on.
+Add the counts for each pair of houses.
+If no pair of different houses has a total of zero, the village is connected.
+We never need trips longer than one road fewer than the number of houses.
+A trip that wastes time can always be shortened.
+So longer trips tell us nothing new.
+A second form lets every house also stay put for one step.
+It gives the same answer.
+\end{plainwords}
+
+\begin{proposition}[One pair at a time]\label{prop:pair}
+Let $G$ have $N\ge2$ vertices and let $i\ne j$.
+The following three statements are equivalent.
+\begin{enumerate}
+\item[(i)] There is an $(n_i,n_j)$-path in $G$ (in the sense of textbook Definition 2.1.1).
+\item[(ii)] There is a whole number $k$ with $1\le k\le N-1$ and $(A^k)_{ij}>0$.
+\item[(iii)] $S_{ij}>0$.
+\end{enumerate}
+\end{proposition}
+
+\begin{proposition}[The $I+A$ form]\label{prop:iplusa}
+Let $G$ have $N\ge2$ vertices, let $m\ge N-1$ be a whole number, and let $i\ne j$.
+Then $\big((I+A)^m\big)_{ij}>0$ if and only if $S_{ij}>0$.
+Every diagonal entry of $(I+A)^m$ is at least $1$.
+\end{proposition}
+
+\begin{theorem}[The connectivity test]\label{thm:test}
+Let $G$ be a graph with $N\ge2$ vertices and adjacency matrix $A$.
+The following are equivalent.
+\begin{enumerate}
+\item[(a)] $G$ is connected.
+\item[(b)] Every off-diagonal entry of $S=A+A^2+\dots+A^{N-1}$ is positive.
+\item[(c)] Every entry of $(I+A)^{N-1}$ is positive.
+\end{enumerate}
+\end{theorem}
+
+The sum form is stated in a published note and in an encyclopedia entry \cite{paramadevan2021adjacency,weisstein_connectedgraph}, and the second form is stated in lecture notes \cite{bai2025adjacency}.
+The encyclopedia entry gives no proof \cite{weisstein_connectedgraph}.
+The note applies a walk-counting statement that says ``paths'' where walks are meant, and passes from a positive entry to a path without the walk-to-path lemma \cite{paramadevan2021adjacency}.
+The lecture notes have only a sketch that again says ``paths'' \cite{bai2025adjacency}.
+The statements of the test are correct.
+So the proofs here are the paper's own (derived), built on \cref{thm:walks} and \cref{lem:walkpath}.
+The chain of premises is listed in \cref{app:testproof}.
+
+\begin{remark}
+The test allows any graph with at least two vertices, connected or not.
+It forbids using only one power, or stopping before the power $N-1$ (\cref{prop:sharp}), or reading the diagonal of $S$ (\cref{rem:edge}).
+\end{remark}
+
+\begin{example}
+For the board graph the matrix $S=\matSB$ has no zero entry, so by \cref{thm:test}(b) the graph is connected (\cref{sec:examples}).
+\end{example}
+
+\begin{nonexample}
+For the graph with only the edge $n_1n_2$, $S=\matSD$ has zeros off the diagonal, so the graph is not connected (\cref{sec:examples}).
+\end{nonexample}
+
+\begin{proof}[Proof of \cref{prop:pair}]
+\emph{(i) implies (ii).}
+A path is a walk, so there is a walk from $n_i$ to $n_j$.
+By \cref{lem:walkpath} there is a path $P$ from $n_i$ to $n_j$ whose length $k$ is at most the length of that walk.
+$P$ has $k$ edges and therefore $k+1$ distinct vertices, and the graph has only $N$ vertices, so $k\le N-1$ (\cref{cor:bound}).
+If $k$ were $0$, $P$ would start and end at the same vertex, but $n_i\ne n_j$, so $k\ge1$.
+$P$ is a walk of length $k$ from $n_i$ to $n_j$, so by \cref{thm:walks} the number $(A^k)_{ij}$ is at least $1$.
+
+\emph{(ii) implies (iii).}
+$S_{ij}=A_{ij}+(A^2)_{ij}+\dots+(A^{N-1})_{ij}$.
+Each term is a count, hence a non-negative whole number (\cref{cor:counts}).
+A sum of non-negative numbers is at least as large as any one of its terms, and the term with the index $k$ from (ii) is positive, so $S_{ij}>0$.
+
+\emph{(iii) implies (ii).}
+If $S_{ij}>0$, a sum of non-negative terms is positive, so at least one term $(A^k)_{ij}$ with $1\le k\le N-1$ is positive.
+
+\emph{(ii) implies (i).}
+If $(A^k)_{ij}>0$ with $k\ge1$, then by \cref{thm:walks} there is at least one walk of length $k$ from $n_i$ to $n_j$.
+As $n_i\ne n_j$, \cref{lem:walkpath} gives a path from $n_i$ to $n_j$ with distinct vertices.
+By \cref{prop:pathtrail} it also has distinct edges, so it is a $(n_i,n_j)$-path in either reading of the word ``path'' (\cref{rem:connected}).
+\end{proof}
+
+\begin{proof}[Proof of \cref{prop:iplusa}]
+The proof expands $(I+A)^m$ with the binomial formula and is given in \cref{app:iplusa}.
+\end{proof}
+
+\begin{proof}[Proof of \cref{thm:test}]
+Statement (a) says that for every pair of vertices there is a path between them.
+For a pair with $u=v$ this is always true (\cref{rem:connected}).
+For pairs with $i\ne j$ it is statement (i) of \cref{prop:pair}.
+So (a) holds if and only if (i) holds for every $i\ne j$.
+By \cref{prop:pair} this is equivalent to (iii) for every $i\ne j$, which is (b).
+By \cref{prop:iplusa} with $m=N-1$ it is also equivalent to the positivity of every off-diagonal entry of $(I+A)^{N-1}$.
+Together with the diagonal entries, which are always positive by \cref{prop:iplusa}, this is (c).
+\end{proof}
+
+\begin{corollary}[Components from $S$]\label{cor:components}
+For any graph, connected or not, with $N\ge2$ vertices and $i\ne j$: $S_{ij}>0$ if and only if $n_i$ and $n_j$ lie in the same component.
+\end{corollary}
+
+\begin{proof}
+\Cref{prop:pair} uses connectivity only through the pair $(n_i,n_j)$: statement (i) says that $n_i\sim n_j$, which is the definition of ``same class'' in \cref{def:component}.
+\end{proof}
+
+\begin{remark}[Distance]\label{rem:distmatrix}
+A shortest walk between two different vertices is a path, by \cref{lem:walkpath} and \cref{prop:shortest}.
+So the smallest $k$ with $(A^k)_{ij}>0$ is the distance $d(n_i,n_j)$ of \cref{def:distance} (derived); this is also stated in two other sources \cite{lehman_mcs_adjacency,paramadevan2021adjacency}.
+\end{remark}
+
+\begin{remark}[The diagonal, and $N=1$, $N=2$]\label{rem:edge}
+For $N=2$ and one edge, $S=A$ has zeros on the diagonal although the graph is connected (script).
+So the diagonal of $S$ cannot be required to be positive.
+For $N\ge3$ and a connected graph the diagonal of $S$ is positive anyway, because every vertex has a neighbour and $(A^2)_{ii}=\deg(n_i)$ (\cref{prop:diag}), but the test does not need this.
+For $N=1$ there are no pairs of different vertices, the graph is connected, and both forms of the test give the right answer, but $S$ is an empty sum, so the test is stated for $N\ge2$ (derived).
+\end{remark}
+
+\subsection{The test as a procedure}
+
+\begin{plainwords}
+Here is the check, step by step.
+First write the table of the village.
+Then multiply the table by itself again and again.
+After each step, add the new counts to a running total.
+Stop after one step fewer than the number of houses.
+Look at every pair of different houses.
+If any total is zero, those two houses cannot reach each other.
+If no total is zero, everyone can reach everyone.
+\end{plainwords}
+
+\begin{test}[Matrix test]\label{test:matrix}
+\emph{Input:} the adjacency matrix $A$ of a graph with $N\ge2$ vertices.
+\begin{enumerate}
+\item Set $P=A$ and $S=A$.
+\item For $k=2,3,\dots,N-1$: replace $P$ by the product $PA$ (now $P=A^k$) and add $P$ to $S$.
+\item Look at the entries $S_{ij}$ with $i\ne j$. If one of them is $0$, the graph is not connected. If none is $0$, the graph is connected.
+\end{enumerate}
+An equivalent form computes $(I+A)^{N-1}$ and reports ``connected'' if no entry is $0$.
[... truncated by build_evidence.py: 59 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/answer3_path.tex b/papers/adjacency-walks-connectivity/sections/answer3_path.tex
new file mode 100644
index 0000000..ec59afa
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/answer3_path.tex
@@ -0,0 +1,48 @@
+\section{Q3: the definition of a path between $n_i$ and $n_j$}\label{sec:pathdef}
+
+\begin{plainwords}
+Pick two houses of the village.
+A path between them is a clean route.
+It starts at the first house and ends at the second.
+It never visits any house twice.
+If the two houses are the same house, the route is just staying home.
+\end{plainwords}
+
+\begin{definition}[Path between $n_i$ and $n_j$; course convention]\label{def:pathbetween}
+Let $n_i$ and $n_j$ be vertices of $G$.
+A \emph{path between $n_i$ and $n_j$} is a walk $w_0,w_1,\dots,w_k$ with $w_0=n_i$ and $w_k=n_j$ in which the vertices $w_0,\dots,w_k$ are pairwise distinct.
+Its length is $k$.
+For $i=j$ the only such path is the single vertex $n_i$, of length $0$.
+\end{definition}
+
+This is a simple path in the sense of textbook Definition 1.2.13 and a path in English usage \cite[p.~22]{petrosyan2015grafneri}.
+It is the specialization of \cref{def:path} to the endpoints $n_i$ and $n_j$.
+The statement that the course uses ``path'' in this sense comes from the assignment text; the board does not say which meaning it uses \cite{whiteboard1,whiteboard2}.
+The definition is therefore an interpretation, and it is qualified.
+
+\begin{remark}
+The definition allows length $0$ (when $i=j$), length $1$ (an edge), and at most $N-1$ edges (\cref{cor:bound}).
+It forbids any repeated vertex, and therefore any repeated edge (\cref{prop:pathtrail}).
+It does not forbid several different paths between the same two vertices; it says only what a path is.
+\end{remark}
+
+\begin{example}
+In the board graph there is exactly one path between $n_1$ and $n_3$, namely $1,2,3$.
+Every path has at most $N-1=2$ edges, so the enumeration of walks up to length $4$ finds all of them (script).
+Between $n_1$ and $n_1$ the only path is the one of length $0$.
+\end{example}
+
+\begin{nonexample}
+In the board graph $1,2,1,2,3$ is a walk between $n_1$ and $n_3$ but not a path between them: it repeats the vertices $1$ and $2$.
+It is not a trail either, because it repeats the edge $n_1n_2$.
+\end{nonexample}
+
+\paragraph{The two textbook readings give the same answers.}
+If ``path'' is read as the textbook's Definition 1.2.12 (a trail), then ``there is a path between $n_i$ and $n_j$'' has the same truth value as in \cref{def:pathbetween}.
+A path is a trail (\cref{prop:pathtrail}), so a path gives a trail.
+A trail is a walk, and a walk contains a path (\cref{lem:walkpath}), so a trail gives a path.
+Hence every sentence of the form ``there is a path between $n_i$ and $n_j$'', in particular the definition of connected, has the same meaning in both readings (derived).
+What changes with the reading is a \emph{count}: the number of trails between two vertices is not the number of paths, and neither is the number of walks (\cref{prop:warning}).
+
+\paragraph{The answer to Q3.}
+A path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ in which all vertices are pairwise distinct.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/background.tex b/papers/adjacency-walks-connectivity/sections/background.tex
new file mode 100644
index 0000000..efb785b
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/background.tex
@@ -0,0 +1,503 @@
+\section{Background: graphs, walks, and paths}\label{sec:background}
+
+Throughout, let $G=(V,E)$ be a finite simple undirected graph with $V=\{n_1,\dots,n_N\}$, let $u,v$ be vertices and let $e,e'$ be edges, as fixed in \cref{tab:notation}.
+The definitions follow the textbook's build order \cite{petrosyan2015grafneri}.
+Where the textbook has a number for a definition, the number is quoted as ``textbook Definition~$x.y.z$''.
+After each definition come a remark on what it allows and forbids, an example, and a non-example.
+
+\subsection{Graphs, adjacency, and degree}
+
+\begin{plainwords}
+A village has a list of houses and a list of roads.
+A road always joins two different houses.
+No two roads join the same pair of houses.
+Roads have no direction.
+The village is small enough that we can count its houses.
+\end{plainwords}
+
+\begin{definition}[Simple undirected graph; textbook Definition 1.1.1]\label{def:graph}
+A \emph{simple undirected graph} is a pair $G=(V,E)$ where $V$ is a finite nonempty set, whose elements are the \emph{vertices}, and $E$ is a set of unordered pairs of distinct elements of $V$, the \emph{edges} \cite[p.~9]{petrosyan2015grafneri}.
+\end{definition}
+
+\begin{remark}\label{rem:graph}
+The definition forbids a loop, because an edge is a pair of distinct vertices.
+It forbids a repeated edge, because $E$ is a set, so a pair occurs at most once.
+It forbids direction, because the pair is unordered, so $n_in_j$ and $n_jn_i$ are the same edge.
+It allows a vertex that lies on no edge, and any finite number of vertices.
+\end{remark}
+
+\begin{example}\label{ex:boardgraph}
+$V=\{n_1,n_2,n_3\}$ and $E=\{n_1n_2,\,n_2n_3\}$.
+This is the board graph: three houses in a row.
+\end{example}
+
+\begin{nonexample}\label{nex:graph}
+Two vertices $n_1,n_2$ joined by two roads, or a road from $n_1$ to $n_1$.
+The first repeats an edge and the second is a loop, so neither is a simple graph.
+\end{nonexample}
+
+\begin{plainwords}
+Two houses are neighbours when one road joins them directly.
+Being neighbours says nothing about longer trips.
+\end{plainwords}
+
+\begin{definition}[Adjacent vertices; textbook Definition 1.1.4]\label{def:adjacent}
+Vertices $u$ and $v$ are \emph{adjacent} if $uv\in E$; then $u$ is a \emph{neighbour} of $v$ \cite[p.~11]{petrosyan2015grafneri}.
+\end{definition}
+
+\begin{remark}
+Adjacency is symmetric, and no vertex is adjacent to itself, because there are no loops.
+It describes direct roads only, not longer connections.
+\end{remark}
+
+\begin{example}
+$n_1$ and $n_2$ are adjacent in the board graph.
+\end{example}
+
+\begin{nonexample}
+$n_1$ and $n_3$ are not adjacent in the board graph, although the trip $n_1,n_2,n_3$ joins them.
+\end{nonexample}
+
+\begin{plainwords}
+The degree of a house is the number of roads that touch it.
+A busy house has a large degree.
+\end{plainwords}
+
+\begin{definition}[Degree]\label{def:degree}
+The \emph{degree} $\deg(n_i)$ of a vertex $n_i$ is the number of edges that contain $n_i$.
+\end{definition}
+
+This is the usual meaning of the word, stated for example as ``the number of edges at that vertex, or the vertex degree'' \cite{quinlan_matrices_graphs}.
+The textbook's own definition of degree was not read, so no textbook number is given.
+
+\begin{remark}
+In a simple graph the degree is also the number of neighbours, because each neighbour is joined by exactly one edge.
+\end{remark}
+
+\begin{example}
+In the board graph $\deg(n_1)=1$, $\deg(n_2)=2$, and $\deg(n_3)=1$.
+\end{example}
+
+\begin{nonexample}
+$\deg(n_1)$ is not $2$ in the board graph, although two other vertices can be reached from $n_1$.
+Only roads at $n_1$ count, and $n_3$ is reached by passing through $n_2$.
+\end{nonexample}
+
+\subsection{The adjacency matrix}
+
+\begin{plainwords}
+Make a square table with one row and one column for every house.
+Write a one where the row house and the column house share a road.
+Write a zero everywhere else.
+This table describes the whole village.
+\end{plainwords}
+
+A \emph{matrix} is a rectangular table of numbers; $A_{ij}$ is the number in row $i$ and column $j$.
+The \emph{transpose} of a matrix swaps its rows and columns, and a matrix is \emph{symmetric} if it equals its transpose, that is, if $A_{ij}=A_{ji}$ for all $i,j$.
+
+\begin{definition}[Adjacency matrix; textbook, printed p.~11, after Definition 1.1.6]\label{def:adjmat}
+The \emph{adjacency matrix} of $G$ is the $N\times N$ matrix $A$ with $A_{ij}=1$ if $n_i$ and $n_j$ are adjacent, and $A_{ij}=0$ otherwise \cite[p.~11]{petrosyan2015grafneri}.
+\end{definition}
+
+The textbook's definition number for this matrix was not recorded, so only its page is given.
+The board writes the same rule as $A_{ij}=1$ if $e_{ij}\in V$ and $A_{ij}=0$ if $e_{ij}\notin V$, with its $V$ standing for the edge set \cite{whiteboard1,whiteboard2}.
+
+\begin{remark}
+The definition allows only the entries $0$ and $1$.
+It depends on how the vertices are numbered: renumbering permutes rows and columns together.
+\end{remark}
+
+\begin{example}\label{ex:boardmatrix}
+The board matrix $\matA$ is the adjacency matrix of the board graph of \cref{ex:boardgraph}: $A_{12}=A_{21}=1$, $A_{23}=A_{32}=1$, and every other entry is $0$.
+\end{example}
+
+\begin{nonexample}
+The matrix with rows $(0\ 1\ 0)$, $(0\ 0\ 1)$, $(0\ 1\ 0)$ is not the adjacency matrix of a simple undirected graph, because $A_{12}=1$ but $A_{21}=0$.
+A matrix with a $1$ on the diagonal (a loop) or an entry $2$ (a double road) is not one either.
+\end{nonexample}
+
+\begin{plainwords}
+The table has some easy features.
+It looks the same when flipped over its diagonal.
+The diagonal holds only zeros.
+Adding up one row tells how many roads touch that house.
+\end{plainwords}
+
+\begin{proposition}[Properties of $A$]\label{prop:rowsums}
+For the adjacency matrix $A$ of a simple undirected graph:
+\begin{enumerate}
+\item every entry is $0$ or $1$;
+\item $A$ is symmetric: $A_{ij}=A_{ji}$;
+\item the diagonal is zero: $A_{ii}=0$;
+\item the sum of row $i$, and of column $i$, equals $\deg(n_i)$;
+\item the sum of all entries equals $2|E|$;
+\item conversely, every $N\times N$ matrix of zeros and ones that is symmetric with zero diagonal is the adjacency matrix of some simple graph with numbered vertices.
+\end{enumerate}
+\end{proposition}
+
+Items 1--3 and 6 are stated in the textbook \cite[pp.~11--12]{petrosyan2015grafneri}, and items 2, 3 and 6 also appear in other notes \cite{quinlan_matrices_graphs,paramadevan2021adjacency}.
+Items 4 and 5 are derived here; a published note states item 4 in a form that allows loops \cite{paramadevan2021adjacency}.
+
+\begin{proof}
+Items 1--3 follow from \cref{def:adjmat}, because adjacency is symmetric and no vertex is adjacent to itself.
+For item 4, the sum of row $i$ is the number of $j$ with $A_{ij}=1$, which is the number of neighbours of $n_i$.
+Each neighbour is joined to $n_i$ by exactly one edge, since there are no repeated edges, and no edge at $n_i$ joins it to itself, since there are no loops.
+So the number of neighbours equals the number of edges at $n_i$, which is $\deg(n_i)$.
+Column $i$ gives the same number by symmetry.
+For item 5, add item 4 over all $i$.
+Each edge $n_in_j$ adds one to $\deg(n_i)$ and one to $\deg(n_j)$, so it is counted twice.
+For item 6, join $n_i$ and $n_j$ exactly when the entry is $1$.
+Symmetry makes this a set of unordered pairs, and the zero diagonal excludes loops.
+\end{proof}
+
+For the board matrix the row sums are $1,2,1$, the column sums are $1,2,1$, and the total is $4=2|E|$ with $|E|=2$ (script, \cref{app:repro}).
+
+\subsection{Walks}
+
+\begin{plainwords}
+A walk is a trip along the roads.
+Start at a house and move to a neighbour, again and again.
+You may pass the same house twice.
+You may drive the same road twice.
+The length of a trip is the number of roads you drove.
+If you drive a road twice, you count it twice.
+Staying at home is also a trip, and its length is zero.
+\end{plainwords}
+
+\begin{definition}[Walk; textbook Definition 1.2.10]\label{def:walk}
+A \emph{walk of length $k$ from $u_0$ to $u_k$}, also called a \emph{$(u_0,u_k)$-walk}, is a sequence $u_0,e_1,u_1,\dots,u_{k-1},e_k,u_k$ of vertices and edges with $e_i=u_{i-1}u_i$ for $1\le i\le k$ \cite[p.~21]{petrosyan2015grafneri}.
+The \emph{length} of the walk is $k$, the number of edges, each edge counted as many times as it occurs \cite[p.~22]{petrosyan2015grafneri}.
+\end{definition}
+
+\begin{remark}\label{rem:walk}
+A walk allows repeated vertices and repeated edges \cite[p.~22]{petrosyan2015grafneri}.
+It forbids one thing only: two consecutive vertices that are not joined by an edge.
+A walk with $k$ edges lists $k+1$ vertices.
+The textbook does not say in so many words that $k=0$ is allowed.
+This paper reads $k=0$ as allowed, because the textbook's property $d(u,u)=0$ of distance needs a path of length $0$ from $u$ to $u$ \cite[p.~23]{petrosyan2015grafneri}, and another text has a length-0 walk as an example \cite[Example 2.9.2]{grinberg2025graph}.
+This is an interpretation and is qualified.
+\end{remark}
+
+\begin{remark}[A walk is its list of vertices]\label{rem:vertexlist}
+In a simple graph there is at most one edge between two vertices, so the edge $e_i=u_{i-1}u_i$ is forced by its two ends.
+Hence a walk of length $k$ from $n_i$ to $n_j$ is the same thing as a sequence $w_0,w_1,\dots,w_k$ of vertices with $w_0=n_i$, $w_k=n_j$ and $w_{t-1},w_t$ adjacent for each $t$ from $1$ to $k$ (derived).
+Two walks are different exactly when these sequences differ at some position.
+From here on a walk is written by its vertices.
+For a graph with repeated edges this step would fail, which is one reason why ``simple'' matters.
+\end{remark}
+
+\begin{example}
+In the board graph the sequence $n_1,n_2,n_3,n_2$, written $1,2,3,2$, is a walk of length $3$ from $n_1$ to $n_2$.
+So is $1,2,1,2,3$, of length $4$, from $n_1$ to $n_3$; it repeats the vertices $1$ and $2$ and the edge $n_1n_2$.
+The textbook's example is $v_1,v_3,v_2,v_4,v_3,v_2,v_4,v_3,v_5$ in its graph of Fig.~1.2.5, a walk of length $8$ \cite[p.~22]{petrosyan2015grafneri}.
+\end{example}
+
+\begin{nonexample}
+$1,3$ is not a walk of the board graph, because $n_1$ and $n_3$ are not adjacent.
+(It would be a walk of the drawing's triangle.)
+The textbook's non-example is $v_3,v_1,v_4,v_2,v_3,v_5$ \cite[p.~22]{petrosyan2015grafneri}.
+\end{nonexample}
+
+\paragraph{The textbook graph.}
+For the textbook's examples the paper needs a graph with a cycle, and the board graph has none.
+The textbook's Fig.~1.2.5 shows a graph on five vertices $v_1,\dots,v_5$.
+The textbook's own examples force the seven edges $v_1v_2$, $v_1v_3$, $v_2v_3$, $v_2v_4$, $v_3v_4$, $v_3v_5$, $v_4v_5$ \cite[p.~22]{petrosyan2015grafneri}.
+Only these seven edges are used below, and the graph they form is called the \emph{textbook graph}; nothing depends on reading other lines of the figure.
+Its vertices are written $1,\dots,5$ in the sequences below.
+
+\begin{plainwords}
+A trip is closed when it ends at the house where it began.
+That is the only new rule.
+The trip may still pass houses and roads many times.
+\end{plainwords}
+
+\begin{definition}[Closed walk; textbook Definition 1.2.11]\label{def:closed}
+A $(u_0,u_k)$-walk is \emph{closed} if $u_0=u_k$ \cite[p.~22]{petrosyan2015grafneri}.
+\end{definition}
+
+\begin{remark}
+A closed walk allows everything that a walk allows and forbids only a different start and end.
+A walk of length $0$ is closed.
+In a simple graph no closed walk has length $1$, since that would be a loop, and a closed walk of length $2$ has the form $u,w,u$ and uses one edge twice (derived).
+\end{remark}
+
+\begin{example}
+In the board graph $2,1,2$ is a closed walk of length $2$, and so is $2,3,2,1,2$ of length $4$.
+\end{example}
+
+\begin{nonexample}
+$1,2,3$ is not closed in the board graph: it starts at $1$ and ends at $3$.
+\end{nonexample}
+
+\begin{plainwords}
+Now add one rule.
+Never drive the same road twice.
+You may still pass the same house twice, if you come back by a different road.
+English books call such a trip a trail.
+Our textbook calls it a path.
+This paper says trail, so that the word path can keep one meaning.
+\end{plainwords}
+
+\begin{definition}[Trail; textbook Definition 1.2.12, which names it ``path'']\label{def:trail}
+A $(u_0,u_k)$-walk is a \emph{trail} if its edges $u_0u_1,\dots,u_{k-1}u_k$ are pairwise distinct \cite[p.~22]{petrosyan2015grafneri}.
+\end{definition}
+
[... truncated by build_evidence.py: 259 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/conclusion.tex b/papers/adjacency-walks-connectivity/sections/conclusion.tex
new file mode 100644
index 0000000..d656f8b
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/conclusion.tex
@@ -0,0 +1,21 @@
+\section{Conclusion}\label{sec:conclusion}
+
+The three questions have direct answers.
+
+\paragraph{Q1.}
+For a simple undirected graph with adjacency matrix $A$ and a whole number $k\ge1$, the entry $(A^k)_{ij}$ is the number of walks of length $k$ from $n_i$ to $n_j$ (\cref{thm:walks}, proved by induction on $k$ from the definition of the matrix product; the statement is standard \cite{quinlan_matrices_graphs,grinberg2025graph}).
+It counts walks and not paths: in the board graph $(A^2)_{11}=1$, the walk $1,2,1$, which is neither a path nor a trail (\cref{prop:warning}).
+
+\paragraph{Q2.}
+A graph with $N\ge2$ vertices is connected if and only if every off-diagonal entry of $A+A^2+\dots+A^{N-1}$ is positive, and equivalently if and only if $(I+A)^{N-1}$ has no zero entry (\cref{thm:test}, derived here).
+The proof uses the walk-counting theorem and the fact that every walk contains a path of no greater length, so powers beyond $N-1$ add nothing; the bound cannot be lowered to $N-2$ (\cref{prop:sharp}).
+The board graph, with $S=\matSB$, is connected; the graph with the edge $n_1n_2$ only, with $S=\matSD$, is not.
+Breadth-first search is an alternative that needs no matrix powers \cite{schost2026bfs}.
+
+\paragraph{Q3.}
+A path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ in which all vertices are pairwise distinct, that is, the textbook's simple path (Definition 1.2.13) \cite[p.~22]{petrosyan2015grafneri}.
+The textbook's own word ``path'' (Definition 1.2.12) allows repeated vertices and is called a trail here.
+The statement that the course uses the first meaning comes from the assignment text and is an interpretation; the existence of a path between two vertices is the same under both readings (\cref{sec:pathdef}).
+
+\paragraph{What remains open.}
+The reading of the mark above $A$ on the board, the mismatch between the board's drawing and its matrix, and the question which test the lecturer intended are not settled by the sources (\cref{sec:limits}).
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/discussion.tex b/papers/adjacency-walks-connectivity/sections/discussion.tex
new file mode 100644
index 0000000..faf2590
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/discussion.tex
@@ -0,0 +1,69 @@
+\section{Discussion: limits, disagreements, and cost}\label{sec:discussion}
+
+\subsection{What is proved and what is only checked}
+
+The two main results, \cref{thm:walks} and \cref{thm:test}, are proved in full from the definitions, using \cref{lem:walkpath} for the second.
+The computer checks are tests of the statements and not proofs: the walk count was compared with brute-force enumeration for all labelled simple graphs on $2$ to $5$ vertices, and the test was compared with BFS for all labelled simple graphs on $2$ to $6$ vertices (\cref{app:crosschecks}).
+The proof of \cref{thm:test} is only as good as \cref{thm:walks} and \cref{lem:walkpath}.
+The first is stated by four sources \cite{quinlan_matrices_graphs,grinberg2025graph,lehman_mcs_adjacency,bai2025adjacency}.
+The second combines the textbook's lemma, which needs $u\ne v$ and states no length bound, with a version from another text that allows $u=v$ and gives the bound \cite{petrosyan2015grafneri,grinberg2025graph}; the paper proves the combined form itself.
+The arithmetic is ordinary integer arithmetic.
+Entries are counts and hence non-negative, which is what makes ``a sum is positive if and only if some term is positive'' valid; with subtraction or modular arithmetic that step would fail (derived).
+
+\subsection{Conventions that change the words but not the mathematics}\label{sec:conventions2}
+
+\begin{itemize}
+\item \emph{Path.}
+Under the textbook's own word, ``path'' allows repeated vertices (Definition 1.2.12), and a reader who uses it will count trails \cite{petrosyan2015grafneri}.
+The paper states which meaning it uses and keeps it (\cref{tab:naming}).
+The board does not say which meaning it uses, and the course reading comes from the assignment text.
+This does not change the connectivity result (\cref{rem:connected}), and it changes only counts (\cref{prop:warning}).
+\item \emph{Cycle.}
+The textbook's cycle is a closed trail and the English cycle is the textbook's simple cycle \cite{petrosyan2015grafneri,grinberg2025graph}.
+Cycles are not needed for the main results.
+\item \emph{Length $0$.}
+Whether a walk of length $0$ is allowed, and whether a closed trail of length $0$ is a cycle, is not stated in the textbook pages read (\cref{rem:walk}, \cref{rem:cycle}).
+For $i\ne j$ the connectivity result needs only paths of length at least $1$.
+\item \emph{The mark above $A$.}
+If the mark is an $n$ and not a $k$, \cref{thm:walks} still describes $(A^n)_{ij}$, so the mathematics is unchanged; the reading of the board remains open \cite{whiteboard1,whiteboard2}.
+\item \emph{The drawing.}
+The drawing and the matrix on the board disagree on the line $1$--$3$ and on an arrowhead (\cref{sec:conventions}).
+The paper follows the matrix and does not guess which one the lecturer intended.
+\end{itemize}
+
+\subsection{Where the sources disagree}\label{sec:disagree}
+
+One published note states its Theorem 1 as ``the entry counts different paths of length $l$'', while its own property 7 speaks of walks \cite{paramadevan2021adjacency}.
+As written, Theorem 1 is false for any definition of path that forbids repeated vertices or repeated edges, by \cref{prop:warning}.
+This paper does not cite that theorem as support for \cref{thm:walks}; it cites the notes that say walks \cite{quinlan_matrices_graphs,grinberg2025graph,lehman_mcs_adjacency,bai2025adjacency}.
+The note and the lecture notes that state the connectivity test explain it by ``paths'' where walks are meant, so their explanation is wrong although their statements of the test are correct (\cref{sec:conn}) \cite{paramadevan2021adjacency,bai2025adjacency}.
+Eigenvalue-based tests are outside the scope of this note, and nothing is claimed about them.
+
+\subsection{Cost of the matrix test and of breadth-first search}\label{sec:cost}
+
+This subsection is an estimate that counts operations and does not time programs.
+Take the school method, in which one product of two $N\times N$ matrices takes $N^3$ scalar multiplications.
+Reaching $A^{N-1}$ from $A$ takes $N-2$ products, so the matrix test costs about $(N-2)N^3$ multiplications: $98{,}000{,}000$ for $N=100$ (script).
+By \cref{prop:iplusa} the exponent $N-1$ may be replaced by any larger exponent, so one can square $I+A$ repeatedly until the exponent $2^t$ is at least $N-1$.
+That takes $t$ squarings, $7$ for $N=100$, costing $7{,}000{,}000$ multiplications (script); the script checked this version against BFS on every labelled graph with at most $6$ vertices.
+BFS takes time proportional to $n+m$, the numbers of vertices and edges, when the graph is given by adjacency lists \cite{schost2026bfs}.
+When the input is the matrix $A$ itself, BFS reads each row once, which is $N^2=10{,}000$ entries for $N=100$ (derived).
+The entries of the powers also grow fast: for the complete graph on $10$ vertices the largest entry of $A^9$ is $38{,}742{,}049$ (script).
+The matrix test is useful because its answer is a clean statement about powers of $A$, not because it is fast.
+Faster matrix multiplication methods were not examined.
+The cited slides compare BFS with no matrix test, and the count of $N-2$ products is this paper's own \cite{schost2026bfs}.
+
+\subsection{Limits and open questions}\label{sec:limits}
+
+\begin{itemize}
+\item The theorems are for simple graphs.
+With loops or repeated edges the entry $A_{rj}$ may exceed $1$ and $A_{ii}$ may be nonzero; the same proof then counts walks with multiplicity (interpretation), but \cref{prop:rowsums} changes.
+The test is not claimed for directed graphs: no source was checked for them, and the symmetry of $A$ is used.
+\item The textbook states no walk-counting theorem and no matrix connectivity test in the pages read, and a search of the book found none; the rest of the book was not read page by page, so this absence is qualified \cite{petrosyan2015grafneri}.
+\item The brute-force checks cover small graphs only.
+\item The test says connected or not.
+The sum $S$ does not list a path; \cref{cor:components} gives the components and \cref{rem:distmatrix} the distances.
+\item Open: whether the lecturer's intended answer to the board's question 2 was the sum test, the $(I+A)^{N-1}$ test, or BFS; the board shows only the question.
+\item Open: the reading of the mark above $A$, and the mismatch between the drawing and the matrix.
+Only the user can settle these.
+\end{itemize}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/example.tex b/papers/adjacency-walks-connectivity/sections/example.tex
new file mode 100644
index 0000000..06222d4
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/example.tex
@@ -0,0 +1,166 @@
+\section{Worked examples}\label{sec:examples}
+
+Every matrix, sum, and count in this section was computed by script (\cref{app:repro}); the matrices are written out entry by entry so that they can be checked against the graphs.
+
+\subsection{The board graph and its powers}
+
+\begin{plainwords}
+We take the village from the board.
+It has three houses in a row.
+The first and last houses each have one road.
+The middle house has two roads.
+We count trips of two roads, then of three roads.
+We list every trip, so the reader can see that each count is right.
+\end{plainwords}
+
+The graph has the vertices $n_1,n_2,n_3$ and the edges $n_1n_2$ and $n_2n_3$; this is the graph of the board matrix (\cref{sec:conventions}).
+Its adjacency matrix and the powers up to $A^5$ are
+\[
+A=\matA,\quad A^2=\matAtwo,\quad A^3=\matAthree,
+\]
+\[
+A^4=\matAfour,\quad A^5=\matAfive .
+\]
+Also $A^3=2A$ and $A^{k+2}=2A^k$ for $k=1,\dots,5$ (script).
+The matrix $A$ is symmetric with zero diagonal, and the row sums $1,2,1$ are the degrees (\cref{prop:rowsums}).
+
+\emph{Explicit walks} (derived by enumeration, labels $1,2,3$ for $n_1,n_2,n_3$).
+\begin{itemize}
+\item Length $1$: $1,2$ and $2,3$ and their reverses.
+\item Length $2$: from $1$ to $1$: $1,2,1$ (one walk). From $1$ to $3$: $1,2,3$ (one). From $2$ to $2$: $2,1,2$ and $2,3,2$ (two). From $3$ to $3$: $3,2,3$ (one).
+\item Length $3$: from $1$ to $2$: $1,2,1,2$ and $1,2,3,2$ (two). From $2$ to $3$: $2,1,2,3$ and $2,3,2,3$ (two).
+\end{itemize}
+Each count equals the corresponding matrix entry, as \cref{thm:walks} says; the script asserts this for every entry of $A$, $A^2$ and $A^3$.
+
+\emph{The sums from the inductive step.}
+The step of the proof of \cref{thm:walks} adds up one term for each choice of the second-last vertex $n_r$.
+For $(A^3)_{12}$ the terms are $(A^2)_{1r}A_{r2}$ for $r=1,2,3$, namely $1\cdot1+0\cdot0+1\cdot1=2$.
+The term for $r=1$ is the walk $1,2,1$ followed by the step to $n_2$, giving $1,2,1,2$; the term for $r=3$ is the walk $1,2,3$ followed by the step to $n_2$, giving $1,2,3,2$.
+Likewise $(A^2)_{22}=1\cdot1+0\cdot0+1\cdot1=2$ and $(A^2)_{11}=0\cdot0+1\cdot1+0\cdot0=1$.
+
+\emph{Counts by walk length.}
+\Cref{tab:walkcounts} counts, over all start and end vertices, the walks, trails, paths and closed walks of each length $k$ by enumeration.
+The entries of $A^k$ for $k=1,\dots,5$ agree with the enumeration (script).
+
+\begin{table}[ht]
+\centering
+\caption{Walks, trails, paths and closed walks of length $k$ in the board graph, over all start and end vertices (script \texttt{m2\_walks.py}).}\label{tab:walkcounts}
+\begin{tabular}{@{}ccccc@{}}
+\toprule
+$k$ & walks & trails & paths & closed walks\\
+\midrule
+0 & 3 & 3 & 3 & 3\\
+1 & 4 & 4 & 4 & 0\\
+2 & 6 & 2 & 2 & 4\\
+3 & 8 & 0 & 0 & 0\\
+4 & 12 & 0 & 0 & 8\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+From $n_1$ to $n_3$ there are three walks of length at most $4$: $1,2,3$ (length $2$), and $1,2,1,2,3$ and $1,2,3,2,3$ (length $4$); only the first is a path (script).
+The numbers of walks from $n_1$ to $n_2$ for $k=1,\dots,5$ are $1,0,2,0,4$, and the numbers of paths among them are $1,0,0,0,0$ (script), as used in \cref{prop:warning}.
+
+\emph{The drawing.}
+The drawing on the board also has the line $1$--$3$ and an arrowhead on the line $1$--$2$.
+If the line $1$--$3$ were an edge, the triangle $1,2,3,1$ would be a simple cycle (\cref{ex:cycle}), and the matrix would have $A_{13}=A_{31}=1$.
+It does not, and this paper follows the matrix.
+
+\subsection{A connected example}
+
+\begin{plainwords}
+Take three houses in a row.
+A road joins the first and the second house.
+Another road joins the second and the third house.
+The first and the third house share no road.
+Can you still go from one to the other?
+Yes, through the middle house.
+We expect the check to say connected.
+\end{plainwords}
+
+\begin{example}[Connected; the board graph, $N=3$, $N-1=2$]\label{ex:conn}
+\[
+A=\matA,\quad A^2=\matAtwo,\quad S=A+A^2=\matSB,\quad (I+A)^2=\matIB .
+\]
+$S$ has no zero entry off the diagonal (it has none anywhere), so by \cref{thm:test}(b) the graph is connected.
+$(I+A)^2$ has no zero entry, so by \cref{thm:test}(c) the graph is connected.
+The two answers agree.
+The entry $A_{13}$ is $0$, so no road joins $n_1$ and $n_3$, yet $(A^2)_{13}=1$: there is exactly one walk of length $2$ from $n_1$ to $n_3$, namely $1,2,3$.
+The $(1,3)$ entry of $(I+A)^2$ is $1=\binom{2}{2}(A^2)_{13}$, since the other two terms vanish there, and $(I+A)^2=I+2A+A^2$ holds entry by entry (script).
+BFS from vertex $1$ reaches $\{1,2,3\}$ (script).
+\end{example}
+
+\subsection{A disconnected example}
+
+\begin{plainwords}
+Now take three houses again.
+Only one road exists, between the first and second house.
+The third house stands alone.
+Nobody can walk to it.
+We expect the check to say not connected.
+The check should also show that the third house is a piece by itself.
+\end{plainwords}
+
+\begin{example}[Disconnected; edge $n_1n_2$ only, $N=3$, $N-1=2$]\label{ex:disc}
+\[
+A=\matD,\quad A^2=\matDtwo,\quad S=\matSD,\quad (I+A)^2=\matID .
+\]
+The off-diagonal zeros of $S$ are at $(1,3)$, $(2,3)$, $(3,1)$ and $(3,2)$, and the zeros of $(I+A)^2$ are at the same four places.
+So by \cref{thm:test} the graph is not connected, and by \cref{cor:components} the vertices $n_1$ and $n_2$ lie in one component and $n_3$ in another: the components are $\{n_1,n_2\}$ and $\{n_3\}$, which agrees with BFS (script).
+Higher powers do not help: the entries $(1,3)$ and $(2,3)$ of $A^k$ are $0$ for $k=1,\dots,6$, and in fact no walk reaches $n_3$ at all.
+\end{example}
+
+\subsection{The bound $N-1$ is needed}
+
+\begin{plainwords}
+Now take four houses in a row.
+The first and the last house are three roads apart.
+So a check that stops at trips of two roads cannot see that they are connected.
+We write out the tables and watch what happens.
+\end{plainwords}
+
+\begin{example}[The path on four vertices, $N=4$]\label{ex:four}
+The edges are $n_1n_2$, $n_2n_3$, $n_3n_4$.
+\[
+A=\matP,\quad A^2=\matPtwo,\quad A^3=\matPthree .
+\]
+\[
+A+A^2=\matPsmall \quad(N-2\text{ powers}),\qquad A+A^2+A^3=\matPfull\quad(N-1\text{ powers}).
+\]
+With $N-2=2$ powers the $(1,4)$ entry is $0$, and the test would wrongly say ``not connected''.
+With $N-1=3$ powers every entry is positive.
+This is the case $N=4$ of \cref{prop:sharp}.
+\end{example}
+
+\subsection{Exhaustive agreement with breadth-first search}
+
+\begin{plainwords}
+Examples on a few villages are not proof.
+So we also ran the check on every possible village with up to six houses.
+Each time we compared it with the marking method.
+The two methods always gave the same answer.
+\end{plainwords}
+
+\Cref{tab:exhaustive} reports a script that built every labelled simple graph with $N=2,\dots,6$ vertices, ran the sum test and the $(I+A)^{N-1}$ test, and compared them with an independent BFS.
+The last column shows what goes wrong with only $N-2$ powers.
+This is a test of the statements and not a replacement for the proofs in \cref{sec:conn}, and it covers $N\le6$ only.
+
+\begin{table}[ht]
+\centering
+\caption{Exhaustive check over all labelled simple graphs with $N$ vertices (script \texttt{m3\_connectivity.py}). Columns ``sum test'' and ``$(I+A)^{N-1}$ test'' give the number of graphs on which the test agrees with BFS.}\label{tab:exhaustive}
+\begin{tabular}{@{}rrrrrr@{}}
+\toprule
+$N$ & graphs & connected & sum test agrees & $(I+A)^{N-1}$ test agrees & wrong with $N-2$ powers\\
+\midrule
+2 & 2 & 1 & 2 & 2 & 1\\
+3 & 8 & 4 & 8 & 8 & 3\\
+4 & 64 & 38 & 64 & 64 & 12\\
+5 & 1024 & 728 & 1024 & 1024 & 60\\
+6 & 32768 & 26704 & 32768 & 32768 & 360\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+For $N=3$ the $N-2$ test is wrong on $3$ of the $8$ graphs, the three labelled paths, and for $N=4$ on $12$ of $64$.
+For $N=2$ the sum with $N-2=0$ powers is empty and is wrong on the one connected graph.
+The same script also confirmed that the statement of \cref{cor:components} and the repeated-squaring version of the test (\cref{sec:cost}) agree with BFS on all these graphs.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/introduction.tex b/papers/adjacency-walks-connectivity/sections/introduction.tex
new file mode 100644
index 0000000..78778b1
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/introduction.tex
@@ -0,0 +1,142 @@
+\section{Introduction}\label{sec:intro}
+
+\subsection{The question and where it came from}
+
+A lecture whiteboard shows a small graph, its table of zeros and ones, and two questions about that table \cite{whiteboard1,whiteboard2}.
+The board states the problem as follows: a graph with $N$ nodes is given through its adjacency matrix $A$; (1) what does the entry in row $i$ and column $j$ of a power of $A$ represent, and (2) how does one know whether the graph is connected \cite{whiteboard1,whiteboard2}.
+The board also gives a definition of a connected graph, which uses the word ``path'' \cite{whiteboard1,whiteboard2}.
+The assignment text added a third question: what is the definition of a path between two vertices $n_i$ and $n_j$.
+That third question comes from the assignment, not from the board.
+The paper therefore answers three questions.
+
+\begin{enumerate}
+\item[Q1.] What does the entry $(A^k)_{ij}$ of the $k$-th power of the adjacency matrix represent?
+\item[Q2.] How can one decide from $A$ alone whether the graph is connected?
+\item[Q3.] What is the definition of a path between the vertices $n_i$ and $n_j$?
+\end{enumerate}
+
+\emph{Reading of the board.}
+In question 1 the board puts a small mark above the letter $A$.
+In both photographs the mark looks like a small $n$ or a pair of quotation marks, not clearly a $k$ \cite{whiteboard1,whiteboard2}.
+This paper reads the mark as an exponent $k$, because the assignment text asks about $A^k$.
+This is an interpretation, and it is qualified: the board does not settle it.
+It does not change the mathematics, because \cref{thm:walks} holds for every positive whole exponent, whatever letter is used.
+
+\subsection{The story used throughout}\label{sec:story}
+
+Every explanation marked ``In plain words'' uses one story.
+A village has a number of houses.
+Each house is a point.
+Each road joins exactly two different houses.
+Every road can be driven in both directions.
+No road leads from a house back to itself.
+No two roads join the same pair of houses.
+A trip is a list of houses, one after another, where each house is at the other end of a road from the house before.
+A trip may pass the same house twice and may drive the same road twice.
+A clean route is a trip that never visits the same house twice.
+The village of the board has three houses in a row: a road from the first house to the second, and a road from the second house to the third.
+The first and third houses have no road between them.
+The mathematics below uses the same village; the terms are matched in \cref{tab:story}.
+
+\begin{table}[ht]
+\centering
+\caption{The story and the mathematics. The right column names the definitions that are introduced in \cref{sec:background}.}\label{tab:story}
+\begin{tabular}{@{}ll@{}}
+\toprule
+Story & Mathematics\\
+\midrule
+house & vertex\\
+road & edge\\
+village & simple undirected graph (\cref{def:graph})\\
+trip & walk (\cref{def:walk})\\
+clean route & path (\cref{def:path})\\
+table of roads & adjacency matrix (\cref{def:adjmat})\\
+village in one piece & connected graph (\cref{def:connected})\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\subsection{What the paper shows}
+
+The answers, stated briefly and proved later, are these.
+
+\begin{itemize}
+\item \emph{Q1} (\cref{sec:walks}). For $k\ge1$, the entry $(A^k)_{ij}$ is the number of walks of length $k$ from $n_i$ to $n_j$.
+The statement appears in standard lecture notes \cite{quinlan_matrices_graphs,bai2025adjacency}; the proof in this paper is written out in full.
+The entry counts walks, not paths, and \cref{prop:warning} gives a counterexample.
+One web source states the theorem with the word ``paths'', which is wrong for the usual meanings of that word \cite{paramadevan2021adjacency}; this is discussed in \cref{sec:disagree}.
+\item \emph{Q2} (\cref{sec:conn}). For $N\ge2$ vertices the graph is connected if and only if every entry off the diagonal of $A+A^2+\dots+A^{N-1}$ is positive.
+A published note states this test and lecture notes state its second form, and both prove it loosely \cite{paramadevan2021adjacency,bai2025adjacency}.
+The proof in this paper is complete (derived here).
+\item \emph{Q3} (\cref{sec:pathdef}). A path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ with no repeated vertex.
+This is the course textbook's simple path, Definition 1.2.13 \cite[p.~22]{petrosyan2015grafneri}.
+\end{itemize}
+
+The course textbook states neither the walk-counting theorem nor the matrix test in the pages that were checked, and a search of the whole book found no such theorem or test; the absence is qualified because the rest of the book was not read page by page \cite{petrosyan2015grafneri}.
+Both results are therefore proved here, and the text says so each time.
+
+\subsection{Conventions, assumptions, and kinds of statement}\label{sec:conventions}
+
+\paragraph{Assumptions.}
+The graph is finite, simple, and undirected.
+This is the setting of the assignment, and it agrees with the symmetric matrix with zero diagonal on the board \cite{whiteboard1,whiteboard2}.
+The textbook's graphs are of this kind too \cite[p.~9]{petrosyan2015grafneri}.
+Directed graphs and graphs with repeated edges are not treated (\cref{sec:limits}).
+
+\paragraph{The example graph.}
+The board shows a drawing of three vertices and, beside it, a matrix with rows $(0\ 1\ 0)$, $(1\ 0\ 1)$, $(0\ 1\ 0)$.
+The matrix encodes the two edges $n_1n_2$ and $n_2n_3$ only.
+The drawing shows three lines: one from $1$ to $2$ with an arrowhead at $2$, one from $1$ to $3$, and one from $2$ to $3$ \cite{whiteboard1,whiteboard2}.
+So the drawing has an edge $1$--$3$ that the matrix lacks, and an arrowhead that a symmetric matrix does not support.
+The problem statement says that the graph is given through its adjacency matrix \cite{whiteboard1,whiteboard2}.
+This paper therefore takes the matrix as the example graph, calls it the \emph{board graph}, and treats the extra line and the arrowhead as a mismatch that it reports and does not resolve.
+When a graph with a cycle is needed, the drawing's triangle is used and is labelled as the triangle.
+
+\paragraph{Notation.}
+\Cref{tab:notation} fixes the letters.
+The board writes $(G,V)$ for the graph and $e_{ij}\in V$ in its matrix definition, where its $V$ is the edge set; the textbook writes $G=(V,E)$ with $E$ the edge set \cite{whiteboard1,whiteboard2,petrosyan2015grafneri}.
+This is a difference of notation only.
+The board names the vertices $n_i$; the textbook names them $v_i$ \cite{whiteboard1,whiteboard2,petrosyan2015grafneri}.
+This paper uses the board's $n_i$.
+
+\begin{table}[ht]
+\centering
+\caption{Notation used in this paper.}\label{tab:notation}
+\begin{tabular}{@{}p{0.2\textwidth}p{0.72\textwidth}@{}}
+\toprule
+Symbol & Meaning\\
+\midrule
+$G=(V,E)$ & a finite simple undirected graph with vertex set $V$ and edge set $E$ (textbook letters)\\
+$N$ & the number of vertices, $N=|V|$ (the board writes $|G|=N$)\\
+$n_1,\dots,n_N$ & the vertices (the board's names; the textbook's $v_i$)\\
+$uv$, $e_{ij}$ & the edge between $u$ and $v$; the edge between $n_i$ and $n_j$\\
+$A$, $A_{ij}$ & the adjacency matrix and its entry in row $i$, column $j$\\
+$A^k$, $(A^k)_{ij}$ & the $k$-th power of $A$ and its entry in row $i$, column $j$\\
+$I$ & the $N\times N$ identity matrix (ones on the diagonal, zeros elsewhere)\\
+$k$ & the length of a walk, or an exponent; a positive whole number unless stated\\
+$S$ & the sum $A+A^2+\dots+A^{N-1}$ (\cref{def:S})\\
+$\deg(n_i)$ & the degree of $n_i$ (\cref{def:degree})\\
+$d(u,v)$ & the distance between $u$ and $v$ (\cref{def:distance})\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\paragraph{The word ``path''.}
+The word has more than one meaning in the sources.
+The textbook's own ``path'' (Definition 1.2.12) allows a repeated vertex, and it calls a path without a repeated vertex a ``simple path'' (Definition 1.2.13) \cite[p.~22]{petrosyan2015grafneri}.
+Two English texts call the second kind a path and the first kind a trail \cite{grinberg2025graph,wikipedia_path_graph_theory}.
+The assignment states that in the course a path has no repeated vertex; that statement comes from the assignment text and not from a file, so it is recorded as an interpretation.
+This paper uses \emph{path} for a walk without repeated vertices and \emph{trail} for the textbook's Definition 1.2.12, and \cref{tab:naming} gives the three conventions side by side.
+
+\paragraph{Kinds of statement.}
+A statement with a citation is taken from the cited source.
+A statement marked \emph{derived} is proved or computed in this paper; every number in such a statement was computed by script (\cref{app:repro}).
+Statements marked \emph{interpretation}, \emph{estimate}, or \emph{open} are labelled in the same way, and the textbook's definition numbers are always written ``textbook Definition~1.2.10'' and so on, so that they cannot be mistaken for the numbers of this paper.
+
+\subsection{Organization}
+
+\Cref{sec:background} builds the prerequisites in the textbook's order: graph, adjacency, the adjacency matrix, walk, trail, path, cycle, and distance, with the lemma that every walk contains a path.
+\Cref{sec:walks} answers Q1, \cref{sec:conn} answers Q2, and \cref{sec:pathdef} answers Q3.
+\Cref{sec:examples} works the board graph and three further graphs through in full.
+\Cref{sec:discussion} states the limits, and \cref{sec:conclusion} gives the direct answers.
+The appendices hold longer derivations, the textbook's terms, the transcription of the photographs, and the scripts.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/self-evaluation.md b/papers/adjacency-walks-connectivity/self-evaluation.md
new file mode 100644
index 0000000..fa814e7
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/self-evaluation.md
@@ -0,0 +1,147 @@
+# Self evaluation: Walks, Paths and Connectivity from the Adjacency Matrix
+
+Author notes. All 77 evidence claims were left unchanged in content (only derivation locators in the base and module fragments were updated to the real section, table and label numbers, and the merged file was rebuilt with `merge_evidence.py`). No claim was added, so `evidence/modules/author.json` does not exist. Unverified claims in the text: none (0 in the evidence file). Qualified claims used and disclosed in the text: C24, C29, m1-9, m2-8, m2-15, C36, m3-11. Every number in the paper is produced by a script in `appendices/scripts/`.
+
+## sections/introduction.tex: Introduction
+
+Purpose: state the three questions and where each came from, fix the village story, preview the answers, fix assumptions, notation and the kinds of statement, and give the organization.
+
+Claims and support:
+- The board states the problem, question 1 and question 2 and a definition of connected: C25, C27 (whiteboard1, whiteboard2).
+- The mark above A is not clearly k; reading it as k is an interpretation: C29, m1-9 (qualified).
+- Q3 comes from the assignment text, not from the board: brief section 1; no evidence claim, so stated as the assignment's, not cited.
+- Board notation (G,V), e_ij in V, |G| = N, n_i against the textbook's G = (V,E), v_i: C25, C26.
+- Drawing shows 1-2 with arrowhead, 1-3, 2-3; matrix encodes only 1-2 and 2-3; the matrix is the example: C28.
+- Textbook graphs are finite, simple, undirected: C1.
+- Textbook "path" (1.2.12) allows repeated vertices, "simple path" (1.2.13) does not; English texts differ: C15, C16, C21, C23; course reading from assignment text: C24 (qualified).
+- Walk-counting statement in standard notes: C6; the web note that says "paths": C11; test statements in a note and lecture notes with loose proofs: C34, C36, m3-12.
+- Textbook has no walk-counting theorem and no matrix test in the pages read; full-book search found none; qualified: m3-11.
+
+Conclusions and premises: "both results are proved here" follows from m3-11 (absence in the textbook, qualified) and C34/C36/m3-12 (sources prove loosely).
+
+Not justified: the statement that the course meaning of "path" is "no repeated vertex" rests on the assignment text only (C24, qualified), as the paper says.
+
+## sections/background.tex: Background: graphs, walks, and paths
+
+Purpose: textbook-order prerequisites (graph, adjacent, degree, adjacency matrix, walk, closed walk, trail, path, cycle, simple cycle, naming table, distance, walk-contains-path lemma, length bound), each with plain words, remark, example, non-example.
+
+Claims and support:
+- Definition of graph, adjacent, adjacency matrix and its properties 1-3, 6: C1, C2, C3, C4. Row sums equal degrees and sum of entries 2|E|: m1-1 (derived; source with loops C5). Board writes the matrix rule with e_ij in V: C26.
+- Walk, length, repeats allowed: C12, C13. Walk is its vertex list: m1-2 (derived). Length 0 allowed: m2-15 (qualified; textbook property d(u,u) = 0 from m2-4, Grinberg example in m2-5).
+- Textbook examples for walk, trail, path, simple cycle: m2-1, m2-2. Closed walk: C14. Trail: C15, C21. Path: C16, C21. Distinct vertices give distinct edges: m2-10 (derived; Grinberg exercise in m2-5). Cycle and simple cycle: C17, C22. Board graph has no cycle, trails equal paths in it, triangle has a simple cycle: m2-14 (script). Naming table: m2-7, C23. Distance and its three properties: C18, m2-4; shortest walk = shortest trail = shortest path: m2-12; properties from definition: m2-16.
+- Lemma (walk contains path, any u, v, length bound): C19, C20, m2-3, m2-9 (derived). Path has at most N - 1 edges: C33, m2-6, m2-11 (derived). Board distances and counts: m2-13.
+
+Conclusions and premises: Lemma follows by strong induction on the length (premise: the cut construction is a walk, checked in the proof); the length bound follows from k + 1 distinct vertices among N.
+
+Not justified or qualified: degree (Definition on degree) has no textbook number because the textbook's own definition of degree was not read; it is cited to the lecture-note remark (C9 quote). The seven textbook-graph edges are the ones the textbook's own examples force (m2-1, m2-2); this reading is the module's, not a separate claim. "A figure eight is a cycle" is marked derived from Definition 1.2.14 and has no evidence claim of its own. The statements about renumbering vertices permuting rows and columns, and that a closed walk of length 2 must reuse an edge, are elementary and marked derived or unmarked remarks without separate claims.
+
+## sections/answer1_walks.tex: Q1: what the entry of a power of A counts
+
+Purpose: define matrix product and power, state and prove the walk-counting theorem by induction, give consequences, and show that the entry counts walks and not paths.
+
+Claims and support:
+- Theorem: C6 (Quinlan Thm 1.1.3, Grinberg Thm 4.5.10, Lehman Cor 9.3.3, Bai Thm 1); proof route C7; the proof as written: m1-3 (derived); finite check m1-4.
+- Where hypotheses are used (simplicity twice, undirectedness only for symmetry, multigraph version): m1-8 (interpretation).
+- Corollary (non-negative integers, positivity means a walk, symmetry): m1-7 (derived).
+- (A^2)_ii = degree and trace 2|E|: C9, derived here.
+- Walks are not paths, under both textbook readings: C8, C10, m1-6 (derived); board numbers 1,0,2,0,4 walks and 1,0,0,0,0 paths: m1-6 and `author_numbers.py`.
+- A^0 = I convention: C7 (Grinberg).
+
+Conclusions and premises: Q1 answer follows from Theorem (induction: base k = 1 from Definition of A; step from the partition by second-last vertex and the bijection when A_rj = 1). Warning follows from the diagonal proposition and from "a path from n_i to n_i is the single vertex".
+
+Not justified: nothing beyond the textbook gap (m3-11, qualified).
+
+## sections/answer2_connectivity.tex: Q2: deciding connectivity from the matrix
+
+Purpose: define connected, components, S, prove the test and its second form, state it as a procedure, show N - 1 is sharp, and give BFS.
+
+Claims and support:
+- Definition of connected, board's version: C30, C25. Walk or path give the same connectivity: C32 and derived Remark.
+- Components, Remark 2.1.1: C31, m3-1. Textbook examples: m3-2.
+- Test statement: C34 (Paramadevan Thm 2, MathWorld); second form: C36 (qualified, Bai); proofs of both: C35, C37 (derived), m3-3, m3-5, m3-9; loose proofs in sources: m3-12.
+- Path has at most N - 1 edges: C33. N - 1 cannot be lowered: m3-4 (derived, script). Edge cases N = 1, 2 and diagonal of S: m3-3. Components from S: m3-5. Distance as smallest k: C38 (derived with m2-12).
+- BFS decides connectivity, correctness statement: C39, m3-13; agreement with matrix test on all graphs up to 6 vertices: m3-8 (check, not proof).
+
+Conclusions and premises: Theorem follows from Proposition (one pair at a time) and Proposition (I + A form). Proposition one pair: premises Walk counting (C6), Lemma (m2-9), Corollary (m2-11), path implies trail (m2-10), non-negative counts (m1-7). I + A form: binomial expansion with positive coefficients (C37, m3-9).
+
+Not justified: the textbook does not state the test (m3-11, qualified). The proof of the I + A form is in the appendix.
+
+## sections/answer3_path.tex: Q3: the definition of a path between n_i and n_j
+
+Purpose: give the definition of a path between n_i and n_j under the course convention and show that the existence statement is the same under the textbook's other reading.
+
+Claims and support: Definition and its identity with textbook Definition 1.2.13: C16, C24, m2-8 (qualified; the course reading comes from the assignment text and the board does not say). One path between n_1 and n_3 in the board graph: m2-13. Same truth value under both readings: m2-9, m2-10, C32 (derived). Counts differ by reading: C10, m1-6.
+
+Conclusion and premises: Q3 answer is the definition itself. Qualification: the course reading of "path" is not in any file.
+
+Not justified: nothing beyond the qualification above.
+
+## sections/example.tex: Worked examples
+
+Purpose: write out every matrix for the board graph, the connected and disconnected examples, the four-vertex path, and the exhaustive check.
+
+Claims and support: board matrix, A^2 to A^5, A^3 = 2A, row sums, walk lists, hand sums: m1-5, m1-1. Walk, trail, path counts by length: m2-13 (script `m2_walks.py`). Connected example numbers: m3-6. Disconnected example numbers: m3-7. Four-vertex path matrices and N - 2 failure: m3-4. Exhaustive check table, failures with N - 2 powers (3 of 8, 12 of 64, 60, 360, 1 for N = 2): m3-8, m3-4. Drawing against matrix: C28. The matrices printed in the paper are generated by `appendices/scripts/author_numbers.py` and input from `figures/generated_numbers.tex`; assertions there compare each power with a direct walk enumeration.
+
+Conclusions and premises: each reading follows from Theorem (test) and the printed matrices.
+
+Not justified: the exhaustive table's "wrong with N - 2 powers" column is from the module script (checked: copy output is identical), not recomputed by `author_numbers.py`.
+
+## sections/discussion.tex: Discussion: limits, disagreements, and cost
+
+Purpose: separate proof from computer check, list convention choices, record where sources disagree, give the cost estimate, and list limits and open questions.
+
+Claims and support: sources for walk counting: C6; lemma combination: C19, C20; conventions: C15, C16, C17, C22, C24, m2-15; mark above A: C29, m1-9; drawing: C28; Paramadevan Theorem 1 wrong as written: C11, C10; loose proofs: m3-12; cost counts (98,000,000 and 7,000,000 for N = 100; N^2 = 10,000; 38,742,049): m3-10 (estimate; script); BFS O(n + m) with adjacency lists: C39, m3-13; textbook absence: m3-11; multigraph interpretation: m1-8.
+
+Conclusions and premises: "the matrix test is useful for its clean statement, not speed" is an interpretation resting on m3-10's counts. Repeated squaring is justified by m3-9.
+
+Not justified: none unsupported. Faster matrix multiplication was not examined, and the text says so. C39's wording "N - 1 matrix products" disagrees with the count N - 2 in m3-10; the paper uses N - 2 and says the slides do not make the comparison.
+
+## sections/conclusion.tex: Conclusion
+
+Purpose: direct answers to Q1, Q2, Q3 and what stays open.
+
+Claims and support: Q1: C6, m1-3, C8, m1-6. Q2: C34, C35, C37, m3-4, C39. Q3: C16, C24, m2-8. Open items: C28, C29, m3-11.
+
+Conclusions and premises: each answer repeats the theorem or definition proved above.
+
+Not justified: nothing new.
+
+## appendices/derivations.tex: Derivations and checks
+
+Purpose: proofs of the distance properties (A.1), the counterexample table (A.2), the premise chain of the test (A.3), the I + A proof (A.4), and the finite cross-checks (A.5).
+
+Claims and support: m2-12, m2-16 (A.1); C10, m1-6 (A.2); C35 and premises C6, C20, C33, C30 (A.3); C37, m3-9 (A.4); m1-4, m3-8, m3-4, and the m2 script checks m2-9 to m2-12 (A.5; numbers 73, 381, 4695 walks, 300 random graphs, 192696 walks are from `m2_walks_output.txt`).
+
+Conclusions and premises: A.4 follows from the binomial expansion and positivity of coefficients; for m greater than N - 1 it uses the length bound.
+
+Not justified: the random-test numbers in A.5 are quoted from the module script output, not independently recomputed.
+
+## appendices/course-terms.tex: The textbook's terms and numbers
+
+Purpose: table of textbook definition numbers and printed pages used.
+
+Claims and support: C1, C2, C3, C4, C12 to C19, C30, C31, m3-1. The textbook's number for the adjacency matrix definition is not recorded; the table says so.
+
+Conclusions and premises: none beyond the table.
+
+Not justified: pages are the printed pages as recorded in the evidence file; this author did not re-read the book, because the evidence file is declared final.
+
+## appendices/photographs.tex: The whiteboard photographs
+
+Purpose: transcription of the board and the edge by edge comparison of drawing and matrix.
+
+Claims and support: C25, C26, C27, C28, C29. The photographs are included as images; the transcription is taken from the evidence quotes (C27 words "it's" and "adj." as on the board).
+
+Conclusions and premises: the arrowhead as a stray mark is an interpretation (brief assumption), labelled as such.
+
+Not justified: reading of the mark above A (qualified, C29).
+
+## appendices/reproducibility.tex: Reproducibility
+
+Purpose: list the scripts that produced every number and how to run them.
+
+Claims and support: scripts `author_numbers.py` (new), `m1_walks.py`, `m2_walks.py`, `m3_connectivity.py`. Outputs of the three module scripts were re-run in this session and are identical to the saved outputs.
+
+Conclusions and premises: none.
+
+Not justified: nothing.
```

# Agent reports

## paper-author-round1

The paper is written and builds cleanly. I did not run or hand-verify the textbook pages again; the evidence file is final and I used it as given.

**Files created in `papers/adjacency-walks-connectivity/`**
- `main.tex`, `references.bib` (11 entries, keys equal the evidence source ids), `self-evaluation.md`, and the compiled `main.pdf` (31 pages).
- `sections/`: `introduction`, `background`, `answer1_walks`, `answer2_connectivity`, `answer3_path`, `example`, `discussion`, `conclusion`.
- `appendices/`: `derivations`, `course-terms`, `photographs`, `reproducibility`.
- `appendices/scripts/`: copies of the three module scripts and their outputs, plus a new `author_numbers.py` and its output.
- `figures/generated_numbers.tex`: the matrices in the paper, written by `author_numbers.py`.

**Edits to existing files.** I did not edit `evidence/evidence.json` by hand. In `evidence.base.json` and `modules/m1.json`, `m2.json` and `m3.json` I changed only the `derivation` locator strings, so they name the paper's real proposition, table and appendix numbers. Then I rebuilt the merged file with `merge_evidence.py`. No claim was added, so there is no `author.json`.

**Mechanical checks**
- `build.sh`: exit 0, no LaTeX errors, undefined references or undefined citations.
- `check_citations.py`: cited keys 11, bib entries 11, evidence sources 11, errors 0, warnings 0.
- `check_claims.py`: 11 sources, 70 supported, 7 qualified, 0 unverified, 0 removed, errors 0, warnings 0.
- `check_evidence_rebuild.py`: rebuild from base plus 3 fragments, 0 differences.
- `inspect_pdf.py`: 31 pages, errors 0, warnings 1. The warning is one overfull box of 0.36 pt, which I left.
- `check_self_evaluation.py`: inputs 13, errors 0, warnings 0.
- Re-running `m1_walks.py`, `m2_walks.py` and `m3_connectivity.py` reproduces their saved outputs exactly.
- I read `build/main.txt` from start to end and fixed what it showed. One real fix: the Theorem 4.15 paragraph had confused which source gave which proof.

**Unverified claims in the text:** none.

**Qualified claims, each disclosed in the text:** C24 and m2-8 (the course meaning of "path"), C29 and m1-9 (the mark above A), m2-15 (length-0 walks), C36 (the second form of the test, whose only source has a proof sketch), and m3-11 (the textbook's silence on both theorems).

**Not fully justified**
- **Textbook references.** The textbook's own definition of degree and its number for the adjacency-matrix definition were never recorded, so `background.tex` gives the matrix only a page (p. 11) and cites degree to a lecture-note remark.
- **Textbook graph.** The seven edges I use for the textbook's Fig. 1.2.5 are the ones its own examples force. That reading is the module's, and no claim of its own covers it.
- **Walk and trail counts.** Some counts printed in the paper come from the module scripts, not from `author_numbers.py`: the walk, trail and path table, the exhaustive-check table, and the random-graph counts. Those outputs match the saved files.
- **Bibliography years.** Years are `n.d.` where the evidence has none, because the citation checker requires a year field.
- **Armenian text.** The textbook's Armenian is not reproduced, since pdflatex has no Armenian support configured. I used English glosses and a transliterated title.

## paper-evaluator-round1

SCORES
1 Correctness: 5 -- I recomputed every number I could with my own script, and all match the paper: the board powers A to A^5, S, (I+A)^2 and the disconnected matrices (sections/example.tex, Examples 6.1 and 6.2), the P4 matrices (Example 6.3), Table 4, Table 5 (graphs 2/8/64/1024/32768; connected 1/4/38/728/26704; N-2 failures 1/3/12/60/360), the walk-test case counts 40/360/5120/76800 (Section 3.2), the costs 98,000,000 and 7,000,000, and the largest entry 38,742,049 of A^9 for K10 (Section 7.4). The proofs of Theorem 3.5, Lemma 2.45, Proposition 4.13, Proposition 4.14 (Appendix A.4) and Theorem 4.15 are valid step by step.
2 Evidence coverage: 4 -- The 77 claims in evidence.json cover every cited statement, and the quotes match. One exception: Definition 2.9 (sections/background.tex:69-71) cites Quinlan's remark about walks of length 2 as the definition of degree and says the textbook definition "was not read". The textbook defines degree as Definition 1.2.1 on printed p. 16.
3 Citation integrity: 4 -- Eight sources checked (seven fetched or read locally, plus both board photos), and all support the attributed statements, including the paper's accurate criticism of Paramadevan's Theorem 1 and its proof of Theorem 2. One description is wrong: sections/introduction.tex:67 calls the peer-reviewed journal article [7] a "web source".
4 Logical validity: 5 -- Every conclusion follows. The walk-to-path step in the proof of Proposition 4.13 that the cited sources skip is supplied by Lemma 2.45. The trail and path readings of "connected" are shown to agree (Remark 4.2, Section 5). The case i = j and N = 1 is handled (Remark 4.21).
5 Understandability: 4 -- The plain-words layer and the story of houses and roads are applied almost everywhere. A few terms are used without explanation: "metric space" (background.tex:413), "reflexive, symmetric and transitive" (answer2_connectivity.tex:55), "queue" (answer2_connectivity.tex:293), "adjacency lists" (discussion.tex:49), and the binomial coefficient in example.tex:89, which appears before Appendix A.4 explains it.
6 Completeness: 4 -- Every objective in the brief is met. Two small gaps: the textbook number for degree is missing (background.tex:71), and Table 3 has no explicit "course" column although the brief and the text at background.tex:366 say it does.
7 Methodological rigor: 5 -- Every claim is tagged as cited, derived, interpretation or open. The script checks are presented as tests, not proofs (Sections 6.5 and 7.1), and the integer arithmetic assumption is stated (Section 7.1).
8 Critical analysis: 5 -- Section 7.3 identifies and explains the source that says "paths" where it means walks. The drawing-versus-matrix mismatch and the mark above A are reported, not hidden (Sections 1.1, 1.4 and 7.5). Section 7.4 discusses cost. The textbook absence claim is qualified (Sections 1.3 and 7.5), and I confirmed it: the book's only later use of the adjacency matrix is Kirchhoff's theorem on printed p. 60.
9 Internal consistency: 4 -- Terms (walk, trail, path) and notation (n_i, N, S) are consistent throughout. Two small inconsistencies: Table 3's header "This paper" against the text's "course" (background.tex:366-375), and [7] called a "web source" in introduction.tex:67 but a "published note" in Sections 4.4 and 7.3.
10 Reproducibility: 5 -- Appendix D names a script and saved output for every number. figures/generated_numbers.tex holds the matrices, and they agree with my independent computation.
11 LaTeX and PDF quality: 4 -- 31 pages, references resolve, and the matrices render (page 22 checked as an image). inspect_pdf reports 0 errors and 1 warning: an overfull hbox of 0.36pt at Example 2.29.
12 Answer relevance: 5 -- Sections 3.5, 4.8 and 5 and the Conclusion (Section 8) answer Q1, Q2 and Q3 directly, and nothing outside the brief is claimed.

FINDINGS
F1 | minor | sections/background.tex:69-71 (Definition 2.9) | Says the textbook's definition of degree "was not read" and cites a Quinlan remark about walks as the definition, but the textbook defines degree as Definition 1.2.1 on printed p. 16 (PDF p. 17), as the number of edges incident to the vertex; this misses the brief's requirement to cite textbook numbers. | Title Definition 2.9 "textbook Definition 1.2.1", cite [9, p. 16], delete the "not read" sentence, add an evidence claim with the p. 16 quote, and add the row to Table 7.
F2 | minor | sections/introduction.tex:67 | "One web source states the theorem with the word 'paths'" describes [7], which is a peer-reviewed journal article (JSc EUSL 12(1), DOI 10.4038/jsc.v12i1.29) and is called a "published note" elsewhere. | Replace "One web source" with "One published note".
F3 | minor | sections/background.tex:366-375 (Table 3) | The text says the table lists "the course, textbook, and English names", but the columns are Textbook, English, This paper. | Rename the last column "Course / this paper", or reword line 366 to match the columns.
F4 | minor | sections/answer2_connectivity.tex:204 (Corollary 4.19) | No plain-words paragraph comes before this corollary, against the study-note rule in the brief that every theorem-like statement has one. | Add one, e.g. "If the running total for two houses is positive, they are in the same piece of the village; if it is zero, they are in different pieces."
F5 | minor | sections/background.tex:413 | "the pair (V,d) is a metric space" is not explained for a first-time reader. | Add: "that is, d behaves like an ordinary distance: properties 1 to 3 above are exactly the rules a distance must obey."
F6 | minor | sections/answer2_connectivity.tex:55 | "reflexive, symmetric and transitive" is used without explanation. | Add one clause per word: "every vertex is related to itself, u ~ v gives v ~ u, and u ~ v with v ~ w gives u ~ w."
F7 | minor | sections/answer2_connectivity.tex:293; sections/discussion.tex:49 | "queue" and "adjacency lists" are not explained. | Add "a queue is a list served first-in, first-out" and "an adjacency list stores, for each vertex, the list of its neighbours."
F8 | minor | sections/example.tex:89 | The binomial coefficient binom(2,2) and the expansion (I+A)^2 = I + 2A + A^2 are used before Appendix A.4 explains them. | Add "(binomial expansion, Appendix A.4)" or write the product out: (I+A)(I+A) = I + A + A + A^2.
F9 | minor | Example 2.29 (sections/background.tex; build/main.log:828) | Overfull hbox of 0.36pt. | Allow a line break in the vertex sequence, or reword the sentence slightly.

CITATION SPOT CHECKS
quinlan_matrices_graphs | fetched | supports | Definition 1.1.1, Notes 1-2, Theorem 1.1.3 and its proof (sum of (A^{k-1})_{ir}A_{rj} sorted by second-last vertex), and "the number of edges at that vertex, or the vertex degree" all appear verbatim. No author or date in the file, as the bib entry says.
paramadevan2021adjacency | fetched | supports | Metadata matches (JSc EUSL 12(1) pp. 13-21, DOI 10.4038/jsc.v12i1.29). Properties 7-9, Theorem 1 ("different paths"), Theorem 2 (sum test with i != j) and Theorem 3 are verbatim. The paper's criticism that the proof says "paths" and goes from b_ij != 0 to a path without a lemma is accurate.
bai2025adjacency | fetched | supports | Title, author and date match. Theorem 1 says walks, followed by "counts walks — not paths". Theorem 2 is the (I+A)^{n-1} criterion, with a proof sketch that says "paths", as the paper states.
weisstein_connectedgraph | fetched | supports | States that a graph on n&gt;1 vertices is connected iff the sum of A^k for k=1..n-1 has no zero off-diagonal entries, with no proof, as the paper states.
grinberg2025graph | fetched | supports | arXiv v3, "Spring 2025 edition, June 7, 2025", 454 pp. Exercise 2.9, Corollary 2.9.7, Section 2.9.4 ("vertices to spare"), Proposition 2.9.10, Definitions 2.9.12, 2.10.1 and 3.4.5, and Theorem 4.5.10 (proof by induction from C^0 = I_n) are all present.
schost2026bfs | fetched | supports | Winter 2026 slides by Éric Schost. Correctness: "there is a walk s ; v in G if and only if discovered[v]"; "testing if G is connected"; adjacency lists; "Total: O(n + m)".
petrosyan2015grafneri | fetched (local file, PDF pp. 12-13, 17, 22-24, 49-50) | supports | The wording of Definitions 1.1.4, 1.2.10-1.2.16, Lemma 1.2.1 (u != v, induction on length), the distance properties, Definition 2.1.1, the components paragraph and Remark 2.1.1 matches the paper's rendering and page locators. The degree definition (Definition 1.2.1, p. 16) exists but is not cited (F1).
whiteboard1 / whiteboard2 | fetched (local images viewed) | supports | The transcription is accurate: matrix 010/101/010, arrowhead at 2, lines 1-2, 1-3 and 2-3, and a mark above A that looks like quotation marks or a small n, as the paper says.

UNVERIFIED CLAIMS IN TEXT
C24 | Definition 2.31 note and Definition 5.1 note (course meaning of "path", from the assignment text) | qualified
C29 | Section 1.1 "Reading of the board"; Appendix C (mark above A read as k) | qualified
C36 | Section 4.4 after Theorem 4.15 ((I+A)^{N-1} form, Bai accessed partially) | qualified
m1-9 | Section 7.2, item on the mark above A | qualified
m2-8 | Section 5, note after Definition 5.1 | qualified
m2-15 | Remark 2.19 (length-0 walks allowed) | qualified
m3-11 | Sections 1.3 and 7.5 (textbook states neither theorem; independently confirmed by full-text search) | qualified

Mechanical checks: check_citations: 11 keys, 11 bib entries, 11 sources, 0 errors, 0 warnings. check_claims: 70 supported, 7 qualified, 0 unverified, 0 errors. inspect_pdf: 31 pages, 0 errors, 1 warning (F9). I did not run build.sh because it writes build files; main.pdf is present and current. I did not observe release condition 9 (self-evaluation coverage), as instructed.

RECOMMENDATION
PASS -- There are no critical or major findings, every dimension scores at least 4, every observable release condition holds, and the nine minor findings should be fixed or documented before release.

## technician-reader-round1

FINDINGS

F1 | comprehension | Abstract: "Both theorems are proved in full, because the course textbook does not state them in the pages checked [9]." | The abstract names three questions but then says "both theorems" without saying which two they are. The abstract also uses "walk", "path", "vertex", "off the diagonal" and "(I + A)^(N−1)" with no gloss. "I" is not defined there. | Name the two theorems ("the walk-counting theorem and the connectivity test"). Add a half-sentence defining I as the identity matrix. | 

F2 | comprehension | 1.1: "the board puts a small mark above the letter A... a small n or a pair of quotation marks, not clearly a k [4, 5]." | The reader cannot see the photographs until Appendix C. Sections 1.1 and 1.4 describe the board's drawing in words ("an arrowhead at 2", "an edge 1–3 that the matrix lacks") with no figure. The reader must take these descriptions on faith for 25 pages. | Add a forward pointer ("see Figure 1, Appendix C") at the first mention, or move the figure into Section 1.1.

F3 | comprehension | 1.1 and 1.4: "The assignment text added a third question"; "the assignment states that in the course a path has no repeated vertex." | "The assignment", "the board" and "the course" are never introduced. The reader does not know who wrote the assignment, whether it is available, or why the paper depends on it. The "[4, 5]" citations point to photographs, but the assignment text has no citation at all. | Add one sentence at the start of 1.1 saying what the assignment is and that it is unavailable as a file. Alternatively cite it as a numbered source.

F4 | comprehension | 1.3: "both prove it loosely [7, 1]"; "(derived here)"; "(qualified)"; 1.4 "Kinds of statement". | The labels "derived", "interpretation", "qualified", "estimate" and "open" are defined only in the last paragraph of 1.4. The reader meets "qualified" in 1.1 and the abstract before then. "Qualified" is never defined precisely. It seems to mean "caveated", but this is a guess. | Define "qualified" in one sentence and move the "Kinds of statement" paragraph before first use, or add a forward reference.

F5 | comprehension | 1.2 and 1.4 (Table 1, "Definition 2.18", "Definition 2.31", "Definition 2.13"). | The roles of "plain words" paragraphs versus formal definitions are clear. However, the story fixes "trip" as the word for "walk" and "clean route" for "path", while the paper later says "trail". Trail has no entry in Table 1. The "In plain words" for trail says "Our textbook calls it a path", which clashes with the story's "clean route". | Add "trail" to Table 1 (for example "trip with no repeated road").

F6 | comprehension | 1.4: "The board writes (G, V) for the graph and eij ∈ V in its matrix definition, where its V is the edge set." | This is confusing. The reader has not yet seen what is on the board, and a vertex set V that is secretly the edge set is hard to follow. | Say "the board uses V for the edge set (probably a slip)" and move the details to Appendix C, keeping only the paper's own notation in the main text.

F7 | comprehension | 1.4 and 2.3: "The textbook's Fig. 1.2.5 shows a graph on five vertices... The textbook's own examples force the seven edges..." | The textbook graph is introduced inside a block of walk examples. The reader cannot see the figure and must trust the reconstruction from the edge list. The figure is never reproduced. | Draw the seven-edge textbook graph as a small figure, or list the edges as a labelled example (for example "Example 2.20a") before it is used.

F8 | comprehension | 2.1: "The textbook's own definition of degree was not read, so no textbook number is given." Also Definition 2.13, "The textbook's definition number for this matrix was not recorded." | This is bookkeeping about the author's process, not about the mathematics. It makes the reader wonder whether the definitions were checked. | Drop it from the body and keep it in Appendix B, or state it once in 1.4.

F9 | comprehension | Definition 2.18: "u0, e1, u1, ..., uk−1, ek, uk of vertices and edges with ei = ui−1 ui". | The notation ui−1ui for an edge is explained earlier (Table 2, "uv, eij"), but the symbol "ei" is introduced as an edge and is also the index in "eij" (the board's edge). The two uses of e look alike. | Say "the i-th edge ei joins ui−1 and ui".

F10 | comprehension | Remark 2.19: "The textbook does not say in so many words that k = 0 is allowed. This paper reads k = 0 as allowed, because the textbook's property d(u,u) = 0 of distance needs a path of length 0." | This is a long justification for a small convention. The reader cannot tell why it matters: the length-0 walk is needed only later (Lemma 2.45, Remark 4.2). | Add "needed in Lemma 2.45 and Remark 4.2" to say why the point is raised.

F11 | comprehension | 2.3, Remark 2.28: "In the board graph every trail is also a path... for every length from 0 to 4 ... (derived, checked by script for lengths up to 4)." | The reader is asked to take a claim for lengths 0 to 4 on trust. A short argument is available: the board graph is a path with 3 vertices and no cycle. The text then says the claim is "derived" yet only "checked by script". | Replace with one sentence of reasoning ("the board graph has no cycle, so no trail revisits a vertex"), or label it "checked" only.

F12 | comprehension | 2.4 (Cycles): "Cycles are not needed for the main results; they are given because the textbook's list of definitions includes them." | A full page of definitions, examples and non-examples (Definitions 2.36 and 2.37, Remark 2.38) is not used afterwards. The reader cannot tell whether to retain it. Likewise for Table 3 and the trail material, which is needed only for Remark 4.2. | Mark 2.4 as skippable at its start, or move it to an appendix.

F13 | comprehension | Definition 2.41 and the text after it: "The textbook's 'path' here is its Definition 1.2.12, a trail. The definition does not depend on whether one reads trail or path..." | The reader is told that "the pair (V,d) is a metric space" with no explanation of "metric space". Distance is used later only in Remark 4.20. | Delete the metric-space sentence or gloss it ("d behaves like an ordinary distance").

F14 | comprehension | Lemma 2.45 proof: "Form the sequence W′ = u0, ..., ui, uj+1, ..., uk; if j = k nothing follows ui." | This is the hardest step to follow and I had to read it three times. The index juggling hides the idea of cutting out the loop between ui and uj. The edge case j = k is stated inside a sentence about the sequence. The trace example appears only after the proof. | Add one sentence before the formal construction ("delete everything after the first ui up to and including uj, so the walk goes from ui straight on to uj+1"), or put the trace first.

F15 | comprehension | Definition 3.1: "(XY)ij = Σ_{r=1}^N Xir Yrj" and the following remark that "A^0 = I... corresponds to one walk of length 0". | The pdf text of the formula is garbled in my reading, but the intent is clear. A technician who has not met matrix products will rely on the "plain words". The identity matrix I appears in Table 2 and in the abstract without a display of an example. | Show I once for N = 3. Show one numeric row-times-column product before Theorem 3.5.

F16 | comprehension | Proof of Theorem 3.5: "Wk(i, j) is the sum over r = 1, ..., N of the number of walks of length k from ni to nj whose second-last vertex is nr. Fix r. We claim that the number in class r is Wk−1(i, r) · Arj." | The reader is not told in advance why the sum is organised by the second-last vertex. The proof is correct in form but long. The two bullet cases are clear. The "Why the argument is valid" paragraph then repeats it. | Open the proof with a roadmap sentence ("a walk of length k is a walk of length k−1 plus one final step; that final step is allowed exactly when Arj = 1").

F17 | comprehension | 3.2, end: "A computer check supports the theorem but is not a proof: ... all 40, 360, 5120 and 76800 tested cases of (k, i, j) agreed." | The numbers 40, 360, 5120 and 76800 are not explained. The reader cannot tell how they arise (A.5 says k runs to 4 for N ≤ 4 and to 3 for N = 5, so the count depends on k, N, and the graph count). | Give the formula, for example "graphs × N² pairs × values of k", or drop the counts.

F18 | comprehension | Proposition 3.11: "If ni has at least one neighbour, then (A²)ii = deg(ni) &gt; 0, but no path, and no trail, of length 2 from ni to ni exists." | "The first inequality" in the proof refers to "&gt; 0", but the statement has no inequality symbol sign besides "&gt;". The claim "no trail" is explained only by the edge being used twice, which is fine. The final sentence "Hence (A^k)ij is in general not the number of paths" does not follow from a single diagonal example unless one adds that k = 2 is a specific case. | Say "so the entry (A²)ii counts a walk that is not a path; hence the entries are not path counts".

F19 | comprehension | Definition 4.5 (Connected component): "On the vertex set V write u ∼ v if G has a (u, v)-path. This relation is reflexive, symmetric and transitive, so V splits into classes." | Reflexive, symmetric, transitive and "classes" (equivalence relation) are used without explanation. The claim that the relation has these properties is not shown. | State "equivalence relation" with a one-line gloss and a pointer to why transitivity holds (join two walks).

F20 | comprehension | Definition 4.9 (new notation S) and Remark 4.10. | S is defined as a sum of N−1 powers, but the reader does not see why N−1 is the right stopping point until Section 4.4. The "plain words" tell the reader to stop at "one step short" without a reason. | Add "(the reason is Corollary 2.46)" to the definition.

F21 | comprehension | Proposition 4.14: "(I + A)^m ij &gt; 0 if and only if Sij &gt; 0. Every diagonal entry of (I + A)^m is at least 1." | The purpose of this second form is never stated in the main text: why would one prefer (I + A)^(N−1)? The reason appears only in 7.4 (repeated squaring). Its proof is deferred to Appendix A.4 although it is a half-page argument. | At first mention, add one sentence on motivation ("it can be computed by repeated squaring, Section 7.4").

F22 | comprehension | Proposition 4.13, statement (i): "There is an (ni, nj)-path in G (in the sense of textbook Definition 2.1.1)." | The parenthetical is confusing. Definition 2.1.1 is about "connected", and the text calls the textbook "path" a trail. The reader does not know which meaning of "path" statement (i) uses. | Replace with "a path (Definition 2.31) from ni to nj" and refer to Remark 4.2 for the trail reading.

F23 | comprehension | Proof of Theorem 4.15: "Together with the diagonal entries, which are always positive by Proposition 4.14, this is (c)." | The step from positivity of off-diagonal entries of (I+A)^(N−1) to (b) uses Proposition 4.14 with Sij, and the diagonal remark is easy to miss. Statement (a) also requires u = v pairs, which the proof dismisses by Remark 4.2. The chain is correct but spread over four references. | Add a three-line outline of the proof: (a) iff each pair joined, (b) via Prop 4.13, (c) via Prop 4.14.

F24 | comprehension | Remark 4.21: "For N = 2 and one edge, S = A has zeros on the diagonal although the graph is connected. ... For N = 1 ... S is an empty sum." | This sits in a remark in the middle of the proof area and mixes three cases. The sentence "For N ≥ 3 and a connected graph the diagonal of S is positive anyway" is an unproved claim, said to be unneeded. | Split into short bullets, or cut the N ≥ 3 claim since the test does not need it.

F25 | comprehension | 4.6: "Enough: Proposition 4.13 shows that if a trip between two different vertices exists at all, a trip of length at most N − 1 exists... Not fewer: the next statement shows that N − 1 cannot be lowered." | The heading says "N − 2 are not", but the argument for "not fewer" is a single counterexample family. The text says "the next statement shows" but a "plain words" paragraph sits between. The term "trip" is used while the formal statement uses "walk". | Use "walk" in this paragraph, or state that the claim is shown by Proposition 4.23 for a path graph.

F26 | comprehension | Proposition 4.23 and Example 6.3. | The example prints A + A² as "(N − 2 powers)" with the (1,4) entry 0. The reader must locate the entry in a 4×4 matrix with no highlight. | Mark the (1,4) entry (for example boldface) and say "top-right entry".

F27 | comprehension | 4.7, Remark 4.24: "Its correctness statement in the source is that for every vertex v there is a walk from s to v if and only if v is discovered when the search ends [10]." | BFS, "queue" and "discovered" are used before being defined. The plain-words version helps. The claim "agree on all 32768 labelled graphs with 6 vertices" is taken on faith from a script. | State briefly that the BFS comparison is only a sanity check, with a pointer to Table 5.

F28 | comprehension | 6.1: "Also A³ = 2A and A^(k+2) = 2A^k for k = 1, ..., 5 (script)." | The reader is told this pattern without any reason or relevance to the questions. It does not return afterwards. | Delete it, or say why it matters (it shows that the entries grow).

F29 | comprehension | Table 4 (6.1). | The columns "trails" and "paths" are equal in every row, and the table includes k = 0 with a "closed walks" count of 3 but k = 1 with 0. The reader cannot tell what the table is meant to show. The caption does not say. The reported "walks" for k = 4 (12) is not tied to the matrix entries shown (the sum of A⁴ is 12). | Add one sentence on the point of the table ("walks multiply while paths stop at length 2"). State that the walk column equals the sum of the entries of A^k.

F30 | comprehension | Table 5: "wrong with N − 2 powers" column: 1, 3, 12, 60, 360. | The numbers are not explained. The text covers N = 3 (3 graphs) and N = 4 (12 graphs) only. The reader cannot check the 60 and 360, or see why they are the numbers of labelled graphs on which the shortened test fails. | State the rule (for example, the shortened test errs exactly on graphs of diameter N−1, that is, labelled paths, which number N!/2), or say that no pattern is claimed.

F31 | comprehension | 7.4: "Reaching A^(N−1) from A takes N − 2 products, so the matrix test costs about (N − 2)N³ multiplications: 98,000,000 for N = 100 ... t squarings, 7 for N = 100, costing 7,000,000 multiplications." | "t squarings" and "2^t ≥ N − 1" are given without a derivation (log2 99 is about 6.6, so 7). The "BFS reads each row once... N² = 10,000" claim is derived with no argument. The conclusion "useful because its answer is a clean statement ..., not because it is fast" is an opinion. | Show the arithmetic in one line, or say these are illustrative estimates.

F32 | comprehension | 7.3: "As written, Theorem 1 is false for any definition of path that forbids repeated vertices or repeated edges... so their explanation is wrong although their statements of the test are correct." | The reader is told that published sources are wrong. The only evidence given is Proposition 3.11, and the sources are not quoted. The reader has to take the claim about [7] and [1] on faith. | Quote the sentence from [7] in the body, or soften to "as we read it".

F33 | comprehension | Sections 1.3, 7.1, 7.5: repeated statements ("the rest of the book was not read page by page", "qualified") at three places, plus Appendix B. | The same caveat is repeated at least four times, which hides the main results. The reader needs it once, in 1.4. | State it once in 1.4 and refer to it.

F34 | comprehension | Section 7.5, "Open: whether the lecturer's intended answer to the board's question 2 was the sum test, the (I+A)^(N−1) test, or BFS... Only the user can settle these." | "The user" is not a reader of a paper. The sentence addresses the person who gave the task, so the paper's frame (study note versus a reply to a request) is unclear. | Replace "Only the user can settle these" with "These can be settled only by the lecturer".

F35 | comprehension | Appendix D: "The scripts are copies of the ones in the folder modules/, which are kept as the module records." | The reader has no access to "modules/" or "figures/generated_numbers.tex" and cannot tell whether the scripts are shipped with the paper. The text also names script names (m1_walks.py and so on) throughout the body. | State where the scripts can be obtained, or remove the internal folder names from the paper.

F36 | comprehension | Section 5 (Q3), whole section. | Section 5 repeats Definition 2.31 almost word for word. After the long treatment in Section 2, I could not say what Section 5 adds beyond the endpoint notation and the claim that both readings of "path" agree. | Fold Section 5 into Section 2.3, or state at its head that it only restates Definition 2.31 for the question Q3.

F37 | comprehension | Whole paper, structure. | The paper is 31 pages for three short questions. The answers appear in the abstract and Section 1.3, but the main chain of reasoning (walk counting, then walk-to-path, then the test) is spread over Sections 2 to 4, with side topics (cycles, metric space, naming conventions, BFS, cost) in between. The reader cannot easily tell what is essential and what is context. | Add a "reading path" line in 1.5 listing the sections needed for the proofs (2.3, 2.7, 3.1-3.2, 4.1-4.4) and the optional ones.

READER SUMMARY
The paper starts from a lecture-board photograph that shows a small graph and its table of zeros and ones (the adjacency matrix A). It asks three things. First, what does entry (i,j) of the k-th power of A mean? Second, how can one tell from A alone whether the graph is connected? Third, what is a "path" between two vertices? Its answers are as follows. Entry (i,j) of A^k counts the walks of length k from vertex i to vertex j. A walk may revisit vertices and reuse edges, so the entry does not count paths. It is proved by induction on k, by sorting walks by their second-last vertex. A graph with at least two vertices is connected exactly when every off-diagonal entry of A + A² + … + A^(N−1) is positive. The same holds when (I + A)^(N−1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path, and that a path on N vertices has at most N−1 edges. So longer walks add nothing, and stopping at N−2 can fail, as the four-house row shows. A path is defined as a walk with no repeated vertex. The paper notes that its textbook calls this a "simple path" and uses "path" for a walk with no repeated edge (which the paper calls a "trail"). It also notes that the board's drawing and matrix disagree, and that the mark above A on the board is read as an exponent k. The results are checked by script against breadth-first search on all graphs with up to six vertices. The paper says the matrix test is neat but not fast, compared with breadth-first search. I can state this, but I cannot say why the study note needed 31 pages, or which parts the main argument needs and which are context.

# Evaluation report

## evaluation-report.md

# Evaluation report

## Round 1, 2026-10-31

Question: For a simple undirected graph with N vertices given by its
adjacency matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how
can one determine from A whether the graph is connected, and (3) what is
the definition of a path between vertices n_i and n_j? (from `brief.md`)

Scope: Finite simple undirected graphs; walks, trails, paths, cycles and
distance; connectivity and components; the matrix-power connectivity test
in both forms (sum of powers and (I + A)^(N-1)) with full proofs; a
breadth-first search alternative stated for comparison; worked examples on
the three-vertex board graph, a disconnected three-vertex graph, and the
four-vertex path. Study-note register with the textbook standard and the
plain words layer. Directed graphs, multigraphs, weighted graphs,
eigenvalue methods, and implementation code are out of scope.

Research summary: 11 sources in `evidence/evidence.json` (the course
textbook as a local file, two whiteboard photos, one preprint, one
peer-reviewed article, five web sources, one lecture-slide set); 77
claims (70 supported, 7 qualified, 0 unverified). Three modules (m1
adjacency matrix and walk counting, m2 walks, trails, paths, cycles, m3
connectivity from the adjacency matrix). Research and modules were final
inputs for this run (one round of research, round 0). This probe is the
author stage only: one draft, one evaluation round, no revision.

Model levels: research 2, modules 2, author 2, reader 2, evaluator 3,
orchestrator session model (configured claude-fable-5-1, level 4).
Hierarchy requirement: met (evaluator level 3 exceeds author and module
level 2). Levels are configured levels taken from `model-levels.md`; a
runtime fallback is not observable from inside the session and none was
reported by the harness for the evaluator.

Mechanical checks (run by the orchestrator after the author returned):
build pass (exit 0, 1 overfull box of 0.36 pt), citations pass (11 cited
keys, 11 bib entries, 11 evidence sources, 0 errors), claims pass (70
supported, 7 qualified, 0 unverified, 0 errors), pdf pass (31 pages, 0
errors, 1 warning), evidence rebuild pass (0 differences), self-evaluation
pass (13 inputs covered, 0 errors). The gate passed on the first run; no
failure was sent back to the author.

### Scores

| Dimension | Score | Observation |
|---|---|---|
| 1 Correctness | 5 | Evaluator recomputed every number by script (board powers A to A^5, S, (I+A)^2, disconnected matrices, P4 matrices, Tables 4 and 5, case counts 40/360/5120/76800, cost figures, largest entry of A^9 for K10) and all match. Proofs of Theorem 3.5, Lemma 2.45, Propositions 4.13 and 4.14, Theorem 4.15 valid step by step. |
| 2 Evidence coverage | 4 | All 77 claims cover every cited statement with matching quotes. Exception: Definition 2.9 (`sections/background.tex:69-71`) cites a Quinlan remark for degree and says the textbook definition was not read, although the textbook has Definition 1.2.1 on printed p. 16. |
| 3 Citation integrity | 4 | Eight sources checked (seven fetched or read locally plus both board photos); all support the attributed statements. `sections/introduction.tex:67` calls the peer-reviewed article [7] a "web source". |
| 4 Logical validity | 5 | Every conclusion follows; the walk-to-path step skipped by the sources is supplied by Lemma 2.45; the trail and path readings of "connected" are shown to agree; i = j and N = 1 handled in Remark 4.21. |
| 5 Understandability | 4 | Plain-words layer applied almost everywhere. Unexplained: "metric space" (`background.tex:413`), "reflexive, symmetric and transitive" (`answer2_connectivity.tex:55`), "queue" (`answer2_connectivity.tex:293`), "adjacency lists" (`discussion.tex:49`), binomial coefficient at `example.tex:89` before Appendix A.4. |
| 6 Completeness | 4 | Every brief objective met. Gaps: textbook number for degree missing (`background.tex:71`); Table 3 lacks the "course" column the text at `background.tex:366` announces. |
| 7 Methodological rigor | 5 | Every claim tagged as cited, derived, interpretation or open; script checks presented as tests, not proofs (Sections 6.5, 7.1); integer arithmetic assumption stated. |
| 8 Critical analysis | 5 | Section 7.3 explains the source that says "paths" for walks; drawing-versus-matrix mismatch and the mark above A reported (Sections 1.1, 1.4, 7.5); cost discussed in 7.4; textbook absence claim qualified and independently confirmed by the evaluator. |
| 9 Internal consistency | 4 | Terms and notation consistent. Table 3 header "This paper" against the text's "course"; [7] called "web source" in the introduction but "published note" in Sections 4.4 and 7.3. |
| 10 Reproducibility | 5 | Appendix D names a script and saved output for every number; `figures/generated_numbers.tex` agrees with the evaluator's independent computation. |
| 11 LaTeX and PDF quality | 4 | 31 pages, references resolve, matrices render (page 22 checked as image). One overfull hbox of 0.36 pt at Example 2.29. |
| 12 Answer relevance | 5 | Sections 3.5, 4.8, 5 and the Conclusion answer Q1, Q2 and Q3 directly; nothing outside the brief is claimed. |

### Findings

Evaluator findings (full text in `reports/paper-evaluator-round1.md`).
This probe is a single author-stage round with no revision, so every
finding stays open and is documented here with that reason. None is
critical or major.

| Id | Severity | Location | Defect | Status |
|---|---|---|---|---|
| F1 | minor | `sections/background.tex:69-71` (Definition 2.9) | Degree cited to a Quinlan remark and marked "not read" in the textbook, although the textbook defines it as Definition 1.2.1 on printed p. 16; misses the brief's rule to cite textbook numbers. | documented: open, no revision in this probe |
| F2 | minor | `sections/introduction.tex:67` | Peer-reviewed article [7] described as "One web source". | documented: open, no revision in this probe |
| F3 | minor | `sections/background.tex:366-375` (Table 3) | Text announces course, textbook and English columns; table has Textbook, English, This paper. | documented: open, no revision in this probe |
| F4 | minor | `sections/answer2_connectivity.tex:204` (Corollary 4.19) | No plain-words paragraph before the corollary, against the study-note rule. | documented: open, no revision in this probe |
| F5 | minor | `sections/background.tex:413` | "metric space" unexplained. | documented: open, no revision in this probe |
| F6 | minor | `sections/answer2_connectivity.tex:55` | "reflexive, symmetric and transitive" unexplained. | documented: open, no revision in this probe |
| F7 | minor | `sections/answer2_connectivity.tex:293`; `sections/discussion.tex:49` | "queue" and "adjacency lists" unexplained. | documented: open, no revision in this probe |
| F8 | minor | `sections/example.tex:89` | Binomial coefficient and expansion of (I+A)^2 used before Appendix A.4 explains them. | documented: open, no revision in this probe |
| F9 | minor | Example 2.29 (`sections/background.tex`; `build/main.log:828`) | Overfull hbox of 0.36 pt. | documented: open, no revision in this probe |

Technician reader: 37 comprehension findings, recorded verbatim in
`reader-findings.md` under Round 1 and in
`reports/technician-reader-round1.md`. The reader's summary paragraph
states the three questions and the paper's answers correctly (walk count,
sum-of-powers test with the (I + A)^(N-1) form, path as a walk with no
repeated vertex, the board mismatch and the mark above A); it matches the
paper's actual conclusion, so no major finding arises from it. The
reader's recurring points are that the 31-page length hides which sections
the main argument needs (its F12, F33, F36, F37), that several terms are
used before explanation (F13, F15, F19, F27, overlapping evaluator F5 to
F8), and that some reported counts are not explained (F17, F30). These are
advisory for the next revision round and are left open for the same
reason as the evaluator findings.

### Citation and claim coverage

Sources: 11 (1 local-file textbook with partial access, 2 local
whiteboard photos, 1 preprint with partial access, 1 peer-reviewed article,
5 web sources, 1 lecture-slide set with partial access). Claims: 70
supported, 7 qualified, 0 unverified, 0 removed. Evaluator spot checks: 8
source records checked (quinlan_matrices_graphs, paramadevan2021adjacency,
bai2025adjacency, weisstein_connectedgraph, grinberg2025graph,
schost2026bfs fetched; petrosyan2015grafneri and the two whiteboard photos
read locally), all "supports".

### Unverified claims and access limits

- No unverified claims in the text.
- Qualified claims, each disclosed in the text: C24 and m2-8 (course
  meaning of "path", from the assignment text, which is not a file);
  C29 and m1-9 (the mark above A read as the exponent k); m2-15 (walks of
  length 0 allowed, a reading of the textbook); C36 (the (I + A)^(N-1)
  form, whose only source has a proof sketch and was accessed partially);
  m3-11 (the textbook states neither theorem in the pages checked;
  confirmed by the evaluator with a full-text search).
- Access limits: the textbook (petrosyan2015grafneri), the Grinberg
  preprint, and the Schost slides are recorded as partial access; the
  Bai page as partial access. The textbook's PDF text layer drops most
  symbols, so formulas were read from page images.
- Author's own list of what it could not fully justify (from
  `reports/paper-author-round1.md`): the textbook's degree definition and
  the number of its adjacency-matrix definition were not recorded (now
  evaluator F1); the seven edges of textbook Fig. 1.2.5 are the module's
  reading; some printed counts come from the module scripts rather than
  the author script; bibliography years are "n.d." where the evidence has
  none; Armenian text is given in English gloss and transliteration.

### Known limitations

- Single round: no revision was made and the evaluator's minor findings
  and the reader's comprehension findings are not resolved.
- The evaluator did not run `build.sh` itself (it writes build files)
  and did not observe release condition 9; the orchestrator ran both
  checks and they pass.
- The paper is 31 pages for a three-question study note; the reader could
  not tell which sections carry the main argument.
- Armenian textbook text is not reproduced in the PDF.

Decision: PASS -- Every dimension scores at least 4, there is no critical
or major finding, all seven qualified claims are qualified in the text,
the hierarchy requirement is met, every mechanical check passes, the self
evaluation covers all 13 input files, and the independent evaluation
recommends PASS. The nine minor findings are documented above as open
because this probe is one round with no revision; they should be fixed in
the next revision before any further release.

# Reader findings

## reader-findings.md

# Reader findings

## Round 1, 2026-10-31

Technician reader findings for the draft evaluated in round 1, verbatim from the agent.

FINDINGS

F1 | comprehension | Abstract: "Both theorems are proved in full, because the course textbook does not state them in the pages checked [9]." | The abstract names three questions but then says "both theorems" without saying which two they are. The abstract also uses "walk", "path", "vertex", "off the diagonal" and "(I + A)^(N−1)" with no gloss. "I" is not defined there. | Name the two theorems ("the walk-counting theorem and the connectivity test"). Add a half-sentence defining I as the identity matrix. | 

F2 | comprehension | 1.1: "the board puts a small mark above the letter A... a small n or a pair of quotation marks, not clearly a k [4, 5]." | The reader cannot see the photographs until Appendix C. Sections 1.1 and 1.4 describe the board's drawing in words ("an arrowhead at 2", "an edge 1–3 that the matrix lacks") with no figure. The reader must take these descriptions on faith for 25 pages. | Add a forward pointer ("see Figure 1, Appendix C") at the first mention, or move the figure into Section 1.1.

F3 | comprehension | 1.1 and 1.4: "The assignment text added a third question"; "the assignment states that in the course a path has no repeated vertex." | "The assignment", "the board" and "the course" are never introduced. The reader does not know who wrote the assignment, whether it is available, or why the paper depends on it. The "[4, 5]" citations point to photographs, but the assignment text has no citation at all. | Add one sentence at the start of 1.1 saying what the assignment is and that it is unavailable as a file. Alternatively cite it as a numbered source.

F4 | comprehension | 1.3: "both prove it loosely [7, 1]"; "(derived here)"; "(qualified)"; 1.4 "Kinds of statement". | The labels "derived", "interpretation", "qualified", "estimate" and "open" are defined only in the last paragraph of 1.4. The reader meets "qualified" in 1.1 and the abstract before then. "Qualified" is never defined precisely. It seems to mean "caveated", but this is a guess. | Define "qualified" in one sentence and move the "Kinds of statement" paragraph before first use, or add a forward reference.

F5 | comprehension | 1.2 and 1.4 (Table 1, "Definition 2.18", "Definition 2.31", "Definition 2.13"). | The roles of "plain words" paragraphs versus formal definitions are clear. However, the story fixes "trip" as the word for "walk" and "clean route" for "path", while the paper later says "trail". Trail has no entry in Table 1. The "In plain words" for trail says "Our textbook calls it a path", which clashes with the story's "clean route". | Add "trail" to Table 1 (for example "trip with no repeated road").

F6 | comprehension | 1.4: "The board writes (G, V) for the graph and eij ∈ V in its matrix definition, where its V is the edge set." | This is confusing. The reader has not yet seen what is on the board, and a vertex set V that is secretly the edge set is hard to follow. | Say "the board uses V for the edge set (probably a slip)" and move the details to Appendix C, keeping only the paper's own notation in the main text.

F7 | comprehension | 1.4 and 2.3: "The textbook's Fig. 1.2.5 shows a graph on five vertices... The textbook's own examples force the seven edges..." | The textbook graph is introduced inside a block of walk examples. The reader cannot see the figure and must trust the reconstruction from the edge list. The figure is never reproduced. | Draw the seven-edge textbook graph as a small figure, or list the edges as a labelled example (for example "Example 2.20a") before it is used.

F8 | comprehension | 2.1: "The textbook's own definition of degree was not read, so no textbook number is given." Also Definition 2.13, "The textbook's definition number for this matrix was not recorded." | This is bookkeeping about the author's process, not about the mathematics. It makes the reader wonder whether the definitions were checked. | Drop it from the body and keep it in Appendix B, or state it once in 1.4.

F9 | comprehension | Definition 2.18: "u0, e1, u1, ..., uk−1, ek, uk of vertices and edges with ei = ui−1 ui". | The notation ui−1ui for an edge is explained earlier (Table 2, "uv, eij"), but the symbol "ei" is introduced as an edge and is also the index in "eij" (the board's edge). The two uses of e look alike. | Say "the i-th edge ei joins ui−1 and ui".

F10 | comprehension | Remark 2.19: "The textbook does not say in so many words that k = 0 is allowed. This paper reads k = 0 as allowed, because the textbook's property d(u,u) = 0 of distance needs a path of length 0." | This is a long justification for a small convention. The reader cannot tell why it matters: the length-0 walk is needed only later (Lemma 2.45, Remark 4.2). | Add "needed in Lemma 2.45 and Remark 4.2" to say why the point is raised.

F11 | comprehension | 2.3, Remark 2.28: "In the board graph every trail is also a path... for every length from 0 to 4 ... (derived, checked by script for lengths up to 4)." | The reader is asked to take a claim for lengths 0 to 4 on trust. A short argument is available: the board graph is a path with 3 vertices and no cycle. The text then says the claim is "derived" yet only "checked by script". | Replace with one sentence of reasoning ("the board graph has no cycle, so no trail revisits a vertex"), or label it "checked" only.

F12 | comprehension | 2.4 (Cycles): "Cycles are not needed for the main results; they are given because the textbook's list of definitions includes them." | A full page of definitions, examples and non-examples (Definitions 2.36 and 2.37, Remark 2.38) is not used afterwards. The reader cannot tell whether to retain it. Likewise for Table 3 and the trail material, which is needed only for Remark 4.2. | Mark 2.4 as skippable at its start, or move it to an appendix.

F13 | comprehension | Definition 2.41 and the text after it: "The textbook's 'path' here is its Definition 1.2.12, a trail. The definition does not depend on whether one reads trail or path..." | The reader is told that "the pair (V,d) is a metric space" with no explanation of "metric space". Distance is used later only in Remark 4.20. | Delete the metric-space sentence or gloss it ("d behaves like an ordinary distance").

F14 | comprehension | Lemma 2.45 proof: "Form the sequence W′ = u0, ..., ui, uj+1, ..., uk; if j = k nothing follows ui." | This is the hardest step to follow and I had to read it three times. The index juggling hides the idea of cutting out the loop between ui and uj. The edge case j = k is stated inside a sentence about the sequence. The trace example appears only after the proof. | Add one sentence before the formal construction ("delete everything after the first ui up to and including uj, so the walk goes from ui straight on to uj+1"), or put the trace first.

F15 | comprehension | Definition 3.1: "(XY)ij = Σ_{r=1}^N Xir Yrj" and the following remark that "A^0 = I... corresponds to one walk of length 0". | The pdf text of the formula is garbled in my reading, but the intent is clear. A technician who has not met matrix products will rely on the "plain words". The identity matrix I appears in Table 2 and in the abstract without a display of an example. | Show I once for N = 3. Show one numeric row-times-column product before Theorem 3.5.

F16 | comprehension | Proof of Theorem 3.5: "Wk(i, j) is the sum over r = 1, ..., N of the number of walks of length k from ni to nj whose second-last vertex is nr. Fix r. We claim that the number in class r is Wk−1(i, r) · Arj." | The reader is not told in advance why the sum is organised by the second-last vertex. The proof is correct in form but long. The two bullet cases are clear. The "Why the argument is valid" paragraph then repeats it. | Open the proof with a roadmap sentence ("a walk of length k is a walk of length k−1 plus one final step; that final step is allowed exactly when Arj = 1").

F17 | comprehension | 3.2, end: "A computer check supports the theorem but is not a proof: ... all 40, 360, 5120 and 76800 tested cases of (k, i, j) agreed." | The numbers 40, 360, 5120 and 76800 are not explained. The reader cannot tell how they arise (A.5 says k runs to 4 for N ≤ 4 and to 3 for N = 5, so the count depends on k, N, and the graph count). | Give the formula, for example "graphs × N² pairs × values of k", or drop the counts.

F18 | comprehension | Proposition 3.11: "If ni has at least one neighbour, then (A²)ii = deg(ni) &gt; 0, but no path, and no trail, of length 2 from ni to ni exists." | "The first inequality" in the proof refers to "&gt; 0", but the statement has no inequality symbol sign besides "&gt;". The claim "no trail" is explained only by the edge being used twice, which is fine. The final sentence "Hence (A^k)ij is in general not the number of paths" does not follow from a single diagonal example unless one adds that k = 2 is a specific case. | Say "so the entry (A²)ii counts a walk that is not a path; hence the entries are not path counts".

F19 | comprehension | Definition 4.5 (Connected component): "On the vertex set V write u ∼ v if G has a (u, v)-path. This relation is reflexive, symmetric and transitive, so V splits into classes." | Reflexive, symmetric, transitive and "classes" (equivalence relation) are used without explanation. The claim that the relation has these properties is not shown. | State "equivalence relation" with a one-line gloss and a pointer to why transitivity holds (join two walks).

F20 | comprehension | Definition 4.9 (new notation S) and Remark 4.10. | S is defined as a sum of N−1 powers, but the reader does not see why N−1 is the right stopping point until Section 4.4. The "plain words" tell the reader to stop at "one step short" without a reason. | Add "(the reason is Corollary 2.46)" to the definition.

F21 | comprehension | Proposition 4.14: "(I + A)^m ij &gt; 0 if and only if Sij &gt; 0. Every diagonal entry of (I + A)^m is at least 1." | The purpose of this second form is never stated in the main text: why would one prefer (I + A)^(N−1)? The reason appears only in 7.4 (repeated squaring). Its proof is deferred to Appendix A.4 although it is a half-page argument. | At first mention, add one sentence on motivation ("it can be computed by repeated squaring, Section 7.4").

F22 | comprehension | Proposition 4.13, statement (i): "There is an (ni, nj)-path in G (in the sense of textbook Definition 2.1.1)." | The parenthetical is confusing. Definition 2.1.1 is about "connected", and the text calls the textbook "path" a trail. The reader does not know which meaning of "path" statement (i) uses. | Replace with "a path (Definition 2.31) from ni to nj" and refer to Remark 4.2 for the trail reading.

F23 | comprehension | Proof of Theorem 4.15: "Together with the diagonal entries, which are always positive by Proposition 4.14, this is (c)." | The step from positivity of off-diagonal entries of (I+A)^(N−1) to (b) uses Proposition 4.14 with Sij, and the diagonal remark is easy to miss. Statement (a) also requires u = v pairs, which the proof dismisses by Remark 4.2. The chain is correct but spread over four references. | Add a three-line outline of the proof: (a) iff each pair joined, (b) via Prop 4.13, (c) via Prop 4.14.

F24 | comprehension | Remark 4.21: "For N = 2 and one edge, S = A has zeros on the diagonal although the graph is connected. ... For N = 1 ... S is an empty sum." | This sits in a remark in the middle of the proof area and mixes three cases. The sentence "For N ≥ 3 and a connected graph the diagonal of S is positive anyway" is an unproved claim, said to be unneeded. | Split into short bullets, or cut the N ≥ 3 claim since the test does not need it.

F25 | comprehension | 4.6: "Enough: Proposition 4.13 shows that if a trip between two different vertices exists at all, a trip of length at most N − 1 exists... Not fewer: the next statement shows that N − 1 cannot be lowered." | The heading says "N − 2 are not", but the argument for "not fewer" is a single counterexample family. The text says "the next statement shows" but a "plain words" paragraph sits between. The term "trip" is used while the formal statement uses "walk". | Use "walk" in this paragraph, or state that the claim is shown by Proposition 4.23 for a path graph.

F26 | comprehension | Proposition 4.23 and Example 6.3. | The example prints A + A² as "(N − 2 powers)" with the (1,4) entry 0. The reader must locate the entry in a 4×4 matrix with no highlight. | Mark the (1,4) entry (for example boldface) and say "top-right entry".

F27 | comprehension | 4.7, Remark 4.24: "Its correctness statement in the source is that for every vertex v there is a walk from s to v if and only if v is discovered when the search ends [10]." | BFS, "queue" and "discovered" are used before being defined. The plain-words version helps. The claim "agree on all 32768 labelled graphs with 6 vertices" is taken on faith from a script. | State briefly that the BFS comparison is only a sanity check, with a pointer to Table 5.

F28 | comprehension | 6.1: "Also A³ = 2A and A^(k+2) = 2A^k for k = 1, ..., 5 (script)." | The reader is told this pattern without any reason or relevance to the questions. It does not return afterwards. | Delete it, or say why it matters (it shows that the entries grow).

F29 | comprehension | Table 4 (6.1). | The columns "trails" and "paths" are equal in every row, and the table includes k = 0 with a "closed walks" count of 3 but k = 1 with 0. The reader cannot tell what the table is meant to show. The caption does not say. The reported "walks" for k = 4 (12) is not tied to the matrix entries shown (the sum of A⁴ is 12). | Add one sentence on the point of the table ("walks multiply while paths stop at length 2"). State that the walk column equals the sum of the entries of A^k.

F30 | comprehension | Table 5: "wrong with N − 2 powers" column: 1, 3, 12, 60, 360. | The numbers are not explained. The text covers N = 3 (3 graphs) and N = 4 (12 graphs) only. The reader cannot check the 60 and 360, or see why they are the numbers of labelled graphs on which the shortened test fails. | State the rule (for example, the shortened test errs exactly on graphs of diameter N−1, that is, labelled paths, which number N!/2), or say that no pattern is claimed.

F31 | comprehension | 7.4: "Reaching A^(N−1) from A takes N − 2 products, so the matrix test costs about (N − 2)N³ multiplications: 98,000,000 for N = 100 ... t squarings, 7 for N = 100, costing 7,000,000 multiplications." | "t squarings" and "2^t ≥ N − 1" are given without a derivation (log2 99 is about 6.6, so 7). The "BFS reads each row once... N² = 10,000" claim is derived with no argument. The conclusion "useful because its answer is a clean statement ..., not because it is fast" is an opinion. | Show the arithmetic in one line, or say these are illustrative estimates.

F32 | comprehension | 7.3: "As written, Theorem 1 is false for any definition of path that forbids repeated vertices or repeated edges... so their explanation is wrong although their statements of the test are correct." | The reader is told that published sources are wrong. The only evidence given is Proposition 3.11, and the sources are not quoted. The reader has to take the claim about [7] and [1] on faith. | Quote the sentence from [7] in the body, or soften to "as we read it".

F33 | comprehension | Sections 1.3, 7.1, 7.5: repeated statements ("the rest of the book was not read page by page", "qualified") at three places, plus Appendix B. | The same caveat is repeated at least four times, which hides the main results. The reader needs it once, in 1.4. | State it once in 1.4 and refer to it.

F34 | comprehension | Section 7.5, "Open: whether the lecturer's intended answer to the board's question 2 was the sum test, the (I+A)^(N−1) test, or BFS... Only the user can settle these." | "The user" is not a reader of a paper. The sentence addresses the person who gave the task, so the paper's frame (study note versus a reply to a request) is unclear. | Replace "Only the user can settle these" with "These can be settled only by the lecturer".

F35 | comprehension | Appendix D: "The scripts are copies of the ones in the folder modules/, which are kept as the module records." | The reader has no access to "modules/" or "figures/generated_numbers.tex" and cannot tell whether the scripts are shipped with the paper. The text also names script names (m1_walks.py and so on) throughout the body. | State where the scripts can be obtained, or remove the internal folder names from the paper.

F36 | comprehension | Section 5 (Q3), whole section. | Section 5 repeats Definition 2.31 almost word for word. After the long treatment in Section 2, I could not say what Section 5 adds beyond the endpoint notation and the claim that both readings of "path" agree. | Fold Section 5 into Section 2.3, or state at its head that it only restates Definition 2.31 for the question Q3.

F37 | comprehension | Whole paper, structure. | The paper is 31 pages for three short questions. The answers appear in the abstract and Section 1.3, but the main chain of reasoning (walk counting, then walk-to-path, then the test) is spread over Sections 2 to 4, with side topics (cycles, metric space, naming conventions, BFS, cost) in between. The reader cannot easily tell what is essential and what is context. | Add a "reading path" line in 1.5 listing the sections needed for the proofs (2.3, 2.7, 3.1-3.2, 4.1-4.4) and the optional ones.

READER SUMMARY
The paper starts from a lecture-board photograph that shows a small graph and its table of zeros and ones (the adjacency matrix A). It asks three things. First, what does entry (i,j) of the k-th power of A mean? Second, how can one tell from A alone whether the graph is connected? Third, what is a "path" between two vertices? Its answers are as follows. Entry (i,j) of A^k counts the walks of length k from vertex i to vertex j. A walk may revisit vertices and reuse edges, so the entry does not count paths. It is proved by induction on k, by sorting walks by their second-last vertex. A graph with at least two vertices is connected exactly when every off-diagonal entry of A + A² + … + A^(N−1) is positive. The same holds when (I + A)^(N−1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path, and that a path on N vertices has at most N−1 edges. So longer walks add nothing, and stopping at N−2 can fail, as the four-house row shows. A path is defined as a walk with no repeated vertex. The paper notes that its textbook calls this a "simple path" and uses "path" for a walk with no repeated edge (which the paper calls a "trail"). It also notes that the board's drawing and matrix disagree, and that the mark above A on the board is read as an exponent k. The results are checked by script against breadth-first search on all graphs with up to six vertices. The paper says the matrix test is neat but not fast, compared with breadth-first search. I can state this, but I cannot say why the study note needed 31 pages, or which parts the main argument needs and which are context.

# Author self-evaluation

## self-evaluation.md

# Self evaluation: Walks, Paths and Connectivity from the Adjacency Matrix

Author notes. All 77 evidence claims were left unchanged in content (only derivation locators in the base and module fragments were updated to the real section, table and label numbers, and the merged file was rebuilt with `merge_evidence.py`). No claim was added, so `evidence/modules/author.json` does not exist. Unverified claims in the text: none (0 in the evidence file). Qualified claims used and disclosed in the text: C24, C29, m1-9, m2-8, m2-15, C36, m3-11. Every number in the paper is produced by a script in `appendices/scripts/`.

## sections/introduction.tex: Introduction

Purpose: state the three questions and where each came from, fix the village story, preview the answers, fix assumptions, notation and the kinds of statement, and give the organization.

Claims and support:
- The board states the problem, question 1 and question 2 and a definition of connected: C25, C27 (whiteboard1, whiteboard2).
- The mark above A is not clearly k; reading it as k is an interpretation: C29, m1-9 (qualified).
- Q3 comes from the assignment text, not from the board: brief section 1; no evidence claim, so stated as the assignment's, not cited.
- Board notation (G,V), e_ij in V, |G| = N, n_i against the textbook's G = (V,E), v_i: C25, C26.
- Drawing shows 1-2 with arrowhead, 1-3, 2-3; matrix encodes only 1-2 and 2-3; the matrix is the example: C28.
- Textbook graphs are finite, simple, undirected: C1.
- Textbook "path" (1.2.12) allows repeated vertices, "simple path" (1.2.13) does not; English texts differ: C15, C16, C21, C23; course reading from assignment text: C24 (qualified).
- Walk-counting statement in standard notes: C6; the web note that says "paths": C11; test statements in a note and lecture notes with loose proofs: C34, C36, m3-12.
- Textbook has no walk-counting theorem and no matrix test in the pages read; full-book search found none; qualified: m3-11.

Conclusions and premises: "both results are proved here" follows from m3-11 (absence in the textbook, qualified) and C34/C36/m3-12 (sources prove loosely).

Not justified: the statement that the course meaning of "path" is "no repeated vertex" rests on the assignment text only (C24, qualified), as the paper says.

## sections/background.tex: Background: graphs, walks, and paths

Purpose: textbook-order prerequisites (graph, adjacent, degree, adjacency matrix, walk, closed walk, trail, path, cycle, simple cycle, naming table, distance, walk-contains-path lemma, length bound), each with plain words, remark, example, non-example.

Claims and support:
- Definition of graph, adjacent, adjacency matrix and its properties 1-3, 6: C1, C2, C3, C4. Row sums equal degrees and sum of entries 2|E|: m1-1 (derived; source with loops C5). Board writes the matrix rule with e_ij in V: C26.
- Walk, length, repeats allowed: C12, C13. Walk is its vertex list: m1-2 (derived). Length 0 allowed: m2-15 (qualified; textbook property d(u,u) = 0 from m2-4, Grinberg example in m2-5).
- Textbook examples for walk, trail, path, simple cycle: m2-1, m2-2. Closed walk: C14. Trail: C15, C21. Path: C16, C21. Distinct vertices give distinct edges: m2-10 (derived; Grinberg exercise in m2-5). Cycle and simple cycle: C17, C22. Board graph has no cycle, trails equal paths in it, triangle has a simple cycle: m2-14 (script). Naming table: m2-7, C23. Distance and its three properties: C18, m2-4; shortest walk = shortest trail = shortest path: m2-12; properties from definition: m2-16.
- Lemma (walk contains path, any u, v, length bound): C19, C20, m2-3, m2-9 (derived). Path has at most N - 1 edges: C33, m2-6, m2-11 (derived). Board distances and counts: m2-13.

Conclusions and premises: Lemma follows by strong induction on the length (premise: the cut construction is a walk, checked in the proof); the length bound follows from k + 1 distinct vertices among N.

Not justified or qualified: degree (Definition on degree) has no textbook number because the textbook's own definition of degree was not read; it is cited to the lecture-note remark (C9 quote). The seven textbook-graph edges are the ones the textbook's own examples force (m2-1, m2-2); this reading is the module's, not a separate claim. "A figure eight is a cycle" is marked derived from Definition 1.2.14 and has no evidence claim of its own. The statements about renumbering vertices permuting rows and columns, and that a closed walk of length 2 must reuse an edge, are elementary and marked derived or unmarked remarks without separate claims.

## sections/answer1_walks.tex: Q1: what the entry of a power of A counts

Purpose: define matrix product and power, state and prove the walk-counting theorem by induction, give consequences, and show that the entry counts walks and not paths.

Claims and support:
- Theorem: C6 (Quinlan Thm 1.1.3, Grinberg Thm 4.5.10, Lehman Cor 9.3.3, Bai Thm 1); proof route C7; the proof as written: m1-3 (derived); finite check m1-4.
- Where hypotheses are used (simplicity twice, undirectedness only for symmetry, multigraph version): m1-8 (interpretation).
- Corollary (non-negative integers, positivity means a walk, symmetry): m1-7 (derived).
- (A^2)_ii = degree and trace 2|E|: C9, derived here.
- Walks are not paths, under both textbook readings: C8, C10, m1-6 (derived); board numbers 1,0,2,0,4 walks and 1,0,0,0,0 paths: m1-6 and `author_numbers.py`.
- A^0 = I convention: C7 (Grinberg).

Conclusions and premises: Q1 answer follows from Theorem (induction: base k = 1 from Definition of A; step from the partition by second-last vertex and the bijection when A_rj = 1). Warning follows from the diagonal proposition and from "a path from n_i to n_i is the single vertex".

Not justified: nothing beyond the textbook gap (m3-11, qualified).

## sections/answer2_connectivity.tex: Q2: deciding connectivity from the matrix

Purpose: define connected, components, S, prove the test and its second form, state it as a procedure, show N - 1 is sharp, and give BFS.

Claims and support:
- Definition of connected, board's version: C30, C25. Walk or path give the same connectivity: C32 and derived Remark.
- Components, Remark 2.1.1: C31, m3-1. Textbook examples: m3-2.
- Test statement: C34 (Paramadevan Thm 2, MathWorld); second form: C36 (qualified, Bai); proofs of both: C35, C37 (derived), m3-3, m3-5, m3-9; loose proofs in sources: m3-12.
- Path has at most N - 1 edges: C33. N - 1 cannot be lowered: m3-4 (derived, script). Edge cases N = 1, 2 and diagonal of S: m3-3. Components from S: m3-5. Distance as smallest k: C38 (derived with m2-12).
- BFS decides connectivity, correctness statement: C39, m3-13; agreement with matrix test on all graphs up to 6 vertices: m3-8 (check, not proof).

Conclusions and premises: Theorem follows from Proposition (one pair at a time) and Proposition (I + A form). Proposition one pair: premises Walk counting (C6), Lemma (m2-9), Corollary (m2-11), path implies trail (m2-10), non-negative counts (m1-7). I + A form: binomial expansion with positive coefficients (C37, m3-9).

Not justified: the textbook does not state the test (m3-11, qualified). The proof of the I + A form is in the appendix.

## sections/answer3_path.tex: Q3: the definition of a path between n_i and n_j

Purpose: give the definition of a path between n_i and n_j under the course convention and show that the existence statement is the same under the textbook's other reading.

Claims and support: Definition and its identity with textbook Definition 1.2.13: C16, C24, m2-8 (qualified; the course reading comes from the assignment text and the board does not say). One path between n_1 and n_3 in the board graph: m2-13. Same truth value under both readings: m2-9, m2-10, C32 (derived). Counts differ by reading: C10, m1-6.

Conclusion and premises: Q3 answer is the definition itself. Qualification: the course reading of "path" is not in any file.

Not justified: nothing beyond the qualification above.

## sections/example.tex: Worked examples

Purpose: write out every matrix for the board graph, the connected and disconnected examples, the four-vertex path, and the exhaustive check.

Claims and support: board matrix, A^2 to A^5, A^3 = 2A, row sums, walk lists, hand sums: m1-5, m1-1. Walk, trail, path counts by length: m2-13 (script `m2_walks.py`). Connected example numbers: m3-6. Disconnected example numbers: m3-7. Four-vertex path matrices and N - 2 failure: m3-4. Exhaustive check table, failures with N - 2 powers (3 of 8, 12 of 64, 60, 360, 1 for N = 2): m3-8, m3-4. Drawing against matrix: C28. The matrices printed in the paper are generated by `appendices/scripts/author_numbers.py` and input from `figures/generated_numbers.tex`; assertions there compare each power with a direct walk enumeration.

Conclusions and premises: each reading follows from Theorem (test) and the printed matrices.

Not justified: the exhaustive table's "wrong with N - 2 powers" column is from the module script (checked: copy output is identical), not recomputed by `author_numbers.py`.

## sections/discussion.tex: Discussion: limits, disagreements, and cost

Purpose: separate proof from computer check, list convention choices, record where sources disagree, give the cost estimate, and list limits and open questions.

Claims and support: sources for walk counting: C6; lemma combination: C19, C20; conventions: C15, C16, C17, C22, C24, m2-15; mark above A: C29, m1-9; drawing: C28; Paramadevan Theorem 1 wrong as written: C11, C10; loose proofs: m3-12; cost counts (98,000,000 and 7,000,000 for N = 100; N^2 = 10,000; 38,742,049): m3-10 (estimate; script); BFS O(n + m) with adjacency lists: C39, m3-13; textbook absence: m3-11; multigraph interpretation: m1-8.

Conclusions and premises: "the matrix test is useful for its clean statement, not speed" is an interpretation resting on m3-10's counts. Repeated squaring is justified by m3-9.

Not justified: none unsupported. Faster matrix multiplication was not examined, and the text says so. C39's wording "N - 1 matrix products" disagrees with the count N - 2 in m3-10; the paper uses N - 2 and says the slides do not make the comparison.

## sections/conclusion.tex: Conclusion

Purpose: direct answers to Q1, Q2, Q3 and what stays open.

Claims and support: Q1: C6, m1-3, C8, m1-6. Q2: C34, C35, C37, m3-4, C39. Q3: C16, C24, m2-8. Open items: C28, C29, m3-11.

Conclusions and premises: each answer repeats the theorem or definition proved above.

Not justified: nothing new.

## appendices/derivations.tex: Derivations and checks

Purpose: proofs of the distance properties (A.1), the counterexample table (A.2), the premise chain of the test (A.3), the I + A proof (A.4), and the finite cross-checks (A.5).

Claims and support: m2-12, m2-16 (A.1); C10, m1-6 (A.2); C35 and premises C6, C20, C33, C30 (A.3); C37, m3-9 (A.4); m1-4, m3-8, m3-4, and the m2 script checks m2-9 to m2-12 (A.5; numbers 73, 381, 4695 walks, 300 random graphs, 192696 walks are from `m2_walks_output.txt`).

Conclusions and premises: A.4 follows from the binomial expansion and positivity of coefficients; for m greater than N - 1 it uses the length bound.

Not justified: the random-test numbers in A.5 are quoted from the module script output, not independently recomputed.

## appendices/course-terms.tex: The textbook's terms and numbers

Purpose: table of textbook definition numbers and printed pages used.

Claims and support: C1, C2, C3, C4, C12 to C19, C30, C31, m3-1. The textbook's number for the adjacency matrix definition is not recorded; the table says so.

Conclusions and premises: none beyond the table.

Not justified: pages are the printed pages as recorded in the evidence file; this author did not re-read the book, because the evidence file is declared final.

## appendices/photographs.tex: The whiteboard photographs

Purpose: transcription of the board and the edge by edge comparison of drawing and matrix.

Claims and support: C25, C26, C27, C28, C29. The photographs are included as images; the transcription is taken from the evidence quotes (C27 words "it's" and "adj." as on the board).

Conclusions and premises: the arrowhead as a stray mark is an interpretation (brief assumption), labelled as such.

Not justified: reading of the mark above A (qualified, C29).

## appendices/reproducibility.tex: Reproducibility

Purpose: list the scripts that produced every number and how to run them.

Claims and support: scripts `author_numbers.py` (new), `m1_walks.py`, `m2_walks.py`, `m3_connectivity.py`. Outputs of the three module scripts were re-run in this session and are identical to the saved outputs.

Conclusions and premises: none.

Not justified: nothing.

# Module reports

## m1.md

# Module m1: Adjacency matrix and walk counting

Register: study-note. Evidence fragment: `evidence/modules/m1.json` (claims `m1-1` to `m1-9`; existing claims `C1` to `C11`, `C29` are reused by id). Computations: `modules/m1_walks.py`, output in `modules/m1_walks_output.txt`.

Labels used for kinds of statement: [fact] established and sourced; [derived] proved or computed here; [interpretation]; [open] not settled.

## 1. Purpose

This module answers board question 1: what does the entry (A^k)_ij of a power of the adjacency matrix represent. It establishes (i) the definition of the adjacency matrix A of a finite simple undirected graph and its basic properties; (ii) the theorem that (A^k)_ij is the number of walks of length k from n_i to n_j, with a complete induction proof; (iii) the warning that this counts walks, not paths, with explicit counterexamples; (iv) the board matrix as the running example, with A^2 and A^3 computed by script. It serves research question (1) directly, and supplies the theorem that module m3 uses to answer question (2).

## 2. Prerequisites

| Concept | Defined where |
|---|---|
| Finite set, sequence, sum with index r | assumed school mathematics |
| Matrix, entry, row, column, transpose | defined here at first use (Section 3.3) |
| Matrix product (XY)_ij = sum over r of X_ir Y_rj | defined here (Section 3.5) |
| Walk, length of a walk | one-sentence statement here (Definition 5); full treatment, including trail, path, cycle, and the naming conventions, in module m2 |
| Path between n_i and n_j (no repeated vertex) | module m2; used here only in the warning (Section 5.3) |
| Connected graph, connectivity test | module m3 |

## 3. Explanation from first principles

### 3.1 Notation and the story

Notation list. The graph is G with vertex set V = {n_1, ..., n_N} (the board's names; the textbook writes v_1, ..., v_n) and edge set E (the board writes V for the edge set; this is a notation difference only, C26). N is the number of vertices, |E| the number of edges. An edge between n_i and n_j is written n_i n_j or e_ij. A is the N by N adjacency matrix, A_ij its entry in row i and column j. k, r, i, j are positive-integer indices or exponents.

In plain words. Picture a small village. Each house is a point. Each road joins exactly two houses. Every road can be walked in both directions. No road leads from a house back to itself. No two roads join the same pair of houses. Everything below is about this village and about trips along its roads.

### 3.2 Graph, adjacency, degree

In plain words. A village has a list of houses and a list of roads. A road always joins two different houses. Two houses are neighbours if a road joins them directly. The number of roads at a house is how busy that house is.

**Definition 1 (simple undirected graph; textbook Section 1.1, Definition 1.1.1, C1).** A *simple undirected graph* is G = (V, E) where V is a finite nonempty set of *vertices* and E is a set of unordered pairs of distinct vertices, the *edges*.

*Remark.* The definition forbids a loop (an edge from a vertex to itself, because the pair must be of distinct elements) and a repeated edge (E is a set, so a pair occurs at most once). It forbids direction (the pair is unordered, so n_i n_j and n_j n_i are the same edge). It allows isolated vertices and any number of vertices that is finite.

*Example.* V = {n_1, n_2, n_3}, E = {n_1n_2, n_2n_3}: the board graph, a path of three houses in a row.

*Non-example.* V = {n_1, n_2}, with two roads both joining n_1 and n_2, or a road from n_1 to n_1. The first repeats an edge, the second is a loop; neither is simple.

**Definition 2 (adjacent; textbook Definition 1.1.4, C2).** Vertices u and v are *adjacent* if uv is in E. Then u is a *neighbour* of v.

*Remark.* Adjacency is symmetric (uv = vu) and no vertex is adjacent to itself, because there are no loops. It says nothing about longer connections.

*Example.* n_1 and n_2 are adjacent in the board graph.

*Non-example.* n_1 and n_3 are not adjacent in the board graph, although a two-road trip joins them.

**Definition 3 (degree).** The *degree* of a vertex n_i, written deg(n_i), is the number of edges that contain n_i. [The source for the word is the remark quoted in C9, "the number of edges at that vertex, or the vertex degree"; the textbook's own definition of degree was not read, so no textbook number is cited.]

*Remark.* In a simple graph the degree is also the number of neighbours, since each neighbour is joined by exactly one edge.

*Example.* In the board graph deg(n_1) = 1, deg(n_2) = 2, deg(n_3) = 1.

*Non-example.* deg(n_1) is not 2 although two other houses (n_2 and n_3) can be reached from n_1: only roads at n_1 count, and n_3 is reached by passing through n_2.

### 3.3 The adjacency matrix

In plain words. Make a square table with one row and one column for every house. Write a one where the row house and column house share a road. Write a zero everywhere else. This table is a complete description of the village.

A *matrix* is a rectangular table of numbers; A_ij is the number in row i and column j. The *transpose* swaps rows and columns.

**Definition 4 (adjacency matrix; textbook Section 1.1 after Definition 1.1.6, p. 11, C2; board: first line).** For a graph G with vertices n_1, ..., n_N, the *adjacency matrix* A is the N by N matrix with A_ij = 1 if n_i and n_j are adjacent and A_ij = 0 otherwise. (The textbook's definition number for A(G) was not recorded; its location is printed p. 11.)

*Remark.* The definition allows only the entries 0 and 1. It depends on the numbering of the vertices: renumbering permutes rows and columns together. The board writes the same rule as "A_ij = 1 if e_ij is in the edge set, 0 if not" (C26).

*Example.* The board matrix, rows (0 1 0), (1 0 1), (0 1 0), is the adjacency matrix of the graph in Definition 1's example: A_12 = A_21 = 1, A_23 = A_32 = 1, all else 0.

*Non-example.* The matrix with rows (0 1 0), (0 0 1), (0 1 0) is not the adjacency matrix of any simple undirected graph: A_12 = 1 but A_21 = 0 (it would need a one-way road). Neither is a matrix with a 1 on the diagonal (a loop) or an entry 2 (a double road).

In plain words. The table has some easy features. It looks the same when flipped over its diagonal. The diagonal holds only zeros. Adding a row counts the roads at that house.

**Proposition 1 (properties of A; textbook p. 11-12, C3, C4; row sums m1-1).** For the adjacency matrix A of a simple undirected graph:
1. every entry is 0 or 1;
2. A is symmetric: A_ij = A_ji for all i, j;
3. the diagonal is zero: A_ii = 0 for all i;
4. the sum of row i, and of column i, equals deg(n_i);
5. the sum of all entries equals 2|E|;
6. conversely, every N by N matrix of zeros and ones that is symmetric with zero diagonal is the adjacency matrix of some simple graph with numbered vertices.

*Proof.* [derived for 4 and 5; 1 to 3 and 6 are [fact] from the textbook, C3 and C4.] Items 1 to 3 are read off Definition 4 and Definition 2: adjacency is symmetric and irreflexive. For 4, the sum of row i is the number of j with A_ij = 1, that is, the number of neighbours of n_i. Each neighbour is joined to n_i by exactly one edge (no repeated edges) and no edge at n_i joins it to itself (no loops), so this number equals the number of edges at n_i, which is deg(n_i). Column i is the same by symmetry. For 5, add item 4 over all i: each edge n_i n_j contributes one to deg(n_i) and one to deg(n_j), hence is counted twice. For 6, join n_i and n_j exactly when the entry is 1; symmetry makes this a legitimate set of unordered pairs and the zero diagonal excludes loops. QED

Board matrix check (script): row sums 1, 2, 1; column sums 1, 2, 1; total 4 = 2|E| with |E| = 2.

### 3.4 Why row sums are the degrees (the idea in brief)

A one in row i marks one neighbour; counting ones counts neighbours; neighbours correspond one to one with roads. That is all item 4 says. The qualification "simple" is what makes "one neighbour = one road". Paramadevan and Sotheeswaran state it as "off diagonal entries plus twice the diagonal entries" because their matrices may have loops (C5); with a zero diagonal it reduces to the row sum.

### 3.5 Walks and matrix powers

In plain words. A walk is a trip along the roads. You start at a house and move to a neighbour, again and again. You may pass the same house twice. You may use the same road twice. The length of a trip is the number of roads you travelled.

**Definition 5 (walk; textbook Definition 1.2.10, C12; full treatment in module m2).** A *walk of length k from u_0 to u_k* is a sequence u_0, e_1, u_1, ..., u_{k-1}, e_k, u_k of vertices and edges with e_i = u_{i-1}u_i for 1 <= i <= k. (The textbook calls it "շրջանցում"; module m2 gives the naming table, the related definitions 1.2.11 to 1.2.16, and the course convention for "path".)

*Remark.* The definition allows repeated vertices and repeated edges (C13) and allows length 0 (a single vertex). It forbids jumps: consecutive vertices must be adjacent.

*Example.* In the board graph, 1-2-3-2 (that is, n_1, n_2, n_3, n_2) is a walk of length 3 from n_1 to n_2; it repeats n_2 and the edge n_2n_3.

*Non-example.* 1-3-2 is not a walk: n_1 and n_3 are not adjacent.

*Matrix power.* The *product* of two N by N matrices X and Y is the matrix XY with (XY)_ij = sum over r = 1..N of X_ir Y_rj, that is, row i of X times column j of Y entry by entry, then added. The powers are A^1 = A and A^k = A^{k-1} A for k >= 2. (Convention A^0 = identity matrix, one walk of length 0 from a vertex to itself, is used by Grinberg, C7; the board question concerns positive exponents, and this module treats k >= 1.)

### 3.6 Reduction: a walk is its list of houses

[derived, m1-2] In a simple graph there is at most one edge between two vertices, so the edge e_i = u_{i-1}u_i in Definition 5 is forced by the vertices u_{i-1} and u_i. Hence a walk of length k from n_i to n_j is the same thing as a sequence w_0, w_1, ..., w_k of vertices with w_0 = n_i, w_k = n_j and w_{t-1}, w_t adjacent for each t from 1 to k. Two walks are different exactly when these sequences differ at some position. The proof below counts such sequences. For a multigraph this step fails, which is one reason the hypothesis "simple" matters.

### 3.7 The walk-counting theorem

In plain words. Take the table of roads and multiply it by itself. Each number in the new table counts trips of two roads. The trips run from the row house to the column house. Multiply again and you count trips of three roads. The count includes trips that turn back. So the table counts trips, not clean routes.

**Theorem 1 (walk counting; C6; Quinlan Theorem 1.1.3; proof m1-3).** Let A be the adjacency matrix of a simple undirected graph G with vertices n_1, ..., n_N and let k >= 1 be an integer. Then (A^k)_ij is the number of walks of length k from n_i to n_j, for all i, j.

*Remark.* The theorem allows i = j (closed walks) and counts every walk once, with repeats of vertices and edges permitted. It forbids reading the number as a count of paths. The textbook (Petrosyan et al.) does not state this theorem (the brief records this), so it is proved here.

*Example.* For the board graph, (A^2)_13 = 1, the walk 1-2-3 (Section 5.2).

*Non-example.* (A^2)_12 = 0 does not say that n_1 and n_2 are unconnected. It says only that no walk of length exactly 2 joins them; walks of length 1 and of length 3 do exist.

*Proof* (by induction on k). Write W_k(i,j) for the number of walks of length k from n_i to n_j. We prove W_k(i,j) = (A^k)_ij for all i, j, for each k >= 1. By Section 3.6 we count vertex sequences.

*Base case k = 1.* A walk of length 1 from n_i to n_j is a sequence (w_0, w_1) = (n_i, n_j) with n_i, n_j adjacent. There is exactly one such sequence if n_i and n_j are adjacent and none otherwise. So W_1(i,j) = A_ij = (A^1)_ij.

*Induction hypothesis.* Let k >= 2 and suppose W_{k-1}(i,j) = (A^{k-1})_ij for all i, j.

*Inductive step.* Fix i and j. Every walk (w_0, ..., w_k) of length k from n_i to n_j has a vertex w_{k-1} just before the end; Because k >= 2, the walk w_0, ..., w_{k-1} that remains after deleting the last vertex still has length k-1 >= 1, so the hypothesis applies to it (for k = 1 the second-last vertex is n_i itself and nothing remains to count, which is why k = 1 is the separate base case). Let w_{k-1} = n_r, where r is one of 1..N. Sort the walks into N classes by the value of r. The classes are disjoint (each walk has exactly one second-last vertex) and together contain every walk, so
W_k(i,j) = sum over r = 1..N of (number of walks of length k from n_i to n_j whose second-last vertex is n_r).

Fix r. We claim the number in class r is W_{k-1}(i,r) * A_rj.
- If n_r and n_j are not adjacent (A_rj = 0), no walk can have n_r followed by n_j, so class r is empty: the count is 0 = W_{k-1}(i,r) * 0.
- If n_r and n_j are adjacent (A_rj = 1), delete the last vertex of a walk in class r. The remaining sequence w_0, ..., w_{k-1} has w_0 = n_i, w_{k-1} = n_r, consecutive vertices adjacent: it is a walk of length k-1 from n_i to n_r. Conversely, any walk of length k-1 from n_i to n_r followed by n_j is a sequence of length k+1 vertices whose consecutive pairs are adjacent (the new pair n_r, n_j is adjacent), so it is a walk of length k from n_i to n_j with second-last vertex n_r. Deleting and appending are inverse to each other, so they are a one-to-one matching, and the count is W_{k-1}(i,r) = W_{k-1}(i,r) * 1.

Therefore W_k(i,j) = sum over r of W_{k-1}(i,r) A_rj. By the induction hypothesis W_{k-1}(i,r) = (A^{k-1})_ir, so W_k(i,j) = sum over r of (A^{k-1})_ir A_rj, which is the (i,j) entry of the product A^{k-1} A = A^k by the definition of the matrix product and of powers. This proves the statement for k, and by induction for all k >= 1. QED

*Why the argument is valid.* The sum over the second-last vertex covers each walk exactly once, and the matching in the case A_rj = 1 is a bijection; these two facts are the only places where counting could go wrong. Simplicity is used twice: to identify a walk with its vertex sequence (Section 3.6), and so that A_rj, which is the number of edges between n_r and n_j, is 0 or 1 (m1-8). Undirectedness is not used in the induction; it only gives symmetry of A [interpretation, m1-8; the digraph versions in C6 agree].

### 3.8 Corollary

In plain words. A count is never negative and always a whole number. The table of trips stays the same when flipped over its diagonal. A positive number means at least one such trip exists.

**Corollary 1 (m1-7).** For a simple undirected graph and k >= 1: (a) every entry of A^k is a non-negative integer, and a sum of powers of A has a positive (i,j) entry iff some summand does; (b) (A^k)_ij > 0 iff there is a walk of length exactly k from n_i to n_j; (c) A^k is symmetric.

*Proof.* (a), (b): by Theorem 1 the entry is a count. (c): (A^k)^T = (A^T)^k = A^k since A is symmetric; alternatively, reversing the sequence of a walk matches walks from n_i to n_j with walks from n_j to n_i. QED

*Special case (C9, [fact]; derived here).* (A^2)_ii = deg(n_i): the walks of length 2 from n_i to n_i are n_i, n_r, n_i with n_r a neighbour, one for each neighbour. Hence trace(A^2) = sum of degrees = 2|E| (Proposition 1, item 5). On the board graph the diagonal of A^2 is (1, 2, 1), the degrees; trace 4 = 2|E|.

## 4. Evidence

| Statement | Claim id | What supports it |
|---|---|---|
| Graph is finite, simple, undirected (textbook) | C1 | Textbook Section 1.1, Definition 1.1.1; Quinlan Definition 1.1.1 |
| Definition of adjacent and of A | C2 | Textbook p. 11, Definition 1.1.4 and the definition of A(G); Quinlan Definition 1.1.2 |
| A symmetric, zero diagonal | C3 | Textbook p. 11 remark; Quinlan notes |
| Converse (symmetric, zero-diagonal 0/1 matrix is an adjacency matrix) | C4 | Textbook p. 12; Paramadevan property 9 |
| Row sum = degree; total = 2|E| | C5 (source, medium), m1-1 (proof) | Paramadevan property 8 states it with loops; proof written in Section 3.3, checked by script |
| Walk in a simple graph = vertex sequence | m1-2 | Textbook Definition 1.1.1 and Definition 1.2.10 (C12), Grinberg Definition 2.9.1(a); short derivation |
| Walk definition (Definition 5) | C12, C13 (module m2) | Textbook p. 21-22, Definition 1.2.10 and remark |
| Walk-counting theorem | C6 | Quinlan Theorem 1.1.3 (simple undirected), Grinberg Theorem 4.5.10, Lehman et al. Corollary 9.3.3, Bai Theorem 1 |
| Standard proof route | C7 | Quinlan proof; Grinberg Section 4.5.5 |
| The proof as written in this module | m1-3 | Derived here; matches the Quinlan route; finite cross-check m1-4 |
| Corollaries (a) to (c) | m1-7 | Derived from Theorem 1 |
| Where hypotheses are used | m1-8 | Interpretation; Grinberg and Lehman digraph versions |
| (A^2)_ii = degree | C9 | Quinlan remark after Theorem 1.1.3; derivation in Section 3.8 |
| Walks are not paths | C8 | Bai ("counts walks - not paths"), Grinberg Example 2.9.2 |
| Counterexample | C10, m1-6 | Definitions 1.2.12 and 1.2.13 (textbook), script enumeration |
| Board matrix, A^2, A^3, A^4, A^5 | m1-5 | Board (C28) for the matrix, script for the powers |
| Contradiction: Paramadevan Theorem 1 says "paths" | C11 | Not used for the proof; see Section 7 |
| Reading of the mark above A | C29 (qualified), m1-9 (qualified) | Both whiteboard photos; the user's text |

Status notes. C29 and m1-9 are qualified because the mark in the photos is not clearly k. Everything else listed is supported. Source access is partial for the textbook (pages 9-12, 21-23, 48-49 read), Grinberg, and Bai; the specific passages quoted were read.

## 5. Derivations, worked examples, reproducible calculations

### 5.1 The script

Path: `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/modules/m1_walks.py` (pure Python integers, no libraries). Run with `python3 -I papers/adjacency-walks-connectivity/modules/m1_walks.py` from the repository root. Full output is saved in `modules/m1_walks_output.txt`. The script defines matrix product and power, enumerates walks by depth-first search, tests whether a walk is a path (distinct vertices) or a trail (distinct edges), and compares with matrix powers.

### 5.2 Worked example: the board matrix

In plain words. We take the village from the board. It has three houses in a row. The first and last houses each have one road. The middle house has two roads. We count trips of two roads, then of three roads. We list every trip so the reader can see each count is right.

The graph: vertices n_1, n_2, n_3; edges n_1n_2 and n_2n_3 (path of three houses). The board drawing also shows a line from 1 to 3 and an arrowhead at 2 on the 1-2 line; the matrix has A_13 = 0 and is symmetric. Following the brief, the matrix defines the graph, and the mismatch is reported, not resolved (C28; assumption in brief Section 7). [m1-5]

Script output (verbatim):

```
A            A^2          A^3
0 1 0        1 0 1        0 2 0
1 0 1        0 2 0        2 0 2
0 1 0        1 0 1        0 2 0
```
Also by script: A^4 = rows (2 0 2), (0 4 0), (2 0 2); A^5 = rows (0 4 0), (4 0 4), (0 4 0); A^3 = 2A; A^(k+2) = 2 A^k for k = 1..5; trace(A^2) = 4 = 2|E|; diagonal of A^2 = (1, 2, 1) = degrees.

Explicit walks (script, vertex labels 1 to 3):
- Length 1: 1-2; 2-3 (and their reverses).
- Length 2: from 1 to 1: 1-2-1 (1 walk). From 1 to 3: 1-2-3 (1). From 2 to 2: 2-1-2 and 2-3-2 (2). From 3 to 3: 3-2-3 (1).
- Length 3: from 1 to 2: 1-2-1-2 and 1-2-3-2 (2). From 2 to 3: 2-1-2-3 and 2-3-2-3 (2).
Each count equals the corresponding matrix entry; the script asserts this for every entry of A, A^2, A^3.

Hand-checkable sums from the induction step (script output):
- (A^2)_22 = sum over r of A_2r A_r2 = 1*1 + 0*0 + 1*1 = 2.
- (A^3)_12 = sum over r of (A^2)_1r A_r2 = 1*1 + 0*0 + 1*1 = 2, where the term r = 1 is the length 2 walk 1-2-1 extended by the step to n_2 (giving 1-2-1-2), and the term r = 3 is the length 2 walk 1-2-3 extended by the step to n_2 (giving 1-2-3-2).
- (A^2)_11 = 0*0 + 1*1 + 0*0 = 1.

Brute-force cross-check [derived, m1-4; a finite check, not a proof]: for all labelled simple graphs on N = 2, 3, 4, 5 vertices (2, 8, 64, 1024 graphs) the walk enumeration equals the matrix entry in all 40, 360, 5120, and 76800 tested (k, i, j) cases (k up to 5 for N <= 4, up to 3 for N = 5).

### 5.3 The warning: walks are not paths

In plain words. A trip may turn back and visit the same house twice. A clean route never visits a house twice. The table counts trips, so it counts turn-back trips too. A house with one neighbour always has a two-road trip that goes out and returns.

[derived, m1-6; C8, C10] In the board graph:
- (A^2)_11 = 1 > 0, the walk 1-2-1. It goes along the edge n_1n_2 and back along it. It repeats the vertex n_1, so it is not a path in the course sense (textbook Definition 1.2.13, distinct vertices; English "path"). It repeats the edge n_1n_2, so it is not a path in textbook Definition 1.2.12 (distinct edges; English "trail") either. So under every convention there is no path from n_1 to n_1 counted by (A^2)_11, and (A^2)_11 > 0 shows the entry cannot be a count of paths.
- General case [derived, from C9]: whenever n_i has at least one neighbour, (A^2)_ii = deg(n_i) > 0.
- (A^3)_12 = 2: the walks 1-2-1-2 and 1-2-3-2. Neither is a path or a trail. Yet the only path from n_1 to n_2 has length 1, and the script finds, for k = 1, 2, 3, 4, 5, the numbers of walks from n_1 to n_2 as 1, 0, 2, 0, 4 and the numbers of paths among them as 1, 0, 0, 0, 0. So the entries grow with k (A^(k+2) = 2A^k) while the number of paths does not.
- What a positive entry does guarantee [derived from Theorem 1, and used by m3]: a walk of length k exists; module m2 proves that then a path of length at most k exists. The converse of the warning is therefore harmless for connectivity, but the entry value is not a path count.

Paramadevan and Sotheeswaran (2021), Theorem 1, says the entry equals the number of "different paths" (C11). Their own property 7 says walks. This module does not rely on their Theorem 1; the counterexample above shows it is false if "path" means distinct vertices or distinct edges.

## 6. Assumptions and their reasons

1. The graph is finite, simple, undirected: stated in the user's assignment, consistent with the symmetric zero-diagonal board matrix (brief Section 7).
2. The exponent is a positive integer k and the mark above A is k. The theorem holds for every positive integer exponent, so the answer does not depend on the letter (m1-9, qualified).
3. The board matrix defines the example graph, because the board says the graph is given through its adjacency matrix (brief Section 7). The drawing shows an extra line 1-3.
4. In this module "path" always means distinct vertices (course convention, Definition 1.2.13, C24 which is itself qualified); the textbook's Definition 1.2.12 object is called a trail here. Module m2 owns this table.
5. A^0 is not used. If the author wants it: the identity matrix, one walk of length 0 from a vertex to itself.
6. Vertices are named n_1, ..., n_N and written by index in the walk lists (1-2-3 means n_1, n_2, n_3).

## 7. Limitations, failure cases, competing explanations

- The proof covers simple graphs only. With loops or multiple edges A_rj may be greater than 1 or A_ii nonzero; the same proof then counts walks with multiplicity (m1-8, [interpretation]), but the properties in Proposition 1 items 1, 3 and 4 change.
- The walk count grows quickly; the theorem says nothing about the number of paths, which needs other methods. Not treated.
- The brute-force check is finite; it supports, but does not replace, the proof.
- Competing explanation 1: read the entry as the number of "paths" (Paramadevan and Sotheeswaran Theorem 1). Rejected by the counterexample in Section 5.3.
- Competing explanation 2: the mark above A is the number of vertices N rather than a power k. The theorem still describes (A^N)_ij, so nothing changes in the mathematics; the reading remains open for the board (C29).
- Under the textbook's own Definition 1.2.12 "path" (distinct edges), the statement "the entry counts paths" is also false (the walk 1-2-1-2 shows it for (A^3)_12), so the warning holds under both textbook readings.
- The textbook has no walk-counting theorem; there is no textbook number to cite for Theorem 1.

## 8. Dependencies and conflicts

- Depends on m2 for the full definition of walk. Section 3.5 states Definition 1.2.10 and nothing more. m2 must keep the sentence "a walk may repeat vertices and edges" (C13) and the naming table, so that this module's "trail" for Definition 1.2.12 and "path" for 1.2.13 match.
- m3 uses Theorem 1 and Corollary 1 (a), (b). The notation n_i, A, N, k is the shared one in the brief. The theorem and corollary labels here are "Theorem 1" and "Corollary 1" inside module m1; the orchestrator should renumber when merging into the paper so that they match the textbook-style numbering.
- Conflict recorded in the evidence file: C11 (Paramadevan Theorem 1) against C6 and C8. Resolved here as in the existing contradiction entry: walks, with the counterexample in Section 5.3.
- Terminology to reconcile: C6 and C7 write v_i; this module writes n_i (the board's names), as the brief requires.
- Two claim ids in the file say "to be written by m1" (C10 derivation `appendices/derivations.tex`, C7 proof): this module supplies the content as Theorem 1 and Section 5.3; the orchestrator should point the appendix to Sections 3.7 and 5.3.

## 9. Open questions

1. The mark above A on the board: k, n, or quotation marks (C29, qualified). Only the user can settle it; the mathematics does not depend on it.
2. The board drawing has three lines and an arrowhead; the matrix has two edges. Not settled; the paper follows the matrix.
3. The textbook's number for the definition of A(G) (printed p. 11, after Definition 1.1.6) and its definition of degree were not recorded in the evidence file, so Definitions 3 and 4 do not carry textbook numbers. A later read of printed pp. 9-12 could add them.
4. Whether the author wants A^0 and the k = 0 case included: not needed for the board question.

## m2.md

# Module m2: Walks, trails, paths, cycles, and the course convention

Register: study-note. Owner: module m2. Depends on: nothing. Used by: m1
(walk, length), m3 (path, Lemma L1, Corollary L2).

Labels used in this report for the kind of statement: **[fact]** (stated in
a source, with a claim id), **[derived]** (proved here), **[interpretation]**,
**[qualified]** (rests on something the sources do not settle). Items marked
D, L, P are numbered inside this module; the textbook's own numbers are given
beside them. All numbers in this report are printed by
`modules/m2_walks.py`; its full output is in
`modules/m2_walks_output.txt` and is quoted in Section 5.

## 1. Purpose

This module fixes the words that the other two modules use. It establishes:

1. the textbook's Definitions 1.2.10 to 1.2.16 (walk, closed walk, path,
   simple path, cycle, simple cycle, distance), each with its number and
   page, a remark, an example and a non-example;
2. one table of the three naming conventions (course, textbook, English);
3. the definition of "a path between n_i and n_j" under the course
   convention (answers question 3 of the brief);
4. the lemma that every walk from u to v contains a path from u to v
   (textbook Lemma 1.2.1 for u different from v; Grinberg Corollary 2.9.7
   for the general case), with a proof a beginner can follow;
5. the length of a walk, and distance.

Question served: question 3 directly; questions 1 and 2 indirectly, because
"walk" is the object that powers of A count (m1) and "path" is the object in
the definition of connected (m3).

## 2. Prerequisites

Everything is defined before use below. Nothing is owned by another module.

- **Graph, vertex, edge, simple, undirected.** Notation, taken from the brief
  (section 7), not a claim: a graph is G = (V, E). V is a finite set of
  vertices. E is a set of edges. Each edge is an unordered pair of two
  different vertices, written uv. Simple means: no loop (an edge from a
  vertex to itself) and no two edges with the same pair of ends. So an edge
  is determined by its two ends. The board writes (G, V) and e_ij in V for
  the textbook's G = (V, E) and e in E; this is a difference of notation
  only (claim C26). The board names the vertices n_1, ..., n_N; the textbook
  names them v_i. In this report the vertices of the three-vertex board
  graph are written 1, 2, 3, meaning n_1, n_2, n_3.
- **Sequence.** A list of vertices in a fixed order, repeats allowed. A
  sequence of k+1 vertices has k steps.
- **The board graph B.** Vertices 1, 2, 3. Edges 12 and 23. This is the graph
  of the board matrix with rows 0 1 0 / 1 0 1 / 0 1 0 (claim C28, brief
  section 7: the matrix is the example). Edge 13 does not exist in B.
- **The board drawing T.** The board drawing also shows a line from 1 to 3
  (claim C28). Graph T has vertices 1, 2, 3 and edges 12, 13, 23, a
  triangle. T is not the example graph. It is used only where a graph with a
  cycle is needed, and it is always labelled T.
- **The textbook graph G_tb.** The textbook's Fig. 1.2.5 has five vertices
  v1, ..., v5. The textbook's examples force at least these seven edges:
  v1v2, v1v3, v2v3, v2v4, v3v4, v3v5, v4v5. Only these seven edges are used
  here, so nothing depends on reading the rest of the figure. In the
  scripts this graph is called G.

## 3. Explanation from first principles

### 3.0 The story

One story, to be fixed in the introduction of the paper and reused by every
"In plain words" paragraph. Vertices are houses. Edges are straight roads,
each joining two different houses, and there is at most one road between
two houses. A trip is a list of houses you pass. The board graph B is three
houses in a row: house 1, house 2, house 3, with a road from 1 to 2 and a
road from 2 to 3 and no road from 1 to 3.

### 3.1 Walk and length

**In plain words.** A trip is a list of houses, one after another. Every
next house must be at the other end of a road from the house before. You may
pass the same house twice. You may use the same road twice. The length of a
trip is the number of roads you drove. If you drive a road twice, count it
twice. Staying at home is also a trip, and its length is zero.

**Definition D1 (textbook Definition 1.2.10, printed p. 21; claim C12).**
Let G = (V, E) be a graph. A *walk of length k from u_0 to u_k*, also called
a *(u_0, u_k)-walk*, is a sequence u_0, e_1, u_1, ..., u_{k-1}, e_k, u_k of
vertices and edges with e_i = u_{i-1}u_i for 1 <= i <= k. In a simple graph
the edges are determined by the vertices, so a walk is written by its
vertices alone, u_0, u_1, ..., u_k, where every two consecutive vertices
form an edge. The *length* of the walk is k, the number of edges, each edge
counted as many times as it occurs (claim C13; Grinberg Definition 2.9.1(b),
claim m2-5).

**Remark (what D1 allows and forbids).** A walk allows repeated vertices and
repeated edges (textbook, remark after 1.2.10, p. 22, claim C13). It forbids
only one thing: two consecutive vertices that are not joined by an edge.
Length counts steps, not different edges or different vertices. A walk with
k edges lists k+1 vertices. The textbook does not say in so many words that
k = 0 is allowed. This module reads k = 0 as allowed, for the reason in claim
m2-15 [qualified]: the textbook's own distance property d(u, u) = 0 (claim
m2-4) needs a (u, u)-path of length 0.

**Example.** In B the sequence 1, 2, 1, 2, 3 is a walk from n_1 to n_3 of
length 4: its steps 12, 21, 12, 23 are all edges. Vertices 1 and 2 each
occur twice, and edge 12 is used twice. (Script, section 1:
"(1, 2, 1, 2, 3) length 4 walk".)
The textbook's example (claim m2-1): v1, v3, v2, v4, v3, v2, v4, v3, v5 is a
walk of G_tb, of length 8.

**Non-example.** In B the sequence 1, 3 is not a walk, because 13 is not an
edge of B (the matrix has A_13 = 0). It would be a walk of T, the drawing.
The textbook's non-example (claim m2-1): v3, v1, v4, v2, v3, v5 is not a
walk of G_tb. (The step v1, v4 is the one that fails: the other steps are
edges forced by the textbook's other examples, so the textbook's statement
shows that v1v4 is not an edge.)

### 3.2 Closed walk

**In plain words.** A trip is closed when it ends at the house where it
began. That is the only new rule. The trip may still pass houses and roads
many times.

**Definition D2 (textbook Definition 1.2.11, printed p. 22; claim C14).** A
(u_0, u_k)-walk is *closed* if u_0 = u_k.

**Remark.** Allows everything D1 allows. Forbids only a different start and
end. A walk of length 0 is closed. A closed walk of length 1 cannot exist in
a simple graph (it would be a loop), and one of length 2 must use one edge
twice, namely u, w, u.

**Example.** In B the walk 2, 1, 2 is closed, of length 2. So is
2, 3, 2, 1, 2, of length 4.

**Non-example.** In B the walk 1, 2, 3 is not closed: it starts at 1 and
ends at 3.

### 3.3 Trail (the textbook calls this "path")

**In plain words.** Now add one rule. Never drive the same road twice. You
may still pass the same house twice, if you come back by a different road.
English books call such a trip a trail. Our textbook calls it a path. This
paper says trail, so the word path can keep one meaning.

**Definition D3 (textbook Definition 1.2.12, printed p. 22; claim C15).** A
(u_0, u_k)-walk is a *trail* if its edges u_0u_1, ..., u_{k-1}u_k are
pairwise distinct. The textbook calls it a *path* (Armenian: ճանապարհ) and
writes |P| for its length, the number of its edges. The textbook's wording
for D3 is "path"; this report writes "trail" for it, and "textbook path"
when it needs to point at the textbook's word.

**Remark.** D3 allows repeated vertices. It forbids repeated edges. In a
trail, a vertex can recur only if the trip left it by one road and came
back by another, so the trail passes round a loop of the graph.

**Example (textbook, claim m2-1).** In G_tb, v1, v3, v2, v4, v3, v5 is a
trail: its edges v1v3, v3v2, v2v4, v4v3, v3v5 are distinct, but vertex v3
occurs twice.

**Non-example (textbook, claim m2-1).** In G_tb, v1, v3, v2, v4, v3, v2,
v4, v3, v5 is a walk but not a trail: the edge v3v2 occurs twice. In B the
walk 1, 2, 1, 2, 3 is not a trail, since edge 12 occurs twice.

**What B cannot show.** In B every trail is also a path in the sense of D4
(script, section 1: trails = paths for every length 0 to 4). B has no
closed trail of positive length, so a trail cannot come back to a vertex.
To see a trail that is not a path, a graph with a cycle is needed; the
textbook's G_tb is used. This is an observation checked by script for
lengths up to 4, not a theorem used later.

### 3.4 Path (the textbook calls this "simple path"); the course convention

**In plain words.** Now add a stronger rule. Never visit the same house
twice. Then you also never drive the same road twice, because driving a road
twice means visiting a house twice. A trip like this is what our course
calls a path. It goes straight from start to end without any loop.

**Definition D4 (textbook Definition 1.2.13, printed p. 22; claim C16).** A
(u_0, u_k)-walk is a *path* if all its vertices u_0, ..., u_k are pairwise
distinct. The textbook calls this a *simple path* (Armenian: պարզ ճանապարհ)
and writes P_n for the simple path on n vertices. The textbook defines it as
a trail with distinct vertices; Proposition P1 below shows that distinct
vertices already give distinct edges, so the two ways of saying it agree.

**Course convention [interpretation, qualified; claim C24].** In the course
"path" means D4: no repeated vertices. This comes from the user's assignment
text recorded in the brief, not from a file; the textbook supplies the
definition under the name "simple path". The board does not say which
meaning of "path" it uses. This paper uses D4 for "path" everywhere.

**Remark.** D4 forbids repeated vertices and therefore repeated edges. It
allows length 0: a single vertex is a path from that vertex to itself. It
allows length 1: an edge. It does not allow closed paths of positive length,
because the first and last vertex would be equal.

**Example.** In B, 1, 2, 3 is a path from n_1 to n_3 of length 2 (script
section 1). The textbook's example (claim m2-2): v1, v3, v4, v5 is a simple
path in G_tb.

**Non-example.** In B, 1, 2, 3, 2 is a walk but not a path: vertex 2
occurs twice. In G_tb, v1, v3, v2, v4, v3, v5 is not a simple path (claim
m2-2): vertex v3 occurs twice, although it is a trail.

**Definition D4' (a path between n_i and n_j, course convention; answers
question 3 of the brief).** Let n_i and n_j be vertices of G. A *path
between n_i and n_j* is a walk w_0, w_1, ..., w_k with w_0 = n_i and
w_k = n_j in which w_0, w_1, ..., w_k are pairwise distinct vertices. That is
a simple path in the textbook's sense (1.2.13) and a path in English
usage. Its length is k. For i = j the only such path is the single vertex
n_i, of length 0. [interpretation, qualified, claim m2-8; the qualification
is the one on C24.]

**Example.** In B the paths between n_1 and n_3: exactly one, 1, 2, 3
(script section 1; every path has at most N - 1 = 2 edges by L2, so the
enumeration of walks up to length 4 finds them all). In B between n_1 and
n_1: only the path of length 0.

**Non-example.** In B, 1, 2, 1, 2, 3 is a walk between n_1 and n_3 but not a
path between them under D4'. It is not a trail either.

**Proposition P1 [derived, claim m2-10].** In a simple graph, a walk with
pairwise distinct vertices has pairwise distinct edges. So every path is a
trail.

*Proof.* Let u_0, ..., u_k have distinct vertices. Take two steps with
indices a < b (steps a and b are the edges u_{a-1}u_a and u_{b-1}u_b, for
1 <= a < b <= k). The vertex u_b has an index larger than a, and so it differs
from both u_a and u_{a-1}, whose indices are at most a. But u_b is an end of the
second edge, and it is not an end of the first. So the two edges are
different. This is Grinberg's Exercise 2.9, which he states and leaves as an
exercise (claim m2-5). ∎

### 3.5 Cycle (textbook) and simple cycle (English "cycle")

**In plain words.** A cycle is a closed trip that never drives the same road
twice. The textbook lets such a trip pass a house twice on the way. A simple
cycle is stricter. It passes no house twice, except the start, which is also
the end. A simple cycle is a ring of houses with a road between each
neighbour pair.

**Definition D5 (textbook Definition 1.2.14, printed p. 22; claim C17).** A
trail that is a closed walk is called a *closed path* or *cycle* (Armenian:
փակ ճանապարհ կամ ցիկլ). In words of this paper: a *cycle* is a closed trail,
a (u_0, u_k)-walk with u_0 = u_k and pairwise distinct edges. Vertices may
repeat.

**Definition D6 (textbook Definition 1.2.15, printed p. 22; claim C17).** A
cycle is *simple* if only its first and last vertices repeat. The textbook
writes C_n for the simple cycle on n vertices, n >= 3 (claim m2-2).

**Remark.** D5 allows repeated vertices (a figure eight is a cycle). It
forbids repeated edges and open walks. D6 forbids any repeated vertex other
than the closing one, and the condition n >= 3 forbids the degenerate cases:
in a simple graph a closed trail cannot have length 1 or 2, and length 0 is a
single vertex, which this paper does not count as a cycle (claim m2-15,
[qualified]; the textbook is silent on the length-0 case). English usage:
Grinberg's "cycle" is a closed walk with k >= 3 and distinct vertices
w_0, ..., w_{k-1}, which is D6, not D5 (claim C22).

**Example (D6).** In T, the triangle of the board drawing, 1, 2, 3, 1 is a
simple cycle of length 3 (script section 2). The textbook's example (claim
m2-2): v1, v3, v4, v2, v1 is a simple cycle of G_tb.

**Example (D5, not D6).** The textbook's v3, v2, v1, v3, v5, v4, v3 in G_tb
is a cycle in the sense of 1.2.14 (closed, six distinct edges) but not a
simple cycle: v3 occurs three times (claim m2-2; script section 3).

**Non-example.** In B, 1, 2, 1 is a closed walk but not a cycle: edge 12 is
used twice. In fact B has no cycle at all (script section 1: no cycle of
positive length among closed walks of length up to 6). In T, 1, 2, 1 is
likewise a closed walk, not a cycle.

Cycles are not needed for the main results of the paper; they are given
because the brief asks for Definitions 1.2.10 to 1.2.16.

### 3.6 The three naming conventions in one table

The same two properties (edges distinct, vertices distinct) get different
names in the three conventions. "Course" is the user's statement for the
word path; for cycle the course convention is not stated, so the paper
follows the textbook for cycle and always writes "simple cycle" for the
English "cycle". Source for each row: the claim ids in the last column.

| Property of the walk | Textbook (Armenian, number) | English (Grinberg, Wikipedia) | Course / this paper | Claims |
|---|---|---|---|---|
| any sequence of steps along edges | շրջանցում, walk (1.2.10) | walk | walk | C12, C13 |
| walk with first = last | փակ շրջանցում, closed walk (1.2.11) | closed walk | closed walk | C14 |
| no repeated edge, vertices may repeat | ճանապարհ, "path" (1.2.12) | trail | trail | C15, C21 |
| no repeated vertex (so no repeated edge) | պարզ ճանապարհ, "simple path" (1.2.13) | path | **path** | C16, C21, C24 |
| closed, no repeated edge, vertices may repeat | ցիկլ or փակ ճանապարհ, "cycle" (1.2.14) | closed trail ("circuit" in some books; use is not uniform) | cycle (textbook meaning) | C17, C22 |
| closed, no repeated vertex except first = last, k >= 3 | պարզ ցիկլ, "simple cycle" (1.2.15) | cycle | simple cycle | C17, C22 |

So the word "path" has three meanings across the sources (claims C15, C16,
C21, C23; contradictions entry 1). The two meanings of "cycle" are in
contradictions entry 2. Wikipedia records that some authors use "path" for
repeated vertices and "simple path" for distinct vertices, the textbook's
pattern (claim C23), so the course convention is one of at least two in
use. The table is claim m2-7.

### 3.7 Distance

**In plain words.** The distance between two houses is the number of roads
on the shortest trip between them. If no trip exists, the distance is
declared infinite. A house is at distance zero from itself. The distance from
the first house to the second equals the distance from the second to the
first, because you can drive any trip backwards. Going by a third house never
makes the trip shorter than the shortest trip.

**Definition D7 (textbook Definition 1.2.16, printed pp. 22-23; claim C18).**
The *distance* d(u, v) = d_G(u, v) between vertices u and v is the length of
a shortest (u, v)-path if at least one (u, v)-path exists, and +infinity
otherwise.

The textbook's "path" in D7 is its 1.2.12 (trail). The definition does not
depend on whether one reads trail or path, because the shortest of each has
the same length (Proposition P2 below, claim m2-12).

**Properties (textbook, claim m2-4; proofs in P3, claim m2-16).**
1. d(u, v) >= 0, and d(u, v) = 0 if and only if u = v.
2. d(u, v) = d(v, u).
3. d(u, v) <= d(u, w) + d(w, v).

So when the graph is connected, (V, d) is a metric space (textbook, same
place).

**Remark.** D7 allows the value +infinity, which is not an integer; this is
how a missing path shows up. It forbids negative values and any value that
is not the length of an actual trip.

**Example.** In B: d(1, 2) = 1, d(2, 3) = 1, d(1, 3) = 2, d(i, i) = 0 for
each i (script section 6). The walk 1, 2, 1, 2, 3 has length 4, but the
distance d(1, 3) is 2: the shortest.

**Non-example.** The number 4 is not the distance from 1 to 3 in B, even
though a walk of length 4 exists (distance is the minimum, not any length).
Also, in the graph D with vertices 1, 2, 3 and the single edge 12, the
distance d(1, 3) is not a number: it is +infinity (script section 6). D is the
board graph with the edge 23 removed. (m3 may use the same graph as its
disconnected example; the orchestrator should keep the two consistent.)

### 3.8 The lemma: every walk contains a path

**In plain words.** Suppose you can drive from one house to another. Then
you can do it without visiting any house twice. Look at your trip. If it
passes some house twice, you went round a loop. Cut the loop out. What is
left is still a trip from the same start to the same end. It is shorter.
Keep cutting loops until none are left. The trip that remains visits every
house at most once. It is never longer than the first trip.

**Lemma L1 (textbook Lemma 1.2.1, printed p. 23, for u different from v;
Grinberg Corollary 2.9.7, document p. 39, in general; claims C19, C20,
derived in m2-9).** Let u and v be vertices of a simple graph G (equal or
not). If there is a (u, v)-walk of length k, then there is a (u, v)-path
of length at most k. All vertices and edges of this path are vertices and
edges of the walk.

The textbook states L1 only for u different from v and says "from any
(u, v)-walk one can extract a simple (u, v)-path" (claim C19), without a
bound on the length. Its proof gives the bound (it shows the shorter walk
has smaller length), so the bound is the textbook's too. The case u = v is
needed here because a closed walk, such as 2, 1, 2 in B, has u = v: the
path it contains is the single vertex of length 0.

*Idea.* Induction on the length k of the walk. If the vertices are all
different, the walk is already a path. If not, cut the loop between two equal
vertices; the result is a shorter walk with the same ends; apply the
induction hypothesis to it. This is the textbook's method ("by induction on
the length of the walk", claim m2-3).

*Proof.* We prove, by strong induction on k, the statement S(k): every
(u, v)-walk of length k, for any vertices u and v, contains a (u, v)-path of
length at most k.

*Base case, k = 0.* A walk of length 0 is a single vertex u, so v = u. A single
vertex has no repeated vertex, so the walk is itself a path, of length 0 <= 0.

*Induction hypothesis.* Let k >= 1 and assume S(m) holds for every m < k.

*Step.* Let u_0, u_1, ..., u_k be a (u, v)-walk, so u_0 = u and u_k = v.

Case 1: the vertices u_0, ..., u_k are pairwise distinct. Then the walk is
a path, of length k <= k. Done.

Case 2: some vertex occurs twice. Then there are indices i < j with
u_i = u_j. Form the sequence W' = u_0, u_1, ..., u_i, u_{j+1}, ..., u_k. If
j = k the part after u_i is empty and W' ends at u_i. We check that W'
is a (u, v)-walk:
 (a) it starts at u_0 = u;
 (b) it ends at v: if j < k its last vertex is u_k = v; if j = k its last
     vertex is u_i = u_j = u_k = v;
 (c) every two consecutive vertices form an edge: before the cut these are
     consecutive vertices of the old walk; the join is the pair
     (u_i, u_{j+1}) = (u_j, u_{j+1}), which is a step of the old walk; after
     the join they are consecutive vertices of the old walk again.
The length of W' is i + (k - j). Since i < j, this is less than k, so W' has
some length m < k. By the induction hypothesis S(m), W' contains a (u, v)-path
of length at most m, and m < k, so at most k. Every vertex and edge of that
path is one of W', and so one of the old walk. ∎

*Why the proof is valid.* Each cut removes at least one step (j - i >= 1), so
the length drops by at least 1 and the process stops after at most k cuts. A
walk that cannot be cut has no repeated vertex, which is the definition of a
path. In the textbook's version, u is different from v, so k >= 1 and the base
case is k = 1: a walk of one edge between two different vertices is a path.
The textbook's induction keeps u and v fixed, so the new walk W' also joins
two different vertices and the hypothesis applies.

*Worked trace (script section 4).* The textbook's walk v1, v3, v2, v4, v3,
v2, v4, v3, v5 of G_tb, written 1, 3, 2, 4, 3, 2, 4, 3, 5:
 - length 8; u_1 = u_4 = 3; cut; get 1, 3, 2, 4, 3, 5 (length 5);
 - again u_1 = u_4 = 3; cut; get 1, 3, 5 (length 2);
 - 1, 3, 5 has distinct vertices: a path of length 2 <= 8.
In B, 1, 2, 1, 2, 3 has u_0 = u_2 = 1; cutting gives 1, 2, 3, a path. The
closed walk 2, 1, 2 cuts to the single vertex 2, of length 0. The closed
walk 1, 2, 3, 2, 1 cuts to the single vertex 1.

**Corollary L2 (path length bound) [derived, claim m2-11].** In a graph with
N vertices every path has at most N - 1 edges. Hence if there is a walk from
u to v, there is one of length at most N - 1.

*Proof.* A path of length k lists k + 1 pairwise distinct vertices; there are
only N vertices, so k + 1 <= N, that is k <= N - 1. For the second part, apply
L1: a path inside the walk has length at most that of the walk and at most
N - 1. Grinberg gives the same argument (claim m2-6). ∎

For B, N = 3, so a path has at most 2 edges; the longest path in B has 2 edges
(script section 7).

**Proposition P2 [derived, claim m2-12].** For vertices u, v of a simple
graph, the following three numbers are equal: the length of a shortest
(u, v)-walk, of a shortest (u, v)-trail, of a shortest (u, v)-path. Each is
+infinity when the corresponding set is empty, and the three sets are empty
together. So d(u, v) in D7 is the same whether "path" in D7 is read as trail
or as path.

*Proof.* Every path is a trail (P1) and every trail is a walk, so the sets
of lengths satisfy: lengths of paths are among lengths of trails, which are
among lengths of walks. Hence min over walks <= min over trails <= min over
paths. By L1, a shortest walk contains a path of at most the same length, so
min over paths <= min over walks. Therefore all three minima are equal. If
there is no walk there is no trail and no path. If there is a walk, L1 gives
a path. So the three sets are empty together. ∎

Grinberg makes the same remark: "a shortest walk from u to v (if it exists)
must also be a shortest path from u to v" (claim m2-6).

**Proposition P3 (the distance properties) [derived, claim m2-16].** The
three properties of D7 follow from the definition.

*Proof.* Use P2 to compute d by shortest walks.
1. Lengths are 0, 1, 2, ... or +infinity, so d >= 0. The walk consisting of
   u alone has length 0, so d(u, u) = 0. If d(u, v) = 0 there is a walk of
   length 0 from u to v; it is the single vertex, so v = u.
2. If u_0, ..., u_k is a (u, v)-walk then u_k, ..., u_0 is a (v, u)-walk of the
   same length (each step is an edge, and edges are unordered). So the sets
   of walk lengths from u to v and from v to u are equal, and so are their
   minima.
3. If d(u, w) or d(w, v) is +infinity, the right side is +infinity and the
   inequality holds. Otherwise take a shortest (u, w)-walk and a shortest
   (w, v)-walk and join them at w. The result is a (u, v)-walk of length
   d(u, w) + d(w, v). The shortest (u, v)-walk is no longer than this. ∎

## 4. Evidence

Claims already in `evidence/evidence.json` (module tag m2) and what they
rest on. Quote text is in that file.

| Claim | What it says | Support |
|---|---|---|
| C12 | Definition 1.2.10 walk | textbook p. 21, quote; Grinberg Def. 2.9.1(a) |
| C13 | Repeats allowed; length counts each edge as often as it occurs | textbook p. 22, remark after 1.2.10 |
| C14 | Definition 1.2.11 closed walk | textbook p. 22 |
| C15 | Definition 1.2.12 "path" = distinct edges (English trail) | textbook p. 22 |
| C16 | Definition 1.2.13 simple path = distinct vertices | textbook p. 22 |
| C17 | Definitions 1.2.14, 1.2.15 cycle, simple cycle | textbook p. 22 |
| C18 | Definition 1.2.16 distance | textbook pp. 22-23 |
| C19 | Lemma 1.2.1 (u different from v) | textbook p. 23 |
| C20 | Corollary 2.9.7 (any u, v; length bound) | Grinberg p. 39, Prop. 2.9.5 p. 38 |
| C21 | English meaning of path and trail | Grinberg Defs 2.9.1(c), 3.4.5; Wikipedia |
| C22 | English meaning of cycle | Grinberg Def. 2.10.1(b) |
| C23 | Some authors use "simple path" for distinct vertices | Wikipedia |
| C24 | Course convention for "path" [qualified] | textbook Def. 1.2.13 and the user's text in the brief |
| C25-C28 | Board definition of connected, matrix, drawing | whiteboard photos |

New claims in `evidence/modules/m2.json` (ids m2-1 to m2-16):

| Claim | Kind | Status | What it says |
|---|---|---|---|
| m2-1 | fact | supported | Textbook examples for 1.2.10 and 1.2.12 (printed p. 22) |
| m2-2 | fact | supported | Textbook examples for 1.2.13 and 1.2.15, and C_n for n >= 3 (printed p. 22; the simple-path example is printed after 1.2.14) |
| m2-3 | fact | supported | Textbook proof method of Lemma 1.2.1 (p. 23) |
| m2-4 | fact | supported | Textbook distance properties 2 and 3, and the metric-space statement (p. 23) |
| m2-5 | fact | supported | Grinberg: definition of length, length-0 path, path edges are distinct (exercise) |
| m2-6 | fact | supported | Grinberg p. 40: path has at most n - 1 edges; shortest walk is shortest path |
| m2-7 | fact | supported | The naming table |
| m2-8 | interpretation | qualified | Definition D4' of a path between n_i and n_j |
| m2-9 | derived | supported | Lemma L1 in general, with length bound (proof in Section 3.8) |
| m2-10 | derived | supported | Proposition P1: distinct vertices imply distinct edges |
| m2-11 | derived | supported | Corollary L2: a path has at most N - 1 edges |
| m2-12 | derived | supported | Proposition P2: shortest walk = shortest trail = shortest path |
| m2-13 | derived | supported | Classification of the board-graph examples and their counts (script) |
| m2-14 | derived | supported | B has no cycle and trails equal paths in B; T has a simple cycle (script) |
| m2-15 | interpretation | qualified | Length-0 walks are allowed; a length-0 closed trail is not counted as a cycle |
| m2-16 | derived | supported | Proposition P3: distance properties from the definition |

Limits of the reading: Chapters 3 to 8 of the textbook were not read, and the
textbook's Lemma 1.2.2 (a closed walk of odd length contains a simple cycle of
odd length, printed p. 23) is not used.

## 5. Calculations (all from `modules/m2_walks.py`)

Script: `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/modules/m2_walks.py`.
Run with `python3 -I modules/m2_walks.py`; output saved in
`modules/m2_walks_output.txt`. The script implements D1 to D6 literally
(a walk checks every step against the edge set; a trail checks that edges
are distinct; a path checks that vertices are distinct), then:

Board graph B, classification of the examples (script section 1):

| Sequence | Length | Type |
|---|---|---|
| 1, 2, 3 | 2 | walk, trail, path |
| 1, 2, 1, 2, 3 | 4 | walk only |
| 2, 1, 2 | 2 | walk, closed |
| 2, 3, 2, 1, 2 | 4 | walk, closed |
| 1, 2, 1 | 2 | walk, closed |
| 2 | 0 | walk, closed, trail, path |
| 1, 2 | 1 | walk, trail, path |
| 1, 3 | 1 | not a walk |
| 1, 2, 3, 2 | 3 | walk only |

Number of walks, trails, paths, closed walks of each length in B, counted
over all start and end vertices by enumeration:

| k | walks | trails | paths | closed walks |
|---|---|---|---|---|
| 0 | 3 | 3 | 3 | 3 |
| 1 | 4 | 4 | 4 | 0 |
| 2 | 6 | 2 | 2 | 4 |
| 3 | 8 | 0 | 0 | 0 |
| 4 | 12 | 0 | 0 | 8 |

(Consistency with m1: the enumeration equals the entries of A^k for
k = 1, ..., 5, all i, j, script section 1. The proof is m1's.) Walks from
1 to 3 of length at most 4: 1, 2, 3 (length 2); 1, 2, 1, 2, 3 and
1, 2, 3, 2, 3 (length 4); only the first is a path.

Triangle T (script section 2): 1, 2, 3, 1 is a walk, closed, trail, cycle and
simple cycle. 1, 2, 1 is closed only.

Textbook graph G_tb with the seven forced edges (script section 3):

| Sequence | Length | Type |
|---|---|---|
| 1, 3, 2, 4, 3, 2, 4, 3, 5 | 8 | walk only |
| 3, 1, 4, 2, 3, 5 | 5 | not a walk |
| 1, 3, 2, 4, 3, 5 | 5 | walk, trail (textbook "path"), not a path |
| 1, 3, 4, 5 | 3 | walk, trail, path |
| 3, 2, 1, 3, 5, 4, 3 | 6 | closed, trail, cycle, not simple |
| 1, 3, 4, 2, 1 | 4 | closed, trail, cycle, simple cycle |

Each row agrees with what the textbook says about that sequence (claims m2-1
and m2-2).

Lemma traces (script section 4): length 8 to length 5 to length 2 for the
textbook walk, as in Section 3.8; 1, 2, 1, 2, 3 to 1, 2, 3; 2, 1, 2 to 2;
1, 2, 3, 2, 1 to 1.

Exhaustive and random tests (script section 5): L1's construction produced a
path with the same ends, no longer than the walk, with vertices from the walk,
for all 73 walks of length 0 to 6 in B, all 381 in T, all 4695 in G_tb: 0
failures. On 300 random graphs with N from 2 to 7 (seed 20261027) and 192696
walks of length 0 to 5: 0 failures of L1; 0 failures of P1 (every path has
distinct edges); 0 paths longer than N - 1 (L2); 0 disagreements between
BFS distance and the shortest walk, shortest trail and shortest path (P2).
These are checks of the proofs, not proofs.

Distance (script section 6): in B, d(1, 2) = 1, d(1, 3) = 2, d(2, 3) = 1,
d(i, i) = 0. In D (single edge 12): d(1, 2) = 1; d(1, 3) = d(2, 3) = infinity.
Path bound (script section 7): the longest path in B has 2 edges = N - 1.

## 6. Assumptions and their reasons

- Finite, simple, undirected graph: the brief, section 7 (the user's text
  and the symmetric board matrix). With multigraphs, a walk would need its
  edges listed, not only its vertices; with directed graphs, step direction
  would matter.
- A walk of length 0 is allowed: needed so that d(u, u) = 0 and so that a
  closed walk contains a path (L1 with u = v). [qualified, m2-15.]
- "Path" means distinct vertices: the user's statement (brief, section 7);
  the textbook's name for it is "simple path". [qualified, C24.]
- The example graph is B (the matrix), not the drawing: the brief, section 7.
  The drawing's triangle T is used only where a cycle is needed, and is
  labelled.
- Only the seven edges forced by the textbook's own examples are used for
  G_tb: so that no claim rests on reading edges off the figure.
- Quotes from the textbook are copied from the page images (PDF pages 22 to
  24); the text layer drops symbols. Math letters are plain Unicode with
  subscripts written as digits, the same convention as the existing
  evidence quotes.

## 7. Limitations, failure cases, competing explanations

- **Competing conventions for path.** Under the textbook's own word,
  "path" allows repeated vertices (1.2.12). A reader who takes a path in the
  textbook sense will count trails. The paper must state which meaning it
  uses at first use and keep it (table in 3.6). Competing explanation: the
  board may use either meaning; the board does not say (C24). This does not
  change the connectivity result (P2, L1): a trail from u to v exists if and
  only if a path from u to v exists, so every statement of the form "there
  is a path between n_i and n_j" has the same truth value in both readings.
  It changes the counts: the number of trails from u to v is not the number
  of paths, and neither is the number of walks (m1).
- **Competing conventions for cycle.** The textbook's cycle is a closed trail;
  the English cycle is the textbook's simple cycle (C22). Not needed by the
  main results.
- **Example graph without a cycle.** B is a tree. In B trails and paths
  coincide, so B cannot illustrate the difference between D3 and D4; the
  textbook's G_tb does it. B cannot illustrate cycles either; T and G_tb do.
- **Textbook placement.** In the printed text, the sentence that shows
  v1, v3, v2, v4, v3, v5 is not a simple path and v1, v3, v4, v5 is one comes
  after Definition 1.2.14, not right after 1.2.13. Claim C16 puts it under
  Definition 1.2.13; the content is about 1.2.13, the printed position is
  after 1.2.14 (m2-2 locates it). It is a presentation quirk of the book, not
  an error of mathematics.
- **Length 0.** The textbook does not state whether k = 0 is allowed, and does
  not say whether a length-0 closed trail is a cycle (m2-15, qualified).
- **Not covered.** Directed graphs, multigraphs, infinite graphs, weighted
  distance, algorithms for shortest paths other than the remark that
  breadth-first search computes d (checked by script only as a test of P2,
  not described as a method here; that belongs to m3).
- The lemma and propositions here are derived by me; the textbook states L1
  without the bound and gives P3's three properties without proof. The
  module's proofs of P1, P2, P3, L2 are not in the textbook; Grinberg has P1
  as an exercise, L2 and the "shortest walk is shortest path" remark in
  prose (claims m2-5, m2-6).

## 8. Dependencies and conflicts

Depends on no module.

Quotable statements for m1 and m3 (copy verbatim):

- **Walk and length.** "A walk of length k from u_0 to u_k is a sequence of
  vertices u_0, u_1, ..., u_k of G such that every two consecutive vertices
  are joined by an edge (in a simple graph the edges are determined by the
  vertices). Vertices and edges may repeat. The length of the walk is k, the
  number of edges, each edge counted as many times as it occurs. This is the
  textbook's Definition 1.2.10."
- **Path (course convention).** "A path between n_i and n_j is a walk from
  n_i to n_j in which all vertices are pairwise distinct. This is the
  textbook's simple path, Definition 1.2.13, and the English path. The
  textbook's own word 'path', Definition 1.2.12, means a walk with pairwise
  distinct edges; this paper calls that a trail."
- **Lemma L1.** "If there is a walk of length k from u to v, there is a
  path from u to v of length at most k, whose vertices and edges all belong
  to the walk (textbook Lemma 1.2.1 for u different from v; Grinberg
  Corollary 2.9.7 in general)."
- **Corollary L2.** "In a graph with N vertices every path has at most N - 1
  edges. So if there is a walk from u to v, there is a walk of length at
  most N - 1 from u to v."
- **Distance.** "The distance d(u, v) is the length of a shortest path from
  u to v, or +infinity if there is none; it also equals the length of a
  shortest walk from u to v (Proposition P2)."

For m1: m1 uses D1 and the word "walk" with the length counted with
multiplicity, and its counterexample (A^2)_ii > 0 should say that the
two-step walk i, j, i is a closed walk of length 2 that is not a trail and
not a path (it uses one edge twice and visits i twice); the script (section 1)
lists 1, 2, 1 and 2, 1, 2 on B as closed walks that are neither trails nor paths.

For m3: m3 needs L1 and L2 (a path has at most N - 1 edges) to restrict
powers to 1, ..., N - 1; and the definition D4' for "connected". For the
disconnected example, D (single edge 12) is used here; m3 should say whether
it uses the same graph.

Conflicts: none with the brief. A naming point for all modules: write
"trail" for the textbook's 1.2.12 "path" and "path" for D4. The textbook's
word "path" must never be used for 1.2.12 without saying so.

## 9. Open questions

- Does the course use "cycle" in the textbook's (1.2.14) or the English
  sense? The user stated only the meaning of "path". This module follows the
  textbook for "cycle" and writes "simple cycle" for the English one.
- Does the board's "path" allow length 0 (n_i joined to itself)? For
  connectivity this does not matter (a pair with i different from j needs a
  path of length at least 1).
- The textbook's Fig. 1.2.5 was read only for the seven edges its examples
  force. Whether v1v5 and other lines are edges was not settled and is not
  needed.

## m3.md

# Module m3: Connectivity from the adjacency matrix

Owner: m3. Register: study-note. Depends on m1 (walk counting) and m2 (walks,
paths, Lemma 1.2.1). Script: `modules/m3_connectivity.py`; its full output is
`modules/m3_connectivity.out.txt` and is reproduced in Section 5.
Evidence fragment: `evidence/modules/m3.json` (new claims `m3-1` to `m3-13`);
older claims C30 to C39 in `evidence/evidence.json` are cited by id.

Labels used in the text: **[fact]** established fact from a source,
**[derived]** proved here or computed by the script, **[interp]**
interpretation, **[estimate]**, **[open]**. Numbers of the form 3.x are
provisional paper numbers; the textbook's numbers are always written as
"textbook Definition 2.1.1" and so on.

## 1. Purpose

This module answers question 2 of the brief: how can one tell from the
adjacency matrix A alone whether a graph with N vertices is connected? It
establishes

1. the textbook's definition of connected (Definition 2.1.1, printed p. 48)
   and of components (printed p. 49, in prose, no number), with the board's
   own definition beside them;
2. the test: for N >= 2, G is connected if and only if every off-diagonal entry
   of S = A + A^2 + ... + A^(N-1) is positive; equivalently every entry of
   (I + A)^(N-1) is positive;
3. a complete proof for a beginner, built on two supplied results (walk
   counting from m1 and the walk-to-path lemma from m2);
4. why the last power is N - 1 and why N - 2 would fail;
5. a connected and a disconnected three-vertex example with every matrix
   written out and computed by script;
6. breadth-first search as the alternative, in one paragraph, and one remark
   on cost.

The textbook states no such test in the pages read (claim m3-11, unverified
beyond those pages), and the two web sources that state the test prove it
loosely (claim m3-12). So the paper proves it itself; the proof below is the
text for `appendices/derivations.tex` and is the derivation behind claims C35
and C37.

## 2. Prerequisites

Each item is defined here in one line, with the owner module.

| Concept | Meaning | Owner |
|---|---|---|
| graph G = (V, E) | finite, simple, undirected; V = {n_1, ..., n_N}, so N = number of vertices (textbook Definition 1.1.1 area, claim C1) | m1 |
| adjacency matrix A | N x N, A_ij = 1 if n_i, n_j are adjacent, else 0; symmetric, zero diagonal (C2, C3) | m1 |
| matrix power A^k | A multiplied by itself k times; A^0 = I, the identity matrix (1 on the diagonal, 0 elsewhere) | m1 |
| walk of length k | a sequence u_0, u_1, ..., u_k of vertices with each consecutive pair adjacent; vertices and edges may repeat; k is the number of steps (textbook Definition 1.2.10, C12, C13) | m2 |
| path | a walk with no repeated vertex (course convention, textbook Definition 1.2.13 "simple path", C16, C24) | m2 |
| textbook "path" | a walk with distinct edges (textbook Definition 1.2.12, English "trail"; C15) | m2 |
| Result W (walk counting) | for k >= 1, (A^k)_ij is the number of walks of length k from n_i to n_j (C6) | m1 |
| Result L (walk-to-path lemma) | if there is a walk of length k from u to v, there is a path from u to v of length at most k (textbook Lemma 1.2.1 for u != v, C19; length bound from Grinberg Corollary 2.9.7, C20) | m2 |

Supplied by m1 (one sentence): **Result W**, for every integer k >= 1 the
(i, j) entry of A^k is the number of walks of length k from n_i to n_j.

Supplied by m2 (one sentence): **Result L**, if some walk from u to v has
length k, then some path (no repeated vertex) from u to v has length at most
k (this includes u = v, where the path is the one-vertex walk of length 0).

Reminder of why L is true, owned by m2: if a walk visits a vertex twice, cut
out the part between the two visits; the result is still a walk, shorter, with
the same ends; repeat until no vertex repeats.

Two small facts used here, proved inline in Section 3: a path with k edges has
k + 1 distinct vertices, so k <= N - 1 (claim C33); and, by Result W, every
entry of every power of A is a nonnegative integer, because it is a count.

## 3. Explanation from first principles

### 3.0 The story and the notation

The story fixed in the introduction: the vertices are houses of a village, the
edges are roads. A walk is a trip along roads in which you may pass a house or
a road twice. A path is a trip that never visits a house twice.

Notation (board letters, textbook letters in brackets): vertices n_i
[textbook v_i]; N vertices [textbook n]; A the adjacency matrix; I the N x N
identity matrix; S the sum defined in Definition 3.3 below.

### 3.1 Connected graphs

**In plain words.** A village has houses. Some houses are joined by a road. A
trip goes from house to house along roads. You may pass the same house twice on
a trip. Sometimes you can reach every house from every other house. Then the
village is called connected. If one house is cut off, the village is not
connected.

**Definition 3.1** (textbook Definition 2.1.1, printed p. 48; board: "Graph is
called connected if for any n_i, n_j there exists a path between nodes").
Let G = (V, E) be a graph. G is *connected* if for any two vertices u and v of
G there is a (u, v)-path in G. [fact: C30, C25]

**Remark 3.1.**
1. In the textbook "path" here is Definition 1.2.12, a walk with distinct
   edges, vertices may repeat. The board does not say which meaning it uses and
   the course convention is "no repeated vertex". The definition does not
   depend on the choice: a walk of any kind between two different vertices
   contains a path with distinct vertices (Result L), and a walk with distinct
   vertices has distinct edges, so the two readings accept exactly the same
   graphs. [derived from C19, C20, C21]
2. "Any two vertices" includes u = v. For u = v the walk with one vertex and no
   edges is a (u, u)-path, so these pairs are always satisfied. Reading the
   definition as "any two different vertices" changes nothing. [interp; the
   textbook does not discuss u = v]
3. The definition forbids exactly one thing: a pair of vertices with no trip
   between them.

**Example 3.1** (satisfies the definition). The board graph: vertices 1, 2, 3
with edges 1-2 and 2-3 (the matrix on the board; see Section 6 for the drawing
mismatch, claim C28). The pair 1, 3 is joined by the path 1, 2, 3; the pairs
1, 2 and 2, 3 are joined by one edge. The textbook's own examples of connected
graphs are the complete graphs, the complete bipartite graphs, and the three
graphs of its Fig. 2.1.1 (printed p. 48). [fact: m3-2]

**Non-example 3.1** (violates the definition). Three vertices with only the
edge 1-2. No walk starts at vertex 3 and ends elsewhere, so the pair 1, 3 has
no path. The textbook's Fig. 2.1.2 (printed p. 49) shows a graph that is not
connected and has four components. [derived, fact: m3-2]

### 3.2 Components

**In plain words.** Look at a village that is not connected. It falls into
pieces. Inside one piece every house can reach every other house. No road joins
two different pieces. Each piece is called a component. A connected village has
exactly one piece.

**Definition 3.2** (textbook, printed p. 49, in the paragraph after Definition
2.1.1; the book gives it in prose without a number). On the vertex set V
define u ~ v to mean that G has a (u, v)-path. This relation is reflexive,
symmetric and transitive, so V splits into classes V_1, ..., V_p. The induced
subgraphs G_j = G[V_j] are the *connected components* of G (Armenian:
կապակցվածության բաղադրիչներ). [fact: m3-1, C31]

**Remark 3.2.** Components are pieces that cannot be enlarged: a vertex
reachable from a vertex of V_j lies in V_j. The textbook's Remark 2.1.1: G is
connected if and only if it has exactly one component. [fact: C31]

**Example 3.2.** The graph of Non-example 3.1 (edge 1-2 only) has the two
components G[{1, 2}] and G[{3}]; the board graph has the single component
G[{1, 2, 3}]. [derived, script output in Section 5]

**Non-example 3.2.** G[{1}] is not a component of the graph with edge 1-2
only, although it is a connected subgraph: vertex 2 can be reached from
vertex 1, so 2 belongs to the same class as 1. A component is a whole class,
not any connected piece. [derived]

### 3.3 The matrices used by the test

**In plain words.** We need a name for the running total. It adds the counts
of trips with one road, two roads, and so on. We stop one step short of the
number of houses. The whole check uses this one total.

**Definition 3.3** (new notation, not from the textbook). For a graph with N >= 2
vertices let S = A + A^2 + ... + A^(N-1), the sum of the first N - 1 powers of
A, added entry by entry. I denotes the identity matrix.

**Remark 3.3.** By Result W, S_ij is the number of walks from n_i to n_j whose
length is between 1 and N - 1. Hence every entry of S is a nonnegative integer.
The diagonal of S counts closed walks and plays no role in the test (reason in
Remark 3.5). [derived from C6]

**Example 3.3.** For the board graph, S = A + A^2 is written out in
Section 5: its first row is 1 1 1.

**Non-example 3.3.** A^2 alone is not S for N = 3, where S = A + A^2. The
matrix A^2 of the board graph has the zero entry (1, 2) although vertices 1 and
2 are joined by an edge, and A alone has the zero entry (1, 3) although vertices
1 and 3 are connected. Either one alone would wrongly report "not connected"
(script, Example 3.5). [derived]

### 3.4 The test and its proof

**In plain words.** We want a quick check for a village. We only have the table
that says which houses share a road. From the table we can count trips. Count
the trips with one road, with two roads, and so on. Add the counts for each pair
of houses. If no pair of different houses has a total of zero, the village is
connected. We never need trips longer than one road fewer than the number of
houses. A trip that wastes time can always be shortened. So longer trips tell
us nothing new. A second form lets every house also stay where it is for one
step. It gives the same answer.

**Proposition 3.1** (one pair at a time). Let G have N >= 2 vertices and let
i != j. The following four statements are equivalent.

- (i) There is a (n_i, n_j)-path in G (textbook Definition 2.1.1 sense).
- (ii) There is an integer k with 1 <= k <= N - 1 and (A^k)_ij > 0.
- (iii) S_ij > 0.
- (iv) The (i, j) entry of (I + A)^(N-1) is positive.

**Theorem 3.2** (the connectivity test). Let G be a graph with N >= 2
vertices and adjacency matrix A. The following are equivalent.

- (a) G is connected.
- (b) Every off-diagonal entry of S = A + A^2 + ... + A^(N-1) is positive.
- (c) Every entry of (I + A)^(N-1) is positive.

[derived: C35 for (a) <=> (b), C37 for (b) <=> (c); statement in the sources
C34 and C36]

**Proof of Proposition 3.1.**

*(i) => (ii).* Let W be a (n_i, n_j)-path as in (i). A path in the sense of
Definition 2.1.1 is a walk, so there is a walk from n_i to n_j. By Result L
there is a path P from n_i to n_j whose length k is at most the length of W.
P has k edges and therefore k + 1 vertices, all different from each other. The
graph has only N vertices, so k + 1 <= N, that is k <= N - 1 (claim C33). If
k were 0, P would be a walk with no steps and would start and end at the same
vertex; but n_i != n_j, so k >= 1. P is a walk of length k from n_i to n_j, so
by Result W the number (A^k)_ij is at least 1. This proves (ii).

*(ii) => (iii).* S_ij = (A)_ij + (A^2)_ij + ... + (A^(N-1))_ij. Each term is a
count, hence a nonnegative integer (Result W). A sum of nonnegative numbers is
at least as large as any one of its terms. The term with index k from (ii) is
positive, so S_ij > 0.

*(iii) => (ii).* If S_ij > 0, the sum of nonnegative terms is positive, so at
least one term (A^k)_ij with 1 <= k <= N - 1 is positive. That is (ii).

*(ii) => (i).* If (A^k)_ij > 0 with k >= 1 then, since (A^k)_ij is an integer
count (Result W), there is at least one walk of length k from n_i to n_j. As
n_i != n_j, Result L (textbook Lemma 1.2.1) gives a path from n_i to n_j with
distinct vertices. A walk with distinct vertices has distinct edges, because an
edge is fixed by its two end vertices and two different positions of the walk
have different end vertices. So it is a (n_i, n_j)-path in either reading of the
word "path" (Remark 3.1). This is (i).

*(iii) <=> (iv).* Put m = N - 1. Expand (I + A)^m = (I + A)(I + A)...(I + A),
m factors. Each term of the expansion chooses I or A from each factor and
multiplies the choices in order. Because I times any matrix X equals X, a
product with k letters A and m - k letters I equals A^k. The number of ways to
choose which k of the m factors give A is the binomial coefficient C(m, k).
Therefore

    (I + A)^m = C(m,0) I + C(m,1) A + C(m,2) A^2 + ... + C(m,m) A^m.

Take an entry (i, j) with i != j. The identity has 0 there, so

    ((I + A)^m)_ij = C(m,1) (A)_ij + C(m,2) (A^2)_ij + ... + C(m,m) (A^m)_ij.

Every coefficient C(m, k) with 1 <= k <= m is a positive integer and every
(A^k)_ij is a nonnegative integer. So this sum is positive if and only if at
least one (A^k)_ij with 1 <= k <= m is positive, which holds if and only if
S_ij > 0. This is (iii) <=> (iv). On the diagonal, the term C(m,0) I
contributes 1 and all other terms are nonnegative, so every diagonal entry of
(I + A)^m is at least 1 whatever the graph is. [derived: C37] (end of proof)

**Proof of Theorem 3.2.** (a) says: for every pair of vertices there is a path
between them. For a pair with u = v this is always true (Remark 3.1, item 2).
For pairs with i != j it is statement (i) of Proposition 3.1. So (a) holds if
and only if (i) holds for every i != j. By Proposition 3.1 that is equivalent to
(iii) for every i != j, which is (b). It is also equivalent to (iv) for every
i != j; together with the always positive diagonal this is (c). (end of proof)

**Corollary 3.3** (components from S). For any graph (connected or not) with
N >= 2 and i != j: S_ij > 0 if and only if n_i and n_j lie in the same
component. *Proof.* Proposition 3.1 uses connectivity only through the pair
(n_i, n_j): (i) says n_i ~ n_j, which is the definition of "same class" in
Definition 3.2. (end of proof)  [derived: m3-5]

**Remark 3.4** (by-product, distance). Since a shortest walk between two
different vertices is a path (Result L), the smallest k with (A^k)_ij > 0 is the
distance between n_i and n_j (textbook Definition 1.2.16). The sources C38 state
this. [fact: C38; derived from W and L]

**Remark 3.5** (why the diagonal is skipped, and N = 1, N = 2). For N = 2 and
one edge, S = A has zeros on the diagonal although the graph is connected
(script output, Section 5). So the diagonal of S cannot be required to be
positive. For N >= 3 and connected G the diagonal of S is positive anyway,
because every vertex has a neighbour and (A^2)_ii is the degree of n_i
(claim C9); but the test does not need this. For N = 1 there are no pairs of
different vertices, the graph is connected, S is an empty sum and (I + A)^0 = I
= [1] has no zero entry, so both forms of the test give the correct answer, but
the sum is not defined by the formula and the test is stated for N >= 2.
[derived: m3-3]

### 3.5 The test as a procedure

**In plain words.** Here is the check, step by step. First write the table of
the village. Then multiply the table by itself again and again. After each
step, add the new counts to a running total. Stop after one step fewer than the
number of houses. Look at every pair of different houses. If any total is zero,
those two houses cannot reach each other. If no total is zero, everyone can
reach everyone.

**Test 3.4** (matrix test).
Input: the adjacency matrix A of a graph with N >= 2 vertices.

1. Set P = A and S = A.
2. For k = 2, 3, ..., N - 1: replace P by P x A (now P = A^k) and add P to S.
3. Look at the entries S_ij with i != j. If one of them is 0, the graph is not
   connected. If none is 0, the graph is connected.

(Equivalent form: compute (I + A)^(N-1) and report "connected" if no entry is
0.) Correctness is Theorem 3.2. Step 3 can also be read off pair by pair: a
zero at (i, j) means, by Corollary 3.3, that n_i and n_j are in different
components.

### 3.6 Why N - 1 is enough, and why N - 2 is not

**Why N - 1 is enough.** In Proposition 3.1, (i) => (ii) shows that if a trip
between two different vertices exists at all, a trip of length at most N - 1
exists, because a shortest trip repeats no vertex and a repeat-free trip has at
most N vertices. Adding powers beyond N - 1 cannot change which off-diagonal
entries are positive: if (A^k)_ij > 0 for any k >= 1, a walk exists, hence a path,
hence a walk of length at most N - 1, so some entry of A, ..., A^(N-1) at the same
place is already positive. [derived from C20, C33]

**In plain words** (for the next example). Take four houses in a row. To go from
the first house to the last you must pass every house in between. That takes
three roads. If we counted only trips of up to two roads, we would miss this
pair. We would say the village is cut in two, and we would be wrong. The same
idea works for any row of houses.

**Proposition 3.5** (N - 1 cannot be lowered to N - 2). For every N >= 3 there
is a connected graph with N vertices for which the sum A + ... + A^(N-2) has a
zero off-diagonal entry. *Proof.* Take the path graph with edges 1-2, 2-3, ...,
(N-1)-N. Each step of a walk changes the vertex number by exactly 1. To go from
vertex 1 to vertex N the number must increase by N - 1, so at least N - 1 steps
are needed. A walk of length k < N - 1 from 1 to N does not exist, so by Result
W (A^k)_{1N} = 0 for 1 <= k <= N - 2, and the (1, N) entry of A + ... + A^(N-2)
is 0, although the graph is connected. (end of proof)  [derived: m3-4]

The script confirms it for N = 3, ..., 8 (table in Section 5): the first power
with a nonzero (1, N) entry is N - 1 every time. For N = 3 the graph is the
board graph and the "sum" A + ... + A^(N-2) is A itself, with A_13 = 0. For
N = 4 the matrices are written out in Section 5: A + A^2 has a 0 in positions
(1, 4) and (4, 1), A + A^2 + A^3 has none.

### 3.7 Worked examples

**In plain words** (Example 3.5, connected). Take three houses in a row. A road
joins the first and the second house. Another road joins the second and the
third house. The first and the third house share no road. Can you still go from
one to the other? Yes, through the middle house. We expect the check to say
connected.

**Example 3.5** (connected; the board matrix, edges 1-2 and 2-3, N = 3,
N - 1 = 2). Every product below was computed by `modules/m3_connectivity.py`.

    A          A^2        S = A + A^2    (I + A)^2
    0 1 0      1 0 1      1 1 1          2 2 1
    1 0 1      0 2 0      1 2 1          2 3 2
    0 1 0      1 0 1      1 1 1          1 2 2

Reading: S has no zero entry off the diagonal (it has none anywhere), so by
Theorem 3.2(b) G is connected. (I + A)^2 has no zero entry at all, so by
Theorem 3.2(c) G is connected. The two answers agree. The (1, 3) entry of A is
0, so no road joins vertices 1 and 3, yet (A^2)_13 = 1: there is exactly one
walk of length 2 from vertex 1 to vertex 3, namely 1, 2, 3. The entry (I + A)^2
at (1, 3) is 1 = C(2,2) (A^2)_13, since the other two terms vanish there. Check
of the binomial formula: (I + A)^2 = I + 2A + A^2 holds entry by entry (script).
BFS from vertex 1 reaches {1, 2, 3}. [derived: m3-6]

**In plain words** (Example 3.6, disconnected). Now take three houses again.
Only one road exists, between the first and second house. The third house
stands alone. Nobody can walk to it. We expect the check to say not connected.
The check should also show that the third house is a piece by itself.

**Example 3.6** (disconnected; edge 1-2 only, N = 3, N - 1 = 2).

    A          A^2        S = A + A^2    (I + A)^2
    0 1 0      1 0 0      1 1 0          2 2 0
    1 0 0      0 1 0      1 1 0          2 2 0
    0 0 0      0 0 0      0 0 0          0 0 1

Reading: the off-diagonal zeros of S are at (1, 3), (2, 3), (3, 1) and (3, 2);
the zeros of (I + A)^2 are at the same four places. So by Theorem 3.2 the graph
is not connected, and by Corollary 3.3 vertices 1 and 2 are in one component and
vertex 3 in another: the components are {1, 2} and {3}, which agrees with BFS.
Higher powers do not help: the script checked that entries (1, 3) and (2, 3)
of A^k are 0 for k = 1, ..., 6, and in fact no walk reaches vertex 3 at all.
[derived: m3-7]

**Example 3.7** (the bound N - 1 is needed; path 1-2-3-4, N = 4). From the
script:

    A            A^2          A^3
    0 1 0 0      1 0 1 0      0 2 0 1
    1 0 1 0      0 2 0 1      2 0 3 0
    0 1 0 1      1 0 2 0      0 3 0 2
    0 0 1 0      0 1 0 1      1 0 2 0

    A + A^2 (N - 2 powers)   A + A^2 + A^3 (N - 1 powers)
    1 1 1 0                  1 3 1 1
    1 2 1 1                  3 2 4 1
    1 1 2 1                  1 4 2 3
    0 1 1 1                  1 1 3 1

With N - 2 = 2 powers the (1, 4) entry is 0 and the test would wrongly say
"not connected"; with N - 1 = 3 powers every entry is positive. [derived: m3-4]

### 3.8 Breadth-first search, the alternative

**In plain words.** There is another way, and it needs no table of counts.
Stand at one house and mark it. Then mark every house next to it. Then mark every
house next to those. Keep going until no new house appears. If every house is
marked, the village is connected.

**Remark 3.6** (breadth-first search, BFS). BFS from a start vertex s keeps a
queue of discovered vertices, and repeatedly takes the vertex at the front and
discovers its undiscovered neighbours. Its correctness statement in the source
is that for every vertex v there is a walk from s to v if and only if v is
discovered at the end, so G is connected if and only if every vertex is
discovered when BFS starts from any single vertex s. [fact: C39, m3-13, Schost 2026,
slides 6 and 10 of 20] BFS and the matrix test agree on all 32768 labelled
graphs with 6 vertices and on all smaller ones (script, Section 5; a check, not
a proof). BFS also yields the components directly, as the script's component
lists show.

### 3.9 One remark on cost

**Remark 3.7** (cost, estimate). Counting scalar multiplications with the
school method (N^3 for one product of two N x N matrices): the matrix test
needs N - 2 products to reach A^(N-1), that is (N - 2) N^3, which is 98,000,000
for N = 100 (script). Because Proposition 3.1 holds with any exponent m >= N - 1
in place of N - 1, one can instead square I + A repeatedly until the exponent
2^t is at least N - 1: t squarings, 7 for N = 100, costing 7,000,000 (script);
the script verified this version against BFS on every labelled graph with at most
6 vertices. BFS needs time O(n + m) when the graph is given by adjacency lists
(n vertices, m edges); when the input is the matrix A itself, BFS reads each row
once, N^2 = 10,000 entries for N = 100. The entries of the powers also grow
fast (for the complete graph on 10 vertices the largest entry of A^9 is
38,742,049), which a Boolean version of the product (replace every positive
entry by 1) avoids. The matrix test is useful because the answer is a clean
statement about powers of A, not because it is fast. [estimate: m3-9, m3-10;
support C39 and the slides' data-structure remark]

## 4. Evidence

| Statement in the report | Claim id | What supports it |
|---|---|---|
| Definition 2.1.1 (connected), printed p. 48; same as the board's | C30, C25 | textbook quote; board photos |
| Components, printed p. 49, prose, no number; Remark 2.1.1 | m3-1, C31 | textbook quote ("called the connected components"), Remark 2.1.1; Grinberg Def. 2.9.12 |
| Textbook examples (complete graphs, Fig. 2.1.1) and non-example (Fig. 2.1.2, four components) | m3-2 | textbook quotes, printed pp. 48-49 |
| walk iff path for connectivity | C32, C20 | Grinberg Prop. 2.9.10, Cor. 2.9.7 |
| Result W (walk counting), supplied by m1 | C6 | Quinlan Thm 1.1.3, Grinberg Thm 4.5.10, Lehman et al., Bai Thm 1 |
| Result L (walk contains path, with length bound), supplied by m2 | C19, C20 | textbook Lemma 1.2.1; Grinberg Cor. 2.9.7 |
| A path has at most N - 1 edges | C33 | Grinberg, Section 2.9.4; proved inline in Prop. 3.1 |
| Statement of the sum test | C34 | Paramadevan and Sotheeswaran Thm 2; MathWorld |
| Statement of the (I + A)^(N-1) test | C36 (qualified) | Bai Thm 2 (proof sketch says "paths") |
| Proof of the sum test | C35 (derived) | Prop. 3.1 and Theorem 3.2 above; premises C6, C20 |
| Equivalence of the two forms | C37 (derived) | binomial expansion above; Bai item 3 for the idea |
| The two web proofs say "paths" where walks are meant, and omit the walk-to-path step | m3-12 | quotes from both sources |
| The textbook states no such test in the pages read | m3-11 (unverified) | absence, pages 9-12, 21-23, 48-49 only |
| Edge cases N = 1, N = 2; diagonal of S | m3-3 | derived; script; C9 |
| N - 2 powers do not suffice | m3-4 | derived; script |
| Components from S | m3-5 | derived; script |
| Example 3.5 numbers | m3-6 | script |
| Example 3.6 numbers | m3-7 | script |
| Agreement with BFS on all graphs with at most 6 vertices | m3-8 | script, a check not a proof |
| Exponent m >= N - 1 suffices | m3-9 | derived; script |
| Cost counts | m3-10 (estimate) | script; Schost slides 3, 6, 9 |
| Distance as the smallest k | C38 | Lehman et al., Paramadevan and Sotheeswaran Thm 3 |
| BFS decides connectivity; its correctness statement | C39, m3-13 | Schost 2026 slides 6 and 10 |

## 5. Derivations, worked examples, reproducible calculations

Script: `papers/adjacency-walks-connectivity/modules/m3_connectivity.py`.
Run from the paper folder: `python3 -I modules/m3_connectivity.py` (pure
Python, about 30 seconds, the N = 6 exhaustive loop dominates). Its output was
saved to `modules/m3_connectivity.out.txt` and is reproduced here unchanged.

```
==================================================================
EXAMPLE 1 (connected, the board matrix)  N = 3  edges: [(1, 2), (2, 3)]
A
     0  1  0
     1  0  1
     0  1  0
A^2
     1  0  1
     0  2  0
     1  0  1
S = A + A^2   (N - 1 = 2)
     1  1  1
     1  2  1
     1  1  1
(I + A)^2     (N - 1 = 2)
     2  2  1
     2  3  2
     1  2  2
off-diagonal zeros of S      : []
zero entries of (I+A)^(N-1)  : []
sum test says connected      : True
(I+A)^(N-1) test says        : True
BFS says connected           : True
components (BFS)             : [[1, 2, 3]]
(I+A)^2 == I + 2A + A^2      : True
==================================================================
EXAMPLE 2 (disconnected, edge 1-2 only)  N = 3  edges: [(1, 2)]
A
     0  1  0
     1  0  0
     0  0  0
A^2
     1  0  0
     0  1  0
     0  0  0
S = A + A^2   (N - 1 = 2)
     1  1  0
     1  1  0
     0  0  0
(I + A)^2     (N - 1 = 2)
     2  2  0
     2  2  0
     0  0  1
off-diagonal zeros of S      : [(1, 3), (2, 3), (3, 1), (3, 2)]
zero entries of (I+A)^(N-1)  : [(1, 3), (2, 3), (3, 1), (3, 2)]
sum test says connected      : False
(I+A)^(N-1) test says        : False
BFS says connected           : False
components (BFS)             : [[1, 2], [3]]
(I+A)^2 == I + 2A + A^2      : True
------------------------------------------------------------------
Example 2, higher powers: column 3 of A^k for k = 1..6 is zero off the diagonal: True
==================================================================
N = 2, one edge 1-2 (connected): the sum is just A
A = S
     0  1
     1  0
diagonal of S is zero although G is connected; off-diagonal entries are 1: True
Connected graphs with 3 vertices: diagonal of S positive? path 1-2-3: [1, 2, 1]
==================================================================
Path graph 1-2-...-N: entry (1,N) of A^k first becomes nonzero at k = N-1
   N | smallest k with (A^k)_{1N} > 0 | (1,N) of A+..+A^(N-2) | (1,N) of A+..+A^(N-1)
   3 |                              2 |                      0 |                      1
   4 |                              3 |                      0 |                      1
   5 |                              4 |                      0 |                      1
   6 |                              5 |                      0 |                      1
   7 |                              6 |                      0 |                      1
   8 |                              7 |                      0 |                      1
------------------------------------------------------------------
N = 4, path 1-2-3-4: A, A^2, A^3, A+A^2, A+A^2+A^3
A
     0  1  0  0
     1  0  1  0
     0  1  0  1
     0  0  1  0
A^2
     1  0  1  0
     0  2  0  1
     1  0  2  0
     0  1  0  1
A^3
     0  2  0  1
     2  0  3  0
     0  3  0  2
     1  0  2  0
A + A^2  (N-2 powers: NOT enough)
     1  1  1  0
     1  2  1  1
     1  1  2  1
     0  1  1  1
A + A^2 + A^3  (N-1 powers: enough)
     1  3  1  1
     3  2  4  1
     1  4  2  3
     1  1  3  1
test with N-2 powers says connected: False   test with N-1 powers says connected: True
==================================================================
Exhaustive check over ALL labelled simple graphs, N = 2..6
   N | graphs | connected | sum test = BFS | (I+A)^(N-1) test = BFS | S_ij>0 <=> same component | pattern of (I+A)^m for m = 2^t >= N-1 = BFS | N-2 powers wrong on
   2 |      2 |         1 |              2 |                      2 |                          2 |                                         2 | 1
   3 |      8 |         4 |              8 |                      8 |                          8 |                                         8 | 3
   4 |     64 |        38 |             64 |                     64 |                         64 |                                        64 | 12
   5 |   1024 |       728 |           1024 |                   1024 |                       1024 |                                      1024 | 60
   6 |  32768 |     26704 |          32768 |                  32768 |                      32768 |                                     32768 | 360
==================================================================
Cost remark: scalar multiplications, schoolbook product of two N x N matrices = N^3
   N | (I+A)^(N-1) by N-2 products | by repeated squaring | BFS row scans of A (N^2)
   10 |                       8,000 |                4,000 | 100
      number of squarings t = 4, 2^t = 16 >= N-1 = 9
  100 |                  98,000,000 |            7,000,000 | 10,000
      number of squarings t = 7, 2^t = 128 >= N-1 = 99
 1000 |             998,000,000,000 |       10,000,000,000 | 1,000,000
      number of squarings t = 10, 2^t = 1024 >= N-1 = 999
complete graph K_5: largest entry of A^(N-1) = 52
complete graph K_10: largest entry of A^(N-1) = 38,742,049
complete graph K_20: largest entry of A^(N-1) = 98,920,982,783,015,679,456,199
```

Reading the exhaustive table: in all 2 + 8 + 64 + 1024 + 32768 labelled graphs
the sum test, the (I + A)^(N-1) test, the component statement of Corollary 3.3
and the repeated-squaring version agree with an independent breadth-first
search. The last column shows what goes wrong with N - 2 powers: for N = 3 it
gives the wrong answer on 3 of the 8 graphs (the three labelled paths), for
N = 4 on 12 of 64. For N = 2 the sum with N - 2 = 0 powers is empty and wrong on
the one connected graph. The exhaustive check is a test of the statements, not a
replacement for the proof in Section 3.4; it covers N <= 6 only.

Hand check of Example 3.5, for the reader: row 1 of A is (0, 1, 0), column 3 of
A is (0, 1, 0), so (A^2)_13 = 0*0 + 1*1 + 0*0 = 1, matching the script.

## 6. Assumptions and their reasons

1. The graph is finite, simple, undirected (brief section 7; C1). The proof
   uses the symmetry of A only through walk counting (m1) and the lemma (m2).
2. N >= 2 for the test. For N = 1 there are no pairs of different vertices; see
   Remark 3.5.
3. The board matrix, not the board drawing, is the example graph (brief
   assumption; C28). The drawing shows a third line 1-3 and an arrowhead at 2;
   the matrix has neither. The paper reports the mismatch and does not guess
   which was intended.
4. The mark above A in board question 1 is the power k (C29, qualified). It does
   not affect this module: the test uses A^k for k = 1, ..., N - 1.
5. "Path" in the test's (i) is read in both ways (textbook 1.2.12 and 1.2.13);
   Remark 3.1 shows the choice does not matter.
6. Arithmetic is ordinary integer arithmetic. Entries are counts, hence
   nonnegative, which is what makes "sum positive iff some term positive" valid.
   A different arithmetic (subtraction, modular) would break this step.
7. Matrix entries are exact; the script uses Python integers, so there is no
   rounding.

## 7. Limitations, failure cases, competing explanations

- The proof is only as good as Results W and L. W is stated by four sources
  (C6); L is the textbook's Lemma 1.2.1 plus the length bound from Grinberg
  (C19, C20). The textbook lemma requires u != v and states no length bound; the
  bound comes from the English source and the textbook's proof by induction on the
  length gives it too (contradiction note: C19/C20, resolved in
  `evidence.json`).
- Failure case: dropping the "+ I" or using one power, or stopping at N - 2,
  gives wrong answers (Non-example 3.3, Proposition 3.5, Example 3.7). Using
  only A^(N-1) is wrong too: in the board graph A^2 has the zero entry (1, 2)
  (Example 3.5).
- The test says connected or not; the sum S does not directly list a path.
  Corollary 3.3 gives the components and Remark 3.4 the distances.
- Competing explanations. (1) The two web sources (Paramadevan and Sotheeswaran
  Theorem 2; Bai Theorem 2) explain the test by "paths". That is a wrong
  explanation, since the matrix powers count walks (C11, m3-12); their statements
  of the test are correct. (2) BFS gives the same answer faster, Remark 3.6.
  (3) Eigenvalue and Laplacian tests exist and are out of scope (brief,
  section 3); no claim is made about them here.
- Cost: the numbers in Remark 3.7 are operation counts for the school method of
  multiplication, an estimate; faster matrix multiplication exists and was not
  examined.
- Directed graphs: not examined. The argument for "walk implies path" and the
  symmetric A are used; the paper should not apply the test to digraphs.
- The exhaustive check covers N <= 6 only.

## 8. Dependencies and conflicts

Dependencies on other modules (all as named in the brief).

- **m1.** Needs Result W exactly as stated: for every k >= 1, (A^k)_ij is the
  number of walks of length k from n_i to n_j in a simple undirected graph. If
  m1 states it with "walks" and warns that paths are not counted, as planned
  (C8), nothing else is needed. m1's board example (A^2 for the board matrix) is
  the same matrix as Example 3.5; the numbers agree with `modules/m1_walks.py`
  (A^2 rows 1 0 1 / 0 2 0 / 1 0 1).
- **m2.** Needs Result L with the length bound and with u = v allowed
  (Grinberg Corollary 2.9.7). The textbook's Lemma 1.2.1 is stated for u != v
  and without the length bound. Please make m2 state both: the test needs the
  bound, the proof of the theorem only needs u != v. Also needs m2's statement
  that a walk with distinct vertices has distinct edges (used in Proposition 3.1,
  (ii) => (i)); I proved it in one line where used.
- **Section numbering.** The 3.x numbers here are placeholders; Definition 3.1 is
  textbook Definition 2.1.1 and Definition 3.2 is the unnumbered textbook
  paragraph on printed p. 49.

Conflicts with other claims in the evidence file.

- Claim C39 reads "against N - 1 matrix products for the matrix test". Reaching
  A^(N-1) from A takes N - 2 products (A^2, ..., A^(N-1)); I wrote N - 2 in
  Remark 3.7. The source quote of C39 supports only the BFS time bound, not the
  comparison, so the comparison belongs to m3-10. Orchestrator: correct C39's
  text or treat m3-10 as the authority.
- Claim C39 gives BFS time as O(n + m); the slide computes this for graphs given
  by adjacency lists (slide 6 "given by adjacency lists"; slide 3 gives the
  adjacency matrix size as Theta(n^2)). With the matrix A as input BFS reads N^2
  entries (m3-10). The paper should say which representation.
- Claim C34's text says "Two sources state it; neither gives a fully careful
  proof". Consistent with m3-12.

## 9. Open questions

- [open] Whether the lecturer's intended answer to board question 2 was the sum
  test, the (I + A)^(N-1) test, or BFS: the board shows only the question, not
  the answer.
- [open] Whether the textbook states a matrix connectivity test in Chapters 3 to
  8, which were not read (claim m3-11, unverified).
- [open] The board drawing versus the board matrix (edge 1-3, arrowhead):
  reported, not resolved (C28).
- [open] The board's mark above A in question 1 (C29, qualified).
- [open] Whether to give the test also for directed graphs: out of scope; no
  source checked.
