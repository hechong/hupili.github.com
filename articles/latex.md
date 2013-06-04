---
layout: page
title: Latex Tricks
group: article
mathjax: true
tagline: 
---

{% include JB/setup %}
# Tex Tricks

This page notes down the snippets of TeX usage of HPL. 
He started to learn LaTeX in the summer of 2011. 

## Keep code indent 

The standard package `verbatim` does not work. 
It will eat your code indent. 

```
\usepackage{fancyvrb}
...
\begin{Verbatim}
	your code here ...
\end{Verbatim}
```

## Typical start (preamble)

```
\maketitle

\begin{abstract}
	This is abstract. 
\end{abstract}

\pagebreak
\tableofcontents
\pagebreak	
```

## Draft version

The draft version won't include any graphics, 
thus saving the compilation time. 

```
\documentclass[11pt,a4paper,draft]{article}
```

## CUHK Thesis

   * Basic Latex: http://www.cse.cuhk.edu.hk/~tywong/latex_basics/
   * Advanced Latex: http://www.cse.cuhk.edu.hk/~tywong/latex_adv/
   * CUHK thesis template: http://www.cuhk.edu.hk/clear/download/thesis_template.zip

Short notes on CUHK thesis template:

   * Usually `report` with 11pt font. 
   * `\thesistitle` should match that in "declaration of intention to graduate". 
   Even punctuation or case difference will lead to rejection by CUHK graduate school!
   * Unit of `\linespread{??}` is not the line height. 
   If you want double line spacing, use 1.6; 
   If you want one and a half line space, use 1.3. 
   * You will submit a draft for defense and a final version later. 
   Remember to modify `\submitdate`. 
   * Chapters with a star `\chapter*{}` does not appear in TOC. 

## Floating Objects

   * h: here. 
   * t: top. 
   * b: bottom. 
   * p: the obejct owns a page. 
   * !: try hard to fulfill my request. 

## Table Rotation 

For oversized table, first try to adjust fonts like `\small`, `\tiny`. 
If still oversized, rotate it and place in one single page. 

```
\usepackage{rotating}
...
\begin{center}
	\begin{sideways}
		\begin{tabular}
			...
		\end{tabular}
	\end{sideways}
\end{center}
```

Note the above object is non-float. 
You may see paragraphs broken by the single-page table 
even if there is a lot of space in the previous page. 
Wrap `table` environment at the outer most level to fix this. 
e.g. 

```
\begin{table}
	\begin{center}
		...
	\end{center}
\end{table}
```

## Column Definition of Tabular

   * l: left alignment. 
   * r: right alignment. 
   * c: center alignment. 
   * p: paragaph, will wrap texts. 
   It must be follow by the size of cells. 

`p` is really useful when a cell contains very long strings, 
so that it fit into multiple lines. 

```
\begin{tabular}{p{0.5\linewidth}}
	...	
\end{tabular}
```


## Long Table

Useful for glossary. 

```
\begin{longtable}{...}
	...	
\end{longtable}
```

The column definition is same as `tabular`. 

## Formatting Optimization Problem

I'm not sure what is the best way to do it. 
At least, there are two main approches from the internet. 
One use `eqnarray`, the other use `align`. 

I'll make examples here after I have strong preference...

Remarks: `eqnarray` can be emulated by `tabular`

```
\begin{tabular}{|r|c|l|}
	f(x) & = & 5	
\end{tabular}
```

## Squeeze Out Space 

Insert the following command at the place you want to reduce blank space. 
Adjust the value by trials and errors. 

```
\vspace{-0.25in}
```

This trick can be very useful to compress your paper into required number of pages...

## Multi-column

Refs:

   * <http://physical-thought.blogspot.com/2008/09/two-column-layouts-in-latex.html>

## Useful Symbols

   * `\Rightarrow`,`$\Rightarrow$`: Logic symbol for "if .. then". 

----------------

This article was originally hosted 
[here](http://personal.ie.cuhk.edu.hk/~hpl011/homepage/resource/tex-trick.html).

I'm hesitating to move it.
It looks better there.
The most important feature is the Table-Of-Content (TOC).
There should be other MD engines who can do so and also integrates well with Jekyll.
If anyone is aware of them, please kindly tell me.
