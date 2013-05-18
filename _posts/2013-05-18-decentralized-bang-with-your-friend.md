---
group: blog
layout: post
title: Decentralized "Bang with your friend"
language: en
category: brainstorm
mathjax: true
tags: [":math", ":algorithm", "decentralized", "matching", "privacy"]
---

## Background and Motivation

"Bang with your friends" (BWYF) is a controversial but very hot application on Facebook [3]. 
We are not going to talk about the controversial part. 
There are two recently developed counterparts for two major Chinse SNS vendors
-- "YueTA" [4] and "Papa With Friend" [5]. 

Since its very beginning of BWYF, people had concern about the privacy issue. 
As a centralized service provider, it is very easy to log user's activity. 
Not only those pairs who are matched, but also those who are not. 
It is generally embarassing to let other people know that 
you wanted to date someone but he/she refused to. 
This is also the motivation of such application.
Although the app prevents your real-life friend from knowing it, 
itself becomes "someone" who know everything remotely. 

The solution is to go decentralization.
Without a central server, how to do this matching without disclosing (too much) privacy? 
I'll note some preliminary thoughts on it.
Let's call it Decentralized Bang With Your Friend (DBWYF).

## Cryptographic Methods

I designed a similar homework problem [2] last semester for undergraduates. 
This problem borrows the idea presetned in [1]. 
In that problem, we want to calculate the number of common friends in a secure and private way. 
"secure" is seldom an issue nowadays. 
Just apply asymmetric key to ensure the communication is indeed and only between the two parties. 
The problem is "private" and we have several levels:

   1. After running the protocol, it's OK to let the other side know everything, 
   including those contacts that are not matched. 
   2. After running the protocol, it's OK to let the other side know 
   who are those matched contacts but not those unmatched ones. 
   3. After running the protocol, the two parties **only know the number** of matched contacts 
   but do not who are those matched contacts.

The solutions are none, cryptographic hash, and
[Diffie–Hellman](http://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange), respectively.

Suppose we design the following format

```
MyID,DateID1
MyID,DateID2
MyID,DateID3
...
DateID1,MyID
DateID2,MyID
DateID3,MyID
...
```

where `MyID` is my ID (`-_-//`) and `DateIDx` is the x-th person I want to date with.
We treat each row as a "contact" in the above problem. 
Now this is simply to ask: do we have 2 or 0 contacts in common? 
We can apply the same methods of counting common friends.   
Let's note briefly note the two methods:

   * **Cryptographic Hash**. 
   For each contact of user $x$, 
   calculate the hash values `$h(x_1), h(x_2), \ldots, h(x_n)$`. 
   For each contact of user $y$, 
   calculate the hash values `$h(y_1), h(y_2), \ldots, h(y_n)$`. 
   They exchange the hased lists and count how many hash values they have in common. 
   * **Diffie-Hellman**. 
   Suppose user $x$ and $y$ pick their random key (for this communication) $X$ and $Y$. 
   They also negotiate one large enough prime number $p$. 
   Every operation mentioned below is modular $p$, 
   e.g. $(x^X)$ is the shorthand for $(x^X \mod p)$.
   The process is:
      1. For each contact of user $x$, 
      calculate the values `${x_1}^X, {x_2}^X, \ldots, {x_2}^X$` and give it to the user $y$.
      For each contact of user $y$, 
      calculate the values `${y_1}^Y, {y_2}^Y, \ldots, {y_2}^Y$` and give it to the user $x$.
      2. For the received `${x_1}^X, {x_2}^X, \ldots, {x_2}^X$`, 
      $y$ raise them to his secret key: 
      `${x_1}^{XY}, {x_2}^{XY}, \ldots, {x_2}^{XY}$`.
      $y$ send those values back to $x$. 
      $x$ do similar things. 
      3. The two users compare the two lists. 
      If there is a common contact, `$x_i$` and `$y_j$`, 
      they should result in `$(x_i^X)^Y=x_i^{XY}=y_j^{XY}=(y_j^Y)^X$`.
      The leftmost and rightmost expressions just simulates the exchange process. 

   The powerfulness of this mechanism is that you only know the number of common contacts. 
   Due to the hardness of discrete logorithm, you don't know what is the matched contact. 
   For those unmatched ones, you also don't know.
   See [1] for some subtleties of applying this mechanism. 

## More Adversaries

The application scenario of DBWYF is different from the contacts matching problem [2]. 
There are some caveats in the hash and DH exchange process. 

For the hash scheme, one can exhaustively enumerate the IDs. 
Note that one usually has only several hundred friends
([Dunbar's number](http://en.wikipedia.org/wiki/Dunbar's_number)).
It's very easy to exhaustively enumerate them and know who you want to date with!
This is regardless of whether you salt the hash or not.
In the phone contact matching case, the space is significantly larger,
e.g. 8 digits of phone numbers. 
You can enforce some formats (e.g. "name,number") to further enlarge it, 
which renders enumeration attack infeasible with normal equipments and available information.

The DH exchange scheme is good for privacy preservation. 
However, there are some problems in the protocol sequence. 
There are four steps, and we can visualize them as:

```
1. x -> y: x^X
2. y -> x: y^Y
3. y -> x: x^(XY)
4. x -> y: y^(YX)
```

The arrangement of 3 and 4 is without loss of generality.
Now consider x fakes communication problem after the 3rd step. 
x will know whether they match or not. 
In other words, x will know whether y want to date him/her or not. 
However, y does not know anything.
In this way, x can technically probing y's intention. 
From y's point, this is just a communication problem instead of x's reputation problem. 

In the original common contact counting application, 
the two users will use this shared knowledge further, 
e.g. add each other to the buddy list if they have a lot common friends.
There is no incentive for one user to terminate the protocol unexpectedly. 

## Probabilistic Methods

Now we address the early termination problem.
The problem arise because one full cycle of the protocol suffices to determine 
whether the other side want to date him/her or not. 
If we can enforce the protocol to run mutiple rounds, 
there will be incentive for both users to keep away from early termination. 
Or else, there won't be a confident conclusion.
The software can refuse to perform a second cycle if previous cycles are not finished. 
This Tit-for-Tat idea is widely used in P2P softwares. 

~~More concretely, (example)~~

   * ~~If the user want to date the other side, 
   the software put this contact in the list with probability 0.9. 
   Else the contact is put in the list with probability 0.8.~~
   * ~~If they want to date each other,
   the probability to find a match in every round is 0.81.
   Else the probability is 0.64.~~
   * ~~Just getting the result of one experiment does not say anything. 
   To make the hypothesis testing confident enough,
   they should run multiple rounds (e.g. 20 as a guess).~~

After writing this, I find it not working...
There is another case which has probability 0.72.
This alredy reveals privacy. 
Denote the intention of dating by T or F. 
There are four combinations. 
The ideal scheme should ensure that they can only distinguish (T,T) from the rest. 
When it fails, neither sides could distinguish among (T,F), (F,T), or (F,F). 
Or else, it is embarassing to let the other side know you intention. 
The probabilistic construction looks hard to find a workaround at first glance. 

## Yet More Adversaries

Simply consider unexpected termination is not enough. 
One user can trick the other at the 4-th step of the exchange by using another key instead of $X$. 
In this way, only x knows the real matching result but not y.
x can thus fake contact list to probe y's intention. 
From y's point of view, there is nothing strange.

## Reference

   * [1] Von Arb, M. and Bader, M. and Kuhn, M. and Wattenhofer, R., 
   _Veneta: Serverless friend-of-friend detection in mobile social networking_
   , WIMOB2008 
   * [2] _Secure and private friend matching_, CUHK IERG4130 2012 Fall, Homework2
   * [3] Bang with your friends, 
   <http://www.facebook.com/pages/Bang-with-your-friends/397802486978835>
   , Facebook page. 
   * [4] YueTA, <http://www.36kr.com/p/203308.html>
   * [5] PaPa With Friend, <http://www.36kr.com/p/203338.html>
