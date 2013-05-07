# Eight Roads

This is Pili's personal blog with JekyllBootstrap backend. 

Please visite the website: 
[http://hupili.github.com/](http://hupili.github.com/)

For all usage and documentation of JekyllBootstrap, 
please see: <http://jekyllbootstrap.com>

## ChangeLog and Reference. 

   * Use jQuery to polish markdown output. 
   First trial: center images according to the "alt" attribute. 
   * Support mathjax. Usage: add header "mathjax: true" in your post source file.
   * Add "random posts section". 
   [ref](https://raw.github.com/Hawstein/hawstein.github.com/master/_layouts/post.html)
   * Add more `redcarpet` options, e.g. support strikethrough. 
   [ref](http://stackoverflow.com/questions/13464590/github-flavored-markdown-and-pygments-highlighting-in-jekyll)
   * Add section number using css: 
   [ref1](http://stackoverflow.com/questions/10340276/how-to-add-section-numbers-1-2-3-4-1-automatically-using-css)
   [ref2](https://developer.mozilla.org/en-US/docs/CSS/Counters).
   However the refs do not quite work with "twitter" theme in JB.
   I have to put the `counter-increment` in header instead of "before". 
   * Enable comments for certain pages
   (configure page meta info `comments: true`). 
   * Support finer grained page ordering by merging 
   latest JB with page order feature from TheCodeKing.
   * Make a [buddy list](http://hupili.github.com/pages/buddy-list.html).
   One can assist himself/herself to add a link there. 
   * Feeds layout upgrade, leave room for future by-category feeds. 
   Reference: 
   1) [html redirect](http://www.instant-web-site-tools.com/html-redirect.html) ;
   2) [Jekyll template data](https://github.com/mojombo/jekyll/wiki/Template-Data) ;
   3) [Liquid for Designers](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers) ;
   4) `_includes/JB/pages_list`. 
   * Fix the 
   [excerpt length pitfall](https://github.com/mojombo/jekyll/issues/732). 
   Further reference: 
   [Liquid](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers). 
   This change failed, 
   [further issue](https://github.com/Shopify/liquid/issues/166). 
   * Move side tag bar to the bottom of post. 
   * Ignore 'others' directory so that I can more conveniently do experiments with others Jekyll blogs:
   [Jekyll Ignore](http://blog.patrickcrosby.com/2009/09/05/jekyll-exclude-files.html)
   Also [Jekyll Issue](https://github.com/mojombo/jekyll/issues/77)
   (do not use wildcard). 
   * Adapt [yanping](https://github.com/yanping/art)'s 
   index template to show recent blog list. 
   * Note down
   [yanping](https://github.com/yanping/art). 
   May change comment system to Duoshuo later. 
   * Follow 
   [erjjones](https://github.com/erjjones/erjjones.github.com)'s
   note to setup the site and the feedback button. 

## License

### Original License:

[Creative Commons](http://creativecommons.org/licenses/by-nc-sa/3.0/)

Do I have to inherit it? 
I just don't have time to study the license. 
So all original materials inherited from 
[Jekyll](https://github.com/mojombo/jekyll/)
are covered by this license. 

### License for Other Materials

All other stuffs created by Pili,
if not otherwise stated, 
are released to public domain. 
Cite as you wish. 

![copyleft](http://unlicense.org/pd-icon.png)

[http://unlicense.org](http://unlicense.org)
