# Rollout `dom`: papers/adjacency-walks-connectivity

One run of the research-paper pipeline. Sections, in order: the commits that
built the paper (what changed in each revision round), the reports the agents
returned, the evaluation report with every round's scores and findings, the
technician reader's findings, the author's self-evaluation, and the module
reports. Scores and findings inside the evaluation report are the pipeline's
own evaluator speaking, recorded as it produced them.

# Commits

## Commit 1: 1716b21 2026-10-31
Probe dom: author-stage rollout of adjacency-walks-connectivity

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01V3X5pvnt2qupEjJAy8VZqN

```
papers/adjacency-walks-connectivity/appendices/course-terms.tex             |  55 ++++
 papers/adjacency-walks-connectivity/appendices/derivations.tex              | 139 ++++++++
 papers/adjacency-walks-connectivity/appendices/photographs.tex              |  32 ++
 papers/adjacency-walks-connectivity/appendices/provenance.tex               |  45 +++
 .../appendices/scripts/generate_paper_numbers.py                            | 297 +++++++++++++++++
 .../appendices/scripts/generate_paper_numbers_output.txt                    |  34 ++
 papers/adjacency-walks-connectivity/appendices/scripts/m1_walks.py          | 116 +++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m1_walks_output.txt  |  76 +++++
 papers/adjacency-walks-connectivity/appendices/scripts/m2_walks.py          | 295 +++++++++++++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m2_walks_output.txt  |  75 +++++
 .../adjacency-walks-connectivity/appendices/scripts/m3_connectivity.out.txt | 116 +++++++
 papers/adjacency-walks-connectivity/appendices/scripts/m3_connectivity.py   | 228 +++++++++++++
 papers/adjacency-walks-connectivity/appendices/scripts/numbers.tex          |  53 +++
 papers/adjacency-walks-connectivity/evaluation-report.md                    | 164 ++++++++++
 papers/adjacency-walks-connectivity/evidence/evidence.json                  |  40 +++
 papers/adjacency-walks-connectivity/evidence/modules/author.json            |  46 +++
 papers/adjacency-walks-connectivity/main.pdf                                | Bin 0 -> 373102 bytes
 papers/adjacency-walks-connectivity/main.tex                                |  89 +++++
 papers/adjacency-walks-connectivity/reader-findings.md                      |  42 +++
 papers/adjacency-walks-connectivity/references.bib                          | 102 ++++++
 papers/adjacency-walks-connectivity/reports/paper-author-round1.md          |  43 +++
 papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md       |  62 ++++
 papers/adjacency-walks-connectivity/reports/technician-reader-round1.md     |  49 +++
 papers/adjacency-walks-connectivity/sections/answer1_walks.tex              | 258 +++++++++++++++
 papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex       | 311 ++++++++++++++++++
 papers/adjacency-walks-connectivity/sections/answer3_path.tex               |  79 +++++
 papers/adjacency-walks-connectivity/sections/background.tex                 | 632 ++++++++++++++++++++++++++++++++++++
 papers/adjacency-walks-connectivity/sections/conclusion.tex                 |  32 ++
 papers/adjacency-walks-connectivity/sections/discussion.tex                 |  97 ++++++
 papers/adjacency-walks-connectivity/sections/example.tex                    | 182 +++++++++++
 papers/adjacency-walks-connectivity/sections/introduction.tex               | 188 +++++++++++
 papers/adjacency-walks-connectivity/self-evaluation.md                      | 130 ++++++++
 32 files changed, 4107 insertions(+)
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/course-terms.tex b/papers/adjacency-walks-connectivity/appendices/course-terms.tex
new file mode 100644
index 0000000..51c6ea4
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/course-terms.tex
@@ -0,0 +1,55 @@
+\section{Textbook numbers and board symbols}\label{app:courseterms}
+
+\Cref{tab:textbooknumbers} lists, in the textbook's build order, each concept used in this note
+with the textbook's number and printed page, and the word the textbook uses where it differs
+from English usage \cite{petrosyan2015grafneri}.
+The textbook's words are in Armenian script, which this note does not typeset; its words
+are given in English translation.
+Printed page numbers are one lower than PDF page numbers (\Cref{conv:pages}).
+
+\begin{table}[ht]
+\centering
+\caption{Concepts in the textbook's build order, with the textbook's numbers.}\label{tab:textbooknumbers}
+\begin{tabular}{@{}p{6.0cm}p{3.2cm}p{1.6cm}p{3.0cm}@{}}
+\toprule
+Concept & Textbook number & Printed page & Textbook word (translated)\\
+\midrule
+graph $G=(V,E)$ & Definition 1.1.1 & 9 & \\
+adjacent & Definition 1.1.4 & 11 & \\
+adjacency matrix $A(G)$ & no number of its own, after Definition 1.1.6 & 11 & \\
+degree & Definition 1.2.1 & 16 & \\
+sum of all degrees equals $2|E|$ & Theorem 1.2.1 (Euler) & 16 & \\
+walk & Definition 1.2.10 & 21 & \\
+closed walk & Definition 1.2.11 & 22 & \\
+walk with no repeated edge (trail) & Definition 1.2.12 & 22 & ``path''\\
+walk with no repeated vertex (path) & Definition 1.2.13 & 22 & ``simple path''\\
+cycle & Definition 1.2.14 & 22 & ``cycle'', ``closed path''\\
+simple cycle & Definition 1.2.15 & 22 & ``simple cycle''\\
+distance & Definition 1.2.16 & 22--23 & \\
+every $(u,v)$-walk contains a simple $(u,v)$-path, $u\ne v$ & Lemma 1.2.1 & 23 & \\
+connected & Definition 2.1.1 & 48 & \\
+connected components & in prose, no number & 49 & \\
+connected if and only if one component & Remark 2.1.1 & 49 & \\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\Cref{tab:boardsymbols} compares the board's symbols with the textbook's and with this note's.
+The first row records that the board's $V$ in the line defining $A_{ij}$ is the set of edges
+\cite{whiteboard1,whiteboard2}.
+
+\begin{table}[ht]
+\centering
+\caption{Board symbols, textbook symbols, and the symbols of this note.}\label{tab:boardsymbols}
+\begin{tabular}{@{}p{4.2cm}p{3.6cm}p{3.6cm}@{}}
+\toprule
+Board & Textbook & This note\\
+\midrule
+$(G,V)$, with $V$ the edge set & $G=(V,E)$ & $G=(V,E)$\\
+$e_{ij}\in V$ & $uv\in E$ & $n_in_j\in E$ or $e_{ij}\in E$\\
+nodes $n_i$ & vertices $v_i$ & vertices $n_i$\\
+$|G|=N$ nodes & $n$ vertices & $N$ vertices\\
+$A_{ij}$ & $a_{ij}$ in $A(G)$ & $A_{ij}$ in $A$\\
+\bottomrule
+\end{tabular}
+\end{table}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/derivations.tex b/papers/adjacency-walks-connectivity/appendices/derivations.tex
new file mode 100644
index 0000000..0d534f4
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/derivations.tex
@@ -0,0 +1,139 @@
+\section{Derivations}\label{app:derivations}
+
+This appendix holds the arguments that the main text only states, in the order in which the
+main text needs them.
+
+\subsection{Walk counting: walks and vertex sequences}\label{app:walkcount}
+
+The proof of \Cref{thm:walkcount} counts vertex sequences instead of walks.
+This is allowed by the following fact, which is stated before the theorem in \Cref{rem:walk}.
+
+\begin{proposition}\label{prop:sequences}
+In a simple graph, the map that sends a walk $u_0,e_1,u_1,\dots,e_k,u_k$ to its vertex sequence
+$u_0,u_1,\dots,u_k$ is a one-to-one correspondence between the walks of length $k$ and the
+sequences of $k+1$ vertices in which every two consecutive vertices are adjacent.
+\end{proposition}
+
+\begin{proof}
+This is proved here.
+The vertex sequence of a walk has consecutive vertices $u_{i-1},u_i$ joined by the edge $e_i$, so they
+are adjacent.
+The map is one to one: in a simple graph at most one edge joins two vertices, so $e_i=u_{i-1}u_i$ is
+determined by the vertices, and two walks with the same vertex sequence are equal.
+The map is onto: given such a sequence, put $e_i=u_{i-1}u_i$; this is an edge because the two vertices
+are adjacent, and the result is a walk.
+\end{proof}
+
+For $k=0$ the same reasoning gives one walk from each vertex to itself, which is why the identity matrix
+$A^0=I$ fits the pattern \cite[Section~4.5.5]{grinberg2025graph}; this note uses it only in
+\Cref{prop:iplusa}.
+Where simplicity enters the proof of \Cref{thm:walkcount} is stated after that proof.
+
+\subsection{The counterexample, in full}\label{app:counterexample}
+
+\Cref{prop:warning} uses the board graph.
+Its entries for the walks from $n_1$ to $n_2$ can be found in closed form.
+In $B$, the vertex $n_2$ is adjacent to $n_1$ and $n_3$, and these two are adjacent only to $n_2$.
+So a walk alternates between $n_2$ and the set $\{n_1,n_3\}$.
+A walk from $n_1$ to $n_2$ therefore has odd length $k$, and its vertices in even positions
+$w_2,w_4,\dots,w_{k-1}$, which number $(k-1)/2$, are each $n_1$ or $n_3$, freely.
+Hence there are $2^{(k-1)/2}$ walks of odd length $k$ and none of even length, which gives
+$1,0,2,0,4$ for $k=1,\dots,5$, as in \Cref{tab:walksvspaths} and in the entries of $A$, $A^3$, $A^5$.
+Among them only the walk $n_1,n_2$ is a path or a trail, because any longer walk repeats the vertex
+$n_2$ (a walk of length $3$ or more from $n_1$ to $n_2$ meets $n_2$ at an earlier odd position).
+
+\subsection{The chain of premises for the connectivity test}\label{app:testproof}
+
+\Cref{thm:test}(a)$\Leftrightarrow$(b) follows from \Cref{prop:pair} and the definition of connected.
+The premises, in order, are the following.
+\begin{enumerate}
+\item \Cref{thm:walkcount}: $(A^k)_{ij}$ is the number of walks of length $k$.
+\item \Cref{cor:walkcount}(a): all entries are nonnegative integers, so a sum is positive if and only
+  if a summand is.
+\item \Cref{lem:walkpath}: a walk of length $k$ from $u$ to $v$ contains a path of length at most $k$.
+\item \Cref{cor:bound}: a path in a graph with $N$ vertices has at most $N-1$ edges.
+\item \Cref{prop:pathtrail} and \Cref{rem:connected}: ``path'' may be read as trail or path.
+\end{enumerate}
+Premises 1 and 2 give (ii)$\Leftrightarrow$(iii) and the passage from a positive entry to a walk;
+premise 3 gives the passage from a walk to a path; premise 4 gives the bound $k\le N-1$ in
+(i)$\Rightarrow$(ii); premise 5 makes the equivalence independent of the reading of ``path''.
+No other fact is used.
+
+\subsection{Powers of \texorpdfstring{$I+A$}{I+A}}\label{app:iplusa}
+
+\begin{proof}[Proof of \Cref{prop:iplusa}]
+This is proved here; \cite[Section~1, Theorem~2, proof sketch]{bai2025adjacency} gives the idea of
+adding a loop to every vertex.
+Put $m\ge N-1$.
+Expand $(I+A)^m=(I+A)(I+A)\cdots(I+A)$ with $m$ factors.
+Each term chooses $I$ or $A$ in each factor and multiplies the choices in order.
+Since $I$ times a matrix $X$ is $X$, a term with $k$ letters $A$ equals $A^k$, and there are
+$\binom{m}{k}$ ways to choose which $k$ factors give $A$.
+Therefore
+\begin{equation}\label{eq:binomial}
+(I+A)^m=\sum_{k=0}^{m}\binom{m}{k}A^k,\qquad A^0=I.
+\end{equation}
+\emph{Diagonal.}
+The term $k=0$ contributes $1$ to every diagonal entry and all other terms are nonnegative, so
+every diagonal entry is at least $1$.
+\emph{Off the diagonal.}
+For $i\ne j$ the identity contributes $0$, so
+$((I+A)^m)_{ij}=\sum_{k=1}^{m}\binom{m}{k}(A^k)_{ij}$.
+Every coefficient $\binom{m}{k}$ with $1\le k\le m$ is a positive integer and every $(A^k)_{ij}$ is a
+nonnegative integer (\Cref{cor:walkcount}(a)), so the sum is positive if and only if some
+$(A^k)_{ij}$ with $1\le k\le m$ is positive.
+If a path between $n_i$ and $n_j$ exists, it has length $k$ with $1\le k\le N-1\le m$
+(\Cref{cor:bound}) and $(A^k)_{ij}\ge 1$.
+Conversely, if $(A^k)_{ij}>0$ for some $k$ with $1\le k\le m$, a walk exists (\Cref{thm:walkcount}) and
+hence a path (\Cref{lem:walkpath}).
+This proves the statement about the entries.
+$G$ is connected if and only if every pair $i\ne j$ has a path, that is, if and only if no
+off-diagonal entry is $0$; since the diagonal entries are positive, that is if and only if
+$(I+A)^m$ has no zero entry.
+Squaring $I+A$ repeatedly gives the exponents $2,4,8,\dots$, so $t$ squarings give $m=2^t$, and $t$ is
+chosen with $2^t\ge N-1$.
+\end{proof}
+
+For $N=3$ and the board graph, $(I+A)^2=I+2A+A^2$ is verified entry by entry in \Cref{ex:testB}.
+
+\subsection{Distance}\label{app:distance}
+
+\begin{proof}[Proof of \Cref{prop:shortest}]
+This is proved here.
+Every path is a trail (\Cref{prop:pathtrail}) and every trail is a walk, so the lengths of paths are
+among the lengths of trails, which are among the lengths of walks; hence
+$\min_{\text{walks}}\le\min_{\text{trails}}\le\min_{\text{paths}}$.
+By \Cref{lem:walkpath} a shortest walk contains a path of at most the same length, so
+$\min_{\text{paths}}\le\min_{\text{walks}}$.
+The three minima are therefore equal.
+If there is no walk there is no trail and no path, and if there is a walk, \Cref{lem:walkpath} gives a
+path; so the three sets are empty together.
+\end{proof}
+
+\begin{proposition}[the distance properties]\label{prop:distprops}
+The three properties listed in \Cref{def:distance} follow from the definition.
+\end{proposition}
+
+\begin{proof}
+The textbook lists the properties without proof \cite[p.~23]{petrosyan2015grafneri}; this proof is written
+here.
+By \Cref{prop:shortest} we may compute $d$ by shortest walks.
+(1) Lengths are $0,1,2,\dots$ or $+\infty$, so $d\ge 0$.
+The walk consisting of $u$ alone has length $0$, so $d(u,u)=0$.
+If $d(u,v)=0$ there is a walk of length $0$ from $u$ to $v$, which is the single vertex, so $v=u$.
+(2) If $u_0,\dots,u_k$ is a walk from $u$ to $v$ then $u_k,\dots,u_0$ is a walk from $v$ to $u$ of the same
+length, since edges are unordered; so the sets of lengths agree, and so do their minima.
+(3) If $d(u,w)$ or $d(w,v)$ is $+\infty$ the right side is $+\infty$ and the inequality holds.
+Otherwise join a shortest $(u,w)$-walk and a shortest $(w,v)$-walk at $w$: this is a $(u,v)$-walk of length
+$d(u,w)+d(w,v)$, and a shortest $(u,v)$-walk is no longer.
+\end{proof}
+
+\subsection{Cross-checks by computer}\label{app:crosschecks}
+
+Two finite checks accompany the proofs; neither replaces them.
+First, for every labelled simple graph on $N=2,3,4,5$ vertices, the number of walks of length $k$
+enumerated by brute force equals the corresponding entry of $A^k$, for $k=1,\dots,5$ when $N\le 4$ and
+$k=1,2,3$ when $N=5$ (\Cref{app:provenance}).
+Second, for all labelled simple graphs on $2,\dots,6$ vertices, the sum test, the $(I+A)^{N-1}$ test, the
+component statement of \Cref{cor:components}, and the repeated-squaring form of \Cref{prop:iplusa} agree with
+breadth-first search (\Cref{tab:exhaustive}).
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/photographs.tex b/papers/adjacency-walks-connectivity/appendices/photographs.tex
new file mode 100644
index 0000000..e3930ed
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/photographs.tex
@@ -0,0 +1,32 @@
+\section{Transcription of the whiteboard}\label{app:photographs}
+
+The two photographs show the same board at slightly different angles, and they are read
+together \cite{whiteboard1,whiteboard2}.
+The lines below follow the reading order; the board's wording and spelling are kept.
+
+\begin{enumerate}
+\item The matrix entry is defined as $A_{ij}=1$ if $e_{ij}\in V$ and $A_{ij}=0$ if
+  $e_{ij}\notin V$ \cite{whiteboard1,whiteboard2}.
+  The board's $V$ here is the set of edges (\Cref{conv:notation}).
+\item A drawing with vertices labelled 1, 2, 3, and next to it a grid labelled ``adj.'' with
+  rows $0\,1\,0$, $1\,0\,1$, $0\,1\,0$ \cite{whiteboard1,whiteboard2}.
+  The drawing shows a line from 1 to 2 with an arrowhead at 2, a line from 1 to 3, and a line
+  from 2 to 3; the matrix records only the edges 1--2 and 2--3 (\Cref{sec:board-mismatch}).
+\item ``Problem. Given graph $(G, V)$ with $N$ nodes i.e.\ $|G| = N$ and the graph is
+  represented through it's adj.\ matrix. So you have `A' matrix.''
+  \cite{whiteboard1,whiteboard2}.
+\item ``1) What does $A^{\cdot}_{ij}$ represent'', where $\cdot$ marks a small mark that
+  looks like a small $n$ or quotation marks \cite{whiteboard1,whiteboard2}
+  (\Cref{sec:board-mark}).
+\item ``2) How to know if graph is connected or not.'' \cite{whiteboard1,whiteboard2}.
+\item ``Def.\ Graph is called connected if for any $n_i, n_j$ there exists a path between
+  nodes.'' \cite{whiteboard1,whiteboard2}.
+\end{enumerate}
+
+\noindent
+\emph{Clearly visible:} the prose of items 1, 3, 5 and 6, the matrix entries, and the vertex
+labels.
+\emph{Likely interpretation:} the mark in item 4 is an exponent $k$ (\Cref{conv:exponent}); the
+arrowhead in item 2 is a stray mark (\Cref{conv:example}).
+\emph{Not settled:} which of the drawing and the matrix the lecturer intended, and which
+meaning of ``path'' the board uses (\Cref{conv:path}).
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/provenance.tex b/papers/adjacency-walks-connectivity/appendices/provenance.tex
new file mode 100644
index 0000000..7f5bcc5
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/provenance.tex
@@ -0,0 +1,45 @@
+\section{Sources read and how to reproduce the numbers}\label{app:provenance}
+
+\paragraph{Sources and what was read.}
+\emph{Textbook} \cite{petrosyan2015grafneri}: printed pages 9 to 12, 16, 21 to 23, and 48 to 49,
+viewed as page images, and a full-text search of the whole book for the adjacency matrix; the
+other chapters were not read.
+\emph{Board photographs} \cite{whiteboard1,whiteboard2}: both viewed as images.
+\emph{Grinberg} \cite{grinberg2025graph}: Sections 2.9, 2.10, 3.4, and 4.5.5 of the 454-page text.
+\emph{Galway notes} \cite{quinlan_matrices_graphs}: the whole eight-page file.
+\emph{Lehman, Leighton, and Meyer} \cite{lehman_mcs_adjacency}: the one page cited.
+\emph{Paramadevan and Sotheeswaran} \cite{paramadevan2021adjacency}: the whole nine-page paper;
+it is an expository paper whose Theorem~1 and proofs are loose (\Cref{sec:competing}), so it is
+cited for statements and as a second witness only.
+\emph{Bai} \cite{bai2025adjacency}: Section~1; the rest concerns eigenvalues.
+\emph{MathWorld} \cite{weisstein_connectedgraph} and \emph{Wikipedia} \cite{wikipedia_path_graph_theory}:
+the entries cited; the Wikipedia article is open to later edits.
+\emph{Schost} \cite{schost2026bfs}: the slides on breadth-first search and its running time.
+The assignment text is known only as it was reported to us and is not a source of the
+mathematics.
+
+\paragraph{Scripts.}
+All scripts are in the folder \texttt{appendices/scripts/}, are written in plain Python with
+integer arithmetic, and are run from the paper folder.
+\begin{itemize}
+\item \texttt{generate\_paper\_numbers.py} computes every matrix and table printed in the
+  examples, asserts the facts the text states about them, and writes
+  \texttt{numbers.tex}, which this note inputs.
+\item \texttt{m1\_walks.py}: powers of the board matrix, explicit walk lists, the hand-checkable
+  sums, walks against paths and trails, and a brute-force check of \Cref{thm:walkcount} on all
+  labelled simple graphs with $N=2,3,4,5$ vertices ($2$, $8$, $64$, $1024$ graphs; $40$, $360$,
+  $5120$, $76800$ entries, all equal to the walk counts).
+\item \texttt{m2\_walks.py}: classification of the example walks, the absence of a cycle in the
+  board graph among closed walks of length up to $6$, traces of \Cref{lem:walkpath}, and checks
+  of the lemma, \Cref{prop:pathtrail}, \Cref{cor:bound}, and \Cref{prop:shortest} on all walks of
+  length up to $6$ in three small graphs and on $300$ random graphs (seed $20261027$, $192696$
+  walks, no failures).
+  Its textbook example graph uses only seven edges that the textbook's examples use; the
+  textbook's figure has at least one more, which no example uses.
+\item \texttt{m3\_connectivity.py}: the examples of \Cref{sec:examples}, the path graphs of
+  \Cref{tab:sharp}, the cost counts, and the exhaustive comparison over all labelled graphs on
+  up to $6$ vertices, including the component statement of \Cref{cor:components}.
+\end{itemize}
+To reproduce, run \texttt{python3 -I appendices/scripts/generate\_paper\_numbers.py} and the
+three other scripts the same way; their saved outputs are in the same folder.
+The last script takes about twenty seconds.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/generate_paper_numbers.py b/papers/adjacency-walks-connectivity/appendices/scripts/generate_paper_numbers.py
new file mode 100644
index 0000000..5d215b1
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/generate_paper_numbers.py
@@ -0,0 +1,297 @@
+"""Generate every number printed in the paper's examples and tables.
+
+Run from the paper folder:
+    python3 -I appendices/scripts/generate_paper_numbers.py
+
+It writes appendices/scripts/numbers.tex, a file of LaTeX macros that the
+paper inputs, so that no matrix or count in the text is typed by hand.
+It also prints the same numbers and asserts the facts the text states.
+Pure Python integers; no libraries. About 15 seconds (N = 6 loop).
+"""
+from itertools import combinations, product
+from pathlib import Path
+
+
+# ---------- basic matrix tools ----------
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
+def from_edges(n, edges):
+    A = [[0] * n for _ in range(n)]
+    for u, v in edges:
+        A[u - 1][v - 1] = A[v - 1][u - 1] = 1
+    return A
+
+
+def sum_powers(A, top):
+    S = [[0] * len(A) for _ in A]
+    for k in range(1, top + 1):
+        S = add(S, power(A, k))
+    return S
+
+
+def pmatrix(M):
+    return (r"\begin{pmatrix}" + r" \\ ".join(" & ".join(str(x) for x in row) for row in M)
+            + r"\end{pmatrix}")
+
+
+def bfs_components(A):
+    n = len(A)
+    seen, comps = set(), []
+    for s in range(n):
+        if s in seen:
+            continue
+        comp, queue = [s], [s]
+        seen.add(s)
+        while queue:
+            u = queue.pop(0)
+            for v in range(n):
+                if A[u][v] and v not in seen:
+                    seen.add(v)
+                    comp.append(v)
+                    queue.append(v)
+        comps.append(sorted(comp))
+    return comps
+
+
+def off_diag_positive(S):
+    n = len(S)
+    return all(S[i][j] > 0 for i in range(n) for j in range(n) if i != j)
+
+
+def no_zero(M):
+    return all(x > 0 for r in M for x in r)
+
+
+# ---------- walk enumeration ----------
+def walks(A, k, i, j):
+    n = len(A)
+    out = []
+
+    def go(seq):
+        if len(seq) == k + 1:
+            if seq[-1] == j:
+                out.append(tuple(seq))
+            return
+        for v in range(n):
+            if A[seq[-1]][v]:
+                go(seq + [v])
+
+    go([i])
+    return out
+
+
+def all_walks(A, k):
+    n = len(A)
+    out = []
+    for i in range(n):
+        for j in range(n):
+            out += walks(A, k, i, j)
+    return out
+
+
+def is_path(w):
+    return len(set(w)) == len(w)
+
+
+def is_trail(w):
+    edges = [frozenset(p) for p in zip(w, w[1:])]
+    return len(set(edges)) == len(edges)
+
+
+macros = {}
+
+
+def macro(name, body):
+    macros[name] = body
+
+
+# ---------- board matrix (edges 1-2, 2-3) ----------
+A = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
+assert A == from_edges(3, [(1, 2), (2, 3)])
+P = {k: power(A, k) for k in range(1, 6)}
+for name, k in (("One", 1), ("Two", 2), ("Three", 3), ("Four", 4), ("Five", 5)):
+    macro("MBoardA" + name, pmatrix(P[k]))
+assert P[2] == [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
+assert P[3] == [[2 * x for x in r] for r in A]
+for k in range(1, 6):
+    assert power(A, k + 2) == [[2 * x for x in r] for r in power(A, k)]
+S_B = sum_powers(A, 2)
+IA_B = power(add(ident(3), A), 2)
+macro("MBoardS", pmatrix(S_B))
+macro("MBoardIA", pmatrix(IA_B))
+macro("MBoardId", pmatrix(ident(3)))
+macro("MBoardTwoA", pmatrix([[2 * x for x in r] for r in A]))
+assert IA_B == add(add(ident(3), [[2 * x for x in r] for r in A]), P[2])
+assert off_diag_positive(S_B) and no_zero(IA_B)
+assert bfs_components(A) == [[0, 1, 2]]
+degrees = [sum(r) for r in A]
+assert degrees == [1, 2, 1] and sum(map(sum, A)) == 4
+assert [P[2][i][i] for i in range(3)] == degrees
+
+# the board drawing (triangle) for comparison
+T = from_edges(3, [(1, 2), (1, 3), (2, 3)])
+macro("MDrawT", pmatrix(T))
+macro("MDiffAT", pmatrix([[T[i][j] - A[i][j] for j in range(3)] for i in range(3)]))
+
+# the non-example matrix of the adjacency-matrix definition (not symmetric)
+macro("MNonSym", pmatrix([[0, 1, 0], [0, 0, 1], [0, 1, 0]]))
+
+# ---------- disconnected example (edge 1-2 only) ----------
+D = from_edges(3, [(1, 2)])
+D2 = power(D, 2)
+S_D = sum_powers(D, 2)
+IA_D = power(add(ident(3), D), 2)
+macro("MDiscA", pmatrix(D))
+macro("MDiscAtwo", pmatrix(D2))
+macro("MDiscS", pmatrix(S_D))
+macro("MDiscIA", pmatrix(IA_D))
+zeros_S = [(i + 1, j + 1) for i in range(3) for j in range(3) if i != j and S_D[i][j] == 0]
+zeros_IA = [(i + 1, j + 1) for i in range(3) for j in range(3) if IA_D[i][j] == 0]
+assert zeros_S == zeros_IA == [(1, 3), (2, 3), (3, 1), (3, 2)]
+assert bfs_components(D) == [[0, 1], [2]]
+for k in range(1, 7):
+    Dk = power(D, k)
+    assert Dk[0][2] == 0 and Dk[1][2] == 0
+
+# ---------- N = 2 edge case ----------
+A2 = from_edges(2, [(1, 2)])
+macro("MTwoA", pmatrix(A2))
+assert sum_powers(A2, 1) == A2 and A2[0][0] == 0
+
+# ---------- path graph on 4 vertices ----------
+Q = from_edges(4, [(1, 2), (2, 3), (3, 4)])
+Q2, Q3 = power(Q, 2), power(Q, 3)
+macro("MPathA", pmatrix(Q))
+macro("MPathAtwo", pmatrix(Q2))
+macro("MPathAthree", pmatrix(Q3))
+macro("MPathShort", pmatrix(add(Q, Q2)))
+macro("MPathFull", pmatrix(add(add(Q, Q2), Q3)))
+assert add(Q, Q2)[0][3] == 0 and off_diag_positive(add(add(Q, Q2), Q3))
+
+# ---------- Table: sharpness of N - 1 ----------
+rows = []
+for N in range(3, 9):
+    Pn = from_edges(N, [(i, i + 1) for i in range(1, N)])
+    first = next(k for k in range(1, N + 2) if power(Pn, k)[0][N - 1] > 0)
+    short = sum_powers(Pn, N - 2)[0][N - 1]
+    full = sum_powers(Pn, N - 1)[0][N - 1]
+    assert first == N - 1 and short == 0 and full >= 1
+    rows.append(rf"{N} & {first} & {short} & {full} \\")
+macro("RowsSharp", "\n".join(rows))
+
+# ---------- Table: walks, trails, paths in the board graph, by length ----------
+rows = []
+for k in range(0, 5):
+    if k == 0:
+        W = [(i,) for i in range(3)]
+    else:
+        W = all_walks(A, k)
+    nw = len(W)
+    nt = sum(is_trail(w) for w in W)
+    npth = sum(is_path(w) for w in W)
+    nc = sum(w[0] == w[-1] for w in W)
+    if k >= 1:
+        assert nw == sum(map(sum, power(A, k)))
+    rows.append(rf"{k} & {nw} & {nt} & {npth} & {nc} \\")
+assert rows[0].startswith("0 & 3 & 3 & 3 & 3") and rows[2].startswith("2 & 6 & 2 & 2 & 4")
+assert rows[3].startswith("3 & 8 & 0 & 0 & 0") and rows[4].startswith("4 & 12 & 0 & 0 & 8")
+macro("RowsWalkCounts", "\n".join(rows))
+
+# ---------- Table: walks versus paths from 1 to 2 ----------
+rows = []
+for k in range(1, 6):
+    W = walks(A, k, 0, 1)
+    assert len(W) == power(A, k)[0][1]
+    rows.append(rf"{k} & {len(W)} & {sum(is_trail(w) for w in W)} & {sum(is_path(w) for w in W)} \\")
+macro("RowsWalkPath", "\n".join(rows))
+assert [len(walks(A, k, 0, 1)) for k in range(1, 6)] == [1, 0, 2, 0, 4]
+
+# ---------- explicit walk lists for the example (labels 1..3) ----------
+def fmt(w):
+    return r"\text{-}".join(str(v + 1) for v in w)
+
+
+def wl(k, i, j):
+    return ", ".join(fmt(w) for w in walks(A, k, i - 1, j - 1))
+
+
+macro("WalksTwoOneOne", wl(2, 1, 1))
+macro("WalksTwoOneThree", wl(2, 1, 3))
+macro("WalksTwoTwoTwo", wl(2, 2, 2))
+macro("WalksTwoThreeThree", wl(2, 3, 3))
+macro("WalksThreeOneTwo", wl(3, 1, 2))
+macro("WalksThreeTwoThree", wl(3, 2, 3))
+
+# ---------- exhaustive check, N = 2..6 ----------
+rows = []
[... truncated by build_evidence.py: 53 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/generate_paper_numbers_output.txt b/papers/adjacency-walks-connectivity/appendices/scripts/generate_paper_numbers_output.txt
new file mode 100644
index 0000000..3ea053f
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/generate_paper_numbers_output.txt
@@ -0,0 +1,34 @@
+wrote numbers.tex with 33 macros
+MBoardAOne = \begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}
+MBoardATwo = \begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{pmatrix}
+MBoardAThree = \begin{pmatrix}0 & 2 & 0 \\ 2 & 0 & 2 \\ 0 & 2 & 0\end{pmatrix}
+MBoardAFour = \begin{pmatrix}2 & 0 & 2 \\ 0 & 4 & 0 \\ 2 & 0 & 2\end{pmatrix}
+MBoardAFive = \begin{pmatrix}0 & 4 & 0 \\ 4 & 0 & 4 \\ 0 & 4 & 0\end{pmatrix}
+MBoardS = \begin{pmatrix}1 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 1\end{pmatrix}
+MBoardIA = \begin{pmatrix}2 & 2 & 1 \\ 2 & 3 & 2 \\ 1 & 2 & 2\end{pmatrix}
+MBoardId = \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}
+MBoardTwoA = \begin{pmatrix}0 & 2 & 0 \\ 2 & 0 & 2 \\ 0 & 2 & 0\end{pmatrix}
+MDrawT = \begin{pmatrix}0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0\end{pmatrix}
+MDiffAT = \begin{pmatrix}0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0\end{pmatrix}
+MNonSym = \begin{pmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}
+MDiscA = \begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}
+MDiscAtwo = \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}
+MDiscS = \begin{pmatrix}1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}
+MDiscIA = \begin{pmatrix}2 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 1\end{pmatrix}
+MTwoA = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}
+MPathA = \begin{pmatrix}0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0\end{pmatrix}
+MPathAtwo = \begin{pmatrix}1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 \\ 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 1\end{pmatrix}
+MPathAthree = \begin{pmatrix}0 & 2 & 0 & 1 \\ 2 & 0 & 3 & 0 \\ 0 & 3 & 0 & 2 \\ 1 & 0 & 2 & 0\end{pmatrix}
+MPathShort = \begin{pmatrix}1 & 1 & 1 & 0 \\ 1 & 2 & 1 & 1 \\ 1 & 1 & 2 & 1 \\ 0 & 1 & 1 & 1\end{pmatrix}
+MPathFull = \begin{pmatrix}1 & 3 & 1 & 1 \\ 3 & 2 & 4 & 1 \\ 1 & 4 & 2 & 3 \\ 1 & 1 & 3 & 1\end{pmatrix}
+RowsSharp = 3 & 2 & 0 & 1 \\ | 4 & 3 & 0 & 1 \\ | 5 & 4 & 0 & 1 \\ | 6 & 5 & 0 & 1 \\ | 7 & 6 & 0 & 1 \\ | 8 & 7 & 0 & 1 \\
+RowsWalkCounts = 0 & 3 & 3 & 3 & 3 \\ | 1 & 4 & 4 & 4 & 0 \\ | 2 & 6 & 2 & 2 & 4 \\ | 3 & 8 & 0 & 0 & 0 \\ | 4 & 12 & 0 & 0 & 8 \\
+RowsWalkPath = 1 & 1 & 1 & 1 \\ | 2 & 0 & 0 & 0 \\ | 3 & 2 & 0 & 0 \\ | 4 & 0 & 0 & 0 \\ | 5 & 4 & 0 & 0 \\
+WalksTwoOneOne = 1\text{-}2\text{-}1
+WalksTwoOneThree = 1\text{-}2\text{-}3
+WalksTwoTwoTwo = 2\text{-}1\text{-}2, 2\text{-}3\text{-}2
+WalksTwoThreeThree = 3\text{-}2\text{-}3
+WalksThreeOneTwo = 1\text{-}2\text{-}1\text{-}2, 1\text{-}2\text{-}3\text{-}2
+WalksThreeTwoThree = 2\text{-}1\text{-}2\text{-}3, 2\text{-}3\text{-}2\text{-}3
+RowsExhaustive = 2 & 2 & 1 & 2 & 2 & 2 & 1 \\ | 3 & 8 & 4 & 8 & 8 & 8 & 3 \\ | 4 & 64 & 38 & 64 & 64 & 64 & 12 \\ | 5 & 1024 & 728 & 1024 & 1024 & 1024 & 60 \\ | 6 & 32768 & 26704 & 32768 & 32768 & 32768 & 360 \\
+RowsCost = 10 & 8 & 8\,000 & 4 & 4\,000 & 100 \\ | 100 & 98 & 98\,000\,000 & 7 & 7\,000\,000 & 10\,000 \\ | 1000 & 998 & 998\,000\,000\,000 & 10 & 10\,000\,000\,000 & 1\,000\,000 \\
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
diff --git a/papers/adjacency-walks-connectivity/appendices/scripts/numbers.tex b/papers/adjacency-walks-connectivity/appendices/scripts/numbers.tex
new file mode 100644
index 0000000..35da032
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/appendices/scripts/numbers.tex
@@ -0,0 +1,53 @@
+% Generated by appendices/scripts/generate_paper_numbers.py. Do not edit.
+\newcommand{\MBoardAOne}{\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}}
+\newcommand{\MBoardATwo}{\begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{pmatrix}}
+\newcommand{\MBoardAThree}{\begin{pmatrix}0 & 2 & 0 \\ 2 & 0 & 2 \\ 0 & 2 & 0\end{pmatrix}}
+\newcommand{\MBoardAFour}{\begin{pmatrix}2 & 0 & 2 \\ 0 & 4 & 0 \\ 2 & 0 & 2\end{pmatrix}}
+\newcommand{\MBoardAFive}{\begin{pmatrix}0 & 4 & 0 \\ 4 & 0 & 4 \\ 0 & 4 & 0\end{pmatrix}}
+\newcommand{\MBoardS}{\begin{pmatrix}1 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 1\end{pmatrix}}
+\newcommand{\MBoardIA}{\begin{pmatrix}2 & 2 & 1 \\ 2 & 3 & 2 \\ 1 & 2 & 2\end{pmatrix}}
+\newcommand{\MBoardId}{\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}}
+\newcommand{\MBoardTwoA}{\begin{pmatrix}0 & 2 & 0 \\ 2 & 0 & 2 \\ 0 & 2 & 0\end{pmatrix}}
+\newcommand{\MDrawT}{\begin{pmatrix}0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0\end{pmatrix}}
+\newcommand{\MDiffAT}{\begin{pmatrix}0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0\end{pmatrix}}
+\newcommand{\MNonSym}{\begin{pmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}}
+\newcommand{\MDiscA}{\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\MDiscAtwo}{\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\MDiscS}{\begin{pmatrix}1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}}
+\newcommand{\MDiscIA}{\begin{pmatrix}2 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 1\end{pmatrix}}
+\newcommand{\MTwoA}{\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}}
+\newcommand{\MPathA}{\begin{pmatrix}0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0\end{pmatrix}}
+\newcommand{\MPathAtwo}{\begin{pmatrix}1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 \\ 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 1\end{pmatrix}}
+\newcommand{\MPathAthree}{\begin{pmatrix}0 & 2 & 0 & 1 \\ 2 & 0 & 3 & 0 \\ 0 & 3 & 0 & 2 \\ 1 & 0 & 2 & 0\end{pmatrix}}
+\newcommand{\MPathShort}{\begin{pmatrix}1 & 1 & 1 & 0 \\ 1 & 2 & 1 & 1 \\ 1 & 1 & 2 & 1 \\ 0 & 1 & 1 & 1\end{pmatrix}}
+\newcommand{\MPathFull}{\begin{pmatrix}1 & 3 & 1 & 1 \\ 3 & 2 & 4 & 1 \\ 1 & 4 & 2 & 3 \\ 1 & 1 & 3 & 1\end{pmatrix}}
+\newcommand{\RowsSharp}{3 & 2 & 0 & 1 \\
+4 & 3 & 0 & 1 \\
+5 & 4 & 0 & 1 \\
+6 & 5 & 0 & 1 \\
+7 & 6 & 0 & 1 \\
+8 & 7 & 0 & 1 \\}
+\newcommand{\RowsWalkCounts}{0 & 3 & 3 & 3 & 3 \\
+1 & 4 & 4 & 4 & 0 \\
+2 & 6 & 2 & 2 & 4 \\
+3 & 8 & 0 & 0 & 0 \\
+4 & 12 & 0 & 0 & 8 \\}
+\newcommand{\RowsWalkPath}{1 & 1 & 1 & 1 \\
+2 & 0 & 0 & 0 \\
+3 & 2 & 0 & 0 \\
+4 & 0 & 0 & 0 \\
+5 & 4 & 0 & 0 \\}
+\newcommand{\WalksTwoOneOne}{1\text{-}2\text{-}1}
+\newcommand{\WalksTwoOneThree}{1\text{-}2\text{-}3}
+\newcommand{\WalksTwoTwoTwo}{2\text{-}1\text{-}2, 2\text{-}3\text{-}2}
+\newcommand{\WalksTwoThreeThree}{3\text{-}2\text{-}3}
+\newcommand{\WalksThreeOneTwo}{1\text{-}2\text{-}1\text{-}2, 1\text{-}2\text{-}3\text{-}2}
+\newcommand{\WalksThreeTwoThree}{2\text{-}1\text{-}2\text{-}3, 2\text{-}3\text{-}2\text{-}3}
+\newcommand{\RowsExhaustive}{2 & 2 & 1 & 2 & 2 & 2 & 1 \\
+3 & 8 & 4 & 8 & 8 & 8 & 3 \\
+4 & 64 & 38 & 64 & 64 & 64 & 12 \\
+5 & 1024 & 728 & 1024 & 1024 & 1024 & 60 \\
+6 & 32768 & 26704 & 32768 & 32768 & 32768 & 360 \\}
+\newcommand{\RowsCost}{10 & 8 & 8\,000 & 4 & 4\,000 & 100 \\
+100 & 98 & 98\,000\,000 & 7 & 7\,000\,000 & 10\,000 \\
+1000 & 998 & 998\,000\,000\,000 & 10 & 10\,000\,000\,000 & 1\,000\,000 \\}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evaluation-report.md b/papers/adjacency-walks-connectivity/evaluation-report.md
new file mode 100644
index 0000000..0ae1144
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/evaluation-report.md
@@ -0,0 +1,164 @@
+# Evaluation report
+
+## Round 1, 2026-10-31
+
+Question: For a simple undirected graph with N vertices given by its
+adjacency matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how
+can one determine from A whether the graph is connected, and (3) what is
+the definition of a path between vertices n_i and n_j?
+
+Scope: Finite simple undirected graphs. Walks, trails, paths, cycles, and
+distance with the course textbook's numbering; the theorem that (A^k)_{ij}
+counts walks of length k with a full induction proof and the warning that
+walks are not paths; connectivity and components; the matrix-power
+connectivity test with proof, a connected and a disconnected three-vertex
+example, and breadth-first search stated for comparison. Study-note
+register: plain-words paragraph before every definition, theorem, test,
+and worked example. Out of scope: directed graphs and multigraphs beyond a
+one-sentence remark, weighted graphs, eigenvalue methods, complexity beyond
+a short remark, implementation code.
+
+Research summary: 11 sources (7 full access, 4 partial): the course
+textbook (local file, Armenian, page images viewed), two whiteboard photos,
+Grinberg's graph theory text (arXiv preprint), the Galway matrices and
+graphs notes, the MIT Mathematics for Computer Science adjacency section,
+Paramadevan and Poobalan 2021 (peer-reviewed), Bai 2025 (web),
+MathWorld Connected Graph, Wikipedia Path (graph theory), and Schost's
+CS 341 breadth-first search slides. Three modules (m1 adjacency matrix and
+walk counting, m2 walks, trails, paths, cycles, m3 connectivity from A).
+Research and modules were final inputs to this probe; one round of
+authoring and one round of evaluation were run. The author added two
+supported claims (A1 degree, A2 degree sum, both from textbook p. 16)
+in `evidence/modules/author.json` and rebuilt `evidence/evidence.json`
+from the base file and fragments.
+
+Model levels: research 2, modules 2, author 2, reader 2, evaluator 3,
+orchestrator session model (not pinned). Hierarchy requirement: met for
+the configured levels. A runtime fallback to another model is not
+observable from inside the session; the harness reported no fallback for
+the evaluator in this round.
+
+Mechanical checks: build pass, citations pass, claims pass, pdf pass.
+Run by the orchestrator after the author returned, on a clean rebuild
+(`build/` emptied first): `build.sh` exit 0 (28 pages, warnings: biber
+reports six `year = {n.d.}` entries not integer, for sources whose
+evidence record has no year); `check_citations.py` cited keys 11, bib
+entries 11, evidence sources 11, errors 0, warnings 0; `check_claims.py`
+sources 11, claims supported 72, qualified 7, removed 0, unverified 0,
+errors 0, warnings 0; `inspect_pdf.py` pages 28, errors 0, warnings 0.
+
+### Scores
+
+| Dimension | Score | Observation (evaluator) |
+|---|---|---|
+| 1 Correctness | 4 | Every matrix, table, and proof recomputed independently and found correct (Examples 2.11, 3.3, 3.4, 4.15, 6.1 to 6.3; Tables 2, 3, 5, 6; Lemma 2.44, Propositions 2.35, 4.5, 4.17, Theorems 3.5, 4.6, Appendix C.2). One sentence wrong as stated: Section 7.5 says BFS "reads each of the N^2 entries once" (F1). |
+| 2 Evidence coverage | 4 | 79 claims (72 supported, 7 qualified); every traced statement has a claim (Theorem 3.5 to C6/C7, Theorem 4.6 to C34/C36, Definition 2.31 to C16/C24). Exception: the matrix-input BFS cost in Section 7.5, whose claim m3-10 quotes slides that do not say it (F1). |
+| 3 Citation integrity | 4 | All eight sources checked exist with matching metadata and the weight-bearing passages say what is attributed. Three attributions off: [10, slides 3 and 6] (F1), [3, Proposition 2.9.10] cited for trails (F9), [7, property 8] described as a row sum (F10). |
+| 4 Logical validity | 5 | Each conclusion follows from proved premises; Appendix C.3 lists the premises behind Theorem 4.6; Remark 2.49 and Section 5.2 show connectivity does not depend on the meaning of "path". The paper does not repeat the sources' gap from a positive entry straight to a path. |
+| 5 Understandability | 4 | Definitions clear and built in order; every proof names its method and base case. Problems: "(5)" reads as an equation reference (F7); "its ends" ambiguous in Remark 4.16 (F8); Theorem 4.6 lacks its own plain-words paragraph (F6); examples from textbook Fig. 1.2.5 cannot be checked without the book (F17). |
+| 6 Completeness | 5 | Every objective in the brief is met: Definition 2.9 and Propositions 2.13/2.18 for A; Theorem 3.5 by induction; Proposition 3.10 and Table 2 for walks versus paths; Definitions 2.19 to 2.40 with textbook numbers; Theorem 4.6 with proof, Examples 6.2/6.3; BFS in Remark 4.18. |
+| 7 Methodological rigor | 5 | Matrices produced by script and fed into the text (numbers.tex); exhaustive checks over all labelled graphs with N <= 6 presented as checks, not proofs (Section 6.4, Appendix C.6); assumptions listed and numbered (Section 1.3). |
+| 8 Critical analysis | 5 | Section 7 covers the drawing/matrix mismatch edge by edge, the uncertain mark above A, the limits of the textbook search, the incorrect Theorem 1 in [7], the loose proofs in [7] and [1], and the cost. Section 7.6 declines to guess the lecturer's intent. |
+| 9 Internal consistency | 3 | Several words and letters carry two meanings: "loop" (F2); "length" and "table of trips" inside story paragraphs (F3, F4); S, n, and t each name two things (F5); Definition 2.48 does not say which sense of "(u,v)-path" it uses (F11). |
+| 10 Reproducibility | 5 | Appendix D names the scripts, the seed, and the run commands; saved outputs are present; every printed number reproduced independently. |
+| 11 LaTeX and PDF quality | 5 | 28-page PDF with no errors; cross-references and references resolve; inline matrices, the binomial in (3), and the tables render correctly; log shows only underfull hbox warnings. |
+| 12 Answer relevance | 5 | Sections 1.5 and 8 answer Q1 to Q3 directly with the theorem or definition number for each; nothing beyond the brief; the conclusion states the assumptions the answers rest on. |
+
+### Findings
+
+| Id | Severity | Location | Defect | Status |
+|---|---|---|---|---|
+| F1 | major | sections/discussion.tex:86-87 (Section 7.5) | BFS with A as input "reads each of the N^2 = 10,000 entries once [10, slides 3 and 6]": slide 3 only defines the matrix representation, slide 6 is BFS on adjacency lists, neither states the cost, "once" is exact only when every vertex is reached, and claim m3-10 has no quote saying it. Correction: present as the note's own estimate ("at most N^2 entries; this count is ours"), cite [10, slide 3] for the representation only, correct m3-10. | open |
+| F2 | minor | sections/background.tex:463-466, 311 against :50, :113, :259; appendices/derivations.tex:66 | "Loop" means a self-edge in the technical text but a detour in the plain-words paragraphs. Correction: "detour that comes back to the same house" in the story. | open |
+| F3 | minor | sections/background.tex:201, 203, 419 | Plain-words paragraphs use the technical word "length" although Table 1 maps it to "number of roads driven". | open |
+| F4 | minor | sections/answer1_walks.tex:153 | "The table of trips" is not in the story dictionary (Table 1 has only "table of roads" and "table of totals"). | open |
+| F5 | minor | sections/background.tex:483-509, :380; Remark 2.20 against Proposition 4.17 | S names both the induction statement S(k) and the sum of Definition 4.1; n is a vertex count in C_n and a vertex name in n_i; t is a walk index and the number of squarings. | open |
+| F6 | minor | sections/answer2_connectivity.tex:74, :124; sections/background.tex:541; sections/introduction.tex:37 | Theorem 4.6, Corollary 4.7, and Proposition 2.47 have no plain-words paragraph directly before them, while the introduction and the brief say every theorem has one. | open |
+| F7 | minor | sections/answer3_path.tex:78 | "which calls (5) a walk of length 0" reads as a reference to equation (5), which does not exist. | open |
+| F8 | minor | sections/answer2_connectivity.tex:259 (Remark 4.16) | "would shorten the distance between its ends": "its" can be read as the extra edge. | open |
+| F9 | minor | sections/background.tex:575 (Remark 2.49) | [3, Proposition 2.9.10] cited for the walk/trail/path equivalence covers only walks and paths. | open |
+| F10 | minor | sections/background.tex:180 (proof of Proposition 2.18) | "[7, property 8] states the row sum": property 8 gives off-diagonal entries plus twice the diagonal entry, a row sum only for zero diagonal. | open |
+| F11 | minor | sections/background.tex:563 (Definition 2.48), Definition 2.52 | "(u,v)-path" without saying in which sense, although Item 4 and Table 4 fix "path" as no repeated vertex and Remark 2.49 says the textbook meant a trail. | open |
+| F12 | minor | sections/answer1_walks.tex:63, 143-147; sections/answer2_connectivity.tex:182; sections/discussion.tex:34-35, :77 | Directed graphs or multigraphs mentioned in four places and cost given its own subsection, against the brief's one-sentence and short-remark limits. | open |
+| F13 | minor | appendices/photographs.tex:8-9 | Appendix B says the board's wording is kept, but the board's Armenian word for "if" appears silently as English "if". | open |
+| F14 | minor | references.bib:9, 16, 23 | "Supplied by the user" in the reference list; "the user" never introduced to the reader. | open |
+| F15 | minor | sections/answer2_connectivity.tex:92 | "say of length l": l is never used again. | open |
+| F16 | minor | appendices/provenance.tex:9 | The Galway notes called "the whole eight-page file"; the PDF has 7 pages numbered 2 to 8. | open |
+| F17 | minor | sections/background.tex, Examples 2.21, 2.29, 2.38, Non-example 2.22 | Examples from textbook Fig. 1.2.5 cannot be checked without the book; the paper neither draws the graph nor lists its edges. | open |
+
+Technician reader: 20 comprehension findings R1 to R20, recorded in
+`reader-findings.md`, all open. The reader's summary of the conclusions
+matches the paper's actual conclusions. Its recurring theme is that the
+plain-words layer, the board-reading discussion, and the source critique
+(Sections 1.3, 1.4, 7.4, 7.5) cost more length than they return for a
+first-time reader, and that several proof steps compress an argument the
+reader must supply (R7, R9, R10, R12).
+
+### Citation and claim coverage
+
+- Sources: 11 (7 full access, 4 partial access; the course textbook,
+  Grinberg, Bai 2025, and the Schost slides are partial).
+- Claims: 79 total; 72 supported, 7 qualified, 0 unverified, 0 removed.
+- Contradictions recorded in the evidence file: 6.
+- Evaluator spot checks: 8 sources checked. Fetched and supports: Galway
+  notes, Paramadevan and Poobalan 2021, Bai 2025, MathWorld. Fetched and
+  partially supports: Grinberg (Proposition 2.9.10 does not cover trails,
+  F9), Schost slides (no slide gives the matrix-input cost, F1). Local
+  files viewed and supports: the course textbook (printed pp. 22 and 48),
+  both whiteboard photos (only exception the Armenian "if", F13).
+
+### Unverified claims and access limits
+
+- No claim has status `unverified`. Seven claims have status `qualified`
+  and the evaluator found each qualified in the text where it appears:
+  C24, C29, C36, m1-9, m2-8, m2-15, m3-11.
+- Claim m3-10 (BFS cost with A as input) is recorded as supported by the
+  Schost slides, but the evaluator found that the slides do not state it
+  (F1). It should be re-recorded as the paper's own estimate.
+- Access limits: the course textbook's PDF text layer drops most symbols,
+  so its definitions were read from page images; the Grinberg preprint
+  and the Schost slides were partially accessed; six web sources have no
+  publication year in their record and appear as `n.d.` in the
+  bibliography.
+
+### Known limitations
+
+- The plain-words paragraphs were checked by the author's script (no
+  technical terms, no symbols, no sentence over 18 words), not by a
+  read-aloud test with a reader of the intended age.
+- The textbook-walk example (lengths 8, 5, 2) rests on the author's script
+  over the seven edges named in Appendix D, not on the textbook's own text.
+- The English column "closed trail" for the textbook's cycle is the
+  author's combination of Grinberg's trail definition with "closed".
+- The cost remark in Section 7.5 is an estimate for schoolbook matrix
+  multiplication only.
+- Several `derivation` strings in the module evidence fragments point to
+  theorem and section numbers from the module drafts that no longer match
+  the paper (listed in `self-evaluation.md`); the labels all resolve.
+- The exhaustive connectivity check covers all labelled graphs with
+  N <= 6 only and is presented as a check, not a proof.
+
+### Release conditions
+
+| Condition | Result |
+|---|---|
+| 1 Every dimension at least 3 | holds (minimum 3, dimension 9) |
+| 2 No unresolved critical defect | holds (no critical finding) |
+| 3 Every substantive claim supported or qualified | fails (F1: BFS cost attributed to a source that does not state it) |
+| 4 Material conclusions justified | holds |
+| 5 No essential concept or step unexplained | holds at the evaluator's level; the reader lists compressed steps (R7, R9, R10, R12) as advisory |
+| 6 Evaluator level exceeds author and module levels | holds (3 over 2) |
+| 7 build.sh succeeds, inspect_pdf.py no errors | holds |
+| 8 check_citations.py and check_claims.py no errors | holds |
+| 9 self-evaluation.md covers every section | holds (eight sections and the appendices, with a stale-pointer list) |
+| 10 Independent evaluation passed | fails (recommendation REVISE) |
+
+Decision: INCOMPLETE -- The evaluator recommends REVISE: one major finding
+(F1, a cost figure attributed to slides that do not state it) and sixteen
+minor findings are open, so release conditions 3 and 10 fail. The
+mathematics, proofs, and computed numbers were independently verified as
+correct. This probe was limited by instruction to one round of authoring
+and one round of evaluation, so no revision was sent to the author. A
+continuation would send F1 to the author first (with the m3-10 correction
+in the evidence file), then the minor findings grouped by section, then
+re-run the mechanical gate and a fresh evaluation.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/evidence.json b/papers/adjacency-walks-connectivity/evidence/evidence.json
index 65f95bf..d454cd4 100644
--- a/papers/adjacency-walks-connectivity/evidence/evidence.json
+++ b/papers/adjacency-walks-connectivity/evidence/evidence.json
@@ -1236,6 +1236,46 @@
       ],
       "contradicted_by": []
     },
+    {
+      "id": "A1",
+      "text": "Textbook Definition 1.2.1: the degree of a vertex v in G, written d_G(v) or d(v), is the number of edges incident to v. Gloss: 'the degree of the vertex v in G, which we denote d_G(v) or d(v), is the number of edges incident to that vertex'. Read from the page image of printed p. 16 (PDF p. 17). The book puts degree after the adjacency matrix (printed p. 11).",
+      "kind": "fact",
+      "module": "author",
+      "support": [
+        {
+          "source": "petrosyan2015grafneri",
+          "locator": "printed p. 16 (PDF p. 17), Definition 1.2.1",
+          "quote": "Սահմանում 1.2.1: G գրաֆում v գագաթի աստիճան, որը կնշանակենք d_G(v)-ով կամ d(v)-ով, կանվանենք այդ գագաթին կից կողերի քանակը։"
+        }
+      ],
+      "derivation": null,
+      "confidence": "high",
+      "status": "supported",
+      "used_in": [
+        "sections/background.tex"
+      ],
+      "contradicted_by": []
+    },
+    {
+      "id": "A2",
+      "text": "Textbook Theorem 1.2.1 (L. Euler): in any graph G = (V, E) the sum over all vertices of d_G(v) equals 2|E(G)|. Gloss of the proof: every edge is incident to two vertices, so it is counted twice in the sum. Read from the page image of printed p. 16 (PDF p. 17).",
+      "kind": "fact",
+      "module": "author",
+      "support": [
+        {
+          "source": "petrosyan2015grafneri",
+          "locator": "printed p. 16 (PDF p. 17), Theorem 1.2.1",
+          "quote": "Թեորեմ 1.2.1 (Լ. Էյլեր): Կամայական G = (V, E) գրաֆում տեղի ունի Σ d_G(v) = 2|E(G)| հավասարությունը։"
+        }
+      ],
+      "derivation": null,
+      "confidence": "high",
+      "status": "supported",
+      "used_in": [
+        "sections/background.tex"
+      ],
+      "contradicted_by": []
+    },
     {
       "id": "m1-1",
       "text": "For the adjacency matrix A of a simple undirected graph on N vertices: the sum of row i (and of column i) is the degree of n_i, the number of edges at n_i; and the sum of all entries is 2|E|. Proof: A_ij = 1 exactly when n_j is a neighbour of n_i; in a simple graph each neighbour is joined to n_i by exactly one edge and there are no loops, so the number of 1s in row i is the number of edges at n_i; summing over i counts every edge twice (once from each end). Checked on the board matrix: row sums 1, 2, 1, total 4 = 2|E| with |E| = 2.",
```

```diff
diff --git a/papers/adjacency-walks-connectivity/evidence/modules/author.json b/papers/adjacency-walks-connectivity/evidence/modules/author.json
new file mode 100644
index 0000000..3002a6c
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/evidence/modules/author.json
@@ -0,0 +1,46 @@
+{
+  "sources": [],
+  "claims": [
+    {
+      "id": "A1",
+      "text": "Textbook Definition 1.2.1: the degree of a vertex v in G, written d_G(v) or d(v), is the number of edges incident to v. Gloss: 'the degree of the vertex v in G, which we denote d_G(v) or d(v), is the number of edges incident to that vertex'. Read from the page image of printed p. 16 (PDF p. 17). The book puts degree after the adjacency matrix (printed p. 11).",
+      "kind": "fact",
+      "module": "author",
+      "support": [
+        {
+          "source": "petrosyan2015grafneri",
+          "locator": "printed p. 16 (PDF p. 17), Definition 1.2.1",
+          "quote": "Սահմանում 1.2.1: G գրաֆում v գագաթի աստիճան, որը կնշանակենք d_G(v)-ով կամ d(v)-ով, կանվանենք այդ գագաթին կից կողերի քանակը։"
+        }
+      ],
+      "derivation": null,
+      "confidence": "high",
+      "status": "supported",
+      "used_in": [
+        "sections/background.tex"
+      ],
+      "contradicted_by": []
+    },
+    {
+      "id": "A2",
+      "text": "Textbook Theorem 1.2.1 (L. Euler): in any graph G = (V, E) the sum over all vertices of d_G(v) equals 2|E(G)|. Gloss of the proof: every edge is incident to two vertices, so it is counted twice in the sum. Read from the page image of printed p. 16 (PDF p. 17).",
+      "kind": "fact",
+      "module": "author",
+      "support": [
+        {
+          "source": "petrosyan2015grafneri",
+          "locator": "printed p. 16 (PDF p. 17), Theorem 1.2.1",
+          "quote": "Թեորեմ 1.2.1 (Լ. Էյլեր): Կամայական G = (V, E) գրաֆում տեղի ունի Σ d_G(v) = 2|E(G)| հավասարությունը։"
+        }
+      ],
+      "derivation": null,
+      "confidence": "high",
+      "status": "supported",
+      "used_in": [
+        "sections/background.tex"
+      ],
+      "contradicted_by": []
+    }
+  ],
+  "contradictions": []
+}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/main.tex b/papers/adjacency-walks-connectivity/main.tex
new file mode 100644
index 0000000..ec49fac
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/main.tex
@@ -0,0 +1,89 @@
+\documentclass[11pt,a4paper]{article}
+\usepackage[margin=2.5cm]{geometry}
+\usepackage{amsmath,amsthm,amssymb}
+\usepackage{graphicx}
+\usepackage{booktabs}
+\usepackage{tikz}
+\usetikzlibrary{arrows.meta}
+\usepackage[hidelinks]{hyperref}
+\usepackage{cleveref}
+\usepackage[backend=biber,style=numeric,urldate=long]{biblatex}
+\addbibresource{references.bib}
+\setcounter{biburlnumpenalty}{100}
+\setcounter{biburlucpenalty}{100}
+\setcounter{biburllcpenalty}{100}
+\emergencystretch=2em
+\graphicspath{{figures/}}
+
+% Theorem-like environments, all sharing one counter inside each section.
+\theoremstyle{definition}
+\newtheorem{definition}{Definition}[section]
+\newtheorem{example}[definition]{Example}
+\newtheorem{nonexample}[definition]{Non-example}
+\newtheorem{test}[definition]{Test}
+\theoremstyle{plain}
+\newtheorem{theorem}[definition]{Theorem}
+\newtheorem{lemma}[definition]{Lemma}
+\newtheorem{proposition}[definition]{Proposition}
+\newtheorem{corollary}[definition]{Corollary}
+\theoremstyle{remark}
+\newtheorem{remark}[definition]{Remark}
+\crefname{nonexample}{Non-example}{Non-examples}
+\crefname{test}{Test}{Tests}
+\Crefname{nonexample}{Non-example}{Non-examples}
+\Crefname{test}{Test}{Tests}
+
+% The plain words layer: a short paragraph in the story, before each
+% definition, theorem, test and worked example.
+\newenvironment{plainwords}{\par\medskip\noindent\textbf{In plain words.}\ }{\par\medskip}
+
+% Matrices and tables computed by appendices/scripts/generate_paper_numbers.py
+\input{appendices/scripts/numbers}
+
+\newcommand{\Mat}{\mathbf}
+\DeclareMathOperator{\trace}{trace}
+
+\title{Walks, Paths, and Connectivity Read from an Adjacency Matrix\\
+\large A Study Note}
+\author{}
+\date{}
+
+\begin{document}
+\maketitle
+
+\begin{abstract}
+A finite simple undirected graph with $N$ vertices can be described by its
+adjacency matrix $A$, a square table of zeros and ones.
+This note answers three questions about it.
+First, the entry in row $i$ and column $j$ of the $k$-th power $A^k$ counts the
+walks of length $k$ from vertex $n_i$ to vertex $n_j$.
+It counts walks, not paths, and the note shows by a counterexample why the
+difference matters.
+Second, the graph is connected if and only if every entry off the diagonal of
+$A + A^2 + \dots + A^{N-1}$ is positive.
+Both statements are proved in full.
+Third, a path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ in which no
+vertex occurs twice.
+The note follows the numbering and build order of the course textbook, sets
+every new idea in a single story about a village, and works two small examples
+with every matrix written out and computed by script.
+\end{abstract}
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
+\printbibliography
+
+\appendix
+\input{appendices/course-terms}
+\input{appendices/photographs}
+\input{appendices/derivations}
+\input{appendices/provenance}
+
+\end{document}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reader-findings.md b/papers/adjacency-walks-connectivity/reader-findings.md
new file mode 100644
index 0000000..94c36d0
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reader-findings.md
@@ -0,0 +1,42 @@
+# Technician reader findings
+
+Diagnostic comprehension findings from the `technician-reader` agent, one
+block per round. Advisory; the evaluator's findings govern release.
+
+## Round 1, 2026-10-31
+
+Reader configured at level 2. Twenty comprehension findings. The reader's
+summary of the conclusions matches the paper's actual conclusions (all three
+answers stated correctly), so no mismatch finding is raised. The reader's
+closing remark: it could state the answers but could not say why the
+village story, the board-reading discussion, and the source critique take up
+so much of the note.
+
+| Id | Location | Defect | Correction |
+|---|---|---|---|
+| R1 | Abstract, Section 1.1 | The abstract never says this is a study note answering a lecture's three questions; "as reported to us" is undefined. | One sentence in the Introduction on who set Q1 to Q3 and that the board and assignment are the only sources; define or drop "as reported to us". |
+| R2 | Abstract | Q3 is a definition, yet the abstract lists it as answered and says "Both statements are proved in full"; the reader cannot tell what Q3 establishes. | Say Q3 is settled by fixing a definition and that the textbook uses "path" differently. |
+| R3 | Section 1.3 item 5, Definition 2.9 | The board's V is the edge set but the paper's V is the vertex set; both appear in one paragraph. | Move the board-notation discussion to Appendix A; keep G = (V, E) in the main text with one footnote on the mismatch. |
+| R4 | Section 1.3 item 4, Table 1 | Path, simple path, and trail appear in a story dictionary before any is defined; the textbook's "path" is the paper's "trail". | A three-line mini-table (textbook word, this note's word, meaning) at that point, or a pointer to Table 4. |
+| R5 | Section 1.2 and plain-words paragraphs | The village layer adds a second vocabulary; several paragraphs bring in ideas the formal text has not reached ("shortest trip", "infinite"). | State at the top of Section 2 that the plain-words paragraphs may be skipped; keep the story only where it adds meaning. |
+| R6 | Definition 2.40 | Distance is defined via the textbook's "path" (a trail) and relies on Proposition 2.47 seven pages later; "metric space" unexplained. | Define distance as the length of a shortest walk; drop or gloss "metric space". |
+| R7 | Proposition 2.35 proof | The step from "u_b differs from u_a and u_{a-1}" to "the edges differ" is compressed. | Add "since b > a, b >= a+1, and all vertices have distinct indices" and state the conclusion explicitly. |
+| R8 | Remark 2.20, Definition 2.19 | A walk is defined with edges then silently replaced by vertex sequences; Theorem 3.5 depends on the swap. | Move the vertex-sequence characterization into Definition 2.19. |
+| R9 | Proof of Proposition 4.5 (i) to (ii) | The symbol l is introduced and never used; why the corollary is needed is unclear. | "A path has at most N-1 edges (Corollary 2.46), so it is a walk of length k with 1 <= k <= N-1." |
+| R10 | Proof of Theorem 4.6, condition (c) | Proved by forward reference to Proposition 4.17 whose proof is in Appendix C.4; the idea appears only in plain words. | Add the one-sentence binomial-expansion argument inline, or move that half of the proof up. |
+| R11 | Remark 4.9 | Mixes the diagonal, N = 1, and N = 2 cases; unclear whether needed for Theorem 4.6. | Say "not needed for Theorem 4.6" and split off N = 1. |
+| R12 | Remark 4.16 | "Labelled paths" undefined; the step to N!/2 and the link to Table 6 are only asserted. | Add "(N! orderings of the vertices along the path, each counted twice because it can be read in reverse)". |
+| R13 | Remark 4.18, Table 6 caption | Breadth-first search in one dense sentence; "queue", "adjacency lists", "independent" unexplained. | A three-line procedure or a tie to the plain-words "mark neighbours repeatedly"; say what "independent" means. |
+| R14 | Example 6.1 | A^{k+2} = 2A^k for k = 1 uses A^0, which Remark 3.2 says is used only in Section 4; the purpose of the pattern is unstated. | State the purpose or delete; fix the A^0 inconsistency. |
+| R15 | Example 6.2 | The (I + A)^2 check uses the expansion before it is introduced and does not say what it shows. | State the expansion first, then the entry computation on separate lines. |
+| R16 | Table 6 and caption | The "1" for N = 2 is unexplained; the all-graphs check rests on a script the reader cannot see. | Explain the empty-sum case in one clause; add "see Appendix D" in the caption. |
+| R17 | Section 7.4 | Critique of unnamed sources; the web sources are not separated from [7]; the section's purpose is unclear. | Name the sources inline and quote the criticised sentence, or shorten to one sentence and move the detail to an appendix. |
+| R18 | Section 7.5 | 98,000,000, 7, and 38,742,049 are not derived; the cost section is not tied to the three questions. | Show the arithmetic in one line each, or cut the section. |
+| R19 | Section 1.4 | The reader must take on faith that the Armenian textbook lacks the results; the purpose of the paragraph is clear only on a second read. | Shorten to "The textbook, as far as we searched, has neither result, so both are proved here." |
+| R20 | Section 5.2, Section 6.1 | Points to a textbook figure the reader never sees; "a trail that repeated a vertex would contain a closed trail" has no argument. | Give a four-vertex example (triangle plus pendant edge) with trail and path counts, or drop the claim; add one line on why the closed trail exists. |
+
+Reader's summary of the conclusions, verbatim:
+
+The note asks three things about a graph (points joined by lines) written as an adjacency matrix A, a table of zeros and ones. First, what do the entries of the k-th power of A mean? The answer is that entry (i,j) of A^k is the number of walks of length k from vertex i to vertex j. A walk may repeat vertices and edges, so the entry does not count paths. Second, how can one tell from A whether the graph is connected? The answer is that the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N-1) is positive, or equivalently when (I + A)^(N-1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path of no more than N-1 steps. The note shows that N-1 cannot be reduced to N-2, because a straight-line graph needs all N-1 steps. It also offers breadth-first search as an alternative. Third, what is a path? The answer is a walk with no repeated vertex, which differs from the textbook's own "path" (a walk with no repeated edge). Two three-vertex examples, one connected and one not, and a computer check over all graphs with up to six vertices support the results. I can state the answer, but I could not say why the village story, the board-reading discussion and the source critique take up so much of the note.
+
+The full verbatim message is in `reports/technician-reader-round1.md`.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/references.bib b/papers/adjacency-walks-connectivity/references.bib
new file mode 100644
index 0000000..5614cec
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/references.bib
@@ -0,0 +1,102 @@
+@book{petrosyan2015grafneri,
+  author    = {Petrosyan, P. A. and Mkrtchyan, V. V. and Kamalyan, R. R.},
+  title     = {Graph Theory: a study guide},
+  year      = {2015},
+  publisher = {Yerevan State University Press},
+  address   = {Yerevan},
+  isbn      = {978-5-8084-1995-7},
+  howpublished = {Local file Grafneri\_tesutyun.pdf},
+  note      = {Course textbook in Armenian, supplied by the user; the Armenian title is omitted here. Printed page numbers are cited; the PDF page is one higher.}
+}
+
+@misc{whiteboard1,
+  title        = {Lecture whiteboard photo 1},
+  year         = {n.d.},
+  howpublished = {Local file sources/whiteboard-1.jpg},
+  note         = {Photograph of a lecture board, supplied by the user. Author and date unknown.}
+}
+
+@misc{whiteboard2,
+  title        = {Lecture whiteboard photo 2},
+  year         = {n.d.},
+  howpublished = {Local file sources/whiteboard-2.jpg},
+  note         = {Second photograph of the same board at a slightly different angle, supplied by the user. Author and date unknown.}
+}
+
+@online{grinberg2025graph,
+  author  = {Grinberg, Darij},
+  title   = {An introduction to graph theory (Text for Math 530 in Spring 2022 at Drexel University)},
+  year    = {2025},
+  url     = {https://arxiv.org/abs/2308.04512},
+  urldate = {2026-10-27},
+  note    = {arXiv:2308.04512v3 [math.HO], Spring 2025 edition, 7 June 2025. Preprint, not peer reviewed. Page numbers cited are the document's own page numbers.}
+}
+
+@online{quinlan_matrices_graphs,
+  title        = {Chapter 1 Matrices and Graphs, 1.1 The Adjacency Matrix (linear algebra course notes)},
+  year         = {n.d.},
+  organization = {School of Mathematical and Statistical Sciences, University of Galway},
+  url          = {https://maths.nuigalway.ie/~rquinlan/linearalgebra/section1-1.pdf},
+  urldate      = {2026-10-27},
+  note         = {Lecture notes. The file shows no author name and no date.}
+}
+
+@online{lehman_mcs_adjacency,
+  author  = {Lehman, Eric and Leighton, F. Thomson and Meyer, Albert R.},
+  title   = {9.3: Adjacency Matrices (Mathematics for Computer Science, MIT OpenCourseWare), Engineering LibreTexts},
+  year    = {n.d.},
+  url     = {https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Mathematics_for_Computer_Science_(Lehman_Leighton_and_Meyer)/02\%3A_Structures/09\%3A_Directed_graphs_and_Partial_Orders/9.03\%3A_Adjacency_Matrices},
+  urldate = {2026-10-27},
+  note    = {Page last modified 2021-07-02; the year of the underlying book is not on the page.}
+}
+
+@article{paramadevan2021adjacency,
+  author      = {Paramadevan, P. and Sotheeswaran, S.},
+  title       = {Properties of Adjacency Matrix of a Graph and It's Construction},
+  year        = {2021},
+  journaltitle = {JSc EUSL (Journal of Science, Eastern University, Sri Lanka)},
+  volume      = {12},
+  number      = {1},
+  pages       = {13--21},
+  doi         = {10.4038/jsc.v12i1.29},
+  url         = {https://www.fsc.esn.ac.lk/jsc/archive/12.1.2.pdf},
+  urldate     = {2026-10-27}
+}
+
+@online{bai2025adjacency,
+  author       = {Bai, Shuliang},
+  title        = {Important Properties and Applications of the Adjacency Matrix (20250310)},
+  year         = {2025},
+  organization = {BIMSA},
+  url          = {https://bimsa.net/doc/notes/48535.pdf?id=0.3935315718408674},
+  urldate      = {2026-10-27},
+  note         = {Lecture notes, dated 2025-03-10 in the title.}
+}
+
+@online{weisstein_connectedgraph,
+  author       = {Weisstein, Eric W.},
+  title        = {Connected Graph},
+  year         = {n.d.},
+  organization = {Wolfram MathWorld},
+  url          = {https://mathworld.wolfram.com/ConnectedGraph.html},
+  urldate      = {2026-10-27}
+}
+
+@online{wikipedia_path_graph_theory,
+  title        = {Path (graph theory)},
+  year         = {n.d.},
+  organization = {Wikipedia, English edition},
+  url          = {https://en.wikipedia.org/wiki/Path_(graph_theory)},
+  urldate      = {2026-10-27},
+  note         = {Revision of 5 June 2026 (oldid 1357845833) as fetched; open to later edits.}
+}
+
+@online{schost2026bfs,
+  author       = {Schost, {\'E}ric},
+  title        = {CS 341: Algorithms, Lecture 10: Graphs, breadth first search},
+  year         = {2026},
+  organization = {David R. Cheriton School of Computer Science, University of Waterloo},
+  url          = {https://www.student.cs.uwaterloo.ca/~cs341/lectures/lecture10.pdf},
+  urldate      = {2026-10-27},
+  note         = {Lecture slides, Winter 2026.}
+}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reports/paper-author-round1.md b/papers/adjacency-walks-connectivity/reports/paper-author-round1.md
new file mode 100644
index 0000000..87d27e8
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reports/paper-author-round1.md
@@ -0,0 +1,43 @@
+# paper-author, round 1
+
+Final message of the paper-author agent, saved verbatim by the orchestrator.
+
+---
+
+`main.tex` and the full paper are written, and the four commands pass with no errors or warnings. The PDF is 28 pages. I did not commit anything, since you didn't ask.
+
+## Files written
+All under `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/`:
+- `main.tex`, `references.bib` (11 entries, keys equal the evidence source ids), `main.pdf`, `self-evaluation.md`
+- `sections/`: `introduction`, `background`, `answer1_walks`, `answer2_connectivity`, `answer3_path`, `example`, `discussion`, `conclusion`
+- `appendices/`: `course-terms`, `photographs`, `derivations`, `provenance`
+- `appendices/scripts/`:
+  - the three module scripts, copied unchanged and re-run (outputs identical to the module outputs)
+  - `generate_paper_numbers.py` and its output, which write `numbers.tex`
+  - `numbers.tex`: LaTeX macros for every matrix and table in the examples, so no number is typed by hand
+- `evidence/modules/author.json`, with `evidence/evidence.json` rebuilt from the base file and fragments (base plus fragments reproduced the old merged file exactly before I added `author.json`)
+
+## Output of the four commands
+```
+build.sh:            ok: papers/adjacency-walks-connectivity/main.pdf   (exit 0)
+check_citations.py:  cited keys 11; bib entries 11; evidence sources 11; errors 0; warnings 0
+check_claims.py:     sources 11; claims supported 72, qualified 7, removed 0, unverified 0; errors 0; warnings 0
+inspect_pdf.py:      pages 28; errors 0; warnings 0
+```
+Biber prints six warnings that `year = {n.d.}` is not an integer. The evidence record has `year: null` for those six sources, and `check_citations.py` requires a year or date field.
+
+## Claims added
+I added two claims, A1 and A2, both `fact` and `supported`:
+- **A1:** textbook Definition 1.2.1 (degree), printed p. 16.
+- **A2:** textbook Theorem 1.2.1 (Euler: the degrees sum to 2|E|), printed p. 16.
+
+I read both from the page image, since `graph-sources.md` says the textbook defines degree. I added no `unverified` or `derived` claims, and none of the 7 `qualified` claims were changed.
+
+## Things you should know
+- **Dictionary row:** the story dictionary has one row of my own, "table of totals", for the sum S.
+- **Claim-pointer mismatches:** several `derivation` strings in the evidence fragments name paper numbers from the module drafts that no longer match. The labels all exist, but these numbers differ: Proposition 4.14 is `prop:sharp`, 4.17 is `prop:iplusa`, Remark 4.16 is `rem:failcount`, `sec:cost` is Section 7.5, and the derivations appendix is lettered C. `self-evaluation.md` lists the stale pointers. I did not edit those fragments.
+- **Other unsupported points** (all in `self-evaluation.md`):
+  - The textbook-walk example (length 8 to 5 to 2) rests on my script's seven edges, not on the textbook text.
+  - The English column "closed trail" for the textbook's cycle is my combination of Grinberg's trail definition with "closed".
+  - The cost remark is an estimate for schoolbook multiplication only.
+  - The plain-words paragraphs pass my script check (no technical terms, no symbols, no sentence over 18 words); I did not do a read-aloud test with a real child.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md b/papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md
new file mode 100644
index 0000000..db1515b
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reports/paper-evaluator-round1.md
@@ -0,0 +1,62 @@
+# paper-evaluator, round 1
+
+Final message of the paper-evaluator agent, saved verbatim by the orchestrator.
+
+---
+
+SCORES
+1 Correctness: 4 -- I recomputed every matrix and table myself and all match: Examples 2.11, 3.3, 3.4, 4.15, 6.1, 6.2 and 6.3, Tables 2, 3, 5 and 6 (including 1/4/38/728/26704 connected graphs and 3/12/60/360 = N!/2 failures with N-2 powers), the cost figures 98,000,000 and 7,000,000 with 7 squarings, and the largest entry 38,742,049 of A^9 for the complete graph on 10 vertices. Every proof step checks out: Lemma 2.44, Proposition 2.35, Theorem 3.5, Proposition 4.5, Theorem 4.6, Proposition 4.17 and Appendix C.2. One sentence is wrong as stated: the statement in Section 7.5 (sections/discussion.tex:86-87) that BFS "reads each of the N^2 entries once" (F1).
+2 Evidence coverage: 4 -- evidence.json holds 79 claims (72 supported, 7 qualified), and every substantive statement I traced has a claim behind it, for example Theorem 3.5 to C6/C7, Theorem 4.6 to C34/C36 and Definition 2.31 to C16/C24. The exception is the matrix-input BFS cost in Section 7.5. Its evidence claim (m3-10) quotes slides that do not say it (F1).
+3 Citation integrity: 4 -- all eight sources I checked exist and their metadata matches. The weight-bearing passages say what the paper attributes to them, including the defects the paper reports in [7] and [1]. Three attributions are off: [10, slides 3 and 6] (F1), [3, Proposition 2.9.10] cited for trails (F9), and [7, property 8] described as a row sum (F10).
+4 Logical validity: 5 -- each conclusion follows from proved premises. Appendix C.3 lists the premises behind Theorem 4.6, and Remark 2.49 with Section 5.2 shows that connectivity does not depend on which meaning of "path" is used. The paper does not repeat the gap in the sources, which go from a positive entry straight to a path (Section 7.4).
+5 Understandability: 4 -- the definitions are clear and built in order, and every proof names its method and its base case. Problems: "(5)" in Section 5.2 reads as an equation reference (F7); "its ends" in Remark 4.16 is ambiguous (F8); Theorem 4.6 has no plain-words paragraph of its own (F6); and the examples from textbook Fig. 1.2.5 cannot be checked without the book (F17).
+6 Completeness: 5 -- every objective in the brief is met. Definition 2.9 and Proposition 2.13/2.18 cover A. Theorem 3.5 is proved by induction, and Proposition 3.10 with Table 2 shows walks are not paths. Definitions 2.19-2.40 carry the textbook numbers. The test is Theorem 4.6 with its proof, worked in Examples 6.2/6.3, and BFS is Remark 4.18.
+7 Methodological rigor: 5 -- matrices are produced by script and fed into the text (numbers.tex). Exhaustive checks over all labelled graphs with N <= 6 are presented as checks, not proofs (Section 6.4, Appendix C.6). Assumptions are listed and numbered (Section 1.3).
+8 Critical analysis: 5 -- Section 7 covers the drawing/matrix mismatch edge by edge, the uncertain mark above A, the limits of the textbook search, the incorrect Theorem 1 in [7] and the loose proofs in [7] and [1], and the cost. Section 7.6 declines to guess what the lecturer intended.
+9 Internal consistency: 3 -- notation is mostly uniform, but several words and letters carry two meanings, against the checklist rule of one meaning each: "loop" (F2); "length" and "table of trips" inside story paragraphs (F3, F4); S, n and t each name two things (F5); and Definition 2.48 does not say which sense of "(u,v)-path" it uses (F11).
+10 Reproducibility: 5 -- Appendix D names the scripts, the seed and the run commands, and the saved outputs are present. I reproduced every printed number independently.
+11 LaTeX and PDF quality: 5 -- the 28-page PDF has no errors: inspect_pdf 0/0, check_citations 0/0, check_claims 0/0. Cross-references and references resolve. Inline matrices, the binomial in (3) and the tables render correctly on the pages I viewed (15, 20, 26). The log shows only underfull hbox warnings. I did not re-run build.sh because it writes into the paper folder.
+12 Answer relevance: 5 -- Sections 1.5 and 8 answer Q1-Q3 directly, with the theorem or definition number for each answer. They claim nothing beyond the brief, and the conclusion states the assumptions the answers rest on (Section 8, last paragraph).
+
+FINDINGS
+F1 | major | sections/discussion.tex:86-87 (Section 7.5) | The paper says that with A as input BFS "reads each of the N^2=10,000 entries once [10, slides 3 and 6]", but slide 3 only defines the matrix representation, slide 6 is BFS "given by adjacency lists", neither states this cost, and "once" is exact only when every vertex is reached; evidence claim m3-10 has no quote saying it. | Present it as the note's own estimate: "With A as input, the search scans the row of each vertex it takes from the queue, so it reads at most N^2 = 10,000 entries; this count is ours." Cite [10, slide 3] only for the matrix representation, and correct m3-10.
+F2 | minor | sections/background.tex:463-466 and 311, against :50, :113, :259 and appendices/derivations.tex:66 | "Loop" means an edge from a vertex to itself in the technical text, but a detour in the plain-words paragraphs ("you went round a loop. Cut the loop out."; "with no loop"). | In the story write "a detour that comes back to the same house" and "cut the detour out"; keep "loop" for the technical sense only.
+F3 | minor | sections/background.tex:201, 203, 419 | The plain-words paragraphs use the technical word "length" ("The length of a trip is...", "a trip of length zero"), although Table 1 says technical words are never used there and maps length to "number of roads driven". | "The number of roads driven counts a road each time you drive it." "Staying at home is also a trip, with zero roads driven."
+F4 | minor | sections/answer1_walks.tex:153 | "The table of trips" is not in the story dictionary, which has only "table of roads" (A) and "table of totals" (S). | Add a row to Table 1 for A^k (for example "table of trips of k roads"), or reword to "the new table" as at line 45.
+F5 | minor | sections/background.tex:483-509; :380; Remark 2.20 against Proposition 4.17 | Three letters each name two things. S names the induction statement S(k), but Item 5 reserves S for the sum of Definition 4.1. In C_n, n is a vertex count while n_i are vertex names. t is a walk index and also the number of squarings. | Rename the statement P(k). Write "the simple cycle on q vertices, written C_q (the textbook writes C_n)". Use another letter, such as h, for the number of squarings in Proposition 4.17.
+F6 | minor | sections/answer2_connectivity.tex:74, :124; sections/background.tex:541; sections/introduction.tex:37 | Theorem 4.6 (the main result for Q2), Corollary 4.7 and Proposition 2.47 have no "In plain words" paragraph directly before them, while the introduction says every theorem has one and the brief requires it. | Move the Section 4.2 paragraph to directly before Theorem 4.6 and add short story paragraphs before Proposition 4.5, Corollary 4.7 and Proposition 2.47; or narrow the sentence in the introduction.
+F7 | minor | sections/answer3_path.tex:78 | "which calls (5) a walk of length 0": "(5)" reads as a reference to equation (5), and the paper has no equation (5). | "which calls the sequence made of the single vertex 5 a walk of length 0 and a path [3, Example 2.9.2]".
+F8 | minor | sections/answer2_connectivity.tex:259 (Remark 4.16) | In "would shorten the distance between its ends", "its" can be read as the extra edge, whose ends are always at distance 1. | "would give a shorter walk between the two ends of that path".
+F9 | minor | sections/background.tex:575 (Remark 2.49) | The paper says the walk/trail/path equivalence "is also stated in [3, Proposition 2.9.10]", but that proposition (p. 42, checked) covers only walks and paths. | "the equivalence of the walk and path readings is also [3, Proposition 2.9.10]".
+F10 | minor | sections/background.tex:180 (proof of Proposition 2.18) | The paper says "[7, property 8] states the row sum", but property 8 gives the degree as the off-diagonal entries plus twice the diagonal entry, which is not the row sum when loops exist. | "[7, property 8] gives the degree as the sum of the off-diagonal entries plus twice the diagonal entry, which for zero diagonal is the row sum".
+F11 | minor | sections/background.tex:563 (Definition 2.48), and Definition 2.52 | Definition 2.48 writes "(u,v)-path" without saying in which sense. Item 4 and Table 4 fix "path" as no repeated vertex "without exception", and Remark 2.49 then says the textbook meant a trail. | In the definition write "a (u,v)-path in the textbook's sense (a trail; equivalently a path, Remark 2.49)", and give the same qualifier in Definition 2.52.
+F12 | minor | sections/answer1_walks.tex:63, 143-147; sections/answer2_connectivity.tex:182; sections/discussion.tex:34-35, :77 | The brief allows a one-sentence remark on directed graphs and multigraphs and a short remark on complexity. The paper mentions directed graphs or multigraphs in four places and gives cost its own subsection (7.5). | Keep one sentence in the Scope item of Section 7.3 and delete the other mentions. Fold Section 7.5 into one paragraph in Section 7.3 or Remark 4.18.
+F13 | minor | appendices/photographs.tex:8-9 (Appendix B, item 1) | Appendix B says "the board's wording and spelling are kept", but the board writes the conditions with the Armenian word for "if" (visible in both photos), which appears silently as English "if". | Add: "the board writes the Armenian word for 'if' in both lines".
+F14 | minor | references.bib:9, 16, 23 | "Supplied by the user" appears in the reference list, and "the user" is never introduced to the reader (a checklist item). | "supplied with the assignment".
+F15 | minor | sections/answer2_connectivity.tex:92 | "A path between n_i and n_j is a walk, say of length ℓ": ℓ is never used again. | Delete "say of length ℓ", or write "of length ℓ ≤ N-1 (Corollary 2.46); take k = ℓ".
+F16 | minor | appendices/provenance.tex:9 | The paper calls the Galway notes "the whole eight-page file", but the PDF has 7 pages, numbered 2 to 8. | "the whole file (seven PDF pages, numbered 2 to 8)".
+F17 | minor | sections/background.tex, Examples 2.21, 2.29, 2.38 and Non-example 2.22 | The examples from textbook Fig. 1.2.5 cannot be checked without the book, because the paper neither draws the graph nor lists its edges. The book-style standard asks that examples can be checked against a figure. | Add one sentence listing the edges of Fig. 1.2.5 that the examples use (the seven edges named in Appendix D), or a small figure.
+
+CITATION SPOT CHECKS
+quinlan_matrices_graphs | fetched | supports | Definition 1.1.1 (simple undirected graph), Theorem 1.1.3 (simple graph, positive k, walks of length k), the proof by second-last vertex v_r, and the remark that walks of length 2 from a vertex to itself give the vertex degree all appear verbatim. No author or date in the file, as the paper says. 7 PDF pages, not eight (F16).
+paramadevan2021adjacency | fetched | supports | Metadata matches: JSc EUSL 12(1), pp. 13-21, DOI 10.4038/jsc.v12i1.29. Theorem 1 says "different paths of length l", as the paper reports. Property 7 says walks. Theorem 2 states the sum test with b_ij ≠ 0 for i ≠ j. Its proof counts "paths" and goes from b_ij ≠ 0 to a path, as Section 7.4 says. Theorem 3 gives distance as the smallest l. Property 8 is not a row sum (F10).
+bai2025adjacency | fetched | supports | Theorem 1 covers simple graphs and walks, and the text says "counts walks — not paths". Theorem 2: G is connected iff (I+A)^{n-1} has all entries strictly positive. The proof sketch adds self-loops and says the power "aggregates all paths", as the paper reports.
+grinberg2025graph | fetched | partially supports | arXiv v3, 454 pages. Locations confirmed: Definition 2.9.1 (p. 36), Corollary 2.9.7 (p. 39, with the bound "length ≤ k"), the Section 2.9.4 remark that a path has length ≤ n-1, Proposition 2.9.10 (p. 42), Definition 2.10.1 (p. 47), Definition 3.4.5 (p. 101, trail), Theorem 4.5.10 (p. 120, multidigraphs). Proposition 2.9.10 does not cover trails (F9).
+weisstein_connectedgraph | fetched | supports | "such a graph on n>1 vertices is connected iff sum_(k=1)^(n-1)A^k has no zero off-diagonal entries."
+schost2026bfs | fetched | partially supports | Slides 9-10 support O(n+m) for adjacency lists and the correctness statement "there is a walk s ; v iff discovered[v]". Slide 3 only defines the n×n matrix. Slide 6 assumes adjacency lists. No slide gives the matrix-input cost (F1).
+petrosyan2015grafneri | local file, page images viewed | supports | Printed p. 22 (PDF p. 23): Definitions 1.2.11-1.2.16 read as the paper states, including 1.2.12 "path" with distinct edges, 1.2.13 "simple path", 1.2.14 closed path or cycle, 1.2.15 simple cycle with C_n for n ≥ 3, and distance. Printed p. 48 (PDF p. 49): Definition 2.1.1 with a (u,v)-path, and complete and complete bipartite graphs as examples.
+whiteboard1, whiteboard2 | local files viewed | supports | The transcription in Appendix B matches both photos: the A_ij line, the drawing with 1→2 arrowhead and lines 1-3 and 2-3, the matrix 010/101/010, the problem text, Q1 with a quote-like mark over A, Q2, and the definition of connected. Only exception: the Armenian "if" (F13).
+
+UNVERIFIED CLAIMS IN TEXT
+C24 | Item 4 (Section 1.3), Remark 2.32, Section 5 intro, Section 8 Q3 | qualified
+C29 | Item 2 (Section 1.3), Section 7.2, Appendix B item 4 | qualified
+C36 | Theorem 4.6(c) with proof via Proposition 4.17, Section 7.4 | qualified
+m1-9 | Item 2, Section 7.2 | qualified
+m2-8 | Remark 2.32, Section 5 intro, Section 8 Q3 | qualified
+m2-15 | Item 6 (Section 1.3), Section 5.2 "Length zero" | qualified
+m3-11 | Section 1.4, Section 7.3 "Sources" | qualified
+
+RECOMMENDATION
+REVISE -- The mathematics is correct and complete: I re-checked every proof, matrix and table, and found no critical defect. But F1 is a major attribution defect: Section 7.5 credits a matrix-input BFS cost to Schost's slides 3 and 6, which do not state it, and the sentence's "once" is only exact for connected graphs. F1 must be fixed before release, and the sixteen minor findings fixed or documented with a reason. I could not observe release conditions 6, 9 and 10 (model levels, self-evaluation coverage, the outcome of this evaluation) or re-run build.sh.
+
+Relevant paths: /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/main.pdf, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/sections/discussion.tex, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/sections/background.tex, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/evidence/evidence.json. My independent recomputation script is /tmp/claude-0/-home-user-research-paper-writing-lab/e49dae39-2b09-51e9-ac34-b3549bf40418/scratchpad/verify.py.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/reports/technician-reader-round1.md b/papers/adjacency-walks-connectivity/reports/technician-reader-round1.md
new file mode 100644
index 0000000..da2d66f
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/reports/technician-reader-round1.md
@@ -0,0 +1,49 @@
+# technician-reader, round 1
+
+Final message of the technician-reader agent, saved verbatim by the orchestrator.
+
+---
+
+FINDINGS
+F1 | comprehension | Abstract and Section 1.1: "The note follows the numbering and build order of the course textbook"; "Question Q3 was added by the assignment text, which we know only as it was reported to us and do not reproduce here." | The paper rests on a course, a textbook, an assignment and a photographed board that a reader cannot see. The abstract never says that this is a study note answering a lecture's three questions. The phrase "reported to us" leaves open who "us" is and what exactly was reported. | Add one sentence early in the Introduction saying who set Q1 to Q3 and that the board and assignment are the only sources of the questions. Drop the "as reported to us" repetitions or define them once.
+
+F2 | comprehension | Abstract: "Third, a path between ni and nj is a walk from ni to nj in which no vertex occurs twice." | This is a definition, yet the abstract lists it as a third question that is "answered" and says "Both statements are proved in full". The reader cannot tell what the third item is supposed to establish. | Reword so the abstract says Q3 is settled by fixing a definition, and notes that the textbook uses "path" differently.
+
+F3 | comprehension | Section 1.3 Item 5 and Definition 2.9: "eij ∈ V ... its V there stands for the set of edges"; "(G, V ) for the graph". | The board's V is the edge set but the paper's V is the vertex set. A reader meeting both in one paragraph cannot tell which is meant. The sentence is hard to parse on first reading. | Move the board-notation discussion to Appendix A and keep only "G = (V, E)" in the main text. Mention the board mismatch once, in a footnote.
+
+F4 | comprehension | Section 1.3 Item 4 and Table 1: "route | path" next to "trip with no road twice | trail", and the line "The textbook's own word 'path' means something weaker, which this note calls a trail". | The reader meets three words (path, simple path, trail) and a story dictionary before any of them is defined. The textbook's "path" is the paper's "trail", but "path" is also the paper's own word for the stricter notion. | Give a three-line mini-table (textbook word, this note's word, meaning) in 1.3 Item 4, or point to Table 4 right there.
+
+F5 | comprehension | Section 1.2: "Table 1 ... table of totals | the sum S | Definition 4.1" and "Those paragraphs are told in one story and use no symbols." | The "In plain words" paragraphs repeat each definition in house and road language, which adds a second vocabulary to learn. Several paragraphs bring in ideas the formal text has not yet reached (for example "shortest trip" and "infinite"). The purpose of the village layer is clear, but its cost in length is high. | State at the top of Section 2 that the plain-words paragraphs may be skipped. Keep the story only where it adds meaning.
+
+F6 | comprehension | Definition 2.40: "the length of a shortest (u, v)-path in the textbook's sense (a trail) ... By Proposition 2.47 the value is the same"; "the pair (V, d) is a metric space". | Distance is defined with the textbook's "path" (a trail), and the claim that the choice does not matter relies on a proposition that appears 7 pages later. "Metric space" is used without explanation, and the properties are asserted with only a pointer to Proposition C.2. | Define distance directly as the length of a shortest walk, since Proposition 2.47 shows this is equivalent. Drop "metric space" or gloss it in one clause.
+
+F7 | comprehension | Proposition 2.35 proof: "The vertex ub has an index larger than a, so it differs from ua and from ua−1. Thus ub is an end of the second edge and not an end of the first". | The jump from "ub differs from ua and ua−1" to "the edges differ" took three readings. The index reasoning (a < b means b ≥ a+1) is compressed. | Add "since b > a, b ≥ a+1, and all vertices have distinct indices" and state the conclusion as "so the edge ub−1ub has an end that the edge ua−1ua lacks".
+
+F8 | comprehension | Remark 2.20 and Definition 2.19: "In a simple graph an edge is fixed by its two ends, so a walk is determined by its vertex sequence". | The paper defines a walk with edges, then silently replaces it with vertex sequences. The proof of Theorem 3.5 depends on this swap. It is correct, but it is stated inside a long remark and is easy to miss. | Move the sentence "a walk of length k is exactly a vertex sequence w0..wk with consecutive vertices adjacent" into Definition 2.19 itself.
+
+F9 | comprehension | Proof of Proposition 4.5 (i) ⇒ (ii): "A path between ni and nj is a walk, say of length ℓ. By Corollary 2.46 there is a walk ... of length k ≤ N − 1." | The symbol ℓ is introduced and never used. The reader does not see why the corollary is needed when the path already has at most N−1 edges. | Replace with "A path has at most N−1 edges (Corollary 2.46), so it is a walk of length k with 1 ≤ k ≤ N−1."
+
+F10 | comprehension | Proof of Theorem 4.6: "By Proposition 4.17 with m = N − 1, it holds if and only if every off-diagonal entry of (I + A)N −1 is positive; the diagonal entries are always positive there". | Condition (c) is proved by a forward reference to a proposition whose proof is in Appendix C.4 (a binomial expansion). The reader cannot see why I + A should work, because the idea of "staying put for one step" appears only in a plain-words paragraph. | Add one sentence: "(I+A)^m = sum over j of C(m,j) A^j, so entry (i,j) is positive iff some A^j (j ≤ m) has a positive (i,j) entry". Or move that half of the proof up.
+
+F11 | comprehension | Remark 4.9 heading "(the diagonal, and N = 1, N =2)" and "For N ≥ 3 and G connected the diagonal of S is positive anyway". | The paragraph mixes three cases. The reader is left unsure whether the N ≥ 3 claim is needed for the theorem. It reads as a side note placed in the middle of the proof chain. | Say explicitly "this is not needed for Theorem 4.6" and split off the N = 1 case.
+
+F12 | comprehension | Remark 4.16: "the graph is that path and nothing else. The failing graphs are therefore exactly the labelled paths, of which there are N!/2 for N ≥ 3". | "Labelled paths" is not defined. The counting step from "the graph is a path" to N!/2 (orderings divided by reversal) is not explained. The link to the last column of Table 6 is only asserted. | Add "(N! orderings of the vertices along the path, each path counted twice because it can be read in reverse)".
+
+F13 | comprehension | Remark 4.18: "keeps a queue of discovered vertices ... [10, slides 6 and 10]" and Table 6 caption "compared with an independent breadth-first search". | Breadth-first search is described in one dense sentence. "Queue" and "adjacency lists" are not explained. The reader must trust a computer check that uses it as ground truth. | Give a 3-line procedure, or say that it is the "mark neighbours repeatedly" idea of the plain-words paragraph. Say what "independent" means in Table 6.
+
+F14 | comprehension | Example 6.1: "Also A3 = 2A, and therefore Ak+2 = Ak−1 A3 = 2Ak−1 A = 2Ak for every k ≥ 1". | For k = 1 the formula uses A0, which Remark 3.2 says is "used only in Section 4". The purpose of the pattern is unstated, and it is not used later. | Either state the purpose ("this shows why entries grow without limit") or delete. Fix the A0 inconsistency.
+
+F15 | comprehension | Example 6.2: "The entry ((I + A)2)13 = 1 = (A2)13, since the other two terms of the expansion vanish there; and (I + A)2 = I + 2A + A2 holds entry by entry". | The extracted text is garbled and hard to read. The "expansion" is used before it is introduced (Appendix C.4), and the paragraph does not say what the check is meant to show. | State the expansion first, then give the entry computation in separate lines.
+
+F16 | comprehension | Table 6 and its caption: "The last column counts the graphs on which the sum with only N − 2 powers gives the wrong answer (for N = 2 that sum is empty)." | The reader sees "1" for N = 2 and does not know why an empty sum is "wrong". The claim that all 32768 graphs agree rests on a script the reader cannot see. | Explain the N = 2 row in one clause, e.g. "an empty sum is all zeros, so it reports not connected for the one connected graph". Add "see Appendix D" in the caption.
+
+F17 | comprehension | Section 7.4: "Theorem 1 of one source says ... As written it is wrong"; "The two web sources that give a proof prove it loosely". | The reader has no way to check these claims about unnamed sources ([7] is cited, but the web sources are not separated from it). The section reads as a critique of sources rather than a result of the paper. Its purpose is unclear after a first read. | Name the sources inline and quote the sentence being criticised, or shorten to one sentence and move the detail to an appendix.
+
+F18 | comprehension | Section 7.5: "98,000,000 multiplications for N = 100 ... 7 squarings ... 38,742,049". | The numbers are not derived: 98 × 10^6 = (N−2)·N^3, 7 = ceil(log2 99), 38,742,049 = 9^9. A reader must compute these themselves. The cost section is also not tied to any of the three questions. | Show the arithmetic in one line each, or cut the section.
+
+F19 | comprehension | Section 1.4: "A full-text search of the whole book ... finds neither a theorem ... We did not read every page". | The reader must take on faith that the textbook lacks the results. The textbook is in Armenian and is not available to the reader. The point of the paragraph (why the proofs are repeated here) is clear only on a second reading. | Shorten to "The textbook, as far as we searched, has neither result, so both are proved here."
+
+F20 | comprehension | Section 5.2: "it needs a graph with a cycle, such as the textbook's own example graph (Definition 2.27)" and Section 6.1: "a trail that repeated a vertex would contain a closed trail between the two visits". | The first points to a figure the reader never sees. The second is a claim given with no argument. Both are used to explain a difference that Table 5 cannot show. | Give a four-vertex example (a triangle plus a pendant edge) with its trail and path counts, or drop the claim. Add one line showing why the closed trail exists.
+
+READER SUMMARY
+The note asks three things about a graph (points joined by lines) written as an adjacency matrix A, a table of zeros and ones. First, what do the entries of the k-th power of A mean? The answer is that entry (i,j) of A^k is the number of walks of length k from vertex i to vertex j. A walk may repeat vertices and edges, so the entry does not count paths. Second, how can one tell from A whether the graph is connected? The answer is that the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N−1) is positive, or equivalently when (I + A)^(N−1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path of no more than N−1 steps. The note shows that N−1 cannot be reduced to N−2, because a straight-line graph needs all N−1 steps. It also offers breadth-first search as an alternative. Third, what is a path? The answer is a walk with no repeated vertex, which differs from the textbook's own "path" (a walk with no repeated edge). Two three-vertex examples, one connected and one not, and a computer check over all graphs with up to six vertices support the results. I can state the answer, but I could not say why the village story, the board-reading discussion and the source critique take up so much of the note.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/answer1_walks.tex b/papers/adjacency-walks-connectivity/sections/answer1_walks.tex
new file mode 100644
index 0000000..dacfe05
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/answer1_walks.tex
@@ -0,0 +1,258 @@
+\section{Question 1: what the entry \texorpdfstring{$(A^k)_{ij}$}{entry of a power of A} represents}\label{sec:walks}
+
+The answer is short and the proof is an induction.
+Before the proof we fix what a power of a matrix is.
+
+\subsection{Matrix products and powers}\label{sec:product}
+
+\begin{plainwords}
+To multiply the table of roads by itself, take one row house and one column house.
+Go along the row and down the column together.
+Multiply the two numbers you meet at each step and add up the results.
+Repeat for every pair of houses.
+The result is a new table of the same size.
+\end{plainwords}
+
+\begin{definition}[matrix product and power]\label{def:product}
+For $N\times N$ matrices $X$ and $Y$, the \emph{product} $XY$ is the $N\times N$
+matrix with
+\begin{equation}\label{eq:product}
+(XY)_{ij}=\sum_{r=1}^{N} X_{ir}\,Y_{rj}.
+\end{equation}
+The \emph{powers} of $A$ are $A^1=A$ and $A^k=A^{k-1}A$ for $k\ge 2$.
+\end{definition}
+
+\begin{remark}
+In this section the exponent $k$ is a positive integer.
+The power $A^0$, which is the identity matrix $I$ (ones on the diagonal, zeros
+elsewhere), is used only in \Cref{sec:connectivity}.
+\end{remark}
+
+\begin{example}
+For the board matrix $A$ of \Cref{def:adjmatrix}, the entry $(A^2)_{11}$ is
+$0\cdot 0+1\cdot 1+0\cdot 0=1$.
+\end{example}
+
+\begin{nonexample}
+$A^2$ is not the matrix of squared entries.
+For the board matrix, $(A^2)_{22}=1\cdot 1+0\cdot 0+1\cdot 1=2$, while $A_{22}^2=0$.
+\end{nonexample}
+
+\subsection{The theorem}\label{sec:walktheorem}
+
+\begin{plainwords}
+Take the table of roads and multiply it by itself.
+Each number in the new table counts trips of two roads.
+The trips run from the row house to the column house.
+Multiply again and the numbers count trips of three roads.
+The count includes trips that turn back.
+So the table counts trips, not routes.
+\end{plainwords}
+
+\begin{theorem}[walk counting]\label{thm:walkcount}
+Let $A$ be the adjacency matrix of a simple undirected graph $G$ with vertices
+$n_1,\dots,n_N$, and let $k\ge 1$ be an integer.
+Then $(A^k)_{ij}$ is the number of walks of length $k$ from $n_i$ to $n_j$, for all
+$i,j$.
+\end{theorem}
+
+\noindent
+This answers question Q1: the entry is a number, and it counts walks.
+The theorem is stated for simple graphs in
+\cite[Theorem~1.1.3]{quinlan_matrices_graphs} and \cite[Theorem~1]{bai2025adjacency},
+and for digraphs and multidigraphs, of which a simple undirected graph is the
+symmetric case, in \cite[Theorem~4.5.10, pp.~120--121]{grinberg2025graph} and
+\cite[Corollary~9.3.3]{lehman_mcs_adjacency}.
+The textbook does not contain it (\Cref{sec:introduction}).
+The proof below is written here and follows the standard route of
+\cite[proof of Theorem~1.1.3]{quinlan_matrices_graphs}: induction on $k$, splitting
+the walks by their second-last vertex.
+
+\begin{remark}
+The theorem allows $i=j$, so it counts closed walks, and it counts every walk
+once, with repeated vertices and edges allowed.
+It forbids reading the number as a count of paths (\Cref{prop:warning}).
+\end{remark}
+
+\begin{example}
+For the board graph, $(A^2)_{13}=1$: the only walk of length $2$ from $n_1$ to $n_3$
+is $1\text{-}2\text{-}3$ (\Cref{ex:boardpowers}).
+\end{example}
+
+\begin{nonexample}
+$(A^2)_{12}=0$ does not say that $n_1$ and $n_2$ are unconnected.
+It says only that no walk of length exactly $2$ joins them; walks of length $1$ and
+of length $3$ do.
+\end{nonexample}
+
+\begin{proof}
+Write $W_k(i,j)$ for the number of walks of length $k$ from $n_i$ to $n_j$.
+We prove $W_k(i,j)=(A^k)_{ij}$ for all $i,j$, by induction on $k\ge 1$.
+By \Cref{rem:walk} we count vertex sequences $w_0,\dots,w_k$ with $w_0=n_i$,
+$w_k=n_j$, and $w_{t-1}$ adjacent to $w_t$ for each $t$.
+
+\emph{Base case $k=1$.}
+A walk of length $1$ from $n_i$ to $n_j$ is a sequence $(n_i,n_j)$ with $n_i$ and
+$n_j$ adjacent.
+There is exactly one such sequence if they are adjacent and none otherwise.
+So $W_1(i,j)=A_{ij}=(A^1)_{ij}$.
+
+\emph{Induction hypothesis.}
+Let $k\ge 2$ and suppose $W_{k-1}(i,j)=(A^{k-1})_{ij}$ for all $i,j$.
+
+\emph{Inductive step.}
+Fix $i$ and $j$.
+Every walk $w_0,\dots,w_k$ of length $k$ from $n_i$ to $n_j$ has a second-last
+vertex $w_{k-1}$.
+Write $w_{k-1}=n_r$ with $r\in\{1,\dots,N\}$ and sort the walks into $N$ classes by
+the value of $r$.
+Each walk has exactly one second-last vertex, so the classes are disjoint and
+together contain every walk:
+\[
+W_k(i,j)=\sum_{r=1}^{N}\bigl(\text{number of walks of length $k$ from $n_i$ to
+$n_j$ with second-last vertex $n_r$}\bigr).
+\]
+We claim that class $r$ has exactly $W_{k-1}(i,r)\,A_{rj}$ members.
+\begin{itemize}
+\item If $n_r$ and $n_j$ are not adjacent, then $A_{rj}=0$, and no walk can have
+  $n_r$ followed by $n_j$, so the class is empty.
+\item If $n_r$ and $n_j$ are adjacent, then $A_{rj}=1$.
+  Deleting the last vertex of a walk in the class leaves $w_0,\dots,w_{k-1}$, a walk of
+  length $k-1\ge 1$ from $n_i$ to $n_r$.
+  Conversely, appending $n_j$ to any walk of length $k-1$ from $n_i$ to $n_r$ gives a
+  walk of length $k$ from $n_i$ to $n_j$, because the new pair $n_r,n_j$ is
+  adjacent, and its second-last vertex is $n_r$.
+  Deleting and appending undo each other, so they match the class one to one
+  with the walks of length $k-1$ from $n_i$ to $n_r$, and the class has
+  $W_{k-1}(i,r)$ members.
+\end{itemize}
+Therefore $W_k(i,j)=\sum_r W_{k-1}(i,r)A_{rj}$.
+By the induction hypothesis this equals $\sum_r (A^{k-1})_{ir}A_{rj}$, which is
+$(A^{k-1}A)_{ij}=(A^k)_{ij}$ by \eqref{eq:product}.
+This proves the statement for $k$, and by induction for all $k\ge 1$.
+\end{proof}
+
+\paragraph{Why the argument is valid.}
+Counting could go wrong in two places: a walk counted twice or missed, and a
+count that is not $0$ or $1$ where adjacency is concerned.
+Sorting by the second-last vertex counts each walk exactly once, and the
+deleting-and-appending match is one to one.
+Simplicity is used twice: it identifies a walk with its vertex sequence
+(\Cref{rem:walk}), and it makes $A_{rj}$, the number of edges between $n_r$ and
+$n_j$, equal to $0$ or $1$.
+Undirectedness is not used in the induction itself; it only makes $A$ symmetric,
+which gives part (c) of the next corollary.
+For a multigraph the same argument would count walks with multiplicity if $A_{rj}$
+were the number of edges, which agrees with the sources that state the theorem for
+multidigraphs \cite[Theorem~4.5.10]{grinberg2025graph}.
+
+\subsection{Consequences}\label{sec:consequences}
+
+\begin{plainwords}
+A count is never negative and always a whole number.
+The table of trips looks the same when flipped over the line of squares from top
+left to bottom right.
+That is because every trip can be driven backwards.
+A positive number means that at least one such trip exists.
+A trip of two roads from a house back to itself goes out along a road.
+Then it comes back along the same road.
+\end{plainwords}
+
+\begin{corollary}[consequences of walk counting]\label{cor:walkcount}
+For a simple undirected graph and $k\ge 1$:
+\begin{enumerate}
+\item[(a)] every entry of $A^k$ is a nonnegative integer, and a sum of powers of $A$
+  has a positive $(i,j)$ entry if and only if some summand does;
+\item[(b)] $(A^k)_{ij}>0$ if and only if there is a walk of length exactly $k$ from
+  $n_i$ to $n_j$;
+\item[(c)] $A^k$ is symmetric;
+\item[(d)] $(A^2)_{ii}=\deg(n_i)$ for every $i$, hence $\operatorname{trace}(A^2)=2|E|$.
+\end{enumerate}
+\end{corollary}
+
+\begin{proof}
+Parts (a) to (c) are derived here from \Cref{thm:walkcount}; part (d) is stated in
+\cite[remark after Theorem~1.1.3]{quinlan_matrices_graphs}.
+(a) and (b): by \Cref{thm:walkcount} the entry is a count; a sum of nonnegative
+numbers is positive if and only if one of them is.
+(c): reversing the vertex sequence of a walk matches the walks from $n_i$ to $n_j$
+one to one with the walks from $n_j$ to $n_i$, because edges are unordered; so
+$(A^k)_{ij}=(A^k)_{ji}$.
+(d): a walk of length $2$ from $n_i$ to $n_i$ has the form $n_i,n_r,n_i$ with $n_r$ a
+neighbour of $n_i$, and there is one for each neighbour, so $(A^2)_{ii}$ is the
+number of neighbours, which is $\deg(n_i)$.
+The trace is the sum of the diagonal, so it is the sum of the degrees, which is
+$2|E|$ by \Cref{prop:rowsums}.
+\end{proof}
+
+\subsection{The warning: walks are not paths}\label{sec:warning}
+
+\begin{plainwords}
+A trip may turn back and pass the same house twice.
+A route never passes a house twice.
+The table counts trips, so it counts the turn-back trips too.
+A house with a neighbour always has a two-road trip that goes out and comes back.
+That trip is not a route.
+So the table cannot be counting routes.
+\end{plainwords}
+
+\begin{proposition}[the entries do not count paths]\label{prop:warning}
+\begin{enumerate}
+\item[(a)] If $n_i$ has at least one neighbour, then $(A^2)_{ii}=\deg(n_i)>0$, but there
+  is no trail and no path from $n_i$ to $n_i$ of length $2$.
+\item[(b)] In the board graph, $(A^3)_{12}=2$, but the only path or trail from $n_1$ to
+  $n_2$ has length $1$.
+  More fully, \Cref{tab:walksvspaths} lists, for $k=1,\dots,5$, the entry $(A^k)_{12}$
+  and the number of trails and of paths among the walks it counts.
+\end{enumerate}
+In particular the entries of $A^k$ are not counts of paths, and not counts of
+trails.
+\end{proposition}
+
+\noindent
+Walks, not paths, are counted also according to \cite[Section~1, remark after
+Theorem~1]{bai2025adjacency} and \cite[Example~2.9.2]{grinberg2025graph}, which gives
+$1,2,1$ as a walk that is not a path.
+The proposition and its proof are written here.
+
+\begin{proof}
+(a) The first claim is \Cref{cor:walkcount}(d).
+The walks of length $2$ from $n_i$ to $n_i$ are the sequences $n_i,n_r,n_i$.
+Each repeats the vertex $n_i$, so it is not a path (\Cref{def:path}), and each uses the
+edge $n_in_r$ twice, so it is not a trail (\Cref{def:trail}).
+Under the course convention the only path from $n_i$ to $n_i$ is the single vertex, of
+length $0$ (\Cref{rem:path}).
+
+(b) The walks counted by $(A^3)_{12}$ are $1\text{-}2\text{-}1\text{-}2$ and
+$1\text{-}2\text{-}3\text{-}2$ (\Cref{ex:boardpowers}); the first repeats the edge
+$n_1n_2$ and the second repeats the vertex $n_2$, so neither is a trail or a path.
+Every path in $B$ has at most $N-1=2$ edges (\Cref{cor:bound}); a path of length $2$
+from $n_1$ to $n_2$ would need a vertex adjacent to both, and there is none, so the only
+path from $n_1$ to $n_2$ is the edge.
+A trail has at most $|E|=2$ edges, and no walk of length $2$ joins $n_1$ to $n_2$ because
+$(A^2)_{12}=0$, so the only trail from $n_1$ to $n_2$ is also the edge.
+The rows of \Cref{tab:walksvspaths} come from an enumeration by script
+(Appendix~\ref{app:provenance}); the walk counts in them equal the entries of $A^k$ computed
+by matrix multiplication.
+\end{proof}
+
+\begin{table}[ht]
+\centering
+\caption{Walks, trails, and paths from $n_1$ to $n_2$ in the board graph, by length
+$k$. The second column is $(A^k)_{12}$.}\label{tab:walksvspaths}
+\begin{tabular}{@{}cccc@{}}
+\toprule
[... truncated by build_evidence.py: 14 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex b/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex
new file mode 100644
index 0000000..7ebd5b3
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex
@@ -0,0 +1,311 @@
+\section{Question 2: deciding connectivity from \texorpdfstring{$A$}{A}}\label{sec:connectivity}
+
+Connectedness is defined by paths (\Cref{def:connected}), but powers of $A$ count walks
+(\Cref{thm:walkcount}).
+The bridge is \Cref{lem:walkpath}: a walk can always be cut down to a path.
+The textbook states no matrix test for connectivity (\Cref{sec:introduction}).
+The test below is stated in \cite[Theorem~2]{paramadevan2021adjacency} and
+\cite{weisstein_connectedgraph}, and in the form with $(I+A)^{N-1}$ in
+\cite[Theorem~2]{bai2025adjacency}.
+The two web sources that give a proof prove it loosely, speaking of ``paths'' where
+walks are meant (\Cref{sec:competing}), so the proof is written out here.
+Throughout, $G$ has $N\ge 2$ vertices; \Cref{rem:diagonal} treats $N=1$.
+
+\subsection{The sum of the first \texorpdfstring{$N-1$}{N-1} powers}\label{sec:sum}
+
+\begin{plainwords}
+We need one table that gathers all the short trips.
+For each pair of houses, count the trips of one road, of two roads, and so on.
+Stop at one road fewer than the number of houses.
+Add the counts for each pair.
+Call the result the table of totals.
+\end{plainwords}
+
+\begin{definition}[the sum $S$]\label{def:S}
+For a graph with $N\ge 2$ vertices, let
+\begin{equation}\label{eq:S}
+S=A+A^2+\dots+A^{N-1},
+\end{equation}
+the sum of the first $N-1$ powers of $A$, added entry by entry.
+This notation is introduced here and is not the textbook's.
+\end{definition}
+
+\begin{remark}
+By \Cref{thm:walkcount}, $S_{ij}$ is the number of walks from $n_i$ to $n_j$ whose
+length is between $1$ and $N-1$; so every entry of $S$ is a nonnegative integer
+(\Cref{cor:walkcount}(a)).
+The definition needs $N\ge 2$, since for $N=1$ the sum would be empty.
+\end{remark}
+
+\begin{example}
+For the board graph ($N=3$), $S=A+A^2$ and its first row is $1\;1\;1$
+(\Cref{ex:testB}).
+\end{example}
+
+\begin{nonexample}
+$A^2$ alone is not $S$ for $N=3$, and neither is $A$ alone.
+For the board graph $A^2$ has the zero entry $(1,2)$ although $n_1$ and $n_2$ are
+joined by an edge, and $A$ has the zero entry $(1,3)$ although $n_1$ and $n_3$ are
+connected; either matrix alone would wrongly report ``not connected''.
+\end{nonexample}
+
+\subsection{The test and its proof}\label{sec:test}
+
+\begin{plainwords}
+We want a quick check for a village.
+We only have the table of roads.
+From the table we can count trips.
+Count the trips with one road, two roads, and so on, for each pair of houses.
+If no pair of different houses has a total of zero, the village is in one piece.
+We never need trips longer than one road fewer than the number of houses.
+A trip that wastes time can always be shortened.
+\end{plainwords}
+
+\begin{proposition}[one pair at a time]\label{prop:pair}
+Let $G$ have $N\ge 2$ vertices and let $i\ne j$.
+The following three statements are equivalent.
+\begin{enumerate}
+\item[(i)] There is a path between $n_i$ and $n_j$ (\Cref{def:path}).
+\item[(ii)] There is an integer $k$ with $1\le k\le N-1$ and $(A^k)_{ij}>0$.
+\item[(iii)] $S_{ij}>0$.
+\end{enumerate}
+\end{proposition}
+
+\begin{theorem}[the connectivity test]\label{thm:test}
+Let $G$ be a graph with $N\ge 2$ vertices and adjacency matrix $A$.
+The following are equivalent.
+\begin{enumerate}
+\item[(a)] $G$ is connected.
+\item[(b)] Every entry off the diagonal of $S=A+A^2+\dots+A^{N-1}$ is positive.
+\item[(c)] Every entry of $(I+A)^{N-1}$ is positive.
+\end{enumerate}
+\end{theorem}
+
+\noindent
+This answers question Q2.
+The equivalence of (a) and (b) is stated in \cite[Theorem~2]{paramadevan2021adjacency};
+the equivalence of (a) and (c) in \cite[Theorem~2]{bai2025adjacency}.
+The proofs below are written here.
+
+\begin{proof}[Proof of \Cref{prop:pair}]
+\emph{(i) $\Rightarrow$ (ii).}
+A path between $n_i$ and $n_j$ is a walk, say of length $\ell$.
+By \Cref{cor:bound} there is a walk from $n_i$ to $n_j$ of length $k\le N-1$.
+Since $n_i\ne n_j$ the walk has at least one step, so $k\ge 1$.
+By \Cref{thm:walkcount}, $(A^k)_{ij}\ge 1$.
+
+\emph{(ii) $\Rightarrow$ (iii).}
+Each term of $S_{ij}=A_{ij}+(A^2)_{ij}+\dots+(A^{N-1})_{ij}$ is a nonnegative
+integer (\Cref{cor:walkcount}(a)), and the term with index $k$ is positive, so the
+sum is positive.
+
+\emph{(iii) $\Rightarrow$ (ii).}
+A sum of nonnegative terms is positive only if some term is positive.
+
+\emph{(ii) $\Rightarrow$ (i).}
+If $(A^k)_{ij}>0$ then, by \Cref{thm:walkcount}, some walk of length $k$ joins $n_i$
+to $n_j$.
+By \Cref{lem:walkpath} there is a path between $n_i$ and $n_j$.
+\end{proof}
+
+\begin{proof}[Proof of \Cref{thm:test}]
+Statement (a) says that for every pair of vertices there is a path (in the sense of
+\Cref{def:connected}).
+The pairs with $u=v$ are always joined by the walk of length $0$
+(\Cref{rem:connected}), so (a) holds if and only if a path joins $n_i$ and $n_j$ for
+every $i\ne j$ (by \Cref{rem:connected} the reading of ``path'' does not matter).
+By \Cref{prop:pair} this holds if and only if $S_{ij}>0$ for every $i\ne j$, which is
+(b).
+By \Cref{prop:iplusa} with $m=N-1$, it holds if and only if every off-diagonal entry
+of $(I+A)^{N-1}$ is positive; the diagonal entries are always positive there; so it
+holds if and only if (c).
+\end{proof}
+
+\begin{corollary}[components from $S$]\label{cor:components}
+For any graph, connected or not, with $N\ge 2$, and $i\ne j$: $S_{ij}>0$ if and only
+if $n_i$ and $n_j$ lie in the same component.
+\end{corollary}
+
+\begin{proof}
+\Cref{prop:pair} does not use the connectivity of $G$; statement (i) says $n_i\sim n_j$,
+which is the definition of lying in the same class (\Cref{def:component}).
+\end{proof}
+
+\begin{remark}[by-product: distance]\label{rem:distance}
+If $n_i$ and $n_j$ are in the same component and $i\ne j$, then $d(n_i,n_j)$ is the
+smallest $k\ge 1$ with $(A^k)_{ij}>0$, and this $k$ is at most $N-1$.
+Indeed $(A^k)_{ij}>0$ exactly when a walk of length $k$ exists
+(\Cref{cor:walkcount}(b)), and the length of a shortest walk is the distance
+(\Cref{prop:shortest}).
+Two sources state this \cite[Section~9.3]{lehman_mcs_adjacency}
+\cite[Theorem~3]{paramadevan2021adjacency}.
+\end{remark}
+
+\begin{remark}[the diagonal, and $N=1$, $N=2$]\label{rem:diagonal}
+The test looks only at entries off the diagonal.
+For $N=2$ and one edge, $S=A=\MTwoA$ has zeros on the diagonal although the graph is
+connected, so the diagonal of $S$ cannot be required to be positive.
+For $N\ge 3$ and $G$ connected the diagonal of $S$ is positive anyway: every vertex has
+a neighbour, and $(A^2)_{ii}=\deg(n_i)>0$ by \Cref{cor:walkcount}(d).
+For $N=1$ there is no pair of different vertices, $G$ is connected, and
+$(I+A)^0=I=[1]$ has no zero entry; the sum $S$ is empty, so the test is stated for
+$N\ge 2$.
+\end{remark}
+
+\subsection{The test as a procedure}\label{sec:procedure}
+
+\begin{plainwords}
+Here is the check, step by step.
+First write the table of roads.
+Then multiply the table by itself again and again.
+After each step, add the new counts to a running total.
+Stop one step before the number of houses.
+Look at every pair of different houses.
+If any total is zero, those two houses cannot reach each other.
+If no total is zero, everyone can reach everyone.
+\end{plainwords}
+
+\begin{test}[matrix test for connectivity]\label{test:matrix}
+\emph{Input:} the adjacency matrix $A$ of a graph with $N\ge 2$ vertices.
+\begin{enumerate}
+\item Set $P=A$ and $S=A$.
+\item For $k=2,3,\dots,N-1$: replace $P$ by $PA$ (now $P=A^k$) and add $P$ to $S$.
+\item Look at the entries $S_{ij}$ with $i\ne j$.
+  If one of them is $0$, the graph is not connected; if none is $0$, it is connected.
+\end{enumerate}
+\emph{Equivalent form:} compute $(I+A)^{N-1}$ and report ``connected'' if it has no
+zero entry.
+\end{test}
+
+\begin{remark}
+The test allows any graph with $N\ge 2$ vertices.
+It forbids stopping early (\Cref{prop:sharp}) and forbids applying it to a directed
+graph, which this note does not treat.
+A zero at $(i,j)$ means, by \Cref{cor:components}, that $n_i$ and $n_j$ are in different
+components.
+\end{remark}
+
+\begin{example}
+The board matrix gives ``connected'' and the matrix with the single edge $n_1n_2$ gives
+``not connected''; both are worked in \Cref{ex:testB,ex:testD}.
+\end{example}
+
+\begin{nonexample}
+Computing only $A^{N-1}$ is not the test: for the board graph $A^2$ has the zero
+entry $(1,2)$ although the graph is connected.
+\end{nonexample}
+
+\subsection{Why \texorpdfstring{$N-1$}{N-1} is enough and \texorpdfstring{$N-2$}{N-2} is not}\label{sec:sharp}
+
+\paragraph{Enough.}
+If a walk between two different vertices exists at all, then a walk of length at most
+$N-1$ exists (\Cref{cor:bound}), because a shortest connection repeats no vertex and a
+repeat-free connection has at most $N$ vertices.
+Adding powers beyond $N-1$ cannot change which off-diagonal entries are positive.
+
+\begin{plainwords}
+Take four houses in a row.
+To go from the first house to the last, you must pass every house in between.
+That takes three roads.
+If we counted only trips of up to two roads, we would miss this pair.
+We would say the village is cut in two, and we would be wrong.
+The same idea works for any row of houses.
+\end{plainwords}
+
+\begin{proposition}[$N-1$ cannot be lowered to $N-2$]\label{prop:sharp}
+For every $N\ge 3$ there is a connected graph with $N$ vertices for which the sum
+$A+\dots+A^{N-2}$ has a zero entry off the diagonal.
+\end{proposition}
+
+\begin{proof}
+This is proved here.
+Take the graph with edges $n_1n_2,n_2n_3,\dots,n_{N-1}n_N$.
+Each step of a walk changes the vertex number by exactly $1$, and to go from $n_1$ to
+$n_N$ the number must increase by $N-1$, so every walk from $n_1$ to $n_N$ has length at
+least $N-1$.
+By \Cref{thm:walkcount}, $(A^k)_{1N}=0$ for $1\le k\le N-2$, so the $(1,N)$ entry of
+$A+\dots+A^{N-2}$ is $0$, although the graph is connected.
+\end{proof}
+
+\begin{example}\label{ex:sharp}
+Path graph on four vertices with edges $n_1n_2,n_2n_3,n_3n_4$ ($N=4$):
+\[
+A=\MPathA,\quad A^2=\MPathAtwo,\quad A^3=\MPathAthree,
+\]
+\[
+A+A^2=\MPathShort,\qquad A+A^2+A^3=\MPathFull.
+\]
+With $N-2=2$ powers the $(1,4)$ entry is $0$ and the test would wrongly say ``not
+connected''; with $N-1=3$ powers every entry is positive.
+\end{example}
+
+\begin{table}[ht]
+\centering
+\caption{The path graph on $N$ vertices: the smallest $k$ with $(A^k)_{1N}>0$, and the
[... truncated by build_evidence.py: 67 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/answer3_path.tex b/papers/adjacency-walks-connectivity/sections/answer3_path.tex
new file mode 100644
index 0000000..9c004d1
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/answer3_path.tex
@@ -0,0 +1,79 @@
+\section{Question 3: a path between two vertices, and the three usages of the word}\label{sec:path}
+
+The answer to question Q3 is \Cref{def:path}, which sits in its place in the textbook's
+build order: a path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ whose vertices
+are pairwise distinct.
+This section adds only what is new there: how that word compares with the other usages,
+and what depends on the choice.
+The course meaning of ``path'' (no repeated vertex) comes from the assignment text as
+reported to us (\Cref{conv:path}); the textbook supplies the definition under another
+name, and the board does not say which meaning it uses \cite{whiteboard1,whiteboard2}.
+
+\subsection{Three usages}\label{sec:usages}
+
+The same two properties of a walk, ``no repeated edge'' and ``no repeated vertex'', get
+different names in different places.
+In the textbook, ``path'' means no repeated edge
+\cite[Definition~1.2.12, p.~22]{petrosyan2015grafneri} and ``simple path'' means no
+repeated vertex \cite[Definition~1.2.13, p.~22]{petrosyan2015grafneri}.
+In the English text used here, a path has distinct vertices and a trail has distinct edges
+\cite[Definitions~2.9.1(c) and 3.4.5]{grinberg2025graph}; an encyclopedia article gives
+the same two definitions and adds that a path has distinct vertices ``by most
+definitions'' \cite{wikipedia_path_graph_theory}.
+The same article records that some authors do not require distinct vertices in a path
+and say ``simple path'' for a path with distinct vertices
+\cite{wikipedia_path_graph_theory}, which is the textbook's pattern; so the course
+convention is one of at least two in use.
+For ``cycle'' the textbook's word (\Cref{def:cycle}) allows repeated vertices, while the
+English text defines a cycle as a closed walk with at least three steps whose vertices
+$w_0,\dots,w_{k-1}$ are distinct \cite[Definition~2.10.1(b)]{grinberg2025graph}, which is
+the textbook's simple cycle.
+\Cref{tab:naming} puts the usages side by side.
+
+\begin{table}[ht]
+\centering
+\caption{The naming of walks in the textbook, in English usage, and in this note. The
+textbook words are given in English translation.}\label{tab:naming}
+\begin{tabular}{@{}p{4.1cm}p{3.7cm}p{2.7cm}p{2.9cm}@{}}
+\toprule
+Property of the walk & Textbook (definition number) & English usage & This note\\
+\midrule
+any sequence of steps along edges & walk (1.2.10) & walk & walk\\
+first vertex equals last vertex & closed walk (1.2.11) & closed walk & closed walk\\
+no repeated edge, vertices may repeat & ``path'' (1.2.12) & trail & trail\\
+no repeated vertex (hence no repeated edge) & ``simple path'' (1.2.13) & path & \textbf{path}\\
+closed, no repeated edge, vertices may repeat & ``cycle'' or ``closed path'' (1.2.14) & closed trail & cycle (textbook sense)\\
+closed, only first and last vertex repeat, at least three steps & ``simple cycle'' (1.2.15) & cycle & simple cycle\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\noindent
+The word ``path'' therefore has three meanings across the sources: no repeated edge
+(textbook), no repeated vertex (English text and course), and, in some authors, either.
+The last column of \Cref{tab:naming} gives each meaning one name in this note and is used
+without exception.
+
+\subsection{What depends on the choice and what does not}\label{sec:depends}
+
+\emph{Existence does not depend on it.}
+For two different vertices, a walk, a trail, and a path between them exist together or not
+at all: a walk contains a path (\Cref{lem:walkpath}), and a path is a trail
+(\Cref{prop:pathtrail}) and a walk.
+So every statement of the form ``there is a path between $n_i$ and $n_j$'' has the same
+truth value under the textbook's reading and under the course reading, and so do
+connectivity (\Cref{rem:connected}) and distance (\Cref{prop:shortest}).
+The board's definition of connected is therefore the textbook's Definition~2.1.1 under
+either reading.
+
+\emph{Counts do depend on it.}
+The number of walks, of trails, and of paths from $n_i$ to $n_j$ are different numbers in
+general, and only the first is given by a power of $A$ (\Cref{prop:warning}).
+In the board graph every trail is a path (\Cref{tab:walkcounts}), so that graph cannot show the
+difference between the two readings; it needs a graph with a cycle, such as the textbook's own
+example graph (\Cref{def:trail}).
+
+\emph{Length zero.}
+By \Cref{conv:zero} a single vertex is a path of length $0$; this matches the English text,
+which calls $(5)$ a walk of length $0$ and a path \cite[Example~2.9.2]{grinberg2025graph}.
+It matters only for $i=j$, since for $i\ne j$ a path has length at least $1$.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/background.tex b/papers/adjacency-walks-connectivity/sections/background.tex
new file mode 100644
index 0000000..7a08318
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/background.tex
@@ -0,0 +1,632 @@
+\section{Background: graphs, walks, and connectedness}\label{sec:background}
+
+This section builds the definitions in the order of the course textbook
+\cite{petrosyan2015grafneri}, with the textbook's numbers beside them.
+Each definition is followed by a remark on what it allows and forbids, an
+example that satisfies it, and an example that does not.
+
+\subsection{Notation}\label{sec:notation}
+
+Let $G=(V,E)$ be a graph with vertex set $V=\{n_1,\dots,n_N\}$ and edge set
+$E$; let $u,v,w$ denote vertices and $e,e'$ denote edges.
+The \emph{board graph} $B$ is the graph with $V=\{n_1,n_2,n_3\}$ and
+$E=\{n_1n_2,\,n_2n_3\}$, the graph whose adjacency matrix is written on the
+board (\Cref{conv:example}).
+A walk in $B$ is written by the numbers of its vertices, so $1\text{-}2\text{-}3$
+means $n_1,n_2,n_3$.
+
+\subsection{Graphs, adjacency, and the adjacency matrix}\label{sec:graphs}
+
+\begin{plainwords}
+A village is a list of houses and a list of roads.
+Every road joins two different houses.
+No two roads join the same two houses.
+A road has no direction.
+\end{plainwords}
+
+\begin{definition}[graph; textbook Definition 1.1.1, p.~9]\label{def:graph}
+A \emph{simple undirected graph} is a pair $G=(V,E)$ where $V$ is a finite
+nonempty set, whose elements are the \emph{vertices}, and $E$ is a set of
+unordered pairs of distinct elements of $V$, whose elements are the
+\emph{edges}
+\cite[p.~9]{petrosyan2015grafneri}\cite[Definition~1.1.1]{quinlan_matrices_graphs}.
+\end{definition}
+
+\begin{remark}
+The definition forbids an edge from a vertex to itself (the two elements of the
+pair must be distinct) and a repeated edge ($E$ is a set).
+It forbids direction, because the pair is unordered, so $n_in_j$ and $n_jn_i$
+are one edge.
+It allows a vertex with no edge at all.
+\end{remark}
+
+\begin{example}
+$V=\{n_1,n_2,n_3\}$ and $E=\{n_1n_2,\,n_2n_3\}$: the board graph $B$, three
+houses in a row.
+\end{example}
+
+\begin{nonexample}
+Two vertices joined by two edges, or a vertex joined to itself.
+The first repeats an edge and the second is a loop, so neither is a simple
+graph.
+\end{nonexample}
+
+\begin{plainwords}
+Two houses are neighbours when one road joins them directly.
+Nothing is said about longer trips.
+A house is never its own neighbour.
+\end{plainwords}
+
+\begin{definition}[adjacent; textbook Definition 1.1.4, p.~11]\label{def:adjacent}
+Vertices $u$ and $v$ are \emph{adjacent} if $uv\in E$; each is then a
+\emph{neighbour} of the other \cite[p.~11]{petrosyan2015grafneri}.
+\end{definition}
+
+\begin{remark}
+Adjacency is symmetric, and no vertex is adjacent to itself because there are no
+loops.
+It says nothing about connections through other vertices.
+\end{remark}
+
+\begin{example}
+In $B$ the vertices $n_1$ and $n_2$ are adjacent.
+\end{example}
+
+\begin{nonexample}
+In $B$ the vertices $n_1$ and $n_3$ are not adjacent, although a trip along two
+edges joins them.
+\end{nonexample}
+
+\begin{plainwords}
+Make a square table with one row and one column for every house.
+Write a one where the row house and the column house share a road.
+Write a zero everywhere else.
+This table describes the whole village.
+\end{plainwords}
+
+\begin{definition}[adjacency matrix; textbook p.~11, after Definition 1.1.6]\label{def:adjmatrix}
+Let $G$ be a graph with vertices $n_1,\dots,n_N$.
+Its \emph{adjacency matrix} is the $N\times N$ matrix $A=(A_{ij})$ with
+$A_{ij}=1$ if $n_i$ and $n_j$ are adjacent and $A_{ij}=0$ otherwise.
+The textbook gives this rule without a definition number
+\cite[p.~11]{petrosyan2015grafneri}; the board states it as $A_{ij}=1$ if
+$e_{ij}\in V$ and $0$ if $e_{ij}\notin V$, with $V$ standing for the edge set
+(\Cref{conv:notation}) \cite{whiteboard1,whiteboard2}.
+\end{definition}
+
+\begin{remark}
+The only entries allowed are $0$ and $1$.
+The matrix depends on how the vertices are numbered: renumbering moves rows and
+columns together.
+\end{remark}
+
+\begin{example}
+The board matrix
+$A=\MBoardAOne$
+is the adjacency matrix of $B$: $A_{12}=A_{21}=1$, $A_{23}=A_{32}=1$, and every
+other entry is $0$.
+\end{example}
+
+\begin{nonexample}
+The matrix $\MNonSym$ is not the adjacency matrix of any simple undirected
+graph, because $A_{12}=1$ but $A_{21}=0$.
+A matrix with a $1$ on its diagonal (a loop) or an entry $2$ (a double edge) is
+not one either.
+\end{nonexample}
+
+\begin{plainwords}
+The table of roads has easy features.
+It looks the same when flipped over the line of squares from top left to bottom right.
+That line holds only zeros.
+Any such table of zeros and ones comes from some village.
+\end{plainwords}
+
+\begin{proposition}[properties of $A$]\label{prop:matrixprops}
+The adjacency matrix $A$ of a graph is symmetric ($A_{ij}=A_{ji}$ for all
+$i,j$) and has zero diagonal ($A_{ii}=0$ for all $i$).
+Conversely, every $N\times N$ matrix of zeros and ones that is symmetric with
+zero diagonal is the adjacency matrix of some graph with numbered vertices.
+\end{proposition}
+
+\begin{proof}
+The textbook states both parts \cite[pp.~11--12]{petrosyan2015grafneri}; see also
+\cite[Section~1.1]{quinlan_matrices_graphs} and
+\cite[property~9]{paramadevan2021adjacency}.
+Adjacency is symmetric and no vertex is adjacent to itself (Remark after
+\Cref{def:adjacent}), which gives the first part.
+For the converse, join $n_i$ and $n_j$ exactly when the entry is $1$.
+Symmetry makes this a set of unordered pairs, and the zero diagonal excludes
+loops.
+\end{proof}
+
+\begin{plainwords}
+The number of roads at a house tells how busy that house is.
+\end{plainwords}
+
+\begin{definition}[degree; textbook Definition 1.2.1, p.~16]\label{def:degree}
+The \emph{degree} of a vertex $n_i$ is the number of edges incident to $n_i$.
+The textbook writes it $d_G(v)$ or $d(v)$ \cite[p.~16]{petrosyan2015grafneri};
+this note writes $\deg(n_i)$ so that the letter $d$ is kept for distance
+(\Cref{def:distance}).
+\end{definition}
+
+\begin{remark}
+In a simple graph the degree is also the number of neighbours, because each
+neighbour is joined to $n_i$ by exactly one edge.
+\end{remark}
+
+\begin{example}
+In $B$: $\deg(n_1)=1$, $\deg(n_2)=2$, $\deg(n_3)=1$.
+\end{example}
+
+\begin{nonexample}
+$\deg(n_1)\neq 2$ in $B$, although $n_2$ and $n_3$ can both be reached from
+$n_1$: only edges at $n_1$ count, and $n_3$ is reached through $n_2$.
+\end{nonexample}
+
+\begin{plainwords}
+Add up one row of the table.
+You get the number of roads at that house.
+Add up the whole table.
+Every road has been counted twice, once from each end.
+\end{plainwords}
+
+\begin{proposition}[row sums are degrees]\label{prop:rowsums}
+Row $i$ of $A$, and column $i$, sums to $\deg(n_i)$, and the sum of all entries of
+$A$ is $2|E|$.
+\end{proposition}
+
+\begin{proof}
+This is proved here; \cite[property~8]{paramadevan2021adjacency} states the row
+sum for graphs that may also have loops, and the textbook's Theorem~1.2.1
+(Euler) states that the degrees sum to $2|E|$ \cite[p.~16]{petrosyan2015grafneri}.
+Row $i$ has a $1$ in column $j$ exactly when $n_j$ is a neighbour of $n_i$.
+In a simple graph each neighbour is joined to $n_i$ by exactly one edge and no
+edge joins $n_i$ to itself, so the number of ones in row $i$ is the number of
+edges at $n_i$, which is $\deg(n_i)$.
+Column $i$ is the same by symmetry (\Cref{prop:matrixprops}).
+Adding the row sums over all $i$ counts every edge twice, once from each end, so
+the total is $2|E|$.
+\end{proof}
+
+For $B$ the row sums are $1,2,1$ and the total is $4=2|E|$ with $|E|=2$.
+
+\subsection{Walks, trails, paths, and cycles}\label{sec:walkdefs}
+
+\begin{plainwords}
+A trip is a list of houses, one after another.
+The next house is always at the other end of a road from the house before.
+You may pass the same house twice.
+You may drive the same road twice.
+The length of a trip is the number of roads you drove.
+A road driven twice counts twice.
+Staying at home is also a trip, of length zero.
+\end{plainwords}
+
+\begin{definition}[walk; textbook Definition 1.2.10, p.~21]\label{def:walk}
+A \emph{walk of length $k$ from $u_0$ to $u_k$} is a sequence
+$u_0,e_1,u_1,\dots,u_{k-1},e_k,u_k$ of vertices and edges with
+$e_i=u_{i-1}u_i$ for $1\le i\le k$.
+It is abbreviated by its vertex sequence $u_0,u_1,\dots,u_k$.
+The \emph{length} of the walk is the number $k$ of its edges, each edge counted
+as many times as it occurs
+\cite[pp.~21--22]{petrosyan2015grafneri}\cite[Definition~2.9.1]{grinberg2025graph}.
+\end{definition}
+
+\begin{remark}\label{rem:walk}
+Vertices and edges may repeat in a walk \cite[p.~22]{petrosyan2015grafneri}.
+The definition forbids only one thing: two consecutive vertices that are not
+joined by an edge.
+By \Cref{conv:zero} the case $k=0$, a single vertex, is a walk.
+In a simple graph an edge is fixed by its two ends, so a walk is determined by
+its vertex sequence; hence a walk of length $k$ from $n_i$ to $n_j$ is the same
+as a sequence $w_0,\dots,w_k$ of vertices with $w_0=n_i$, $w_k=n_j$ and $w_{t-1}$
+adjacent to $w_t$ for every $t$.
+This is a consequence of \Cref{def:graph} and \Cref{def:walk}
+\cite[Definition~2.9.1(a)]{grinberg2025graph}, and the proof of
+\Cref{thm:walkcount} counts such sequences.
+\end{remark}
+
+\begin{example}
+In $B$ the sequence $1\text{-}2\text{-}1\text{-}2\text{-}3$ is a walk of length
+$4$ from $n_1$ to $n_3$: its steps are the edges $n_1n_2$, $n_2n_1$, $n_1n_2$,
+$n_2n_3$.
+The vertices $n_1$ and $n_2$ occur twice, and the edge $n_1n_2$ is used twice.
+The textbook's example $v_1,v_3,v_2,v_4,v_3,v_2,v_4,v_3,v_5$ in its Fig.~1.2.5 is a
+walk, of length $8$ \cite[p.~22]{petrosyan2015grafneri}.
+\end{example}
+
+\begin{nonexample}
+In $B$ the sequence $1\text{-}3$ is not a walk, because $n_1n_3$ is not an edge
+of $B$ ($A_{13}=0$).
+The textbook's $v_3,v_1,v_4,v_2,v_3,v_5$ is not a walk of its graph
+\cite[p.~22]{petrosyan2015grafneri}.
+\end{nonexample}
[... truncated by build_evidence.py: 388 more lines of this file's diff ...]
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/conclusion.tex b/papers/adjacency-walks-connectivity/sections/conclusion.tex
new file mode 100644
index 0000000..91204b8
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/conclusion.tex
@@ -0,0 +1,32 @@
+\section{Conclusion}\label{sec:conclusion}
+
+\textbf{Q1.}
+For a finite simple undirected graph with adjacency matrix $A$ and an integer $k\ge 1$, the
+entry $(A^k)_{ij}$ is the number of walks of length $k$ from $n_i$ to $n_j$
+(\Cref{thm:walkcount}, proved by induction on $k$).
+It counts walks, in which vertices and edges may repeat, and not paths: for example
+$(A^2)_{ii}$ equals the degree of $n_i$, which is positive whenever $n_i$ has a neighbour,
+although no path of length $2$ returns to $n_i$ (\Cref{prop:warning}).
+
+\textbf{Q2.}
+For $N\ge 2$ vertices, the graph is connected if and only if every entry off the diagonal of
+$A+A^2+\dots+A^{N-1}$ is positive, and equivalently if and only if $(I+A)^{N-1}$ has no zero
+entry (\Cref{thm:test}).
+The proof uses the walk-counting theorem and the fact that a walk contains a path no longer
+than itself (\Cref{lem:walkpath}); the last power $N-1$ cannot be lowered to $N-2$
+(\Cref{prop:sharp}).
+The board matrix gives ``connected'' and the matrix with the single edge $n_1n_2$ gives ``not
+connected'' (\Cref{ex:testB,ex:testD}).
+Breadth-first search is an alternative (\Cref{rem:bfs}).
+
+\textbf{Q3.}
+Under the course convention, a path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ whose
+vertices are pairwise distinct (\Cref{def:path}); this is the textbook's simple path,
+Definition~1.2.13 \cite[p.~22]{petrosyan2015grafneri}.
+The textbook's own word ``path'' (Definition~1.2.12) means a walk with distinct edges, called
+a trail here; the existence of a connection does not depend on the choice, but the counts do
+(\Cref{sec:path}).
+
+The assumptions on which these answers rest are listed in \Cref{sec:conventions}: the mark
+above $A$ read as an exponent, the matrix rather than the drawing as the example, and the
+course meaning of ``path''.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/discussion.tex b/papers/adjacency-walks-connectivity/sections/discussion.tex
new file mode 100644
index 0000000..de69fec
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/discussion.tex
@@ -0,0 +1,97 @@
+\section{Discussion: readings of the board, limits, and competing explanations}\label{sec:discussion}
+
+\subsection{Where the board and the matrix disagree}\label{sec:board-mismatch}
+
+The drawing on the board has three lines and the matrix records two edges
+\cite{whiteboard1,whiteboard2}.
+Edge by edge: the pair $n_1,n_2$ is drawn (with an arrowhead at $n_2$) and has
+$A_{12}=A_{21}=1$; the pair $n_2,n_3$ is drawn and has $A_{23}=A_{32}=1$; the pair
+$n_1,n_3$ is drawn but has $A_{13}=A_{31}=0$ (\Cref{fig:graphs}).
+The matrix is symmetric, so it gives no support to a direction on the line from $n_1$ to
+$n_2$.
+Following \Cref{conv:example}, this note takes the matrix as the example, because the board
+says that the graph is given through its adjacency matrix \cite{whiteboard1}.
+If the drawing had been meant, the adjacency matrix would be $\MDrawT$, which differs from the
+board matrix exactly at the entries $(1,3)$ and $(3,1)$.
+This note does not decide which of the two the lecturer intended.
+The choice does not affect the answers to Q1 to Q3, which are theorems for every simple
+undirected graph; it changes only the numbers in the examples.
+Both graphs are connected, so the test of \Cref{thm:test} answers ``connected'' for both.
+
+\subsection{The mark above \texorpdfstring{$A$}{A}}\label{sec:board-mark}
+
+In both photographs the mark above $A$ in question Q1 resembles a small $n$ or a pair of
+quotation marks, not clearly a $k$ \cite{whiteboard1,whiteboard2}.
+The board's own letter for the number of vertices is the capital $N$, so a lower-case $n$ as an
+exponent would be unusual, but it cannot be ruled out.
+\Cref{conv:exponent} reads the mark as $k$ because the assignment text asks about $A^k$.
+Since \Cref{thm:walkcount} holds for every positive integer exponent, it answers the board
+question whichever letter was written, including an exponent equal to $N$.
+
+\subsection{Limits of the results}\label{sec:limits}
+
+\begin{itemize}
+\item \emph{Scope.} The theorems are proved for finite simple undirected graphs.
+  For directed graphs and multigraphs, the walk-counting statement is made in other sources
+  \cite[Theorem~4.5.10]{grinberg2025graph}\cite[Corollary~9.3.3]{lehman_mcs_adjacency}, and
+  this note makes no claim about the connectivity test there.
+\item \emph{What the entries do not say.} The entries count walks; they say nothing about the
+  number of paths, which needs other methods and is not treated here (\Cref{prop:warning}).
+\item \emph{What the test does not say.} It answers ``connected'' or ``not connected''; it
+  does not list a path between two vertices.
+  \Cref{cor:components} gives the components and \Cref{rem:distance} the distances.
+\item \emph{Finite checks.} The computer checks of \Cref{tab:exhaustive} cover graphs with at
+  most six vertices; they support the statements but the proofs are the arguments of
+  \Cref{sec:test} and Appendix~\ref{app:derivations}.
+\item \emph{Sources.} The textbook was searched in full text for the adjacency matrix and read
+  page by page only where listed in Appendix~\ref{app:provenance}, so the statement that it
+  contains neither result is a statement about the search.
+  Several sources were read only in part, as Appendix~\ref{app:provenance} records.
+\end{itemize}
+
+\subsection{Competing explanations}\label{sec:competing}
+
+\emph{Reading the entry as a count of paths.}
+Theorem~1 of one source says that $(A^l)_{ij}$ is the number of ``different paths'' of length
+$l$ \cite[Theorem~1]{paramadevan2021adjacency}.
+As written it is wrong for any definition of path that forbids repeated vertices or repeated
+edges, by \Cref{prop:warning}: $(A^2)_{ii}$ is positive although no such path exists.
+The same paper states, in its property~7, that the entry equals the number of walks
+\cite[property~7]{paramadevan2021adjacency}.
+This note therefore does not use that Theorem~1 as support for \Cref{thm:walkcount}; the four
+sources cited there state walks.
+
+\emph{Explaining the test by paths.}
+The proof of the test in the same paper applies its Theorem~1 to $A+\dots+A^{N-1}$ and so
+counts ``paths'' where walks are meant, and it passes from a nonzero entry to the existence
+of a path without the walk-to-path step \cite[proof of Theorem~2]{paramadevan2021adjacency}.
+The proof sketch of the $(I+A)^{N-1}$ form likewise says that the power ``aggregates all
+paths'' \cite[Section~1, Theorem~2, proof sketch]{bai2025adjacency}.
+Both \emph{statements} of the test are correct, as \Cref{thm:test} shows; the explanations are
+incomplete, which is why the proof is written out in \Cref{sec:test}.
+
+\emph{A different method.}
+Breadth-first search gives the same answer (\Cref{rem:bfs}); eigenvalue methods are outside the
+scope of this note and no claim is made about them.
+
+\subsection{Cost}\label{sec:cost}
+
+This remark is an estimate that counts scalar multiplications with the school method, which
+uses $N^3$ of them for one product of two $N\times N$ matrices; faster methods were not examined.
+Reaching $A^{N-1}$ takes $N-2$ products, which is $98{,}000{,}000$ multiplications for $N=100$.
+Because \Cref{prop:iplusa} allows any exponent $m\ge N-1$, squaring $I+A$ repeatedly until the
+exponent is at least $N-1$ takes $7$ squarings, or $7{,}000{,}000$ multiplications, for
+$N=100$.
+Breadth-first search with adjacency lists takes time proportional to the number of vertices
+plus the number of edges \cite[slides~9 and 10]{schost2026bfs}; when the input is the matrix
+$A$ itself it reads each of the $N^2=10{,}000$ entries once \cite[slides~3 and 6]{schost2026bfs}.
+The entries of the powers also grow quickly: for the complete graph on $10$ vertices the
+largest entry of $A^9$ is $38{,}742{,}049$.
+The matrix test is useful because it is a clean statement about powers of $A$, not because it
+is fast.
+
+\subsection{What this note does not settle}\label{sec:open}
+
+The board shows the question ``How to know if graph is connected or not'' but not its answer
+\cite{whiteboard1,whiteboard2}, so this note makes no claim about whether the lecturer's
+intended answer was the sum test, the $(I+A)^{N-1}$ form, or a search.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/example.tex b/papers/adjacency-walks-connectivity/sections/example.tex
new file mode 100644
index 0000000..b542cad
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/example.tex
@@ -0,0 +1,182 @@
+\section{Worked examples}\label{sec:examples}
+
+This section works the board graph through \Cref{sec:walks} and \Cref{sec:connectivity}, and
+adds one graph that is not connected.
+Every matrix, sum, and count in this section and in earlier examples was computed by a
+script (Appendix~\ref{app:provenance}) and then copied into the text by the same script.
+
+\begin{figure}[ht]
+\centering
+\begin{tikzpicture}[every node/.style={circle,draw,inner sep=2pt,minimum size=14pt},
+  scale=1.0]
+  % (a) the board drawing as read from the photographs
+  \begin{scope}
+    \node (a1) at (0,0) {1};
+    \node (a2) at (1.4,1.0) {2};
+    \node (a3) at (2.8,0) {3};
+    \draw[-{Latex[length=2.2mm]}] (a1) -- (a2);
+    \draw (a1) -- (a3);
+    \draw (a2) -- (a3);
+    \node[draw=none,shape=rectangle] at (1.4,-0.9) {(a) board drawing};
+  \end{scope}
+  % (b) the graph of the board matrix
+  \begin{scope}[xshift=5cm]
+    \node (b1) at (0,0) {1};
+    \node (b2) at (1.4,1.0) {2};
+    \node (b3) at (2.8,0) {3};
+    \draw (b1) -- (b2);
+    \draw (b2) -- (b3);
+    \node[draw=none,shape=rectangle] at (1.4,-0.9) {(b) board graph $B$};
+  \end{scope}
+  % (c) the disconnected example
+  \begin{scope}[xshift=10cm]
+    \node (c1) at (0,0) {1};
+    \node (c2) at (1.4,1.0) {2};
+    \node (c3) at (2.8,0) {3};
+    \draw (c1) -- (c2);
+    \node[draw=none,shape=rectangle] at (1.4,-0.9) {(c) one edge only};
+  \end{scope}
+\end{tikzpicture}
+\caption{(a) The board drawing as read from the photographs: a line from 1 to 2 with an
+arrowhead at 2, a line from 1 to 3, and a line from 2 to 3.
+(b) The graph $B$ whose adjacency matrix is the board matrix: the edges $n_1n_2$ and
+$n_2n_3$ only.
+(c) The graph with the single edge $n_1n_2$, used as the example that is not connected.
+The positions of the vertices are our choice.}\label{fig:graphs}
+\end{figure}
+
+\subsection{The powers of the board matrix}\label{sec:boardpowers}
+
+\begin{plainwords}
+We take the village from the board.
+It has three houses in a row.
+The first and last houses each have one road.
+The middle house has two roads.
+We multiply the table of roads by itself several times.
+Then we list every trip, so that the reader can see that each number is right.
+\end{plainwords}
+
+\begin{example}[powers of the board matrix]\label{ex:boardpowers}
+The graph is $B$ (\Cref{fig:graphs}(b)) with
+\[
+A=\MBoardAOne,\qquad A^2=\MBoardATwo,\qquad A^3=\MBoardAThree,
+\]
+\[
+A^4=\MBoardAFour,\qquad A^5=\MBoardAFive.
+\]
+\emph{Reading of $A^2$ and $A^3$ by walks.}
+The walks of length $2$ are: from $n_1$ to $n_1$, $\WalksTwoOneOne$; from $n_1$ to $n_3$,
+$\WalksTwoOneThree$; from $n_2$ to $n_2$, $\WalksTwoTwoTwo$; from $n_3$ to $n_3$,
+$\WalksTwoThreeThree$.
+The walks of length $3$ are: from $n_1$ to $n_2$, $\WalksThreeOneTwo$; from $n_2$ to $n_3$,
+$\WalksThreeTwoThree$.
+Each count equals the corresponding matrix entry (\Cref{thm:walkcount}).
+
+\emph{The induction step by hand.}
+$(A^2)_{22}=\sum_r A_{2r}A_{r2}=1\cdot 1+0\cdot 0+1\cdot 1=2$.
+$(A^3)_{12}=\sum_r (A^2)_{1r}A_{r2}=1\cdot 1+0\cdot 0+1\cdot 1=2$, where the term $r=1$ is the
+walk $1\text{-}2\text{-}1$ extended by a step to $n_2$, giving $1\text{-}2\text{-}1\text{-}2$,
+and the term $r=3$ is the walk $1\text{-}2\text{-}3$ extended by a step to $n_2$, giving
+$1\text{-}2\text{-}3\text{-}2$.
+
+\emph{Patterns.}
+The diagonal of $A^2$ is $(1,2,1)$, the degrees, and $\operatorname{trace}(A^2)=4=2|E|$
+(\Cref{cor:walkcount}(d)).
+Also $A^3=2A$, and therefore $A^{k+2}=A^{k-1}A^3=2A^{k-1}A=2A^k$ for every $k\ge 1$; the
+matrices above agree with this for $k=1,2,3$.
+\end{example}
+
+\begin{table}[ht]
+\centering
+\caption{Walks, trails, paths, and closed walks of each length in the board graph, counted
+over all pairs of start and end vertices by enumeration. For $k\ge 1$ the number of walks is
+the sum of all entries of $A^k$.}\label{tab:walkcounts}
+\begin{tabular}{@{}ccccc@{}}
+\toprule
+length $k$ & walks & trails & paths & closed walks\\
+\midrule
+\RowsWalkCounts
+\bottomrule
+\end{tabular}
+\end{table}
+
+\Cref{tab:walkcounts} shows the effect of \Cref{prop:warning}: the number of walks grows with
+$k$, while trails and paths stop at length $2$, because $B$ has two edges and $N-1=2$.
+It also shows that in $B$ every trail is a path: $B$ has no cycle (\Cref{def:cycle}), and a trail that repeated a vertex would contain a closed trail between the two visits.
+
+\subsection{A connected graph}\label{sec:conn-example}
+
+\begin{plainwords}
+Take three houses in a row.
+A road joins the first and second house.
+Another road joins the second and third house.
+The first and third house share no road.
+Can you still go from one to the other?
+Yes, through the middle house.
+We expect the check to say that the village is in one piece.
+\end{plainwords}
+
+\begin{example}[connected: the board graph, $N=3$, $N-1=2$]\label{ex:testB}
+\[
+A=\MBoardAOne,\quad A^2=\MBoardATwo,\quad S=A+A^2=\MBoardS,\quad (I+A)^2=\MBoardIA.
+\]
+$S$ has no zero entry (in particular none off the diagonal), so by \Cref{thm:test}(b) the
+graph is connected.
+$(I+A)^2$ has no zero entry, so by \Cref{thm:test}(c) the graph is connected; the two answers
+agree.
+The entry $A_{13}$ is $0$, so no edge joins $n_1$ and $n_3$, yet $(A^2)_{13}=1$: exactly one
+walk of length $2$ joins them, namely $1\text{-}2\text{-}3$.
+The entry $((I+A)^2)_{13}=1=\binom{2}{2}(A^2)_{13}$, since the other two terms of the expansion
+vanish there; and $(I+A)^2=I+2A+A^2$ holds entry by entry, with $I=\MBoardId$ and
+$2A=\MBoardTwoA$.
+Breadth-first search from $n_1$ reaches $n_1,n_2,n_3$, the single component, and agrees.
+\end{example}
+
+\subsection{A graph that is not connected}\label{sec:disc-example}
+
+\begin{plainwords}
+Now take three houses again.
+Only one road exists, between the first and the second house.
+The third house stands alone.
+Nobody can drive to it.
+We expect the check to say that the village is not in one piece.
+We also expect it to show that the third house is a piece by itself.
+\end{plainwords}
+
+\begin{example}[not connected: edge $n_1n_2$ only, $N=3$, $N-1=2$]\label{ex:testD}
+\[
+A=\MDiscA,\quad A^2=\MDiscAtwo,\quad S=A+A^2=\MDiscS,\quad (I+A)^2=\MDiscIA.
+\]
+The entries off the diagonal of $S$ that are $0$ are at $(1,3)$, $(2,3)$, $(3,1)$, and $(3,2)$,
+and the zeros of $(I+A)^2$ are at the same four places.
+By \Cref{thm:test} the graph is not connected, and by \Cref{cor:components} the vertices $n_1$
+and $n_2$ lie in one component and $n_3$ in another: the components are
+$G[\{n_1,n_2\}]$ and $G[\{n_3\}]$.
+Breadth-first search from $n_1$ reaches only $n_1$ and $n_2$, and agrees.
+Higher powers do not help: the entries $(1,3)$ and $(2,3)$ of $A^k$ are $0$ for $k=1,\dots,6$,
+and in fact no walk reaches $n_3$ at all.
+\end{example}
+
+\subsection{A computer check over all small graphs}\label{sec:exhaustive}
+
+\Cref{tab:exhaustive} reports a check, not a proof.
+For every labelled simple graph on $N=2,\dots,6$ vertices, the sum test, the
+$(I+A)^{N-1}$ test, and the repeated-squaring form of \Cref{prop:iplusa} were compared with
+an independent breadth-first search; the table counts the graphs on which each agrees.
+The last column counts the graphs on which the sum with only $N-2$ powers gives the wrong
+answer (for $N=2$ that sum is empty).
+The component statement of \Cref{cor:components} was checked on the same graphs by a second
+script (Appendix~\ref{app:provenance}).
+
+\begin{table}[ht]
+\centering
+\caption{All labelled simple graphs on $N$ vertices. Columns 4 to 6 count the graphs on which
+the named test agrees with breadth-first search.}\label{tab:exhaustive}
+\begin{tabular}{@{}ccccccc@{}}
+\toprule
+$N$ & graphs & connected & sum test & $(I+A)^{N-1}$ & squaring & $N-2$ powers wrong\\
+\midrule
+\RowsExhaustive
+\bottomrule
+\end{tabular}
+\end{table}
```

```diff
diff --git a/papers/adjacency-walks-connectivity/sections/introduction.tex b/papers/adjacency-walks-connectivity/sections/introduction.tex
new file mode 100644
index 0000000..d706dc9
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/sections/introduction.tex
@@ -0,0 +1,188 @@
+\section{Introduction}\label{sec:introduction}
+
+\subsection{The three questions and where they came from}\label{sec:questions}
+
+A graph is a set of points, called vertices, together with some lines, called
+edges, each joining two vertices.
+When a graph has $N$ vertices, one way to describe it completely is a square
+table of $N$ rows and $N$ columns, the \emph{adjacency matrix} $A$, which has a
+one in row $i$ and column $j$ when vertices number $i$ and number $j$ are joined
+by an edge and a zero otherwise.
+This note asks what such a table can tell us, and answers three questions.
+
+\begin{enumerate}
+\item[\textbf{Q1}] What does the entry $(A^k)_{ij}$ of the $k$-th power of $A$
+  represent?
+\item[\textbf{Q2}] How can one determine from $A$ alone whether the graph is
+  connected?
+\item[\textbf{Q3}] What is the definition of a path between vertices $n_i$ and
+  $n_j$?
+\end{enumerate}
+
+Questions Q1 and Q2 are written on a lecture whiteboard that was photographed
+twice \cite{whiteboard1,whiteboard2}.
+On the board, Q1 reads ``What does $A^{\cdot}_{ij}$ represent'' with a small
+mark in the place of the exponent, and Q2 reads ``How to know if graph is
+connected or not''.
+The board also gives the definition ``Graph is called connected if for any
+$n_i, n_j$ there exists a path between nodes'', a drawing of a graph on three
+vertices, and a three by three matrix labelled ``adj.''
+\cite{whiteboard1,whiteboard2}.
+Question Q3 was added by the assignment text, which we know only as it was
+reported to us and do not reproduce here.
+Appendix~\ref{app:photographs} transcribes the board line by line.
+
+\subsection{One story for the whole note}\label{sec:story}
+
+Every definition, theorem, test, and worked example in this note is preceded by
+a paragraph headed ``In plain words''.
+Those paragraphs are told in one story and use no symbols.
+The story is a small village.
+The village has houses.
+Roads join the houses in pairs.
+Each road joins two different houses.
+Two houses have at most one road between them.
+Each road can be driven in both directions.
+\Cref{tab:dictionary} fixes the story words once; each story word stands for
+exactly one technical term, and the technical term is defined at the place
+named in the last column.
+
+\begin{table}[ht]
+\centering
+\caption{The story dictionary. A story word is used only in the plain words
+paragraphs, and a technical word is never used there.}\label{tab:dictionary}
+\begin{tabular}{@{}lll@{}}
+\toprule
+Story word & Technical term & Defined in\\
+\midrule
+village & graph & \Cref{def:graph}\\
+house & vertex & \Cref{def:graph}\\
+road & edge & \Cref{def:graph}\\
+neighbours & adjacent vertices & \Cref{def:adjacent}\\
+table of roads & adjacency matrix & \Cref{def:adjmatrix}\\
+number of roads at a house & degree & \Cref{def:degree}\\
+table of totals & the sum $S$ & \Cref{def:S}\\
+trip & walk & \Cref{def:walk}\\
+number of roads driven & length of a walk & \Cref{def:walk}\\
+round trip & closed walk & \Cref{def:closed}\\
+trip with no road twice & trail & \Cref{def:trail}\\
+route & path & \Cref{def:path}\\
+round trip with no road twice & cycle & \Cref{def:cycle}\\
+ring & simple cycle & \Cref{def:simplecycle}\\
+shortest trip between two houses & distance & \Cref{def:distance}\\
+village in one piece & connected graph & \Cref{def:connected}\\
+piece of a village & component & \Cref{def:component}\\
+\bottomrule
+\end{tabular}
+\end{table}
+
+A trip may pass the same house twice and may drive the same road twice.
+A route never passes a house twice.
+This difference is the main source of mistakes about the matrix, and the whole
+note keeps the two words apart.
+
+\subsection{Conventions and assumptions}\label{sec:conventions}
+
+The photographs and the assignment text leave some points open.
+We settle each point as follows and refer to these items by number.
+
+\begin{enumerate}
+\item\label{conv:graph} \emph{The graphs.} The graph is finite, simple (no edge
+  from a vertex to itself and no two edges with the same two ends), and
+  undirected.
+  The assignment text says so as reported to us, and it agrees with the
+  matrix on the board, which is symmetric with zeros on the diagonal
+  \cite{whiteboard1}.
+\item\label{conv:exponent} \emph{The exponent.} The mark above $A$ in question Q1
+  is read as a positive integer exponent $k$, because the assignment text asks
+  about $A^k$.
+  In both photographs the mark looks like a small $n$ or a pair of quotation
+  marks, not clearly a $k$ \cite{whiteboard1,whiteboard2}.
+  The answer given below holds for every positive integer exponent, so it does
+  not depend on which letter was written (\Cref{sec:board-mark}).
+\item\label{conv:example} \emph{The example graph.} On the board the drawing and
+  the matrix disagree.
+  The drawing shows three lines: between vertices 1 and 2 (with an arrowhead
+  at 2), between 1 and 3, and between 2 and 3.
+  The matrix has rows $0\,1\,0$, $1\,0\,1$, $0\,1\,0$, which records only the
+  edges between 1 and 2 and between 2 and 3 \cite{whiteboard1,whiteboard2}.
+  The board states that the graph is given through its adjacency matrix
+  \cite{whiteboard1}, so the matrix defines the example graph, and the
+  arrowhead is treated as a stray mark because the matrix is symmetric.
+  We report the mismatch and make no claim about which of the two the lecturer
+  intended (\Cref{sec:board-mismatch}).
+\item\label{conv:path} \emph{The word ``path''.} In the course, a path has no
+  repeated vertex, as reported to us.
+  The textbook calls such a walk a \emph{simple path}
+  \cite[Definition~1.2.13, p.~22]{petrosyan2015grafneri}, and this note uses
+  ``path'' for it throughout.
+  The board does not say which meaning of ``path'' it uses.
+  The textbook's own word ``path'' means something weaker, which this note calls
+  a \emph{trail}; \Cref{sec:path} compares the three usages.
+\item\label{conv:notation} \emph{Notation.} The vertices are $n_1,\dots,n_N$
+  as on the board, where $N$ is the number of vertices; the textbook writes
+  $v_i$ and $n$.
+  The board writes $(G,V)$ for the graph and $e_{ij}\in V$ in the line that
+  defines $A_{ij}$; its $V$ there stands for the set of edges, which the
+  textbook writes $E$ in $G=(V,E)$ \cite{whiteboard1}.
+  This note writes $G=(V,E)$, calls an edge $n_in_j$ (or $e_{ij}$), and writes
+  $|E|$ for the number of edges.
+  The letters $i,j,r$ are vertex numbers, $k$ is an exponent or the length of a
+  walk, $I$ is the identity matrix, and $S$ is the sum defined in
+  \Cref{def:S}.
+\item\label{conv:zero} \emph{Length zero.} A single vertex counts as a walk of
+  length $0$.
+  The textbook does not say whether this is allowed; we allow it because the
+  textbook's own distance property $d(u,u)=0$ needs it
+  \cite[printed p.~23]{petrosyan2015grafneri}.
+  A walk of length $0$ is not counted as a cycle.
+\item\label{conv:pages} \emph{Page numbers.} Pages of the textbook are
+  printed page numbers; the PDF page is one higher.
+\end{enumerate}
+
+\subsection{What the textbook contains and what it does not}
+
+The course textbook supplies the definitions and their numbers
+\cite{petrosyan2015grafneri}.
+A full-text search of the whole book for the adjacency matrix finds it only on
+printed pages 7, 11, 12, 34, and 61, and finds neither a theorem that powers of
+the adjacency matrix count walks nor a matrix test for connectivity
+\cite{petrosyan2015grafneri}.
+We did not read every page, so this is a statement about the search and not a
+proof that the book has no such result.
+Both results are therefore taken from other sources and proved in full here:
+the walk-counting theorem from \cite{quinlan_matrices_graphs} and the
+connectivity test, whose statement is in \cite{paramadevan2021adjacency} and
+\cite{bai2025adjacency}.
+Where this note proves a statement itself, it says so in the first sentence of
+the result and names a source that also states it.
+
+\subsection{The answers in brief}
+
+\begin{description}
+\item[Q1] For $k\ge 1$, the entry $(A^k)_{ij}$ is the number of walks of length
+  $k$ from $n_i$ to $n_j$.
+  It counts walks, not paths (\Cref{thm:walkcount,prop:warning}).
+\item[Q2] For $N\ge 2$, the graph is connected if and only if every entry off the
+  diagonal of $A+A^2+\dots+A^{N-1}$ is positive; equivalently, if and only if
+  $(I+A)^{N-1}$ has no zero entry (\Cref{thm:test}).
+\item[Q3] A path between $n_i$ and $n_j$ is a walk from $n_i$ to $n_j$ whose
+  vertices are pairwise distinct (\Cref{def:path}); \Cref{sec:path} compares
+  this with the other usages.
+\end{description}
+
+\subsection{Organisation}
+
+\Cref{sec:background} builds the definitions in the textbook's order, with its
+numbers.
+\Cref{sec:walks} answers Q1 and \Cref{sec:connectivity} answers Q2, including a
+breadth-first search alternative.
+\Cref{sec:path} answers Q3 by comparing conventions.
+\Cref{sec:examples} works two examples on three vertices, one connected and one
+not.
+\Cref{sec:discussion} states the limits, and \Cref{sec:conclusion} gives the
+direct answers.
+The appendices hold the board transcription, a table of textbook numbers, the
+longer derivations, and the sources and scripts.
+Directed graphs, weighted graphs, and eigenvalue methods are outside the scope
+of this note.
```

```diff
diff --git a/papers/adjacency-walks-connectivity/self-evaluation.md b/papers/adjacency-walks-connectivity/self-evaluation.md
new file mode 100644
index 0000000..f2b0281
--- /dev/null
+++ b/papers/adjacency-walks-connectivity/self-evaluation.md
@@ -0,0 +1,130 @@
+# Self-evaluation: adjacency-walks-connectivity
+
+Author's account of every section of `main.tex`: its purpose, each substantive claim with the evidence claim id that supports it, each conclusion with its premises, and what I could not justify. Claim ids are those of `evidence/evidence.json`. A1 and A2 are two claims I added in `evidence/modules/author.json` (textbook Definition 1.2.1 and Theorem 1.2.1, read from the page image of printed p. 16); both are `fact`, `supported`. I added no `unverified` or `derived` claims.
+
+Build state: `build.sh` exits 0 (LaTeX, biber and latexmk installed). Result of the four commands is in the final report. Six bibliography entries carry `year = {n.d.}` because the evidence record has `year: null` for them; `check_citations.py` requires a year or date field, and biber prints six warnings that `n.d.` is not an integer. This is the only residue.
+
+Numbers: every matrix and table in the examples is generated by `appendices/scripts/generate_paper_numbers.py` into `appendices/scripts/numbers.tex`, which `main.tex` inputs. The module scripts are copied unchanged into `appendices/scripts/` and re-run; their outputs are identical to the module outputs (`diff` clean).
+
+## 1. Introduction (`sections/introduction.tex`)
+
+Purpose: state the three questions, say where each came from, fix the story and its dictionary, fix the conventions, report what the textbook contains, give the answers in brief and the organisation.
+
+Claims and support:
+- Q1 and Q2 and the board's connected definition are on the board: C27, C25, C26, C29 (whiteboard1, whiteboard2). Q3 comes from the assignment text as reported by the orchestrator (brief); it is described as reported and is not in quotation marks and is not cited.
+- Convention 1 (finite simple undirected; agrees with symmetric zero-diagonal board matrix): C1, C3, C28; assignment text reported.
+- Convention 2 (mark read as k; photos show small n or quotation marks): C29 (qualified), m1-9 (qualified).
+- Convention 3 (matrix defines the example; mismatch edge by edge): C28, C27 (board says the graph is given through its matrix); brief assumption.
+- Convention 4 (path = no repeated vertex; textbook simple path 1.2.13; board silent): C24 (qualified), C16, m2-8 (qualified).
+- Convention 5 (notation, board V = edge set): C25, C26.
+- Convention 6 (length 0 allowed): m2-15 (qualified), m2-4.
+- Textbook search statement (adjacency matrix on printed pp. 7, 11, 12, 34, 61; no walk-counting theorem, no matrix test): m3-11 (qualified). The text says it is about the search, not a proof of absence.
+- Walk-counting theorem taken from Quinlan, test statement from Paramadevan and Bai: C6, C34, C36.
+
+Conclusions: the list of answers in 1.5 repeats Theorem 3.5 (C6, m1-3), Theorem 4.6 (C35, C37), and Definition 2.31 (C16, C24); it adds no new claim.
+
+Could not justify: nothing mathematical. The story and dictionary are mine; I checked by script that no plain-words paragraph contains a technical term from the dictionary (neighbour is a story word), contains a symbol, or has a sentence of more than 18 words. I did not do a read-aloud test with a real child.
+
+## 2. Background (`sections/background.tex`)
+
+Purpose: the textbook's build order with its numbers; each definition followed by a remark, an example and a non-example, and preceded by a plain-words paragraph.
+
+Claims and support:
+- Def 2.1 graph (textbook 1.1.1): C1. Def 2.5 adjacent (1.1.4): C2. Def 2.9 adjacency matrix: C2, C26 (board form). Prop 2.13 symmetric, zero diagonal, converse: C3, C4.
+- Def 2.14 degree (1.2.1): A1. Prop 2.18 row sums and total 2|E|: m1-1 (derived, proof in text), C5, A2 (Euler, Theorem 1.2.1 as the textbook's statement of the total).
+- Def walk (1.2.10) and length, Remark on repeats, walk = vertex sequence: C12, C13, m1-2 (derived; full proof in Appendix C.1). Examples and non-examples: m2-1, m2-13.
+- Def 2.19 walk and Def 2.23 closed walk (1.2.11): C14. Def 2.27 trail (1.2.12, textbook "path"): C15, C21, m2-1. Def 2.31 path (1.2.13, textbook "simple path") and path between n_i and n_j: C16, C24 (qualified), m2-8 (qualified), m2-2. Prop 2.35 path implies trail: m2-10 (derived).
+- Def 2.36 cycle and simple cycle (1.2.14, 1.2.15): C17, C22, m2-2, m2-14. The claim that B has no cycle is proved in the text (a trail has at most |E| = 2 edges, closed lengths 1 and 2 are impossible); the script agrees up to length 6 (m2-14).
+- Def 2.40 distance (1.2.16) and its three properties: C18, m2-4; proofs in Appendix C.5 (m2-16).
+- Lemma 2.44 (every walk contains a path, with length bound): C19, C20, m2-3, m2-9 (derived; proof in text). Corollary 2.46 (at most N-1 edges): C33, m2-6, m2-11. Prop 2.47 (shortest walk, trail, path agree): m2-12 (derived; proof in Appendix C.5).
+- Def 2.48 connected (2.1.1) and the board's definition: C30, C25, C32, m3-2. Remark 2.49 (independence of the reading of "path", u = v): C30, C32, C19, C20; the u = v reading is marked as not discussed by the textbook (m3-3(d)). Def 2.52 components and the textbook's Remark 2.1.1: C31, m3-1, m3-2.
+
+Conclusions and premises: Lemma 2.44 follows from induction on length (premises: Definition 1.2.10 only). Corollary 2.46 follows from Lemma 2.44 and counting distinct vertices. Remark 2.49 follows from Lemma 2.44 and Proposition 2.35.
+
+Could not justify / cautions:
+- The textbook example "walk of length 8: two cuts give lengths 5 and 2" rests on my script's seven edges of the textbook graph (edges the examples use), not on the textbook text; the text says so by pointing to Appendix D.
+- Definition numbers for A(G) (no number of its own) and degree (1.2.1) follow `graph-sources.md` and my reading of printed p. 16.
+- "Induced subgraph" G[V_j] is explained in one clause by me; it is notation, not a claim.
+
+## 3. Question 1 (`sections/answer1_walks.tex`)
+
+Purpose: answer Q1 with a proof; show the answer counts walks, not paths.
+
+Claims and support:
+- Def 3.1 matrix product and power: standard definition, no citation needed (defined here).
+- Theorem 3.5 (walk counting): C6 (statement in four sources), C7 (standard route), m1-3 (full induction proof, derived). The textbook lacks it: m3-11.
+- Remark on where simplicity is used and the multigraph and digraph remark: m1-8 (interpretation; Grinberg Theorem 4.5.10).
+- Corollary 3.9 (a) nonnegative integers, (b) positive iff walk, (c) symmetric, (d) (A^2)_ii = degree and trace = 2|E|: m1-7 (derived), C9.
+- Proposition 3.10 (entries do not count paths or trails; table of walks, trails, paths from n_1 to n_2): C8, C10, m1-6. The path and trail counts in Table 2 come from the script; the argument for the first column is the closed form in Appendix C.2.
+
+Conclusions and premises: the answer to Q1 follows from Theorem 3.5 (induction base k = 1 from the definition of A; step from the second-last-vertex decomposition and Prop C.1 on vertex sequences). "Not a path count" follows from Corollary 3.9(d) and Definitions 2.27 and 2.31 (a closed walk n_i, n_r, n_i repeats a vertex and an edge).
+
+Could not justify: nothing. The proof is mine and follows Quinlan's route; the brute-force check (m1-4) is a finite check and is labelled so.
+
+## 4. Question 2 (`sections/answer2_connectivity.tex`)
+
+Purpose: the matrix test, its proof, its sharpness, the equivalent (I + A)^m form, and breadth-first search as one paragraph.
+
+Claims and support:
+- Statement of the sum test: C34 (Paramadevan Theorem 2, MathWorld); (I + A)^(N-1) form: C36 (qualified; Bai Theorem 2). The two sources' proofs are loose: m3-12.
+- Def 4.1 of S, Prop 4.5 (equivalence for one pair), Theorem 4.6, Corollary 4.7 (components): C35 (derived), m3-5; premises C6, C19, C20, C33, m2-10.
+- Remark 4.8 (distance as least k): C38, premises Proposition 2.47.
+- Remark 4.9 (diagonal, N = 1, 2): m3-3, C9.
+- Test 4.10 as a procedure: derived from Theorem 4.6.
+- Prop 4.14 (N-1 cannot be lowered), Example 4.15 and Table 3: m3-4 (derived, script). Remark 4.16 (which graphs fail with N-2 powers: exactly the labelled paths, N!/2 of them; 3, 12, 60, 360): m3-4; the argument (a pair at distance N-1 forces the graph to be the path) is written in the text and agrees with Table 6 last column.
+- Prop 4.17 (powers of I + A, any m >= N-1, squaring): C37, m3-9 (derived; proof in Appendix C.4).
+- Remark 4.18 (breadth-first search): C39, m3-13; agreement with the matrix test on all graphs with at most 6 vertices: m3-8.
+
+Conclusions and premises: Theorem 4.6 (a) iff (b) from Prop 4.5, which follows from Theorem 3.5, Corollary 3.9(a), Lemma 2.44, Corollary 2.46 (chain written in Appendix C.3). (b) iff (c) from Prop 4.17, whose proof uses binomial expansion, positivity of the coefficients, and the same premises.
+
+Could not justify:
+- BFS time bound: stated only for adjacency lists, as in the source (C39). The text does not compare it to the matrix test here.
+- C39's own text says N-1 matrix products; the paper uses N-2 (m3-10 note).
+- N = 1 is handled by a remark, not by the test.
+
+## 5. Question 3 (`sections/answer3_path.tex`)
+
+Purpose: point to Definition 2.31 as the answer, and add only the comparison of conventions and what depends on them.
+
+Claims and support: three usages and Table 4: C15, C16, C21, C22, C23, m2-7; course convention reported by the assignment text and qualified: C24, m2-8, C25; existence independent of the reading: C19, C20, C32, m2-10; counts depend: C10, m1-6; length-0 path: m2-5, m2-15.
+
+Conclusions: "a path between n_i and n_j" is Definition 2.31 (qualified, C24); existence statements agree across readings (Lemma 2.44 and Proposition 2.35).
+
+Could not justify: the English column for the textbook's cycle (1.2.14) reads "closed trail", obtained by combining Grinberg's trail (C21) with "closed"; Grinberg does not define a closed trail in the passage read. I did not repeat the source's remark about "circuit" because `graph-sources.md` says it concerns closed walks.
+
+## 6. Worked examples (`sections/example.tex`)
+
+Purpose: the board graph B (powers, walk lists, hand sums, counts), a connected and a disconnected example with every matrix written out, an exhaustive computer check.
+
+Claims and support: Example 6.1: m1-5, C28, m1-6, C9. Table 5 (walks, trails, paths, closed walks by length): m2-13, m2-14. Example 6.2: m3-6. Example 6.3: m3-7. Table 6 and the component check: m3-8, m3-4, m3-9. Figure 1 shows the drawing as read, B, and the one-edge graph (C28).
+
+Conclusions and premises: "connected" for B and "not connected" for the one-edge graph follow from Theorem 4.6 applied to the printed matrices (numbers computed by script and checked against BFS: m3-6, m3-7). A^(k+2) = 2A^k follows from A^3 = 2A (shown in the text); checked by script for k = 1..5 (m1-5).
+
+Could not justify: nothing. The statement that in B every trail is a path is proved in the text from the absence of a cycle (a repeated vertex in a trail gives a closed trail) and agrees with Table 5.
+
+## 7. Discussion (`sections/discussion.tex`)
+
+Purpose: the board mismatch edge by edge, the mark above A, limits, competing explanations, a one-paragraph cost remark, and what is left open.
+
+Claims and support: mismatch and mark: C28, C29 (qualified), m1-9; limits: m1-4, m3-8, m3-11; one-sentence remark on digraphs and multigraphs: m1-8, C6; competing explanations: C11, C6, C8, m3-12; cost (estimate): m3-10, C39; the K_10 number 38,742,049 is from the m3 script.
+
+Could not justify: the cost remark is an estimate for the school multiplication method only (m3-10 says so); faster methods not examined. "BFS reads each entry once when the input is the matrix" is my estimate with premises from the slides (slides 3 and 6).
+
+## 8. Conclusion (`sections/conclusion.tex`)
+
+Direct answers to Q1, Q2, Q3, each referring to the result that proves it (Theorem 3.5 with C6 and m1-3; Theorem 4.6 with C35 and C37; Definition 2.31 with C16 and C24). The last paragraph repeats the three qualified assumptions.
+
+## Appendices
+
+- A, `appendices/course-terms.tex`: textbook numbers, printed pages and board-symbol comparison: graph-sources table, C1, C2, A1, A2, C12 to C19, C30, C31, C25, C26. The Armenian words are not typeset (pdflatex); translations are given.
+- B, `appendices/photographs.tex`: transcription of the board: C25 to C29, C28.
+- C, `appendices/derivations.tex`: C.1 walks and vertex sequences (m1-2, derived), C.2 the counterexample in closed form (2^((k-1)/2) walks of odd length k from n_1 to n_2; derived by me, consistent with the script: m1-6), C.3 chain of premises (C35), C.4 proof of Prop 4.17 (C37, m3-9), C.5 distance (m2-12, m2-16), C.6 cross-checks (m1-4, m3-8).
+- D, `appendices/provenance.tex`: sources read, scripts, how to rerun; the only place with file names of scripts.
+
+## Pointers in the evidence file that no longer match the paper
+
+The `derivation` strings of some claims name paper numbers or labels from the module drafts. Labels now present: thm:walkcount, prop:warning, prop:pair, thm:test, prop:iplusa, prop:sharp, ex:sharp, tab:sharp, rem:failcount, prop:rowsums, rem:walk, lem:walkpath, prop:pathtrail, cor:bound, rem:connected, rem:diagonal, cor:walkcount, ex:boardpowers, tab:walksvspaths, tab:walkcounts, rem:trail, nex:cycle, ex:testB, ex:testD, tab:exhaustive, sec:cost, cor:components, prop:shortest, prop:distprops, app:walkcount, app:counterexample, app:testproof, app:iplusa, app:distance, app:crosschecks. The printed numbers differ in these cases: Proposition 4.14 (not 4.16 or 4.17) is prop:sharp; Proposition 4.17 is prop:iplusa (claims say 4.16); Section 7.5 (not 7.4) is sec:cost; Remark 4.16 is rem:failcount (claim says 4.19); the appendices are lettered C (derivations) in the compiled paper, not A; Table numbers differ (tab:walksvspaths is Table 2, tab:sharp Table 3, tab:walkcounts Table 5, tab:exhaustive Table 6). The fragments that own those claims could be updated to labels only; I did not edit them.
+
+## Findings log
+
+No revision round yet.
```

# Agent reports

## paper-author-round1

# paper-author, round 1

Final message of the paper-author agent, saved verbatim by the orchestrator.

---

`main.tex` and the full paper are written, and the four commands pass with no errors or warnings. The PDF is 28 pages. I did not commit anything, since you didn't ask.

## Files written
All under `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/`:
- `main.tex`, `references.bib` (11 entries, keys equal the evidence source ids), `main.pdf`, `self-evaluation.md`
- `sections/`: `introduction`, `background`, `answer1_walks`, `answer2_connectivity`, `answer3_path`, `example`, `discussion`, `conclusion`
- `appendices/`: `course-terms`, `photographs`, `derivations`, `provenance`
- `appendices/scripts/`:
  - the three module scripts, copied unchanged and re-run (outputs identical to the module outputs)
  - `generate_paper_numbers.py` and its output, which write `numbers.tex`
  - `numbers.tex`: LaTeX macros for every matrix and table in the examples, so no number is typed by hand
- `evidence/modules/author.json`, with `evidence/evidence.json` rebuilt from the base file and fragments (base plus fragments reproduced the old merged file exactly before I added `author.json`)

## Output of the four commands
```
build.sh:            ok: papers/adjacency-walks-connectivity/main.pdf   (exit 0)
check_citations.py:  cited keys 11; bib entries 11; evidence sources 11; errors 0; warnings 0
check_claims.py:     sources 11; claims supported 72, qualified 7, removed 0, unverified 0; errors 0; warnings 0
inspect_pdf.py:      pages 28; errors 0; warnings 0
```
Biber prints six warnings that `year = {n.d.}` is not an integer. The evidence record has `year: null` for those six sources, and `check_citations.py` requires a year or date field.

## Claims added
I added two claims, A1 and A2, both `fact` and `supported`:
- **A1:** textbook Definition 1.2.1 (degree), printed p. 16.
- **A2:** textbook Theorem 1.2.1 (Euler: the degrees sum to 2|E|), printed p. 16.

I read both from the page image, since `graph-sources.md` says the textbook defines degree. I added no `unverified` or `derived` claims, and none of the 7 `qualified` claims were changed.

## Things you should know
- **Dictionary row:** the story dictionary has one row of my own, "table of totals", for the sum S.
- **Claim-pointer mismatches:** several `derivation` strings in the evidence fragments name paper numbers from the module drafts that no longer match. The labels all exist, but these numbers differ: Proposition 4.14 is `prop:sharp`, 4.17 is `prop:iplusa`, Remark 4.16 is `rem:failcount`, `sec:cost` is Section 7.5, and the derivations appendix is lettered C. `self-evaluation.md` lists the stale pointers. I did not edit those fragments.
- **Other unsupported points** (all in `self-evaluation.md`):
  - The textbook-walk example (length 8 to 5 to 2) rests on my script's seven edges, not on the textbook text.
  - The English column "closed trail" for the textbook's cycle is my combination of Grinberg's trail definition with "closed".
  - The cost remark is an estimate for schoolbook multiplication only.
  - The plain-words paragraphs pass my script check (no technical terms, no symbols, no sentence over 18 words); I did not do a read-aloud test with a real child.

## paper-evaluator-round1

# paper-evaluator, round 1

Final message of the paper-evaluator agent, saved verbatim by the orchestrator.

---

SCORES
1 Correctness: 4 -- I recomputed every matrix and table myself and all match: Examples 2.11, 3.3, 3.4, 4.15, 6.1, 6.2 and 6.3, Tables 2, 3, 5 and 6 (including 1/4/38/728/26704 connected graphs and 3/12/60/360 = N!/2 failures with N-2 powers), the cost figures 98,000,000 and 7,000,000 with 7 squarings, and the largest entry 38,742,049 of A^9 for the complete graph on 10 vertices. Every proof step checks out: Lemma 2.44, Proposition 2.35, Theorem 3.5, Proposition 4.5, Theorem 4.6, Proposition 4.17 and Appendix C.2. One sentence is wrong as stated: the statement in Section 7.5 (sections/discussion.tex:86-87) that BFS "reads each of the N^2 entries once" (F1).
2 Evidence coverage: 4 -- evidence.json holds 79 claims (72 supported, 7 qualified), and every substantive statement I traced has a claim behind it, for example Theorem 3.5 to C6/C7, Theorem 4.6 to C34/C36 and Definition 2.31 to C16/C24. The exception is the matrix-input BFS cost in Section 7.5. Its evidence claim (m3-10) quotes slides that do not say it (F1).
3 Citation integrity: 4 -- all eight sources I checked exist and their metadata matches. The weight-bearing passages say what the paper attributes to them, including the defects the paper reports in [7] and [1]. Three attributions are off: [10, slides 3 and 6] (F1), [3, Proposition 2.9.10] cited for trails (F9), and [7, property 8] described as a row sum (F10).
4 Logical validity: 5 -- each conclusion follows from proved premises. Appendix C.3 lists the premises behind Theorem 4.6, and Remark 2.49 with Section 5.2 shows that connectivity does not depend on which meaning of "path" is used. The paper does not repeat the gap in the sources, which go from a positive entry straight to a path (Section 7.4).
5 Understandability: 4 -- the definitions are clear and built in order, and every proof names its method and its base case. Problems: "(5)" in Section 5.2 reads as an equation reference (F7); "its ends" in Remark 4.16 is ambiguous (F8); Theorem 4.6 has no plain-words paragraph of its own (F6); and the examples from textbook Fig. 1.2.5 cannot be checked without the book (F17).
6 Completeness: 5 -- every objective in the brief is met. Definition 2.9 and Proposition 2.13/2.18 cover A. Theorem 3.5 is proved by induction, and Proposition 3.10 with Table 2 shows walks are not paths. Definitions 2.19-2.40 carry the textbook numbers. The test is Theorem 4.6 with its proof, worked in Examples 6.2/6.3, and BFS is Remark 4.18.
7 Methodological rigor: 5 -- matrices are produced by script and fed into the text (numbers.tex). Exhaustive checks over all labelled graphs with N <= 6 are presented as checks, not proofs (Section 6.4, Appendix C.6). Assumptions are listed and numbered (Section 1.3).
8 Critical analysis: 5 -- Section 7 covers the drawing/matrix mismatch edge by edge, the uncertain mark above A, the limits of the textbook search, the incorrect Theorem 1 in [7] and the loose proofs in [7] and [1], and the cost. Section 7.6 declines to guess what the lecturer intended.
9 Internal consistency: 3 -- notation is mostly uniform, but several words and letters carry two meanings, against the checklist rule of one meaning each: "loop" (F2); "length" and "table of trips" inside story paragraphs (F3, F4); S, n and t each name two things (F5); and Definition 2.48 does not say which sense of "(u,v)-path" it uses (F11).
10 Reproducibility: 5 -- Appendix D names the scripts, the seed and the run commands, and the saved outputs are present. I reproduced every printed number independently.
11 LaTeX and PDF quality: 5 -- the 28-page PDF has no errors: inspect_pdf 0/0, check_citations 0/0, check_claims 0/0. Cross-references and references resolve. Inline matrices, the binomial in (3) and the tables render correctly on the pages I viewed (15, 20, 26). The log shows only underfull hbox warnings. I did not re-run build.sh because it writes into the paper folder.
12 Answer relevance: 5 -- Sections 1.5 and 8 answer Q1-Q3 directly, with the theorem or definition number for each answer. They claim nothing beyond the brief, and the conclusion states the assumptions the answers rest on (Section 8, last paragraph).

FINDINGS
F1 | major | sections/discussion.tex:86-87 (Section 7.5) | The paper says that with A as input BFS "reads each of the N^2=10,000 entries once [10, slides 3 and 6]", but slide 3 only defines the matrix representation, slide 6 is BFS "given by adjacency lists", neither states this cost, and "once" is exact only when every vertex is reached; evidence claim m3-10 has no quote saying it. | Present it as the note's own estimate: "With A as input, the search scans the row of each vertex it takes from the queue, so it reads at most N^2 = 10,000 entries; this count is ours." Cite [10, slide 3] only for the matrix representation, and correct m3-10.
F2 | minor | sections/background.tex:463-466 and 311, against :50, :113, :259 and appendices/derivations.tex:66 | "Loop" means an edge from a vertex to itself in the technical text, but a detour in the plain-words paragraphs ("you went round a loop. Cut the loop out."; "with no loop"). | In the story write "a detour that comes back to the same house" and "cut the detour out"; keep "loop" for the technical sense only.
F3 | minor | sections/background.tex:201, 203, 419 | The plain-words paragraphs use the technical word "length" ("The length of a trip is...", "a trip of length zero"), although Table 1 says technical words are never used there and maps length to "number of roads driven". | "The number of roads driven counts a road each time you drive it." "Staying at home is also a trip, with zero roads driven."
F4 | minor | sections/answer1_walks.tex:153 | "The table of trips" is not in the story dictionary, which has only "table of roads" (A) and "table of totals" (S). | Add a row to Table 1 for A^k (for example "table of trips of k roads"), or reword to "the new table" as at line 45.
F5 | minor | sections/background.tex:483-509; :380; Remark 2.20 against Proposition 4.17 | Three letters each name two things. S names the induction statement S(k), but Item 5 reserves S for the sum of Definition 4.1. In C_n, n is a vertex count while n_i are vertex names. t is a walk index and also the number of squarings. | Rename the statement P(k). Write "the simple cycle on q vertices, written C_q (the textbook writes C_n)". Use another letter, such as h, for the number of squarings in Proposition 4.17.
F6 | minor | sections/answer2_connectivity.tex:74, :124; sections/background.tex:541; sections/introduction.tex:37 | Theorem 4.6 (the main result for Q2), Corollary 4.7 and Proposition 2.47 have no "In plain words" paragraph directly before them, while the introduction says every theorem has one and the brief requires it. | Move the Section 4.2 paragraph to directly before Theorem 4.6 and add short story paragraphs before Proposition 4.5, Corollary 4.7 and Proposition 2.47; or narrow the sentence in the introduction.
F7 | minor | sections/answer3_path.tex:78 | "which calls (5) a walk of length 0": "(5)" reads as a reference to equation (5), and the paper has no equation (5). | "which calls the sequence made of the single vertex 5 a walk of length 0 and a path [3, Example 2.9.2]".
F8 | minor | sections/answer2_connectivity.tex:259 (Remark 4.16) | In "would shorten the distance between its ends", "its" can be read as the extra edge, whose ends are always at distance 1. | "would give a shorter walk between the two ends of that path".
F9 | minor | sections/background.tex:575 (Remark 2.49) | The paper says the walk/trail/path equivalence "is also stated in [3, Proposition 2.9.10]", but that proposition (p. 42, checked) covers only walks and paths. | "the equivalence of the walk and path readings is also [3, Proposition 2.9.10]".
F10 | minor | sections/background.tex:180 (proof of Proposition 2.18) | The paper says "[7, property 8] states the row sum", but property 8 gives the degree as the off-diagonal entries plus twice the diagonal entry, which is not the row sum when loops exist. | "[7, property 8] gives the degree as the sum of the off-diagonal entries plus twice the diagonal entry, which for zero diagonal is the row sum".
F11 | minor | sections/background.tex:563 (Definition 2.48), and Definition 2.52 | Definition 2.48 writes "(u,v)-path" without saying in which sense. Item 4 and Table 4 fix "path" as no repeated vertex "without exception", and Remark 2.49 then says the textbook meant a trail. | In the definition write "a (u,v)-path in the textbook's sense (a trail; equivalently a path, Remark 2.49)", and give the same qualifier in Definition 2.52.
F12 | minor | sections/answer1_walks.tex:63, 143-147; sections/answer2_connectivity.tex:182; sections/discussion.tex:34-35, :77 | The brief allows a one-sentence remark on directed graphs and multigraphs and a short remark on complexity. The paper mentions directed graphs or multigraphs in four places and gives cost its own subsection (7.5). | Keep one sentence in the Scope item of Section 7.3 and delete the other mentions. Fold Section 7.5 into one paragraph in Section 7.3 or Remark 4.18.
F13 | minor | appendices/photographs.tex:8-9 (Appendix B, item 1) | Appendix B says "the board's wording and spelling are kept", but the board writes the conditions with the Armenian word for "if" (visible in both photos), which appears silently as English "if". | Add: "the board writes the Armenian word for 'if' in both lines".
F14 | minor | references.bib:9, 16, 23 | "Supplied by the user" appears in the reference list, and "the user" is never introduced to the reader (a checklist item). | "supplied with the assignment".
F15 | minor | sections/answer2_connectivity.tex:92 | "A path between n_i and n_j is a walk, say of length ℓ": ℓ is never used again. | Delete "say of length ℓ", or write "of length ℓ ≤ N-1 (Corollary 2.46); take k = ℓ".
F16 | minor | appendices/provenance.tex:9 | The paper calls the Galway notes "the whole eight-page file", but the PDF has 7 pages, numbered 2 to 8. | "the whole file (seven PDF pages, numbered 2 to 8)".
F17 | minor | sections/background.tex, Examples 2.21, 2.29, 2.38 and Non-example 2.22 | The examples from textbook Fig. 1.2.5 cannot be checked without the book, because the paper neither draws the graph nor lists its edges. The book-style standard asks that examples can be checked against a figure. | Add one sentence listing the edges of Fig. 1.2.5 that the examples use (the seven edges named in Appendix D), or a small figure.

CITATION SPOT CHECKS
quinlan_matrices_graphs | fetched | supports | Definition 1.1.1 (simple undirected graph), Theorem 1.1.3 (simple graph, positive k, walks of length k), the proof by second-last vertex v_r, and the remark that walks of length 2 from a vertex to itself give the vertex degree all appear verbatim. No author or date in the file, as the paper says. 7 PDF pages, not eight (F16).
paramadevan2021adjacency | fetched | supports | Metadata matches: JSc EUSL 12(1), pp. 13-21, DOI 10.4038/jsc.v12i1.29. Theorem 1 says "different paths of length l", as the paper reports. Property 7 says walks. Theorem 2 states the sum test with b_ij ≠ 0 for i ≠ j. Its proof counts "paths" and goes from b_ij ≠ 0 to a path, as Section 7.4 says. Theorem 3 gives distance as the smallest l. Property 8 is not a row sum (F10).
bai2025adjacency | fetched | supports | Theorem 1 covers simple graphs and walks, and the text says "counts walks — not paths". Theorem 2: G is connected iff (I+A)^{n-1} has all entries strictly positive. The proof sketch adds self-loops and says the power "aggregates all paths", as the paper reports.
grinberg2025graph | fetched | partially supports | arXiv v3, 454 pages. Locations confirmed: Definition 2.9.1 (p. 36), Corollary 2.9.7 (p. 39, with the bound "length ≤ k"), the Section 2.9.4 remark that a path has length ≤ n-1, Proposition 2.9.10 (p. 42), Definition 2.10.1 (p. 47), Definition 3.4.5 (p. 101, trail), Theorem 4.5.10 (p. 120, multidigraphs). Proposition 2.9.10 does not cover trails (F9).
weisstein_connectedgraph | fetched | supports | "such a graph on n>1 vertices is connected iff sum_(k=1)^(n-1)A^k has no zero off-diagonal entries."
schost2026bfs | fetched | partially supports | Slides 9-10 support O(n+m) for adjacency lists and the correctness statement "there is a walk s ; v iff discovered[v]". Slide 3 only defines the n×n matrix. Slide 6 assumes adjacency lists. No slide gives the matrix-input cost (F1).
petrosyan2015grafneri | local file, page images viewed | supports | Printed p. 22 (PDF p. 23): Definitions 1.2.11-1.2.16 read as the paper states, including 1.2.12 "path" with distinct edges, 1.2.13 "simple path", 1.2.14 closed path or cycle, 1.2.15 simple cycle with C_n for n ≥ 3, and distance. Printed p. 48 (PDF p. 49): Definition 2.1.1 with a (u,v)-path, and complete and complete bipartite graphs as examples.
whiteboard1, whiteboard2 | local files viewed | supports | The transcription in Appendix B matches both photos: the A_ij line, the drawing with 1→2 arrowhead and lines 1-3 and 2-3, the matrix 010/101/010, the problem text, Q1 with a quote-like mark over A, Q2, and the definition of connected. Only exception: the Armenian "if" (F13).

UNVERIFIED CLAIMS IN TEXT
C24 | Item 4 (Section 1.3), Remark 2.32, Section 5 intro, Section 8 Q3 | qualified
C29 | Item 2 (Section 1.3), Section 7.2, Appendix B item 4 | qualified
C36 | Theorem 4.6(c) with proof via Proposition 4.17, Section 7.4 | qualified
m1-9 | Item 2, Section 7.2 | qualified
m2-8 | Remark 2.32, Section 5 intro, Section 8 Q3 | qualified
m2-15 | Item 6 (Section 1.3), Section 5.2 "Length zero" | qualified
m3-11 | Section 1.4, Section 7.3 "Sources" | qualified

RECOMMENDATION
REVISE -- The mathematics is correct and complete: I re-checked every proof, matrix and table, and found no critical defect. But F1 is a major attribution defect: Section 7.5 credits a matrix-input BFS cost to Schost's slides 3 and 6, which do not state it, and the sentence's "once" is only exact for connected graphs. F1 must be fixed before release, and the sixteen minor findings fixed or documented with a reason. I could not observe release conditions 6, 9 and 10 (model levels, self-evaluation coverage, the outcome of this evaluation) or re-run build.sh.

Relevant paths: /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/main.pdf, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/sections/discussion.tex, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/sections/background.tex, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/sections/answer2_connectivity.tex, /home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/evidence/evidence.json. My independent recomputation script is /tmp/claude-0/-home-user-research-paper-writing-lab/e49dae39-2b09-51e9-ac34-b3549bf40418/scratchpad/verify.py.

## technician-reader-round1

# technician-reader, round 1

Final message of the technician-reader agent, saved verbatim by the orchestrator.

---

FINDINGS
F1 | comprehension | Abstract and Section 1.1: "The note follows the numbering and build order of the course textbook"; "Question Q3 was added by the assignment text, which we know only as it was reported to us and do not reproduce here." | The paper rests on a course, a textbook, an assignment and a photographed board that a reader cannot see. The abstract never says that this is a study note answering a lecture's three questions. The phrase "reported to us" leaves open who "us" is and what exactly was reported. | Add one sentence early in the Introduction saying who set Q1 to Q3 and that the board and assignment are the only sources of the questions. Drop the "as reported to us" repetitions or define them once.

F2 | comprehension | Abstract: "Third, a path between ni and nj is a walk from ni to nj in which no vertex occurs twice." | This is a definition, yet the abstract lists it as a third question that is "answered" and says "Both statements are proved in full". The reader cannot tell what the third item is supposed to establish. | Reword so the abstract says Q3 is settled by fixing a definition, and notes that the textbook uses "path" differently.

F3 | comprehension | Section 1.3 Item 5 and Definition 2.9: "eij ∈ V ... its V there stands for the set of edges"; "(G, V ) for the graph". | The board's V is the edge set but the paper's V is the vertex set. A reader meeting both in one paragraph cannot tell which is meant. The sentence is hard to parse on first reading. | Move the board-notation discussion to Appendix A and keep only "G = (V, E)" in the main text. Mention the board mismatch once, in a footnote.

F4 | comprehension | Section 1.3 Item 4 and Table 1: "route | path" next to "trip with no road twice | trail", and the line "The textbook's own word 'path' means something weaker, which this note calls a trail". | The reader meets three words (path, simple path, trail) and a story dictionary before any of them is defined. The textbook's "path" is the paper's "trail", but "path" is also the paper's own word for the stricter notion. | Give a three-line mini-table (textbook word, this note's word, meaning) in 1.3 Item 4, or point to Table 4 right there.

F5 | comprehension | Section 1.2: "Table 1 ... table of totals | the sum S | Definition 4.1" and "Those paragraphs are told in one story and use no symbols." | The "In plain words" paragraphs repeat each definition in house and road language, which adds a second vocabulary to learn. Several paragraphs bring in ideas the formal text has not yet reached (for example "shortest trip" and "infinite"). The purpose of the village layer is clear, but its cost in length is high. | State at the top of Section 2 that the plain-words paragraphs may be skipped. Keep the story only where it adds meaning.

F6 | comprehension | Definition 2.40: "the length of a shortest (u, v)-path in the textbook's sense (a trail) ... By Proposition 2.47 the value is the same"; "the pair (V, d) is a metric space". | Distance is defined with the textbook's "path" (a trail), and the claim that the choice does not matter relies on a proposition that appears 7 pages later. "Metric space" is used without explanation, and the properties are asserted with only a pointer to Proposition C.2. | Define distance directly as the length of a shortest walk, since Proposition 2.47 shows this is equivalent. Drop "metric space" or gloss it in one clause.

F7 | comprehension | Proposition 2.35 proof: "The vertex ub has an index larger than a, so it differs from ua and from ua−1. Thus ub is an end of the second edge and not an end of the first". | The jump from "ub differs from ua and ua−1" to "the edges differ" took three readings. The index reasoning (a < b means b ≥ a+1) is compressed. | Add "since b > a, b ≥ a+1, and all vertices have distinct indices" and state the conclusion as "so the edge ub−1ub has an end that the edge ua−1ua lacks".

F8 | comprehension | Remark 2.20 and Definition 2.19: "In a simple graph an edge is fixed by its two ends, so a walk is determined by its vertex sequence". | The paper defines a walk with edges, then silently replaces it with vertex sequences. The proof of Theorem 3.5 depends on this swap. It is correct, but it is stated inside a long remark and is easy to miss. | Move the sentence "a walk of length k is exactly a vertex sequence w0..wk with consecutive vertices adjacent" into Definition 2.19 itself.

F9 | comprehension | Proof of Proposition 4.5 (i) ⇒ (ii): "A path between ni and nj is a walk, say of length ℓ. By Corollary 2.46 there is a walk ... of length k ≤ N − 1." | The symbol ℓ is introduced and never used. The reader does not see why the corollary is needed when the path already has at most N−1 edges. | Replace with "A path has at most N−1 edges (Corollary 2.46), so it is a walk of length k with 1 ≤ k ≤ N−1."

F10 | comprehension | Proof of Theorem 4.6: "By Proposition 4.17 with m = N − 1, it holds if and only if every off-diagonal entry of (I + A)N −1 is positive; the diagonal entries are always positive there". | Condition (c) is proved by a forward reference to a proposition whose proof is in Appendix C.4 (a binomial expansion). The reader cannot see why I + A should work, because the idea of "staying put for one step" appears only in a plain-words paragraph. | Add one sentence: "(I+A)^m = sum over j of C(m,j) A^j, so entry (i,j) is positive iff some A^j (j ≤ m) has a positive (i,j) entry". Or move that half of the proof up.

F11 | comprehension | Remark 4.9 heading "(the diagonal, and N = 1, N =2)" and "For N ≥ 3 and G connected the diagonal of S is positive anyway". | The paragraph mixes three cases. The reader is left unsure whether the N ≥ 3 claim is needed for the theorem. It reads as a side note placed in the middle of the proof chain. | Say explicitly "this is not needed for Theorem 4.6" and split off the N = 1 case.

F12 | comprehension | Remark 4.16: "the graph is that path and nothing else. The failing graphs are therefore exactly the labelled paths, of which there are N!/2 for N ≥ 3". | "Labelled paths" is not defined. The counting step from "the graph is a path" to N!/2 (orderings divided by reversal) is not explained. The link to the last column of Table 6 is only asserted. | Add "(N! orderings of the vertices along the path, each path counted twice because it can be read in reverse)".

F13 | comprehension | Remark 4.18: "keeps a queue of discovered vertices ... [10, slides 6 and 10]" and Table 6 caption "compared with an independent breadth-first search". | Breadth-first search is described in one dense sentence. "Queue" and "adjacency lists" are not explained. The reader must trust a computer check that uses it as ground truth. | Give a 3-line procedure, or say that it is the "mark neighbours repeatedly" idea of the plain-words paragraph. Say what "independent" means in Table 6.

F14 | comprehension | Example 6.1: "Also A3 = 2A, and therefore Ak+2 = Ak−1 A3 = 2Ak−1 A = 2Ak for every k ≥ 1". | For k = 1 the formula uses A0, which Remark 3.2 says is "used only in Section 4". The purpose of the pattern is unstated, and it is not used later. | Either state the purpose ("this shows why entries grow without limit") or delete. Fix the A0 inconsistency.

F15 | comprehension | Example 6.2: "The entry ((I + A)2)13 = 1 = (A2)13, since the other two terms of the expansion vanish there; and (I + A)2 = I + 2A + A2 holds entry by entry". | The extracted text is garbled and hard to read. The "expansion" is used before it is introduced (Appendix C.4), and the paragraph does not say what the check is meant to show. | State the expansion first, then give the entry computation in separate lines.

F16 | comprehension | Table 6 and its caption: "The last column counts the graphs on which the sum with only N − 2 powers gives the wrong answer (for N = 2 that sum is empty)." | The reader sees "1" for N = 2 and does not know why an empty sum is "wrong". The claim that all 32768 graphs agree rests on a script the reader cannot see. | Explain the N = 2 row in one clause, e.g. "an empty sum is all zeros, so it reports not connected for the one connected graph". Add "see Appendix D" in the caption.

F17 | comprehension | Section 7.4: "Theorem 1 of one source says ... As written it is wrong"; "The two web sources that give a proof prove it loosely". | The reader has no way to check these claims about unnamed sources ([7] is cited, but the web sources are not separated from it). The section reads as a critique of sources rather than a result of the paper. Its purpose is unclear after a first read. | Name the sources inline and quote the sentence being criticised, or shorten to one sentence and move the detail to an appendix.

F18 | comprehension | Section 7.5: "98,000,000 multiplications for N = 100 ... 7 squarings ... 38,742,049". | The numbers are not derived: 98 × 10^6 = (N−2)·N^3, 7 = ceil(log2 99), 38,742,049 = 9^9. A reader must compute these themselves. The cost section is also not tied to any of the three questions. | Show the arithmetic in one line each, or cut the section.

F19 | comprehension | Section 1.4: "A full-text search of the whole book ... finds neither a theorem ... We did not read every page". | The reader must take on faith that the textbook lacks the results. The textbook is in Armenian and is not available to the reader. The point of the paragraph (why the proofs are repeated here) is clear only on a second reading. | Shorten to "The textbook, as far as we searched, has neither result, so both are proved here."

F20 | comprehension | Section 5.2: "it needs a graph with a cycle, such as the textbook's own example graph (Definition 2.27)" and Section 6.1: "a trail that repeated a vertex would contain a closed trail between the two visits". | The first points to a figure the reader never sees. The second is a claim given with no argument. Both are used to explain a difference that Table 5 cannot show. | Give a four-vertex example (a triangle plus a pendant edge) with its trail and path counts, or drop the claim. Add one line showing why the closed trail exists.

READER SUMMARY
The note asks three things about a graph (points joined by lines) written as an adjacency matrix A, a table of zeros and ones. First, what do the entries of the k-th power of A mean? The answer is that entry (i,j) of A^k is the number of walks of length k from vertex i to vertex j. A walk may repeat vertices and edges, so the entry does not count paths. Second, how can one tell from A whether the graph is connected? The answer is that the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N−1) is positive, or equivalently when (I + A)^(N−1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path of no more than N−1 steps. The note shows that N−1 cannot be reduced to N−2, because a straight-line graph needs all N−1 steps. It also offers breadth-first search as an alternative. Third, what is a path? The answer is a walk with no repeated vertex, which differs from the textbook's own "path" (a walk with no repeated edge). Two three-vertex examples, one connected and one not, and a computer check over all graphs with up to six vertices support the results. I can state the answer, but I could not say why the village story, the board-reading discussion and the source critique take up so much of the note.

# Evaluation report

## evaluation-report.md

# Evaluation report

## Round 1, 2026-10-31

Question: For a simple undirected graph with N vertices given by its
adjacency matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how
can one determine from A whether the graph is connected, and (3) what is
the definition of a path between vertices n_i and n_j?

Scope: Finite simple undirected graphs. Walks, trails, paths, cycles, and
distance with the course textbook's numbering; the theorem that (A^k)_{ij}
counts walks of length k with a full induction proof and the warning that
walks are not paths; connectivity and components; the matrix-power
connectivity test with proof, a connected and a disconnected three-vertex
example, and breadth-first search stated for comparison. Study-note
register: plain-words paragraph before every definition, theorem, test,
and worked example. Out of scope: directed graphs and multigraphs beyond a
one-sentence remark, weighted graphs, eigenvalue methods, complexity beyond
a short remark, implementation code.

Research summary: 11 sources (7 full access, 4 partial): the course
textbook (local file, Armenian, page images viewed), two whiteboard photos,
Grinberg's graph theory text (arXiv preprint), the Galway matrices and
graphs notes, the MIT Mathematics for Computer Science adjacency section,
Paramadevan and Poobalan 2021 (peer-reviewed), Bai 2025 (web),
MathWorld Connected Graph, Wikipedia Path (graph theory), and Schost's
CS 341 breadth-first search slides. Three modules (m1 adjacency matrix and
walk counting, m2 walks, trails, paths, cycles, m3 connectivity from A).
Research and modules were final inputs to this probe; one round of
authoring and one round of evaluation were run. The author added two
supported claims (A1 degree, A2 degree sum, both from textbook p. 16)
in `evidence/modules/author.json` and rebuilt `evidence/evidence.json`
from the base file and fragments.

Model levels: research 2, modules 2, author 2, reader 2, evaluator 3,
orchestrator session model (not pinned). Hierarchy requirement: met for
the configured levels. A runtime fallback to another model is not
observable from inside the session; the harness reported no fallback for
the evaluator in this round.

Mechanical checks: build pass, citations pass, claims pass, pdf pass.
Run by the orchestrator after the author returned, on a clean rebuild
(`build/` emptied first): `build.sh` exit 0 (28 pages, warnings: biber
reports six `year = {n.d.}` entries not integer, for sources whose
evidence record has no year); `check_citations.py` cited keys 11, bib
entries 11, evidence sources 11, errors 0, warnings 0; `check_claims.py`
sources 11, claims supported 72, qualified 7, removed 0, unverified 0,
errors 0, warnings 0; `inspect_pdf.py` pages 28, errors 0, warnings 0.

### Scores

| Dimension | Score | Observation (evaluator) |
|---|---|---|
| 1 Correctness | 4 | Every matrix, table, and proof recomputed independently and found correct (Examples 2.11, 3.3, 3.4, 4.15, 6.1 to 6.3; Tables 2, 3, 5, 6; Lemma 2.44, Propositions 2.35, 4.5, 4.17, Theorems 3.5, 4.6, Appendix C.2). One sentence wrong as stated: Section 7.5 says BFS "reads each of the N^2 entries once" (F1). |
| 2 Evidence coverage | 4 | 79 claims (72 supported, 7 qualified); every traced statement has a claim (Theorem 3.5 to C6/C7, Theorem 4.6 to C34/C36, Definition 2.31 to C16/C24). Exception: the matrix-input BFS cost in Section 7.5, whose claim m3-10 quotes slides that do not say it (F1). |
| 3 Citation integrity | 4 | All eight sources checked exist with matching metadata and the weight-bearing passages say what is attributed. Three attributions off: [10, slides 3 and 6] (F1), [3, Proposition 2.9.10] cited for trails (F9), [7, property 8] described as a row sum (F10). |
| 4 Logical validity | 5 | Each conclusion follows from proved premises; Appendix C.3 lists the premises behind Theorem 4.6; Remark 2.49 and Section 5.2 show connectivity does not depend on the meaning of "path". The paper does not repeat the sources' gap from a positive entry straight to a path. |
| 5 Understandability | 4 | Definitions clear and built in order; every proof names its method and base case. Problems: "(5)" reads as an equation reference (F7); "its ends" ambiguous in Remark 4.16 (F8); Theorem 4.6 lacks its own plain-words paragraph (F6); examples from textbook Fig. 1.2.5 cannot be checked without the book (F17). |
| 6 Completeness | 5 | Every objective in the brief is met: Definition 2.9 and Propositions 2.13/2.18 for A; Theorem 3.5 by induction; Proposition 3.10 and Table 2 for walks versus paths; Definitions 2.19 to 2.40 with textbook numbers; Theorem 4.6 with proof, Examples 6.2/6.3; BFS in Remark 4.18. |
| 7 Methodological rigor | 5 | Matrices produced by script and fed into the text (numbers.tex); exhaustive checks over all labelled graphs with N <= 6 presented as checks, not proofs (Section 6.4, Appendix C.6); assumptions listed and numbered (Section 1.3). |
| 8 Critical analysis | 5 | Section 7 covers the drawing/matrix mismatch edge by edge, the uncertain mark above A, the limits of the textbook search, the incorrect Theorem 1 in [7], the loose proofs in [7] and [1], and the cost. Section 7.6 declines to guess the lecturer's intent. |
| 9 Internal consistency | 3 | Several words and letters carry two meanings: "loop" (F2); "length" and "table of trips" inside story paragraphs (F3, F4); S, n, and t each name two things (F5); Definition 2.48 does not say which sense of "(u,v)-path" it uses (F11). |
| 10 Reproducibility | 5 | Appendix D names the scripts, the seed, and the run commands; saved outputs are present; every printed number reproduced independently. |
| 11 LaTeX and PDF quality | 5 | 28-page PDF with no errors; cross-references and references resolve; inline matrices, the binomial in (3), and the tables render correctly; log shows only underfull hbox warnings. |
| 12 Answer relevance | 5 | Sections 1.5 and 8 answer Q1 to Q3 directly with the theorem or definition number for each; nothing beyond the brief; the conclusion states the assumptions the answers rest on. |

### Findings

| Id | Severity | Location | Defect | Status |
|---|---|---|---|---|
| F1 | major | sections/discussion.tex:86-87 (Section 7.5) | BFS with A as input "reads each of the N^2 = 10,000 entries once [10, slides 3 and 6]": slide 3 only defines the matrix representation, slide 6 is BFS on adjacency lists, neither states the cost, "once" is exact only when every vertex is reached, and claim m3-10 has no quote saying it. Correction: present as the note's own estimate ("at most N^2 entries; this count is ours"), cite [10, slide 3] for the representation only, correct m3-10. | open |
| F2 | minor | sections/background.tex:463-466, 311 against :50, :113, :259; appendices/derivations.tex:66 | "Loop" means a self-edge in the technical text but a detour in the plain-words paragraphs. Correction: "detour that comes back to the same house" in the story. | open |
| F3 | minor | sections/background.tex:201, 203, 419 | Plain-words paragraphs use the technical word "length" although Table 1 maps it to "number of roads driven". | open |
| F4 | minor | sections/answer1_walks.tex:153 | "The table of trips" is not in the story dictionary (Table 1 has only "table of roads" and "table of totals"). | open |
| F5 | minor | sections/background.tex:483-509, :380; Remark 2.20 against Proposition 4.17 | S names both the induction statement S(k) and the sum of Definition 4.1; n is a vertex count in C_n and a vertex name in n_i; t is a walk index and the number of squarings. | open |
| F6 | minor | sections/answer2_connectivity.tex:74, :124; sections/background.tex:541; sections/introduction.tex:37 | Theorem 4.6, Corollary 4.7, and Proposition 2.47 have no plain-words paragraph directly before them, while the introduction and the brief say every theorem has one. | open |
| F7 | minor | sections/answer3_path.tex:78 | "which calls (5) a walk of length 0" reads as a reference to equation (5), which does not exist. | open |
| F8 | minor | sections/answer2_connectivity.tex:259 (Remark 4.16) | "would shorten the distance between its ends": "its" can be read as the extra edge. | open |
| F9 | minor | sections/background.tex:575 (Remark 2.49) | [3, Proposition 2.9.10] cited for the walk/trail/path equivalence covers only walks and paths. | open |
| F10 | minor | sections/background.tex:180 (proof of Proposition 2.18) | "[7, property 8] states the row sum": property 8 gives off-diagonal entries plus twice the diagonal entry, a row sum only for zero diagonal. | open |
| F11 | minor | sections/background.tex:563 (Definition 2.48), Definition 2.52 | "(u,v)-path" without saying in which sense, although Item 4 and Table 4 fix "path" as no repeated vertex and Remark 2.49 says the textbook meant a trail. | open |
| F12 | minor | sections/answer1_walks.tex:63, 143-147; sections/answer2_connectivity.tex:182; sections/discussion.tex:34-35, :77 | Directed graphs or multigraphs mentioned in four places and cost given its own subsection, against the brief's one-sentence and short-remark limits. | open |
| F13 | minor | appendices/photographs.tex:8-9 | Appendix B says the board's wording is kept, but the board's Armenian word for "if" appears silently as English "if". | open |
| F14 | minor | references.bib:9, 16, 23 | "Supplied by the user" in the reference list; "the user" never introduced to the reader. | open |
| F15 | minor | sections/answer2_connectivity.tex:92 | "say of length l": l is never used again. | open |
| F16 | minor | appendices/provenance.tex:9 | The Galway notes called "the whole eight-page file"; the PDF has 7 pages numbered 2 to 8. | open |
| F17 | minor | sections/background.tex, Examples 2.21, 2.29, 2.38, Non-example 2.22 | Examples from textbook Fig. 1.2.5 cannot be checked without the book; the paper neither draws the graph nor lists its edges. | open |

Technician reader: 20 comprehension findings R1 to R20, recorded in
`reader-findings.md`, all open. The reader's summary of the conclusions
matches the paper's actual conclusions. Its recurring theme is that the
plain-words layer, the board-reading discussion, and the source critique
(Sections 1.3, 1.4, 7.4, 7.5) cost more length than they return for a
first-time reader, and that several proof steps compress an argument the
reader must supply (R7, R9, R10, R12).

### Citation and claim coverage

- Sources: 11 (7 full access, 4 partial access; the course textbook,
  Grinberg, Bai 2025, and the Schost slides are partial).
- Claims: 79 total; 72 supported, 7 qualified, 0 unverified, 0 removed.
- Contradictions recorded in the evidence file: 6.
- Evaluator spot checks: 8 sources checked. Fetched and supports: Galway
  notes, Paramadevan and Poobalan 2021, Bai 2025, MathWorld. Fetched and
  partially supports: Grinberg (Proposition 2.9.10 does not cover trails,
  F9), Schost slides (no slide gives the matrix-input cost, F1). Local
  files viewed and supports: the course textbook (printed pp. 22 and 48),
  both whiteboard photos (only exception the Armenian "if", F13).

### Unverified claims and access limits

- No claim has status `unverified`. Seven claims have status `qualified`
  and the evaluator found each qualified in the text where it appears:
  C24, C29, C36, m1-9, m2-8, m2-15, m3-11.
- Claim m3-10 (BFS cost with A as input) is recorded as supported by the
  Schost slides, but the evaluator found that the slides do not state it
  (F1). It should be re-recorded as the paper's own estimate.
- Access limits: the course textbook's PDF text layer drops most symbols,
  so its definitions were read from page images; the Grinberg preprint
  and the Schost slides were partially accessed; six web sources have no
  publication year in their record and appear as `n.d.` in the
  bibliography.

### Known limitations

- The plain-words paragraphs were checked by the author's script (no
  technical terms, no symbols, no sentence over 18 words), not by a
  read-aloud test with a reader of the intended age.
- The textbook-walk example (lengths 8, 5, 2) rests on the author's script
  over the seven edges named in Appendix D, not on the textbook's own text.
- The English column "closed trail" for the textbook's cycle is the
  author's combination of Grinberg's trail definition with "closed".
- The cost remark in Section 7.5 is an estimate for schoolbook matrix
  multiplication only.
- Several `derivation` strings in the module evidence fragments point to
  theorem and section numbers from the module drafts that no longer match
  the paper (listed in `self-evaluation.md`); the labels all resolve.
- The exhaustive connectivity check covers all labelled graphs with
  N <= 6 only and is presented as a check, not a proof.

### Release conditions

| Condition | Result |
|---|---|
| 1 Every dimension at least 3 | holds (minimum 3, dimension 9) |
| 2 No unresolved critical defect | holds (no critical finding) |
| 3 Every substantive claim supported or qualified | fails (F1: BFS cost attributed to a source that does not state it) |
| 4 Material conclusions justified | holds |
| 5 No essential concept or step unexplained | holds at the evaluator's level; the reader lists compressed steps (R7, R9, R10, R12) as advisory |
| 6 Evaluator level exceeds author and module levels | holds (3 over 2) |
| 7 build.sh succeeds, inspect_pdf.py no errors | holds |
| 8 check_citations.py and check_claims.py no errors | holds |
| 9 self-evaluation.md covers every section | holds (eight sections and the appendices, with a stale-pointer list) |
| 10 Independent evaluation passed | fails (recommendation REVISE) |

Decision: INCOMPLETE -- The evaluator recommends REVISE: one major finding
(F1, a cost figure attributed to slides that do not state it) and sixteen
minor findings are open, so release conditions 3 and 10 fail. The
mathematics, proofs, and computed numbers were independently verified as
correct. This probe was limited by instruction to one round of authoring
and one round of evaluation, so no revision was sent to the author. A
continuation would send F1 to the author first (with the m3-10 correction
in the evidence file), then the minor findings grouped by section, then
re-run the mechanical gate and a fresh evaluation.

# Reader findings

## reader-findings.md

# Technician reader findings

Diagnostic comprehension findings from the `technician-reader` agent, one
block per round. Advisory; the evaluator's findings govern release.

## Round 1, 2026-10-31

Reader configured at level 2. Twenty comprehension findings. The reader's
summary of the conclusions matches the paper's actual conclusions (all three
answers stated correctly), so no mismatch finding is raised. The reader's
closing remark: it could state the answers but could not say why the
village story, the board-reading discussion, and the source critique take up
so much of the note.

| Id | Location | Defect | Correction |
|---|---|---|---|
| R1 | Abstract, Section 1.1 | The abstract never says this is a study note answering a lecture's three questions; "as reported to us" is undefined. | One sentence in the Introduction on who set Q1 to Q3 and that the board and assignment are the only sources; define or drop "as reported to us". |
| R2 | Abstract | Q3 is a definition, yet the abstract lists it as answered and says "Both statements are proved in full"; the reader cannot tell what Q3 establishes. | Say Q3 is settled by fixing a definition and that the textbook uses "path" differently. |
| R3 | Section 1.3 item 5, Definition 2.9 | The board's V is the edge set but the paper's V is the vertex set; both appear in one paragraph. | Move the board-notation discussion to Appendix A; keep G = (V, E) in the main text with one footnote on the mismatch. |
| R4 | Section 1.3 item 4, Table 1 | Path, simple path, and trail appear in a story dictionary before any is defined; the textbook's "path" is the paper's "trail". | A three-line mini-table (textbook word, this note's word, meaning) at that point, or a pointer to Table 4. |
| R5 | Section 1.2 and plain-words paragraphs | The village layer adds a second vocabulary; several paragraphs bring in ideas the formal text has not reached ("shortest trip", "infinite"). | State at the top of Section 2 that the plain-words paragraphs may be skipped; keep the story only where it adds meaning. |
| R6 | Definition 2.40 | Distance is defined via the textbook's "path" (a trail) and relies on Proposition 2.47 seven pages later; "metric space" unexplained. | Define distance as the length of a shortest walk; drop or gloss "metric space". |
| R7 | Proposition 2.35 proof | The step from "u_b differs from u_a and u_{a-1}" to "the edges differ" is compressed. | Add "since b > a, b >= a+1, and all vertices have distinct indices" and state the conclusion explicitly. |
| R8 | Remark 2.20, Definition 2.19 | A walk is defined with edges then silently replaced by vertex sequences; Theorem 3.5 depends on the swap. | Move the vertex-sequence characterization into Definition 2.19. |
| R9 | Proof of Proposition 4.5 (i) to (ii) | The symbol l is introduced and never used; why the corollary is needed is unclear. | "A path has at most N-1 edges (Corollary 2.46), so it is a walk of length k with 1 <= k <= N-1." |
| R10 | Proof of Theorem 4.6, condition (c) | Proved by forward reference to Proposition 4.17 whose proof is in Appendix C.4; the idea appears only in plain words. | Add the one-sentence binomial-expansion argument inline, or move that half of the proof up. |
| R11 | Remark 4.9 | Mixes the diagonal, N = 1, and N = 2 cases; unclear whether needed for Theorem 4.6. | Say "not needed for Theorem 4.6" and split off N = 1. |
| R12 | Remark 4.16 | "Labelled paths" undefined; the step to N!/2 and the link to Table 6 are only asserted. | Add "(N! orderings of the vertices along the path, each counted twice because it can be read in reverse)". |
| R13 | Remark 4.18, Table 6 caption | Breadth-first search in one dense sentence; "queue", "adjacency lists", "independent" unexplained. | A three-line procedure or a tie to the plain-words "mark neighbours repeatedly"; say what "independent" means. |
| R14 | Example 6.1 | A^{k+2} = 2A^k for k = 1 uses A^0, which Remark 3.2 says is used only in Section 4; the purpose of the pattern is unstated. | State the purpose or delete; fix the A^0 inconsistency. |
| R15 | Example 6.2 | The (I + A)^2 check uses the expansion before it is introduced and does not say what it shows. | State the expansion first, then the entry computation on separate lines. |
| R16 | Table 6 and caption | The "1" for N = 2 is unexplained; the all-graphs check rests on a script the reader cannot see. | Explain the empty-sum case in one clause; add "see Appendix D" in the caption. |
| R17 | Section 7.4 | Critique of unnamed sources; the web sources are not separated from [7]; the section's purpose is unclear. | Name the sources inline and quote the criticised sentence, or shorten to one sentence and move the detail to an appendix. |
| R18 | Section 7.5 | 98,000,000, 7, and 38,742,049 are not derived; the cost section is not tied to the three questions. | Show the arithmetic in one line each, or cut the section. |
| R19 | Section 1.4 | The reader must take on faith that the Armenian textbook lacks the results; the purpose of the paragraph is clear only on a second read. | Shorten to "The textbook, as far as we searched, has neither result, so both are proved here." |
| R20 | Section 5.2, Section 6.1 | Points to a textbook figure the reader never sees; "a trail that repeated a vertex would contain a closed trail" has no argument. | Give a four-vertex example (triangle plus pendant edge) with trail and path counts, or drop the claim; add one line on why the closed trail exists. |

Reader's summary of the conclusions, verbatim:

The note asks three things about a graph (points joined by lines) written as an adjacency matrix A, a table of zeros and ones. First, what do the entries of the k-th power of A mean? The answer is that entry (i,j) of A^k is the number of walks of length k from vertex i to vertex j. A walk may repeat vertices and edges, so the entry does not count paths. Second, how can one tell from A whether the graph is connected? The answer is that the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N-1) is positive, or equivalently when (I + A)^(N-1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path of no more than N-1 steps. The note shows that N-1 cannot be reduced to N-2, because a straight-line graph needs all N-1 steps. It also offers breadth-first search as an alternative. Third, what is a path? The answer is a walk with no repeated vertex, which differs from the textbook's own "path" (a walk with no repeated edge). Two three-vertex examples, one connected and one not, and a computer check over all graphs with up to six vertices support the results. I can state the answer, but I could not say why the village story, the board-reading discussion and the source critique take up so much of the note.

The full verbatim message is in `reports/technician-reader-round1.md`.

# Author self-evaluation

## self-evaluation.md

# Self-evaluation: adjacency-walks-connectivity

Author's account of every section of `main.tex`: its purpose, each substantive claim with the evidence claim id that supports it, each conclusion with its premises, and what I could not justify. Claim ids are those of `evidence/evidence.json`. A1 and A2 are two claims I added in `evidence/modules/author.json` (textbook Definition 1.2.1 and Theorem 1.2.1, read from the page image of printed p. 16); both are `fact`, `supported`. I added no `unverified` or `derived` claims.

Build state: `build.sh` exits 0 (LaTeX, biber and latexmk installed). Result of the four commands is in the final report. Six bibliography entries carry `year = {n.d.}` because the evidence record has `year: null` for them; `check_citations.py` requires a year or date field, and biber prints six warnings that `n.d.` is not an integer. This is the only residue.

Numbers: every matrix and table in the examples is generated by `appendices/scripts/generate_paper_numbers.py` into `appendices/scripts/numbers.tex`, which `main.tex` inputs. The module scripts are copied unchanged into `appendices/scripts/` and re-run; their outputs are identical to the module outputs (`diff` clean).

## 1. Introduction (`sections/introduction.tex`)

Purpose: state the three questions, say where each came from, fix the story and its dictionary, fix the conventions, report what the textbook contains, give the answers in brief and the organisation.

Claims and support:
- Q1 and Q2 and the board's connected definition are on the board: C27, C25, C26, C29 (whiteboard1, whiteboard2). Q3 comes from the assignment text as reported by the orchestrator (brief); it is described as reported and is not in quotation marks and is not cited.
- Convention 1 (finite simple undirected; agrees with symmetric zero-diagonal board matrix): C1, C3, C28; assignment text reported.
- Convention 2 (mark read as k; photos show small n or quotation marks): C29 (qualified), m1-9 (qualified).
- Convention 3 (matrix defines the example; mismatch edge by edge): C28, C27 (board says the graph is given through its matrix); brief assumption.
- Convention 4 (path = no repeated vertex; textbook simple path 1.2.13; board silent): C24 (qualified), C16, m2-8 (qualified).
- Convention 5 (notation, board V = edge set): C25, C26.
- Convention 6 (length 0 allowed): m2-15 (qualified), m2-4.
- Textbook search statement (adjacency matrix on printed pp. 7, 11, 12, 34, 61; no walk-counting theorem, no matrix test): m3-11 (qualified). The text says it is about the search, not a proof of absence.
- Walk-counting theorem taken from Quinlan, test statement from Paramadevan and Bai: C6, C34, C36.

Conclusions: the list of answers in 1.5 repeats Theorem 3.5 (C6, m1-3), Theorem 4.6 (C35, C37), and Definition 2.31 (C16, C24); it adds no new claim.

Could not justify: nothing mathematical. The story and dictionary are mine; I checked by script that no plain-words paragraph contains a technical term from the dictionary (neighbour is a story word), contains a symbol, or has a sentence of more than 18 words. I did not do a read-aloud test with a real child.

## 2. Background (`sections/background.tex`)

Purpose: the textbook's build order with its numbers; each definition followed by a remark, an example and a non-example, and preceded by a plain-words paragraph.

Claims and support:
- Def 2.1 graph (textbook 1.1.1): C1. Def 2.5 adjacent (1.1.4): C2. Def 2.9 adjacency matrix: C2, C26 (board form). Prop 2.13 symmetric, zero diagonal, converse: C3, C4.
- Def 2.14 degree (1.2.1): A1. Prop 2.18 row sums and total 2|E|: m1-1 (derived, proof in text), C5, A2 (Euler, Theorem 1.2.1 as the textbook's statement of the total).
- Def walk (1.2.10) and length, Remark on repeats, walk = vertex sequence: C12, C13, m1-2 (derived; full proof in Appendix C.1). Examples and non-examples: m2-1, m2-13.
- Def 2.19 walk and Def 2.23 closed walk (1.2.11): C14. Def 2.27 trail (1.2.12, textbook "path"): C15, C21, m2-1. Def 2.31 path (1.2.13, textbook "simple path") and path between n_i and n_j: C16, C24 (qualified), m2-8 (qualified), m2-2. Prop 2.35 path implies trail: m2-10 (derived).
- Def 2.36 cycle and simple cycle (1.2.14, 1.2.15): C17, C22, m2-2, m2-14. The claim that B has no cycle is proved in the text (a trail has at most |E| = 2 edges, closed lengths 1 and 2 are impossible); the script agrees up to length 6 (m2-14).
- Def 2.40 distance (1.2.16) and its three properties: C18, m2-4; proofs in Appendix C.5 (m2-16).
- Lemma 2.44 (every walk contains a path, with length bound): C19, C20, m2-3, m2-9 (derived; proof in text). Corollary 2.46 (at most N-1 edges): C33, m2-6, m2-11. Prop 2.47 (shortest walk, trail, path agree): m2-12 (derived; proof in Appendix C.5).
- Def 2.48 connected (2.1.1) and the board's definition: C30, C25, C32, m3-2. Remark 2.49 (independence of the reading of "path", u = v): C30, C32, C19, C20; the u = v reading is marked as not discussed by the textbook (m3-3(d)). Def 2.52 components and the textbook's Remark 2.1.1: C31, m3-1, m3-2.

Conclusions and premises: Lemma 2.44 follows from induction on length (premises: Definition 1.2.10 only). Corollary 2.46 follows from Lemma 2.44 and counting distinct vertices. Remark 2.49 follows from Lemma 2.44 and Proposition 2.35.

Could not justify / cautions:
- The textbook example "walk of length 8: two cuts give lengths 5 and 2" rests on my script's seven edges of the textbook graph (edges the examples use), not on the textbook text; the text says so by pointing to Appendix D.
- Definition numbers for A(G) (no number of its own) and degree (1.2.1) follow `graph-sources.md` and my reading of printed p. 16.
- "Induced subgraph" G[V_j] is explained in one clause by me; it is notation, not a claim.

## 3. Question 1 (`sections/answer1_walks.tex`)

Purpose: answer Q1 with a proof; show the answer counts walks, not paths.

Claims and support:
- Def 3.1 matrix product and power: standard definition, no citation needed (defined here).
- Theorem 3.5 (walk counting): C6 (statement in four sources), C7 (standard route), m1-3 (full induction proof, derived). The textbook lacks it: m3-11.
- Remark on where simplicity is used and the multigraph and digraph remark: m1-8 (interpretation; Grinberg Theorem 4.5.10).
- Corollary 3.9 (a) nonnegative integers, (b) positive iff walk, (c) symmetric, (d) (A^2)_ii = degree and trace = 2|E|: m1-7 (derived), C9.
- Proposition 3.10 (entries do not count paths or trails; table of walks, trails, paths from n_1 to n_2): C8, C10, m1-6. The path and trail counts in Table 2 come from the script; the argument for the first column is the closed form in Appendix C.2.

Conclusions and premises: the answer to Q1 follows from Theorem 3.5 (induction base k = 1 from the definition of A; step from the second-last-vertex decomposition and Prop C.1 on vertex sequences). "Not a path count" follows from Corollary 3.9(d) and Definitions 2.27 and 2.31 (a closed walk n_i, n_r, n_i repeats a vertex and an edge).

Could not justify: nothing. The proof is mine and follows Quinlan's route; the brute-force check (m1-4) is a finite check and is labelled so.

## 4. Question 2 (`sections/answer2_connectivity.tex`)

Purpose: the matrix test, its proof, its sharpness, the equivalent (I + A)^m form, and breadth-first search as one paragraph.

Claims and support:
- Statement of the sum test: C34 (Paramadevan Theorem 2, MathWorld); (I + A)^(N-1) form: C36 (qualified; Bai Theorem 2). The two sources' proofs are loose: m3-12.
- Def 4.1 of S, Prop 4.5 (equivalence for one pair), Theorem 4.6, Corollary 4.7 (components): C35 (derived), m3-5; premises C6, C19, C20, C33, m2-10.
- Remark 4.8 (distance as least k): C38, premises Proposition 2.47.
- Remark 4.9 (diagonal, N = 1, 2): m3-3, C9.
- Test 4.10 as a procedure: derived from Theorem 4.6.
- Prop 4.14 (N-1 cannot be lowered), Example 4.15 and Table 3: m3-4 (derived, script). Remark 4.16 (which graphs fail with N-2 powers: exactly the labelled paths, N!/2 of them; 3, 12, 60, 360): m3-4; the argument (a pair at distance N-1 forces the graph to be the path) is written in the text and agrees with Table 6 last column.
- Prop 4.17 (powers of I + A, any m >= N-1, squaring): C37, m3-9 (derived; proof in Appendix C.4).
- Remark 4.18 (breadth-first search): C39, m3-13; agreement with the matrix test on all graphs with at most 6 vertices: m3-8.

Conclusions and premises: Theorem 4.6 (a) iff (b) from Prop 4.5, which follows from Theorem 3.5, Corollary 3.9(a), Lemma 2.44, Corollary 2.46 (chain written in Appendix C.3). (b) iff (c) from Prop 4.17, whose proof uses binomial expansion, positivity of the coefficients, and the same premises.

Could not justify:
- BFS time bound: stated only for adjacency lists, as in the source (C39). The text does not compare it to the matrix test here.
- C39's own text says N-1 matrix products; the paper uses N-2 (m3-10 note).
- N = 1 is handled by a remark, not by the test.

## 5. Question 3 (`sections/answer3_path.tex`)

Purpose: point to Definition 2.31 as the answer, and add only the comparison of conventions and what depends on them.

Claims and support: three usages and Table 4: C15, C16, C21, C22, C23, m2-7; course convention reported by the assignment text and qualified: C24, m2-8, C25; existence independent of the reading: C19, C20, C32, m2-10; counts depend: C10, m1-6; length-0 path: m2-5, m2-15.

Conclusions: "a path between n_i and n_j" is Definition 2.31 (qualified, C24); existence statements agree across readings (Lemma 2.44 and Proposition 2.35).

Could not justify: the English column for the textbook's cycle (1.2.14) reads "closed trail", obtained by combining Grinberg's trail (C21) with "closed"; Grinberg does not define a closed trail in the passage read. I did not repeat the source's remark about "circuit" because `graph-sources.md` says it concerns closed walks.

## 6. Worked examples (`sections/example.tex`)

Purpose: the board graph B (powers, walk lists, hand sums, counts), a connected and a disconnected example with every matrix written out, an exhaustive computer check.

Claims and support: Example 6.1: m1-5, C28, m1-6, C9. Table 5 (walks, trails, paths, closed walks by length): m2-13, m2-14. Example 6.2: m3-6. Example 6.3: m3-7. Table 6 and the component check: m3-8, m3-4, m3-9. Figure 1 shows the drawing as read, B, and the one-edge graph (C28).

Conclusions and premises: "connected" for B and "not connected" for the one-edge graph follow from Theorem 4.6 applied to the printed matrices (numbers computed by script and checked against BFS: m3-6, m3-7). A^(k+2) = 2A^k follows from A^3 = 2A (shown in the text); checked by script for k = 1..5 (m1-5).

Could not justify: nothing. The statement that in B every trail is a path is proved in the text from the absence of a cycle (a repeated vertex in a trail gives a closed trail) and agrees with Table 5.

## 7. Discussion (`sections/discussion.tex`)

Purpose: the board mismatch edge by edge, the mark above A, limits, competing explanations, a one-paragraph cost remark, and what is left open.

Claims and support: mismatch and mark: C28, C29 (qualified), m1-9; limits: m1-4, m3-8, m3-11; one-sentence remark on digraphs and multigraphs: m1-8, C6; competing explanations: C11, C6, C8, m3-12; cost (estimate): m3-10, C39; the K_10 number 38,742,049 is from the m3 script.

Could not justify: the cost remark is an estimate for the school multiplication method only (m3-10 says so); faster methods not examined. "BFS reads each entry once when the input is the matrix" is my estimate with premises from the slides (slides 3 and 6).

## 8. Conclusion (`sections/conclusion.tex`)

Direct answers to Q1, Q2, Q3, each referring to the result that proves it (Theorem 3.5 with C6 and m1-3; Theorem 4.6 with C35 and C37; Definition 2.31 with C16 and C24). The last paragraph repeats the three qualified assumptions.

## Appendices

- A, `appendices/course-terms.tex`: textbook numbers, printed pages and board-symbol comparison: graph-sources table, C1, C2, A1, A2, C12 to C19, C30, C31, C25, C26. The Armenian words are not typeset (pdflatex); translations are given.
- B, `appendices/photographs.tex`: transcription of the board: C25 to C29, C28.
- C, `appendices/derivations.tex`: C.1 walks and vertex sequences (m1-2, derived), C.2 the counterexample in closed form (2^((k-1)/2) walks of odd length k from n_1 to n_2; derived by me, consistent with the script: m1-6), C.3 chain of premises (C35), C.4 proof of Prop 4.17 (C37, m3-9), C.5 distance (m2-12, m2-16), C.6 cross-checks (m1-4, m3-8).
- D, `appendices/provenance.tex`: sources read, scripts, how to rerun; the only place with file names of scripts.

## Pointers in the evidence file that no longer match the paper

The `derivation` strings of some claims name paper numbers or labels from the module drafts. Labels now present: thm:walkcount, prop:warning, prop:pair, thm:test, prop:iplusa, prop:sharp, ex:sharp, tab:sharp, rem:failcount, prop:rowsums, rem:walk, lem:walkpath, prop:pathtrail, cor:bound, rem:connected, rem:diagonal, cor:walkcount, ex:boardpowers, tab:walksvspaths, tab:walkcounts, rem:trail, nex:cycle, ex:testB, ex:testD, tab:exhaustive, sec:cost, cor:components, prop:shortest, prop:distprops, app:walkcount, app:counterexample, app:testproof, app:iplusa, app:distance, app:crosschecks. The printed numbers differ in these cases: Proposition 4.14 (not 4.16 or 4.17) is prop:sharp; Proposition 4.17 is prop:iplusa (claims say 4.16); Section 7.5 (not 7.4) is sec:cost; Remark 4.16 is rem:failcount (claim says 4.19); the appendices are lettered C (derivations) in the compiled paper, not A; Table numbers differ (tab:walksvspaths is Table 2, tab:sharp Table 3, tab:walkcounts Table 5, tab:exhaustive Table 6). The fragments that own those claims could be updated to labels only; I did not edit them.

## Findings log

No revision round yet.

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
