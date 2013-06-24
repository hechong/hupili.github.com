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

## Operating System Support 

texmacs can run on all major platforms -- Mac OS X, Windows, Linux. 
OS X is the original platform. 
There may be some portability issues for other platforms.
This section documents my test experience. 
Some of the problems listed below may not be caused by texmacs itself. 
They may be environment problems.

### MAC

Very smooth. Minor glitches:

   * If `.pdf` images are linked, the exported PDF will have a blank there.
   * `.png` and `.jpg` images are rendered poorly (saw edge) inside TM.
   The images in the exported PDF are well rendered.

### Windows

   * I tested on win7. I can see the TM come up but it disappears very soon.
   * Somebody mentioned [the crash problem on win8](http://lists.texmacs.org/wws/arc/texmacs-users/2013-05/msg00070.html).
   I tested the patch in [this issue](https://savannah.gnu.org/bugs/?38784). 
   It turns out not working. 

Use Cygwin:

   * Install `texmacs` and `xinit` package using `setup.exe`. 
   * `startxwin` from Cygwin terminal. 
   * `texmacs` from the prompt xTerm. 
   * All default settings should work.

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

## Comments

Two methods pointed out by TM users:

   * Use `specific`. See [man page](http://www.texmacs.org/tmweb/manual/webman-primitives.en.html)
   * Use `flag`.

## CLI Usage

The command `texmacs --convert article.tm article.pdf` is used to compile a `.tm` into `.pdf`.
How to do it in a headless manner (i.e. without GUI window) is still unclear. 
Just note some findings. 

[wikipedia page](http://en.wikipedia.org/wiki/GNU_TeXmacs) notes one way under Linux:


```
xvfb-run texmacs --convert article.tm article.pdf --quit
```

From this [user group post](http://lists.texmacs.org/wws/arc/texmacs-users/2013-06/msg00002.html):

```
texmacs -c $(FILE).tm $(FILE).pdf -x '(print-to-file "file:$(FILE).pdf") (generate-all-aux) (update-current-buffer) (print-to-file "file:$(FILE).pdf") (generate-all-aux) (update-current-buffer) (style-clear-cache) (style-clear-cache) (print-to-file "file://$(PWD)/$(FILE).pdf")' -q
```

It is still not headless. 
Nevertheless, it gives me some pointers for CLI options. 
Try to dig out the usage later.
I think I would need to learn some Scheme. 
I adapted the above commands to the 
[Makefile](https://github.com/hupili/tutorial/blob/master/spectral-clustering/slides/Makefile)
of my spectral clustering presentation.
