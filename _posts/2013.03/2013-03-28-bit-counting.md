---
layout: post
language: en
title: "Bit Counting (Number of one's in an integer)"
tags: [":algorithm", ":interview", "C", "bit", "radix", "summation", "modular"]
---

A classical problem: Given an interger, count the number of one's in it. 

I saw this problem many times and it really has considerable application in engineering.
One may also expect to see it during interviews. 

I revisited the problem today via a link share on Renren.
See the 
[post](http://www.cnblogs.com/graphics/archive/2010/06/21/1752421.html)
in Chinese.
I've seen part of them before. 
The "paralell couting" and so-called "perfect counting" are new to me.
They are interesting but are not well presented. 
That's why I do more survey and note the rationale down.

## Basic Counting

Basic techniques that most people know:

   * Directly loop over all bits and count them.
   This can be done **iteratively** or **recursively**.
   * Since we only care about 1's, it's better to count them directly. 
   `x & (x-1)` can erase the least significant 1;
   `x & ~(x-1)` can retain only the least significant 1
   (same trick is used in _Binary Index Tree_).
   * One straightforward optimization for the above method:
   1) Obtain statistics of your data somehow;
   2) If there are only a few 1's, do the above directly;
   3) If there are a lot 1's, count 0's instead. 
   * Precompute a table to index all numbers of a certain length,
   e.g. 8-bit (good for embeded device), 
   16-bit (good tradeoff between time and space for normal PC), 
   32-bit (almost impossible). 
   You do not have to invoke the above plain methods for every number. 
   The table can be constructed **recursively**.

Those are well explained the reference materials. 
I will not repeat the explanation here. 
Just for my quick note. 

## Paralell Counting

The "paralell couting" and so-called "perfect counting" are new to me.
I should term both of the as parallel couting (later comes the reason).
The "perfect counting" is originated by 
[HAKMEM](http://www.inwap.com/pdp10/hbaker/hakmem/hacks.html#item169).
See [gurmeet's post](http://gurmeet.net/puzzles/fast-bit-counting-routines/)
for some background information.
The method is interesting but none of the posts detailed the rationale, 
especially for the modular operation. 
Here is my short documentation. 

### Counting by Merging

Since we have "merge sort", this method can be called as "merge count". 
They have the same idea behind. 
You first count the number of one's in consecutive bits (every 2 bits). 
Then you go for every 4 bits, 8 bits, ...
The code explain itself better: (from [1], "parallel counting")

```
int BitCount4(unsigned int n) 
{ 
    n = (n & 0x55555555) + ((n >> 1) & 0x55555555) ; 
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333) ; 
    n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f) ; 
    n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff) ; 
    n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff) ; 

    return n ; 
} 
```

### Generalize Merging

You may notice that we can only count the consecutive `k` bits, where `k` is a power of 2. 
Here is a generalization from HAKMEM's approach:
(code snippet from [1])

```
unsigned int tmp = n - ((n >> 1) & 033333333333) - ((n >> 2) & 011111111111);
```

In this way, we can count the number of one's in consecutive 3 bits.
This part is well explained in [1] and [2]. 

How to generalize to 6-bits? 
Now that we already have count in 3-bit sections, 
we can add consecutive 3-bit sections together to form 6-bit count.
One way from [1] and [2]:

```
(tmp + (tmp >> 3)) & 030707070707
```

This may appear as tongue twister for someone. 
It works but is not so unified with above "paralell counting" schema. 
See the following: (not validated)

```
(tmp & 030707070707) + (tmp >> 3) & 030707070707
```

See the difference? 
The 2nd one uses the same schema as above "paralell counting"
We conclude three core operations in merge based approaches:
(from count of `k` consecutive bits to `2k` consecutive bits; 
call this operation as **Double** in the following discussion)

   * Part1: Mask `n` to retain lower `k` bits of every `2k` bits.
   * Part2: Shift `n` right by `k` bits and mask to retain lower `k` bits of every `2k` bits.
   (essentially higher `k` bits of every `2k` bits in original integer).
   * Add two parts together.

How to go from `k` to `3k` **efficiently**? 
A quick thought does not give me a mask and shift based method
similar to the HAKMEM approach.
Neverthe less, we can do it in a plain way, e.g.:
(for `k=1` case; others, construct the mask yourself; numbers are octect; not validated;
call this operation as **Triple** in the following discussion)

```
n = (n & 011111111111) + ((n >> 1) & 011111111111) + ((n >> 2) & 011111111111); 
```

It has one more operations than HAKMEM approach. 
However, I think this one is more understandable and genralizable. 

### Modular Magic Number

How come the 63? 
This is not correctly explained in original posts.
HAKMEM also do not document the rationale in his memo.

Let's approach from the general situation. 
With above merging technique, we already get the count of one's in consecutive `k` bits.
Denote the current intermediate result by `n`. 
We have:

```
n = a0 * (2^k)^0 + a1 * (2^k)^1 + ... 
```

where `a0, a1, ...` are the count for that `k` bits and they are all no greater than `k`.
We want to get the count:

```
c = a0 + a1 + a2 + ...
```

If I write in this way, 
it may be clear to you that a simple modular can eliminate those `(2^k)^i` terms.
More precisely, we know `(2^k)^i === 1 mod (2^k-1)`. 
Then we have:

```
n = c mod (2^k-1)
```

Done. 

In the HAKMEM approach, we first get a per section count with length `k=6`. 
So we want to use `2^k-1=63` as the modular. 

### Generalize Composition

The above analysis shows us an important trick:
modular by `(2^k-1)` can result in a summation of sections of a bit sequence.
Since we can get a per section count sequence with `k=2, 3, 4, 6, 8, 12, ...` easily, 
why not use other modular? 
Actually we can. 
Here are some examples:

   * Triple, Double, Modular 63. (HAKMEM)
   * Double, Double, Double, Modular 255. 
   * ...

The only thing to note is that the modular should be no less than 
maximum number of one's you are counting. 
For the 32-bit interger, the maximum number is 32. 
So 63 is the smallest number to satisfy the criterion. 

Then we can generalize it to counting an 64-bit integer:

   * Triple, Double, Double, Modular 4095. 
   * Double, Double, Double, Modular 255. 
   * ...

One may also try to form sections of `k=7` first and modular 127. 
However, I don't know efficient way to do `k=7` at present.

Can we modular earlier? 
Yes, in some applications, we can.
For example, if your strategy depends on the number of one's modular 7, 
you do not have to count the total number of one's first. 
You can simple do a "Triple" and then "Modular 7". 
This will be significant acceleration if you word length is longer, 
e.g. 128 bit (you save two "Double" operation).

## Reference

   * [1] "Count the number of one's" (in Chinese).
   [http://www.cnblogs.com/graphics/archive/2010/06/21/1752421.html](http://www.cnblogs.com/graphics/archive/2010/06/21/1752421.html)
   * [2] "Puzzle: Fast Bit Counting"
   [http://gurmeet.net/puzzles/fast-bit-counting-routines/](http://gurmeet.net/puzzles/fast-bit-counting-routines/)
   * [3] HAKMEM (bit counting is memo number 169), 
   MIT AI Lab, Artificial Intelligence Memo No. 239, February 29, 1972. 
   [http://www.inwap.com/pdp10/hbaker/hakmem/hacks.html#item169](http://www.inwap.com/pdp10/hbaker/hakmem/hacks.html#item169)

## Further Reading

   * Bit Twiddling Hacks by Sean Anderson at Stanford University.
   [http://graphics.stanford.edu/~seander/bithacks.html](http://graphics.stanford.edu/~seander/bithacks.html)
   * Bitwise Tricks and Techniques by Don Knuth (The Art of Computer Programming, Part IV).
   [http://www-cs-faculty.stanford.edu/~knuth/fasc1a.ps.gz](http://www-cs-faculty.stanford.edu/~knuth/fasc1a.ps.gz)
