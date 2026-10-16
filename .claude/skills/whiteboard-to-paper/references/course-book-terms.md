# Course textbook: terms and where to find them

The course textbook is `Grafneri_tesutyun.pdf` at the repository root
(Graph Theory, in Armenian, Yerevan State University, 216 pages). Printed
page numbers are 1 lower than PDF page numbers in Chapters 1 and 2 (printed
page 11 is PDF page 12).

## How to read it

The PDF has a text layer, but formulas are dropped by text extraction.
Use text for locating, images for reading formulas.

```
pdftotext -layout Grafneri_tesutyun.pdf <scratchpad>/book.txt
awk 'BEGIN{RS="\f"} /keyword/ {print NR}' <scratchpad>/book.txt   # PDF pages
pdftoppm -f <page> -l <page> -r 110 -png Grafneri_tesutyun.pdf <scratchpad>/p
```

Then view the PNG with the Read tool to read the exact formula.

## Notation

- Graph G = (V, E). Vertices v_1, ..., v_n. Edges e_1, ..., e_m. An edge
  between u and v is written uv.
- Adjacency matrix A(G) = (a_ij), n by n, a_ij = 1 if v_i and v_j are
  adjacent, 0 otherwise. States a_ii = 0 and a_ij = a_ji.
- Lecture boards from this course often differ: (G, V) for the graph,
  |G| = N for the vertex count, n_i for vertices, e_ij for edges, A_ij
  uppercase. Keep the board's letters in the paper and note the book's.

## Terms (Chapter 1 and 2)

| Armenian | English | Definition | PDF page |
| --- | --- | --- | --- |
| գագաթ | vertex | 1.1 | 10 |
| կող | edge | 1.1 | 10 |
| հարևան | adjacent (two vertices, or two edges sharing a vertex) | 1.1.4, 1.1.6 | 12 |
| կից | incident (vertex and edge) | 1.1.5 | 12 |
| հարևանության մատրից | adjacency matrix | 1.1 | 12 |
| կցության մատրից | incidence matrix | 1.1 | 13 |
| հարևանության ցուցակ | adjacency list | 1.1 | 13 |
| աստիճան | degree | 1.2 | 15 |
| ենթագրաֆ | subgraph | 1.2 | 19 |
| շրջանցում | walk (vertices and edges may repeat) | 1.2.10 | 22 |
| փակ շրջանցում | closed walk | 1.2.11 | 23 |
| ճանապարհ | path: walk with pairwise distinct edges (English: trail) | 1.2.12 | 23 |
| պարզ ճանապարհ | simple path: pairwise distinct vertices (English: path) | 1.2.13 | 23 |
| ցիկլ | cycle: closed path | 1.2.14 | 23 |
| պարզ ցիկլ | simple cycle | 1.2.15 | 23 |
| հեռավորություն | distance | 1.2.16 | 23 |
| կապակցված գրաֆ | connected graph: a path between any two vertices | 2.1.1 | 49 |
| կապակցվածության բաղադրիչ | connectivity component | 2.1 | 50 |
| երկկողմանի գրաֆ | bipartite graph | 2.2 | 51 |
| ծառ, անտառ | tree, forest | 2.3.1, 2.3.2 | 55 |
| լապլասյան | Laplacian matrix | 2.3 | 62 |

## Results worth citing

- Lemma 1.2.1 (PDF page 24): from any (u, v)-walk with u different from v
  a simple (u, v)-path can be extracted. Proof by induction on length.
- Lemma 1.2.2 (PDF page 24): a closed walk of odd length contains a simple
  cycle of odd length.
- Remark 2.1.1 (PDF page 50): a graph is connected if and only if it has
  one connectivity component.
- Section 1.1 (PDF page 13): every symmetric 0/1 matrix with zero diagonal
  is the adjacency matrix of some labelled graph.

## Not in the book

- No theorem that (A^k)_ij counts walks of length k. Prove it in the paper
  from Definition 1.2.10 and the matrix product rule.
- No matrix power test for connectivity. Derive it from Lemma 1.2.1 and
  Definition 2.1.1.

## Convention conflict to flag

The book's "path" allows repeated vertices. When the lecturer says a path
has no repeated vertices, that is the book's "simple path". Give both
definitions, say which one the paper uses, and note that Lemma 1.2.1 makes
the connectivity definition the same under either reading.
