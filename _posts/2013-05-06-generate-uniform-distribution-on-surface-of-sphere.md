---
layout: post
title: Generate Uniform Distribution on a Sphere
language: en
category: note
mathjax: true
tags: [":math", "uniform", "distribution", "sphere", "probability"]
---

## Background

I met this problem several times. 
e.g. in the context of 
[directional statistics](http://en.wikipedia.org/wiki/Directional_statistics).
e.g. the last step of Max-Cut approximation via SDP [4].
Other applications are like ray effects in games. 
In graphics, the dimension considered is usually low (e.g. 3). 
In other applications, e.g. approx-Max-Cut by SDP, the required dimension would be very high. 

## Conversion between Cartesian and Spherical System

One straighforward but incorrect guess is to generate random points on cartesian system first,
and then map them to spherical system using existing formula. 
[1] provides good visualization of the incorrectness of the straight forward approach. 
In the same tutorial, a construciton is given for 3-D sphere by combining the following elements:

   * Use _Jacobian determinant_ to find the distortion of areas at different latitude.
   * Use _Inverse CDF Method_ to map from uniform distribution to the desired one. 

This construction can be generalized to n-D using the n-Cartesian to n-Spherical transformation. 
See "Spherical coordinates" of [2] for a set of formula. 
Out of the n coordinates, there are two special ones:

   * r: the only one measured in magnitude instead of angle. 
   In the generation of uniform distribution on sphere, we do not care about it. 
   After getting the coordinates on a unit sphere, it is easy to map to arbitrary radius sphere. 
   * "longitude": the only one angular coordinate range in $[0, \pi]$. 

## Marsaglia Algorithm

Digest from [2]:

   * Generate normal distributed i.i.d. $x = (x_1, x_2, \ldots, x_n)$.
   * Output normalized version: $\frac{x}{||x||}$. 

For lower dimensions, this method is not most efficient due to the normal distribution generation. 
However, the framework is general and clean.
It's worth a note. 

Consider $x_i \sim N(0, 1)$, that is

$$ P(x_i) = \frac{1}{\sqrt{2\pi}}e^{x_i^2/2} $$

The joint distribution is:

$$ 
P(x) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}}e^{x_i^2/2} 
=  \frac{1}{(2\pi)^{d/2}}e^{1/2\sum_{i=1}^n x_i^2} 
=  \frac{1}{(2\pi)^{d/2}}e^{r^2/2} 
$$

where $r=\sqrt{\sum_{i=1}^n x_i^2}$.
That means, the probability density only depends on the distance to the origin. 
More formally: 

$$
P(x | r^2=\sum_{i=1}^n x_i^2) = c(r)
$$

for a constanct $c$ given $r$. 
Then the problem boils down to how to obtain samples conditioning on $r^2=\sum_{i=1}^n x_i^2$.
This is given by:

$$
P(\frac{x}{r} | 1=\sum_{i=1}^n (\frac{x_i}{r})^2) = c(1)
$$

So the above process will generate uniform distribution on the surface of a unit sphere.

## Generate By Cutting a Cube 

It is very easy to generate uniform points inside an $n$-dimensional Cube.
We exclude the points outside the $n$-dimensional ball. 
The remaining points are now uniformly distributed in this $n$-dimensional ball. 
Finally, we project all the remaining points to the surface of the ball. 
The correctness of this approach is obvious. 
However, it is inefficient. 
In the construction, we throw away some points outside the ball. 
This portion of points becomes larger and larger very rapidly with the increase of dimension, 
part of the [curse of dimensionality](http://en.wikipedia.org/wiki/Curse_of_dimensionality). 
(nealy no points lies in the sphere when dimension is large)

This is termed as "rejection sampling" by [3].

## Further Reading

[3] comes up with a good survey with codes. 
After watching the [codes](http://ideone.com/oYEVR), 
I just realized the existence of a bunch of 
[PRNG and distribution](http://www.cplusplus.com/reference/random/)
in C++. 
However, the "Trigonometry method" presented there should not work. 
It basically generate uniform distribution on rings for all z-axis. 
It should have denser pole similar to the effect described in [1]. 

## Reference

   * [1] Mathematica wiki, Mathematica/Uniform Spherical Distribution, <http://en.wikibooks.org/wiki/Mathematica/Uniform_Spherical_Distribution>
   * [2] Wikipedia, N-Sphere, <http://en.wikipedia.org/wiki/N-sphere>
   * [3] Jaewon Jung, Generating Uniformly Distributed Points on Sphere, <http://www.altdevblogaday.com/2012/05/03/generating-uniformly-distributed-points-on-sphere/>
   * [4] Goemans, M.X. and Williamson, D.P., 1995, Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming

