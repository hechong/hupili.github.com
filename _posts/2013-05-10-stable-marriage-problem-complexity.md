---
group: blog
layout: post
title: Stable Marriage Problem Complexity Revisited
language: en
category: note
mathjax: true
tags: [":math", ":algorithm", "SMP", "stable", "marriage", "matching"]
---

## Background

See wiki [1] for the problem definition and the original Gale-Shapley algorithm.
To warm up, here's some digest:

   * We have two pool of people, 
   `$M=\lbrace m_1, m_2, \ldots, m_n \rbrace$`
   (for man) 
   and 
   `$W=\lbrace w_1, w_2, \ldots, w_n \rbrace$`
   (for woman). 
   Everyone is aksed to give a strict ordering of the preference of $n$ potential partners.
   Find a matching that is **stable**:
   there does not exist two pairs $(m_i, w_j)$ and $(m_k, w_l)$ s.t. 
   `$w_l \succeq_{m_i} w_j$`
   (from $m_i$'s point of view, $w_l$ is better than $w_j$)
   and 
   `$m_i \succeq_{w_l} m_k$`.
   * The original Gale-Shapley algorithm is proposal based:
   every round, one unmatched man propose to a woman; 
   the woman decides accept or rejct by comparing him with the current partner; 
   a rejected man go back to the unmatched pool. 

## Complexity and Worst Case

The GS algorithm will explore all men's preference list.
After one proposal, either successful or fail, one element of the preference list is removed. 
There are only $n^2$ elements in all men's preference list. 
One can argue that the complexity is $O(n^2)$. 

Although the order of magnitude is $O(n^2)$, I have not found a construction for such a case. 
What I can come up with is just $n^2/2$, namely, 
half of the elements in the preference lists are explored: 

   * Every man's preference list is 
   `$w_1 \succeq w_2 \ldots \succeq w_n$`.
   * Every woman's preference list is 
   `$m_n \succeq m_{n-1} \ldots \succeq m_1$`.

It's easy to show that it stablize after $n(n+1)/2$ rounds
(The upper triangle of the man's preference table is explored).
Looks like I can not easily construct a tighter case.

## Slight Variation: Follow an Ordering to Perform Trials

The algorithm presented above does not require a ordering of the man's proposal sequence. 
We make the recursively fixed variation:

   * Every iteration, an unmatched man $m_i$ make proposal according to his list. 
   * If this man's proposal is accepted and another man $m_j$ becomes unmatched, 
   we let $m_j$ to make proposal (i.e. recursively fix). 
   * One iteration ends until no previous relationhips are broken.

It's easy to verify the correctness. 
The proof for original algorithm still applies.
Actually, in my 1st undergraduate year, I saw someone writting this variation. 
I originally thought he did not understand the _Proposal Algorithm_
and he came up with something that "just works". 
After we submit the codes to OJ, it turns out his code is faster. 
I could not believe that a code full of function recursion turns out to be after than mere looping.

Now I realize that it's of course the case. 
See the variation listed above. 
There are only $n$ iterations in total. 
The time spent on every iteration depends on how many relationships he can break. 
At the $i$-th iteration, there are only $i-1$ matches, i.e. max number of relations broken is $i-1$. 
Consider his own proposal, it consumes at most $i$ elements from the preference list at $i$-th iteration. 
Summing up them together, it is $n(n+1)/2$.

## Average Cost Using Probabilistic Argument

[3] mentions a probabilistic analysis in chapter 3.6.
It turns out the average cost is only $\Theta(n \log n)$ 
if we assume people's preference is uniformly drawn from all possibilities.
The assumption is justifiable: **everyone has his/her own taste**. 

The argument is as follows:

   * First, we can fixed the preference lists of one group, say women's, to arbitrary ones.
   This does not influence the following analysis. 
   * For men, we apply **Deferred Decision Principle**: 
   hide the outcome of random bits until the algorithm need it. 
   In this concrete example, it is equivalent to randomly pick a proposal target when a man is asked to.
   DDP is often used to largely simplify the probability space. 
   * In the original algorithm, the man won't propose to someone who already rejected him. 
   We can relax this condition: 
   randomly pick one out of $n$ women, rather than pick one from the set of women he has not proposed to. 
   This relaxation can only worsen our execution time. 
   Since we want to upperbound the execution time, this relaxation is OK. 
   * Note that the stable marriage solution may not be unique in general
   (e.g. men propose or women propose). 
   However, in the algorithm we discuss, we let men propose, which results in a unique solution. 
   That means, out of the $n$ candidates, only one is in the stable matching.
   We expect the random selection will hit this target. 
   Another view of the problem is:
   we have $n$ item (man), and each one has $1/n$ probability to be obtained (hit the target in stable matching). 
   This reduces to a _Coupon Collection_ problem.
   Since it has a sharp threshoding effect, the time required is $\Theta(n \log n)$.

One can see [3] for a rigorous argument of the complexity of the _Coupon Collection_ problem. 
Here is an intuitive sketch:
(from my friends when we discussed how long does it take to write 
[Yijing](http://en.wikipedia.org/wiki/I_Ching) last summer):

   * When you don't have any type of coupon, it takes just 1 step for you to get 1. 
   * When you already have 1 coupon, you want a different one. 
   You get it with probability $\frac{n-1}{n}$ for one trial. 
   This is the geometric distribution and the expected time to get the new one is $\frac{n}{n-1}$.
   * Similarly, when you already have $i$ unique coupons, 
   the expected time to get next unique one is $\frac{n}{n-i}$.
   * Use the linearity of summation, we can get
   (using [Harmonic Series](http://en.wikipedia.org/wiki/Harmonic_series_%28mathematics%29) )

$$
E(\text{Time})=\sum_{i=0}^{n-1}\frac{n}{n-i} \le n \ln n
$$

## Further Reading

[2] is a relatively recent survey on this problem. 
There are many variations of SMP. 
However, it does not contain quick pointers to improved complexity (algorithm wise or analysis wise). 
The above probabilistic argument from [3] is really eye opening to me.

## Reference

   * [1] Wikipedia, Stable Marriage Problem, 
   [http://en.wikipedia.org/wiki/Stable_marriage_problem](http://en.wikipedia.org/wiki/Hall's_marriage_theorem)
   * [2] Iwama, Kazuo, and Shuichi Miyazaki. "A survey of the stable marriage problem and its variants." Informatics Education and Research for Knowledge-Circulating Society, 2008. ICKS 2008. International Conference on. IEEE, 2008.
   * [3] Rajeev Motwani and Prabhakar Raghavan, 1995, Randomized Algorithms.

