---
group: blog
layout: post
title: 商场布局症
language: ch
category: 
tags: ["商场布局症", "互联网", "商场", "产品", "设计", "人人", "新浪微博", "新闻", "腾讯", "QQ"]
---

## 商场布局理论

最近偷的半天闲暇，来谈一种屎一样的设计——商场布局症。
我不懂设计，不过我是用户，这是发言的基础。
至于“商场布局症”，或许已经有其他学名了，不过我先这样叫着吧。

大家逛商场的时候，可能会发现一种常用的设计：
不管顾客从哪到哪，都尽可能拉大步行距离。
具体的一些表现可能是：

   * 上下楼的电梯不在同一个方向上。
   这样如果找错位置，需要绕至少半圈才能回来。
   * 比较邪恶的，甚至故意用商铺进行阻拦，让人需要绕一圈才能走到再上一楼的电梯。
   * 有的商场精心设计错层电梯，更延长了上上下下的距离。
   * 从一个大超市出来的时候，咦？怎么不是和进来的门在一起的街道？
   从出口走到街道，还有好一段，两边都是各种摊点。

作为商场，这样的设计还是符合逻辑的。
加大步行距离和延长顾客在店内停留时间被视为两种传统的增加收益的方法。
老生经常说，很多人的购买需求是去了商场才有的，而非提前决定的。
对这种顾客，以上两种方法都能增加相关或不相关产品的暴光率，进而增加购物率。
我觉得随着现代节奏的加快，这样的情况是会越来越少的。
像我这类人，肯定是有了需求，甚至打了清单才会去商场的。
真要闲得无聊，宁愿撰篇文拍他一砖，也不愿意将时间浪费在商场中的迂回。
随着网购和物流系统的成熟，以后商场应该会逐渐成为书店这样的角色吧（氛围重于内容）。
不过说到底，商场中的一点迂回并不消耗多少额外时间。
最大的overhead应该是来回商场的路途吧，然后是排队和甄选目标商品。
客观比起来，花在迂回上的时间还是可以接受的。

可悲的是，这种传统的、粗暴的增加内容关联性的手段居然被一些互联网产品所使用，难以理解。
举几个例子吧。

## 例1: 新浪微博iOS上的新闻推送

一个case:

   * 通过notification center显示了几条摘要。
   其中一条突出了“性窒息”死亡这个term，引起了我的注意。
   好奇当然就要点过去看。
   * 点过去竟然是新浪的一个新闻目录页。（附图1）
   不过有点道德的是，该条放在首位
   （就是用这个把人引过来的，要是不放在首位行吗？）。
   * 好吧，继续点进去，结果是一篇长文的一部分。
   拉到底的样子见附图2，需要再点击看余下全文。
   那前面是什么呢？
   前面跟我们要找的南昌航空的信息毫无关系：
   作者先谈最近校园非正常死亡事件有点多了；
   除了南昌航空这个，还有复旦投毒，etc；
   然后搅屎棒一样地数了一下教育和体制的问题；
   然后先对复旦的案例做了比较详细的描述；
   该说南昌航空的事时，就轮到翻页了。
   * 那翻页好吧，终于到主题了。
   写得那叫一个啰嗦，典型的新闻八股：
   从他们的角度来看，在用逐级放大的方式讲述一件事，越来越详细。
   可是从用户的角度来看，过了这么久才找到所需信息，真想用块豆腐把他们拍死。

简评：

   * 过分追求眼球效应。
   * 故意延长操作路径，以期待增加对其他新闻的点击。
   * 挂羊头卖狗肉（明显并非一篇以南昌航空为主的文章）。
   * 对于面向移动终端的文章来说，写作风格太捉急，没把重要和急需的信息放在显眼的位置。
   * 记者通病：喜欢评论而非记述事实；评论多自以为是且严重八股化。

其实早就观察到了商场布局症的存在，但一直没想写。
这次新浪的新闻推送实在恼我了，思维一短路，竟想不出除了“屎”之外的第二个形容词
（“不接地气”？“用户体验差”？顺便群黑一把`-_-//`）。
其实理想的流程是这样的：

   * notification center推送核心关键词。
   比如“性窒息”就可以，引起读者兴趣也不是什么错。
   * 点过去，一小段文字，给两个信息就可以了：
   1）南昌航空的时间证实是性窒息，给正在追踪这件事的同学最直接的信息；
   2）简述一下什么是性窒息以及现场情况，给新来的同学补充知识。
   * 下面一堆相关链接：
   1）复旦投毒案，……；
   2）朱令案，……；
   3）xx校园杀人案，……
   * 至于长篇累牍的评论和缩放式描写，大可压缩于一个超链内：
   [如对本报记者的屁话感兴趣，请继续阅读](http://en?).
   * 可以在导航栏加上返回新闻目录页的链接。

## 例2: 人人小站

人人小站初现的时候是很正常的。
如果有小站发布了日志，点击链接，就直接进入日志相应的日志页面。
记得中途有一次极端的改版：
点了新鲜事链接，会进入小站的聚合页，所有小站的新鲜事都有在上面；
然后你再根据刚才看到的标题去点击，进入那个新鲜事的小站；
最后再在小站自己的界面上点击某个日志。
这里面的逻辑我是完全不明白。
我点击新鲜事的链接，就是因为看到标题和摘要，想读这篇文章。
真不懂其他小站的新鲜事以及这个小站的其他新鲜事与我何干？
现在操作序列已经调整，但还是很屎。
你点一个新鲜事链接，进入的是小站页面，而非日志页面。
看一个小站日志要点两次，真是一种其他的QJ用户的体位。

## 例3: qq新闻推送

不知道qq新闻是不是这行当的鼻祖，但我还有印象的案例中，qq新闻倒是最早的商场布局症患品。
其实大部分时候，右下角来个气泡窗，我们也不会去看，不关心嘛。
偶尔编辑用了点功，出了个吸引眼球的摘要，引得我去看。
结果点过去后，不是相应的新闻页面，反而是qq新闻的目录页。
更甚的是，你因为它而点过去的那条新闻可能不是头条、不是头版，还得找下才看到。
说实在的，真怀疑这些人做过用户调查没有。
强制增加1次PV真有意义？
也许对以展现计价的广告有点用吧。
至于羊头和狗肉，腾讯做的比上面新浪的case只有过，无不及。
我记得有次看到感兴趣的，点两次过去，居然是个专题页，
而气泡窗中最扯眼球的段落（以及相关段落）藏在其中的某篇文章中，真够找的。
设计气泡窗推送的人是缺心眼吗？
既然你知道用户点它，是因为你们摘要的那段话吸引人，为什么不直接导过去呢？

## 总结

   * 增加内容关联性是做服务必要考虑的
   * 商场布局症是传统行业的营销思维遗毒
   * 以优质内容来增加用户停留时间，而非通过延迟用户的操作来增加PV和页面停留等数据
   * 推荐引擎如此成熟的今天，应该用技术手段来增加内容关联性，反对粗暴组装内容
   * 作为互联网时代的信息提供者，应力求简洁，直接命中要害。
   我们不是大爷大妈——买菜回来，悠闲地读着报纸打发时间，连中缝广告都给啃完。

## 附图

附图1：（截图时间比下面的要晚，因为终于找到内容后，觉得设计这套流程的人脑袋全装屎了，准备写篇文章，故又返回来截图）

![style=center;width:30%]({{ site.base_links.pic }}/prosaic/sina_weibo_news_p1.PNG)

附图2：

![style=center;width:30%]({{ site.base_links.pic }}/prosaic/sina_weibo_news_p2.PNG)

