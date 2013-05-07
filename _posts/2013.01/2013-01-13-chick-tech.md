---
group: blog
layout: post
title: "我经历的人人网小黄鸡（技术篇）"
description: "一月将过一半，新学期明天开始，今年至现在，经历过的最有趣的莫过于小黄鸡这个项目了。收获颇多，记之。"
category: 
tags: ["小黄鸡", "人人", "simsimi"]
---
{% include JB/setup %}

## 背景

没听说的同学去[小黄鸡主页](http://page.renren.com/601621937)
看看就知道了。
还有[Github repo](https://github.com/wong2/xiaohuangji/)。
刚看到的时候感觉很有趣，
也和同学讨论了一下。
其实背后的AI对我并不是个太大的问题，
坊间早也流传各种分析，估计是用的simsimi；
即便没有simsimi，类似的智能机器人项目也有很多了。
而小黄鸡如何与人人接口，
才是我最感兴趣的。
因为一直在慢慢地做[snsapi](https://github.com/hupili/snsapi/)，
深知接口是一件很不容易的事情。
特别是小黄鸡每天处理这么大量的请求，
非常好奇它是怎么突破API限制的。
根据[人人API Quota](http://wiki.dev.renren.com/wiki/API_Quota)，
最高级别的授权，也不过是每小时900次获取信息，
那么最小的粒度即为4秒。
而小黄鸡很多时候是秒回，所以一定走了其他渠道。
之前总觉得抓包，分析页面请求，解析页面是件很麻烦的事情，从来没有像样地动手实践过。
随着小黄鸡的开源，各种疑惑都解开了。
看到消息后，立马暂停了其他的工作。
先读了`renren.py`，发现这正是我一直在找的，于是决定这几天先跟一下这个项目，学习学习。
一是学技术，二是学开源合作。
说来惭愧，这么大个人了，还没像样地参与过一个开源项目。
之前的[snsapi](https://github.com/hupili/snsapi/)，
只有两个同学在里面，处理过一个来自网络的pull requet。
虽然从形式上说，是开源的，但是开源合作的味道并为好生尝过。

从9号到13号，投入了4天半在小黄鸡和相关项目上，收获颇多。
开学后重心会移回research，学习也
[更倾向于数学]({% post_url 2013-01-01-2013plan %})，
开发和技术积累应该会慢慢变少。
值得记一下这几天的收获和一些positioning view。

## 技术积累

   * 最初看小黄鸡人人接口和simsimi接口的代码，
   知道了Python的`requests`。
   比`httplib`强大，特别是`Session`，
   自动维护cookie和keepalive，用起来超方便。
   * 阅读了9号的`renren.py`之后，
   发现直接从页面请求json数据也不是一件难事。
   可以说，最重要的是从这个文件得到了信心吧。
   正好，人人登录在香港总是出现验证码，
   这个是原接口中没有解决的，
   如果不解决的话，后面的功能都无从测试。
   于是自己来研究一下，用httpfox抓包，看请求流程，
   然后尝试下载验证码到本地供手动输入。
   * 为了验证同样方法用在snsapi里面的可能性，
   添加了`home_timeline`和`update`两个函数，
   之后就和snsapi完全兼容了。
   使用这个模式，不用再恼火api的quota，以及授权的问题。
   坏处是页面的变动肯定比api更频繁，
   需要的维护力度也更大。
   这块更新写得很随意，只是临时拼凑起功能，
   于是没有发pull到原项目，
   感兴趣的同学可以看
   [这里](https://github.com/hupili/xiaohuangji/blob/hushuo/renren.py)。
   * 基于升级后的人人接口，
   做了[hushuo](https://github.com/hupili/xiaohuangji/tree/hushuo)
   这一个分支。
   代码乱但是可以跑……
   在人人上跑了一天，看到感兴趣的人就回复，
   有at或者re，也去回复。
   后端还是simsimi，只不过比小黄鸡来说，拓展了信息渠道。
   （话说稍微一改就变成抢沙发利器了）
   * 感觉这种模式很有前途（后面有述），
   10号到11号盘算了怎么做一个垂直服务，比如新闻索引，先试试水。
   正好看到有人在微博上分享
   [新浪2012的新闻语料](http://zhangkaixu.github.com/resources.html)，
   就准备用它试试。
   * 解压后的语料大概有1G+，其实也不算大。
   学了下用`BeautifulSoup`做XML的解析。
   然后就是分词、做倒排，准备尝试一下使用redis来存索引。
   先单进程跑了一下，速度比较慢，感觉会跑很久去了。
   正好小黄鸡用了`rq`，于是也学着用rq来分配任务。
   结果是，提交任务的模块迅速跑完
   （扫1G的XML，一个文章一个job）；
   rqworker后来跑了一个晚上还没跑完
   （总25W，第二天还剩15W），
   还把服务器搞得很慢，连ssh登录都卡，副作用足了……
   初步猜测，可能的原因有：
   1、redis已经吃掉8G内存，硬盘交换严重；
   2、redis设置的是每秒fsync，可能太频繁，至于怎么优化redis配置，还没学过；
   3、rq有频繁的删除操作，
   当redis负载小的时候，比如全在内存里，删除是比较迅速的，
   但是当负载大的时候，删除导致更多硬盘交互，
   不仅rqworker卡死（很久拿不到任务），
   整个系统都很卡（cd进个目录都等半天）。
   最后盘算下来，还不如就单进程地跑，一晚上也跑完了，囧……
   之前也只用过Hadoop处理大的任务，
   轻量级并发方面，
   转入Python之前尝试用perl写过一套多进程多机器的
   [LWT](https://github.com/hupili/Lightweight-Distributing-Toolset)。
   用LWT做爬虫实用可以，挂200台机器还好；
   也试过多机并发跑仿真。
   对于这种单机上计算和IO都密集的任务，还没很好地尝试。
   基于这次的亏，之后可以考虑这些点：
   1、多进程；
   2、一进程多job，而不是一进程一job，
   以节省词典IO的overhead；
   3、使用memdisk来hold住词典等频繁读取的资源。
   重要的是分析清楚应用环境，
   感觉rq用于收支接近平衡并且worker的IO量不大的环境中更合适。
   * 12号看到项目发展地很快，dependency越来越多，
   觉得分头改跟不上进度，于是放弃继续单独做垂直Q/A；
   另外，即使做了，之后也没有时间维护。
   作罢，不过我依然觉得这是有前途的。
   * 12号看到wong2的
   [userscripts](https://github.com/wong2/userscripts)，
   感觉很有意思。
   看来从人人能拿到的信息还是挺多的。
   不过暗网抓取一直是学术圈的弱项，
   很多能操作的技术牛人后来也没在读研，
   所以这类数据其实很有价值。
   想起自己之前也写过些简单的，
   比如
   [学校论坛](http://bbs.qshpan.com/)
   的内外网转换，
   也翻出来[放在了github上](https://github.com/hupili/userscripts)。
   受了点启发，于是做了一个类似“我要当学霸”那个app的
   GreaseMonkey脚本，
   [说明见此](https://github.com/hupili/userscripts/blob/master/doc/stop-time-leecher.md)。
   期间在Firefox的ScratchPad上调试了不少时间。
   发现用JS来操作DOM完成一些工作挺有意思的。
   顺便记两个好项目：
   1、[Phantomjs](https://github.com/ariya/phantomjs/)，
   是一个headless browser，可以完美执行JS；
   2、[Brython](http://www.brython.info/index_en.html)，
   是JS写的Python2JS转换器，直接在浏览器执行。
   有了这两个工具，操作页面元素应该会很方便。
   * 11号到12号之间，simsimi对请求加了一些验证，
   于是原来的`simsimi.py`只能说一句话，
   第二句话即会收到错误信息。
   开始猜测是浏览器参数的问题，
   尝试把真实抓包到的参数都加进去没有解决。
   后来发现可能是keepalive的关系，
   于是用`requests.Session`搞定。
   * 小黄鸡的plugin机制还是比较成熟了，
   13号也有同学加了nosetest进去。
   话说nosetest我也没用过，就顺便写了个计算鸡的plugin，
   用下nosetest，感觉这样组织起来确实有章法。
   虽然表达式解析的逻辑没什么好说的，都是调用现成的库，
   怎么限制计算时间倒成了个问题。
   刚开始想用thread，网上也有很多错误建议用thread的，都不work。
   后来才知道Python的thread不支持kill，
   找到一个用process的解决方案，
   封装得很好，
   而且decorator的方式，使用起来很简洁。
   见
   [代码](http://code.activestate.com/recipes/577853-timeout-decorator-with-multiprocessing/)。
   * 另外，在fqj1994的提示下，知道了`sympy`，看起来很强大，
   加到了计算鸡的模块中。
   也是在fqj1994的提示下，知道了`doctest`，
   一看，真是个非常聪明的点子啊，把文档和测试用例完美合一。
   话说，看到这样的id，觉得自己好老……
   5年前的这会，我在干嘛呢？
   学校不让配电脑，平时就看书刷提搞成绩，偶尔通宵打个真三；
   没用过Linux，没用过Python，只用PASCAL写过点OI的题目，
   想起实用的任务就头疼。
   压力略大。

