---
group: blog
layout: post
title: GitHub "Suffered DDOS" in Januray 2013 from A Railway Ticket Booking Plugin -- A Review
language: en
category: 
mathjax: false
tags: ["GitHub", "DDOS", "12306", "ticket", "plugin", "railway", "China", "Spring Festival"]
---

## Review

I'm trying to review one event happened in January 2013.
One 12306 ticket booking plugin [3] "brought down" the service of GitHub. 

I double quote the "brought down" because I was not aware of the accident until several hours later. 
I heard the expression from SinaWeibo and some other news reports, e.g. [2]. 
There are also some reports in foreign language but this even is most influential within mainland China.
One reason is the followup accident that GitHub was blocked by the GFW [1]. 
People have conjectured that the 1306 accident was a cause for the blocking [1].
A simple Google search will mostly return results like [1]. 
Apparently, people have more interest in the GFW blocking event.
However, I'm really interested in the scale and influence of that "DDOS" attack from the plugin.

After a preliminary search, I can not find more details. 
The only thing that every source agrees is that the "DDOS" happened on Jan 15, 2013. 
I wanted a "timeline" showing when do what happen and clear descriptions of the statuses.
[5] is said to contain such a "timeline"
(some posted a [Chinese version](http://weibo.com/1743629872/zeDCkiTxM) on SinaWeibo). 
However, that post is just copied from the issue tracker of [4]. 
I have impression on that issue because I visited there on that day. 
However, [4] seems to have been reset. 
We can not see issues there now, so [5] has some contributions in backing up this important issue. 
The time when "@jnewland" opened that issue can be a good reference of the discovery time. 
Unfortunately, GitHub now presents parsed time (for better human readability). 
We can only get "one day ago" instead of the exact time. 

The first and most official source is of course the status log of GitHub itself [6].
Since the event is happend on our Jan 15, we have to check both 2013-01-15 and 2013-01-16:

> January 16, 2013
> 
> **10:24 UTC** Everything operating normally.
> 
> **9:50 UTC** We are working to resolve issues with a couple of fileserver clusters. Only a small number of users will be affected.
> 
> **9:19 UTC** We are investigating issues with a fileserver cluster.
> 
> **0:52 UTC** Everything operating normally.
>
> -------
> 
> January 15, 2013
> 
> **23:55 UTC** Our upstream provider has confirmed that they will be performing maintenance at 4pm Pacific Time to attempt to mitigate this issue. There may be a brief moment of high latency or packet loss at the top of the hour. We will update again once we have confirmation the maintenance has been completed.
> 
> **23:31 UTC** Upstream network connectivity issues continue to affect GitHub access for a small percentage of users. Weve received notification that one of our upstream network providers will be performing emergency maintenance on malfunctioning device to attempt to resolve this later today. Well update again when we have more information.
> 
> **20:26 UTC** We are continuing to work with providers to diagnose and solve upstream network connectivity issues. We apologize for any inconvenience caused.
> 
> **18:19 UTC** Some users may be experiencing issues accessing GitHub due to packet loss within an upstream providers network. We are attempting to mitigate this issue.
> 
> **12:13 UTC** Performance has recovered and queues cleared. Please contact support@github.com if you are still experiencing any problems.
> 
> **11:52 UTC** Weve identified and blocked several misbehaving API applications. Service and performance are recovering.
> 
> **10:42 UTC** Temporarily throttling api.github.com and raw.github.com traffic to mitigate extremely high loads caused by some misbehaving software.
> 
> **8:52 UTC** Network performance is impacted due to a significant increase in traffic. Working towards a resolution.

It seems to me the only relevant statements are the last four lines. 
The accident description is in orange and the expression is:
"Network performance is impacted due to a significant increase in traffic".
If you compare it to the statement of [2013-06-12](https://status.github.com/messages/2013-06-12), 
the 2013-01-15 accident does not look like a serious one...

To further confirm whether the "bring down" used by Chinese netizen refers to 
the "performance is impacted" used by GitHub, 
we have to determine the report time. 
SinaWeibo may be a good source. 
From my running instance of 
[SNSRouter](https://github.com/hupili/sns-router)
, I can get some result from the DB:

```
sqlite> select username,time,text from msg where text like '%github%' and text like '%12306%';
...
snsapi_test|1358254877|上面灌水的大多也没看 //@连城404: 发这条微博的时候没有仔细考据，冤枉12306了。虽然12306也脱不开干系，但直接将GitHub拖挂的是抢票助手12306_ticket_helper http://t.cn/zjg6Fbz 恳请 @Fenng || @unknown : 抱歉，此微博已被作者删除。查看帮助：http://t.cn/zWSudZc
```

"@连城404" looks like an early reporter of this event. 
The time I forwarded is "Tue Jan 15 21:01:17 HKT 2013". 
It is about 13:00 UTC. 
From GitHub's log, the issue was already resolved.
Unfortunately, when my SNSRouter fetched (a 5 min gap by default) this message, the original post was deleted. 
From the user's Weibo timeline, we can find the rest earliest [message](http://weibo.com/1883627565/zeBCqlURP).
The posting time is 19:12 (UTC 11:12) -- before the "resolution" status update from GitHub.
Now the times are aligned. 

During the writing, I found the advanced search of SinaWeibo is also a good source. 
See the [results](http://s.weibo.com/weibo/github&timescope=custom:2013-01-15-17:2013-01-15-18&nodup=1)
in the first hour when the event was discovered by GitHub.
My impression is the same. 
It looks like most people are just talking according to "@jnewland"'s issue post. 
Only a few SinaWeibo users mentioned "slow".
One [early post](http://weibo.com/1686211971/zeAYQhQTn) was found. 
According to the timestamps, it seems to me:

   * "8:52 UTCNetwork performance is impacted"
   * Soon after that "@jnewland" wrote to "12306.cn" and filed an issue. 
   * Many "developers" flood that issue to leave troll comments
   and forward the link of that issue to SinaWeibo, 
   which become the roots of larger cascades of forwarding.

My question now is:
**Can anyone provide a record of the real influence**? 
e.g. GitHub is very slow (how slow?) at that time. 
e.g. Can not visit GitHub in mainland China during at time. 
e.g. ... whatever description for the **influence**.
I think I was using GitHub those days but I did not have any impression of the "outage/ denial of service".
Did I missed something?

## Conclusions and Remarks

According to the current information at hand:

   * GitHub received tremendous traffic at that time
   but the volume of this traffic is not large enough to be a (hazardous) "DDOS". 
   * The reaction of "@jnewland" makes people think that this is a hazardous accident.
   * Someone coined the term "DDOS" because of the form:
   many bots request some URLs from different locations.
   This is techincally correct but makes people think of "bring down" or "outage" of services.
   "@jnewland"'s issue post appeared as evidence for someone.
   * According to so many troll comments in the issue ticket, 
   we know that most people are simply trying to amplify the event before studying the real cause.
   * Netizens on SinaWeibo amplified the event to another order of magnitude.
   There are even many false statements saying "12306 brings down GitHub", 
   which are juicy and receives a lot attention. 
   * Try different keyword combinations on Google for this event. 
   You will most probably get the discussion of GFW blocking happened a few days later.
   What does it mean? 
   It seems "bring down" happened only for Chinese world but not English world?
   * All the evidence shows that I'm pursuing one accident that "did not exist".
   i.e. the service was not ever "brought down";
   they just received a lot abnormal traffic;
   the forwarding of Chinese netizens made it a serious case;
   no one in other regions of the world cared about or noticed it.

## Reference

   * [1] GreatFire, Jan 2013, "The Block of GitHub in Mainland China", <https://zh.greatfire.org/blog/2013/jan/github-blocked-china-how-it-happened-how-get-around-it-and-where-it-will-take-us>
   * [2] Sina News, Jan 2013, "12306 Ticket Booking Plugin Bring Down GitHub", <http://tech.sina.com.cn/i/csj/2013-01-16/19367984516.shtml>
   * [3] 12306 Ticket Helper Official Page, <http://www.fishlee.net/soft/44/>
   * [4] 12306 Ticket Helper GitHub repo, <https://github.com/iccfish/12306_ticket_helper>
   * [5] OSChina, Jan 2013, Event Log of 12306 Ticket Helper and GitHub, <http://my.oschina.net/jiuxiaoyao/blog/102455> 
   * [6] GitHub, Status of 2013-01-16, <https://status.github.com/messages/2013-01-16>

## Epilogue

I care the real influence because I want to cite this event in one formal document. 
To my suprise, I can not find any rigorous record or review of this event on the Internet.
I have no choice but to compose a citable object myself using this blog.

This post is still under construction. 
If you have any evidence, please inform me.
