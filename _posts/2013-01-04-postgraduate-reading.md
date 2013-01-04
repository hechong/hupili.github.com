---
layout: post
title: "研究生资料阅读的探索"
description: "phd读了1.5年，关于阅读，有些想法：阅读习惯从DFS转向BFS；查找来自原始作者的信息，避免传播损失；重视why而不是how；motivation比methodology更重要；联系和对比；扁平且简短的记录"
category: 
tags: ["postgraduate", "phd", ":exp", ":letter"]
---
{% include JB/setup %}

## 来信

> 暂略
>
> ...
>
> ...

## 回复

我对看长资料也没什么特别好的建议，因为我最多的经验还是看一些中短篇的资料，比如blog post、paper。核心就是一鼓作气，快速地迭代和回溯。过程和你提到的差不多，基本是DFS的，有哪里不懂就赶快找其他资料解决，然后回溯。我也在尝试调整这个模式，因为它对把握一个大方向还是不适合的。根据我观察到的，教授们大多是BFS的方式看资料。

本科的时候，重在基础积累，很多知识的习得是自底向上，所以DFS没什么压力，几层就可以解决了；这个时候，精读也是有益的，训练人对细节的把握。研究生往往是先找问题再找方法，而方法可能是一无所知，DFS容易一下就深入很多层，很快就跑偏了；这个时候，泛读更有益，帮助对整体的把握。

具体到读一篇paper，Keshav的“how to read a paper”提到的3-pass是这个思想。一层一层地深化，根据时间、精力、质量来决定走到哪一层。虽然每个人对xx-pass的定义都不一样，但我觉得可以先自己一边尝试一边定义一下，然后依照这个标准来演练。不管如何定义，有个标准会更有推动力，也便于自己以后回顾。附了一份我11年末刚开始的标准列表，现在来对比，有些变化：1、对于熟知的领域，在pass1的时候不需要读introduction，也可以把握主体思想了，这可能和Keshav没把introduction放入pass1是一个原因吧；2、在pass1的时候，增加了对图、表、公式、布局的一个扫描；3、pass2也未必5-10hr了，对于熟悉的领域，一般会在1-2hr吧……还有不少变化就不赘述了。为了进度跟踪，我自己做了个
[paperdb](https://github.com/hupili/paperdb)
，简单点的用excel打个表格其实就可以了，也可以顺便记下笔记。

具体到大一点的，比如把握一个方向，顺序像很多人建议过的：survey、top-conf的大牛、top-conf的中牛小牛、其他。前几天有朋友推荐过
[nowpublisher](http://www.nowpublishers.com/)
，Foundations and Trends系列质量不错。还有其他获得survey的途径，网上见过一些讨论，没记住。我现在觉得最高效的信息获得方式还是从人这里来，如果有谁比较了解的，直接指向高质量的材料会更快。至于怎么鉴定大牛，暂无系统的方法论，可以参考引用、Google Scholar、MS Academic的数据等。前几天得知一个新站点不错，
[arnetminer](http://arnetminer.org/)
。具体操作上，还有许多需要实践来检验的，核心思想还是BFS了。

上面这些是对各种研究都适用的讨论，具体到系统类的研究，我虽然没什么经验，但也从导师那里观察到了一些可借鉴之处。这学习tutor一门研究生的高级网络技术方面的课，各种系统、协议，每个拿出来都是成百上千页的文档，卒读显然是不可能的。

有两件事印象很深刻。

第一件事是某次遇到一个OSPF中比较偏僻的问题，在数百页的RFC上尝试了寻找未果，去问导师，然后他很快找出Moy的书，翻到了相应的解释。Moy是OSPF的设计者，所以他在书中讲了很多why。相比之下，RFC往往只有what和how；why的部分可能存在于某些讨论组和邮件列表中，但是一般人很难找到。what+how对于系统实现者是有必要的，但也是人最容易忘记的部分，即使曾经精读过的文档，过一两年来看，也陌生了。相反，why往往具有普适性，许多设计思路是跨系统、跨协议、独立于运行环境的，也更适合长期记忆。这个事让我觉得，回归原作者是一条比较好的途径，他们的一个talk、几张slides、blog post都可能传递更多的Insights，这些是自己看数百页文档不会意识到的。

第二件事是他讲ipv6这章和MPLS这章的时候。ipv6我之前也零散接触过，本科老师上课也大概简单讲了一些。过了很久之后，就全部忘了。不说v6的header长什么样，就连天天用的v4的header也印象模糊了。很惊异的是，他就对着一张ipv6 header的slides讲了半小时吧，每个field为什么会是这样，跟之前的v4相比，多了少了的部分是为什么，都十分清楚。至于ATM，我们以前的讲法大概就是说说cell多大、vpi/vci这些概念，然后告诉你ATM已经过时，不细讲了。至于MPLS，印象也就是分了几种包，header怎样。听了导师讲这章之后，才知道从ATM发展到MPLS的前前后后，需要解决的是什么、思想是什么，etc。至于以前记的那些琐碎，除了考试和考级，几乎没有作用，也无法前后联系。虽然中学哲学就灌输了“联系看问题”的思想，但其实我们并没有主动去实践过。之所以本科课程让我们觉得有联系，是因为学校已经安排好了，先学什么后学什么，全不费功夫，这和主动去联系的效果不同。我导师读书的时候，并不是networking方面的，大概从90年代中期，一边工作，然后一边自学。那时在美国是黄金机会，有许多一手的信息。他听过许多原始设计者的talk，自己组织课件的时候也使用他们的材料。前后比较，才能知道background和motivation。往往有了这两个信息后，如何设计都是可以根据自己的逻辑推衍出来的，所以其重要性反而次之；如果不能根据自己的逻辑推衍出来，或者推出相悖的设计，那说明这个设计本身应该有问题；同时关于how，也很容易回文档找到，有印象即可。

最后就是关于记录笔记的问题。前几天和一个朋友交流，确认了两大派系。一派重视工具辅助，另一派重视人脑本身。实际操作并非完全对立，是有结合的，不过侧重不同。我个人比较偏工具派，但是感觉所见的大牛更多是人脑派的。一个基础的问题就是：你记了这么多笔记，之后会回来看吗？我们说的是那种非课程（之后用于考试）的笔记：比如看到有用的网站，收藏起来，加个笔记；看过paper，记录一下思想和方法；etc。工具派比较强迫症，行为模式是“in case”型的：虽然99%可能不会再用到，为了1%，还是要做好记录。人脑派更符合统计意义：既然99%的东西是无用的，那还不如把记录的时间省了，用于重复加深记忆或者吸收新的内容。

关于两种哲学，以后再说吧，我现在讲究的是要做记录，但是尽量从简。上学期上徐雷的机器学习课，印象比较深刻的是他引用阴阳思想中的“阴以简藏”，就是不断抽丝剥茧，提取本质，而人脑只记录最精炼的部分——好比定义和公理。个人经验也是如此。刚来的时候，看paper极为细致，在pdf里面进行批注。后来发现这些批注很难用上，而且搜索起来很困难。大部分重翻一篇paper的时候，你想要的不是它有什么具体的bug，反而是他大概讲了什么。所以你看到附件中有说写“abstract”和“review”，跟bibtex的数据放在一起的，这样的信息对以后更有意义。你可以根据自己能接受的粒度来决定记录到什么程度。喜欢多读少记的，也许的就一个excel表格，记录文档基本信息，一句话备注。喜欢多记点的话，也许可以分到章节。……还有，不一定只记录已经习得的内容，记录不懂的内容也很重要。遇到不懂的先记录下来，避免主线的中断，用外部工具帮你buffer住，这样减轻头脑负担。主线完成后，再来细化。当然，有些核心知识，绕不过的。前一两次提到就先buffer了，后来发现接二连三地出现，于是中断一下，去把它的大意搞清楚。弄懂了大意尽快回来，不要走太远。

## 附件

### --Attachment 1: Pass definition (Sept 2011)--

   * Pass0. This is the initial state. Every paper begins at pass0. At this stage, I've already examined the title, publisher, author, etc. (possibly abstract) This is to make sure things put into this library is closely related to my current research, or I simply have interest in the paper, expecting to be inspired by ideas from inter-disciplinary subjects.
      - **TIME**:5 minutes
      - **ACT**:put in database
   * Pass1. Abstract, introduction/background , conclusion, reference are examined. Notice that I include "introduction" in this round. At this stage of my research career, I'm not fully able to extract enough information from abstract and conclusion. Even some terminology would stuck me there. By examing the introduction or background, I can figure out the precedings of this paper. Then I can decide to start pass2 right away, or come back later.
      - **TIME**:30 min - 2 hour
      - **ACT**:write "abstract" section
   * Pass2. Full text except for detailed deductions. This time, I could understand the problem, its formulation, and outcome. I'll also sweep off terminology issues in this round. If luckily enough, this paper would finish here. Usually, I need to search for more relevant materials to get a better understanding. While reading, I may try to conclude its main methodology and contributions. BTW, I could propose some drawbacks or future improvements.
      - **TIME**:5-10 hour
      - **ACT**:write "review" section
   * Pass3. This time I try to challenge this paper. Before I set out, I'll gurantee I've read most of its precedings. Then I could start the work based on the same assumptions. This reconstruction and challenge process make me fully understand the problem.
      - **TIME**:depends
      - **ACT**:refined review 
