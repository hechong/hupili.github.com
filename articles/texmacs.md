---
layout: page
title: TeXmacs
group: article
mathjax: true
tagline: 
---

{% include JB/setup %}

# TeXmacs

## Forewords

TeXmacs is a powerful structural editor. 
It is a completely different system from LaTeX but backward compatible with it.
My early experience with TeXmacs is quite amusing. 
After going deeper, I find that there are a lot that worth a note: 

   * Although the user manual is very thorough, it does not allow efficient search. 
   * Keyword search on Google usually do not return meaningful results.
   Is it due to the small group of users?
   * The menu design of TM is sometimes non-intuitive. 
   I find one entry at some time but totally missed later.

## Preamble

Document---Part---Create Preamble

## Presentation Slides

Digest from [this thread](http://osdir.com/ml/editors.texmacs.user/2008-09/msg00027.html):

   * Step.1: Document---Style----Seminar
   * Step.2: Document---Page----Size---A5
   * Step.3: Document---Page---Orientation: Landscape 
   * Step.4: Document---Page---Type: Paper

Step.1 matters with the appearance. 
e.g. default header color becomes red. 
Step.2 and Step. 3 make it look like "slides".
Step.4 is to make the page boundary visible inside TM so that you can plan your materials.

One last thing:

   * Use `<new-page>` to create new slides.

I'm wondering whether we have better ways. 
The hack around presented here does not look like the usual way TM handles things.
It is more like a kludge.
There should be some structural editing methods.
e.g. `<new-slide>`, `<slide-header|hello>`, etc.
