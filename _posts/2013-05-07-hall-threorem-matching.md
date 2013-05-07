---
layout: post
title: Hall's Theorem in Layman's Words
language: en
category: note
mathjax: true
tags: [":math", "graph", "Hall's Theorem", "matching"]
---

## Hall's Theorem

The graph theoretic version of Hall's theorem gives the 
necessary and sufficient for the existence of a perfect matching for bipartite graph.
Basic terms:

   * A _bipartite graph_ $G=\<X, Y, E\>$. 
   $X$ and $Y$ are two vertex sets. 
   $E \subset \lbrace(x,y)| x \in X, y \in Y \rbrace$ is the edge set. 
   Note the conventional representation of bipartite graph is different that of a general graph. 
   Given this definition, it is already clear that no edges are within $X$ or $Y$, 
   aka bipartite. 
   * A _matching_ is a set of edges $M \subset E$ such that:
   no vertices appear in $M$ for more than once. 
   * The _maximum matching_ is the matching such that $|M|$ is the maximum.
   * To define the _perfect matching_ in usual sense, we require $|X|=|Y|=n$. 
   Then a perfect matching is a matching such that $|M|=n$.
   * When $|X| \neq |Y|$, one can define a general sense "perfect matching" by 
   _X-saturating matching_ [1]:
   a matching such that $|M|=|X|$.
   One can define a "Y-saturating matching". 
   Since the case is symmetric, we simply discuss the former one and term it as "perfect matching". 

Hall's theorem gives the iff condition for the existence of perfect matching (for $X$).
We define the neighbourhood of a set of nodes, $S \subset X$, as:
$N(S) = \lbrace y | y \in Y, s \in S, (s,y) \in E \rbrace$.
Hall's theorem can be stated as:
There exists a perfect matching if and only if $\forall S \subset X, |N(S)| \ge |S|$. 

## Proof by Construction

### "only if"

The "only if" direction is easy. 
Take the negation, we know 
$\exists S \subset X, |N(S)| < |S|$.
Such $S$ do not have a perfect matching. 
For those sets that are superset of $S$, they do not have a perfect matching, either. 
In particular, $X$ do not have a perfect matching. 

### "if"

We can prove by induction on the size of $S$. 
The base case when $|S|=1$ is trivial.
If there $|N(S)| \ge 1$, match $S$ to any of its neighbour suffices. 

Next we consider how to generate perfect matching for $S$ with $|S|=2$,
if we already have perfect matching for every $S$ with $|S|=1$.

There are only two cases depicted in the left part of the following figure. 
Left is $X$ and right is $Y$. 
Red edge is in previously constructed matching (with smaller size of $S$).
The green node is newly added. 
Suppose we already have a perfect matching $(x,1)$. 
Now we add a new node $y$. 

   * If $y$ is matched to a vertex different than $1$ (say $2$) in previous steps, we are good. 
   A matching of size 2 is obtained, i.e. $\lbrace (x,1), (y,2) \rbrace$. 
   * If $y$ is matched to $1$, we try to find an augmenting path. 
   We know that $|N(\lbrace y,x \rbrace)| \ge 2$ from the Hall's condition.
   That means, at least one of $x$ and $y$ should connect to another vertex. 
      * Suppose $y$ connects to another vertex $2$, simply put $(y,2)$ in the matching and we are done.
      * Suppose $x$ connects to another vertex $2$, we can find an augmenting path as is shown in the second row.

Note that the two cases are just the "least" ones. 
It does no harm for $x$ and $y$ to connect to more vertices.
   
![style=center;test](https://docs.google.com/drawings/d/1BHaf1v2wean4mA4Belu4AMrts25QyZyCt2vLdE_63wI/pub?w=600&h=400)

We can iteratively apply this argument for $S$ with $|S|=k \ge 3$.
One example is shown in the right panel of the above figure. 
We only consider the case when the newly added node contradicts with existing matching. 
Suppose we already know how to insert a new node to a matching of size $\le k-1$:

   * For the new node $w$ and the contradicted node $x$,
   we first leverage the construction for size 2, which is discussed above. 
   * After this first step, $w$ is matched and 
   we can regard $x$ as a newly added node to be matched with a size $k-1$ perfect matching
   (the dashed region).

## Proposition for Regular Bipartite Graphs

One prosition of Hall's theorem is also useful:
**A regular bipartite graph always has a perfect matching**. 

The statement already implicitly includes the fact that $|X|=|Y|$.
Now consider a subset $S \subset X$. 
There are $|S|d$ edges incident to this set, supposing the graph is $d$ regular. 
Assume $|N(S)| < |S|$, we have $d|N(S)| < d|S|$.
That means, some edges start from $S$ do not end in $N(S)$, a contradiction. 
So we know $|N(S)| \ge |S|$ and this is exactly the condition of Hall's theorem.
Note that it is possible for $|N(S)| > |S|$.

## Further Reading

Tutte's Theorem [3] is an extension of Hall's theorem from bipartite to genereal graphs.
[1] has some discussion of Hall's marriage theorem from non graph theoretic aspects.
However, those discussions sound like foreign language to me, I can not dig further at this moment.

## Background

It has application in:
the magical graph and super concentrator construction (L4 of [4]);
$O(n \log n)$ perfect matching for regular bipartite graphs using random walk (L6 of [4]). 

## Reference

   * [1] Wikipedia, Hall's marriage theorem, 
   [http://en.wikipedia.org/wiki/Hall's_marriage_theorem](http://en.wikipedia.org/wiki/Hall's_marriage_theorem)
   * [2] Wikipedia, Matching, 
   <http://en.wikipedia.org/wiki/Matching_(graph_theory)>
   * [3] Wikipedia, Tutte's Theorem, 
   <http://en.wikipedia.org/wiki/Tutte_theorem>
   * [4] Lau Lap Chi, Randomness and Computation, 
   <http://www.cse.cuhk.edu.hk/~chi/csc5450/notes.html>

