---
layout: post
title: "测试Jekyll渲染再转发到renren"
category: 
tags: ["Jekyll", "Github", "Renren", ":snsapi", "snsapi", "markdown"]
---

[本年目标]({% post_url 2013-01-01-2013plan %})之一：
一定要把blog的基础设施弄顺手。

我的需求比较简单：

   * **以一个靠谱的平台作为存储介质。**
   首先是SP要靠谱，以前用过百度和人人，都不靠谱。
   测试方法就是出问题了找人工服务，发现他们完全敷衍用户。
   用它们得随时面临自己劳动成果瞬间消失的风险，不干。
   Github就不一样了，我报bug和问问题已经10余次，每次必响应，大部分是一天内回复。
   考虑到和工作人员都差了半个地球的时区，其实是非常迅速的。
   另外，Git天然去中心化，写作的时候本地就有备份，不用额外劳神。
   用wordpress的时候就恼火啊，过段时间dump一下数据库，再传到服务器之外，
   不知其他同学可有简单方法。
   最后，Jekyll的用户群组的氛围和Github一脉相承，学习起来很容易。
   wordpress的世界里，经常看到有人在下面留言：楼主这个xx功能用的啥插件呢？
   就像是每次有个很火的视频，下面必有人问BGM是什么。。
   这些现象在Jekyll的世界里就不会出现，直接看别人的repo就行了。
   e.g. 点
   [这里](https://raw.github.com/hupili/hupili.github.com/master/_posts/2013-02-18-test-blogging-github-2-renren.md)
   查看本篇blog的源码。
   综上，选择了Github，完胜其他平台几条街啊。
   * **能很方便地在各种平台流通。**
   如今靠订RSS来看博客的人是越来越少了，更多的是靠SNS分享。
   信息流通才产生价值，绝对是条真理。
   做得好的事，晒出去，让他人获益。
   做得不好的事，也放出来求拍砖，自己进步更快。
   最早的计划是以一个独立的wordpress为核心，然后转到多平台。
   之前搜到了各个平台到wordpress的搬家工具，做得不错，却没有反其道的一个分发工具。
   当然，零散的项目，xx2yy这种是很多了。
   不过没有统一接口，使用和维护都麻烦。
   看现状，这条需求只好交给SNSAPI来解决了（嵌入广告，猛击
   [snsapi中文网](http://snsapi.sinaapp.com/)，xuanqinanhai制作，非常专业）。
   * **可以进行简单的格式标记。**
   比如章节、列表、高亮等。
   下限是支持代码块（犹记坑爹的百度空间吃缩进啊）。
   支持更多当然好咯，比如tex风格的公式和表格等。
   使用了一年多的markdown，感觉完全离不开它了。
   自己也尝试过比较渣的扩展，主要支持了tex风格的公式和表格，后来发现不少人也做过类似的事。
   最初也想做成一种中枢语言，编成html、tex、textile、pdf、txt、rst等等。
   后来发现困难是相当高的，即便是零散xx2yy型的工具，很多时候也无法完好工作。
   于是这个想法作罢，还是老实用plain markdown。
   真遇到高级排版需求，就上tex吧。
   平时写个博客，大概排下就好了。
   Jekyll可以配置多种markdown后端，我现在用的是redcarpet，和Github一样。
   可以探索下，也许有的后端已经满足诸如公式这样的需求。
   * **方便检索。**
   之前一直对人人的检索功能耿耿于怀，在上面写的东西自己都要找半天。
   OSN的重心都在信息传递上，对知识管理的支持非常差。
   由于平台封闭，也没法使用第三方的搜索服务。
   现在好了，文章都在一个[repo](https://github.com/hupili/hupili.github.com)里面。
   要快速查找，`grep -R`就出来了，方便吧。
   不想下载repo的同学，也可以直接到Google上搜索。

Jekyll这边跑了一个多月，感觉顺了。
现在开始向SNS分发。
第一站，人人。
[SNSAPI最新的dev](https://github.com/hupili/snsapi/tree/dev)上已经加入RenrenBlog这个plugin。
发blog和发所有平台的status一样！
分发脚本的逻辑很简单：从RSS平台读新的日志，写到RenrenBlog平台中。

最后一个问题就是，写入RenrenBlog的HTML会被过滤成什么样，不太清楚。
不过markdown提供的都是些基本格式，理应支持。
先试下。

来一杆分割线：

---------------------------------------------------

测试开始！

# 这是一级标题

不知道大家什么习惯，我一般是把一级标题当作文章大标题使用的。
在我做的tutorial slides里面全部如此。
如果把一级标题作为章节标题，则会面临没法给文章标题统一排版的尴尬。

## 再来一个二级标题

### 再来一个三级标题 

#### 4级标题

##### 5级标题

###### 6级标题

## 代码段测试

嵌入文字的代码段`python -i snscli.py`。

代码块测试，就把转发脚本贴过来吧，作为demo还不错：
（在github上围观，点[这里](https://github.com/hupili/hupili.github.com/blob/master/tools/distribute.py)）

```
import sys
sys.path.append('snsapi')

import snsapi
from snsapi.platform import RSS
from snsapi.platform import RenrenBlog

def create_rss():
    config = RSS.new_channel()
    config['url'] = 'http://hupili.github.com/feeds/atom-all.xml'
    config['channel_name'] = 'github_rss_all'
    myrss = RSS(config)
    return myrss

def create_renren():
    config = RenrenBlog.new_channel()
    config.update({"app_key": "1c62fea4599e420fb4ac2a1fe38cc546",
    "app_secret": "151655bf6c87414e8571da69d8d7bd40",
    "channel_name": "renren_blog",
    })
    config.auth_info.update({
    "cmd_request_url": "(console_output)",
    "cmd_fetch_code": "(console_input)"
    })
    print config
    myrenren = RenrenBlog(config)
    myrenren.auth()
    return myrenren

import json
try:
    db = json.load(open('post_finger_print.json'))
except IOError:
    db = {}

import atexit
atexit.register(lambda: json.dump(db, open('post_finger_print.json', 'w')) )

def get_one_new_post(post_list):
    '''
	Only for RSSMessage list
	'''
    import hashlib

    for p in post_list:
        #finger_print = hashlib.sha1(p.raw.summary.encode('utf-8')).hexdigest()
        finger_print = p.parsed.link
        if not finger_print in db:
            print "New post!"
            print "Finger print:", finger_print
            print p
            db[finger_print] = 1
            return p

if __name__ == '__main__':
    myrss = create_rss()
    myrenren = create_renren()

    post_list = myrss.home_timeline(1)
    post = get_one_new_post(post_list)
    if post:
        print "Get one new post. Forward to Renren"
        print post.raw.title
        myrenren.update(post.raw.summary, title=post.raw.title)
```

把其中的url和key改成自己的就行了，直接运行。
如果snsapi不是放在当前目录下，修改一下顶上的`sys.path`。

没有高亮的感觉好丑。。
很多人贴gist，不过我有强迫症，不想把东西放得到处都是。
先就这样吧。。

## 列表测试

   * 没有
   * 编号的
   * 列表

   1. 有
   2. 编号
   3. 的列表

## 其他格式

**加粗**的文字。

*斜*的文字。

## 链接和图片

### 纯链接

[http://hupili.github.com/favicon.ico](http://hupili.github.com/favicon.ico)

### 纯图片

![http://hupili.github.com/favicon.ico](http://hupili.github.com/favicon.ico)

### 图片链接

[![](http://hupili.github.com/favicon.ico)](http://hupili.github.com/favicon.ico)

## 测试引用

> 我引用
> 了另外的
> 引用块
> 
> > 我是
> > 引用块1
>
> 啊
>
> > 我是
> > 引用块2

## 恩

貌似一般就这些了？
