---
layout: page
title: Site Building Using Jekyll
group: article
tagline: 
---

## Forwords

This site is built on Jekyll. 
My starting point is the 
[Jekyll-Bootstrap](http://jekyllbootstrap.com)
project. 
I'm constantly adapting the site to enable more functions:

   * Short notes and references goes to the GitHub repo 
   [README]({{site.base_links.this_repo}}/blob/master/README.md)
   of this site. 
   * Longer notes, especially those upgrades that are dirty or incomplete, 
   goes into this article. 

The schema:

   * Code diff URL (Github's `repo/compare/base_commit...head_commit`).
   Code speaks louder and code explains itself for most of the time. 
   * Description (if the code is complex).
   * Reference.
   * Remaining problems. 

## Random Posts

[Code Diff]({{site.base_links.this_repo}}/compare/b02d1ff43aa1c14401d5502c3d9cebcf39626e2a...f33755bca5dc7132f811d451da660b05e99a58c6)

### Reference 

   * <http://kingauthur.info/2012/12/03/the-things-about-jekyll/>
   * From the 
   [Jekyll template data description](https://github.com/mojombo/jekyll/wiki/Template-Data), 
   the `related_posts` are not so related... 
   * According to 
   [this post](http://ecommerce.shopify.com/c/shopify-discussion/t/can-i-use-random-numbers-in-liquid-1250), 
   they had 'random' at the beginning but delibrately took it off. 
   * A self implemented random function (tag). 
   [ref](http://stackoverflow.com/questions/11397245/jekyll-randomly-sort-collection)
   * W3Cschool's jQuery 
   [HTML methods reference](http://www.w3schools.com/jquery/jquery_ref_html.asp).
   * A discussion of 
   ["format" method in JS](http://stackoverflow.com/questions/1038746/equivalent-of-string-format-in-jquery). 
   After reading it, I decided to use the plain old way of concatenation... 

## Search Bar

[Code Diff]({{site.base_links.this_repo}}/compare/f33755bca5dc7132f811d451da660b05e99a58c6...84cc7ed67ea200e9c4f1b6c7e86ce654596ec945)

Since the main function is implemented in `jq_articles.js`, 
the commits are in the last section ("random posts"). 
Only incrementals are in this section. 

### Reference 

   * <http://kingauthur.info/2012/12/03/the-things-about-jekyll/>
   * Download the current latest:
   <http://code.jquery.com/ui/1.10.2/jquery-ui.js> .
   The [one in original post](http://code.jquery.com/ui/1.8.18/jquery-ui.js) does not work well;
   the autocomplete menu appears at the topleft corner of the page, instead of under the search bar.
   * [Position](http://api.jqueryui.com/autocomplete/#option-position)
   the suggestions better. 

### Remaining Problems

   * The top margin of the search bar is not correct. 
   I tried table layout, `vertical-align:middle` and some other methods. 
   None of them works and the final dirty solution is to insert one 
   `<ul></ul>` before the search bar's element. 

## Ordered Navigation Bar

[Code diff]({{site.base_links.this_repo}}/compare/77fc4c0d57f6a08863f2b808a736fb45b307d98a...dae3431360fd05972104003311e966810e821220) of the implementation `page_list` ordering via weighting. 

[Code diff]({{site.base_links.this_repo}}/compare/b6409e6cc555f93db2ffbbb31383b8a810bd5ac1...0d9085e333212c1c099e2f3611023da5144f8a75) of my new manual navigation bar design. 

### Reference

   * A [pull request](https://github.com/plusjade/jekyll-bootstrap/pull/134) of JB
   which demos the way to manage page ordering using weights. 
   This is my original starting point. 
   * From the [page for designer](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers), 
   I did not find the way to assign an array, 
   let alone assigning an array of record elements ("mapping" in YAML's language). 
   * A [Google Group Discussion](https://groups.google.com/forum/?fromgroups=#!topic/liquid-templates/qwE5hWk-Kik)
   which provides a lightweight way using `split` method.
   * [wiki page of YAML](http://en.wikipedia.org/wiki/YAML) but I did not get useful information there.
   * I learned sequence and mapping expression from the [official doc of YAML](http://yaml.org/spec/1.0/).
