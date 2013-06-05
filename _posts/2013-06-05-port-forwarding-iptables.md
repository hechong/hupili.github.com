---
group: blog
layout: post
title: Host/Port Forwarding Using iptables
language: en
category: note
mathjax: false
tags: ["linux", "fedora", "iptables", "port", "host", "forwarding", "nat", "filter", "PREROUTEING", "POSTROUTING", "FORWARD"]
---

## Quick Reference

### Settings

You have two machines `H1` and `H2`. 
You want to forward port `P1` of `H1` to port `P2` of `H2`. 
Use iptables to do it.

### Precaution

The file locations and options are different across systems:

   * `man` before you type.
   * `ls`/`cat` before you write. 

They are just hints for what you should do
(my commands also differs from the reference).

### Allow IP Forwarding

Allow IP forwarding in system.
Possible commands picked from refs [1-3]. 

```
sysctl -w net.ipv4.ip_forward=1
sysctl net.ipv4.ip_forward=1
echo net.ipv4.ip_forward=1 >>/etc/sysctl.conf
echo "1" > /proc/sys/net/ipv4/ip_forward
```

### iptables Notation

Two basic methods to configure iptables:

   1. Use command `iptables xxxx`. 
   This is to interact with the iptables configuration in memeory. 
   2. Use command `iptables-save` to save confs to a file. 
   Edit that file. 
   Use command `iptables-restore` to load confs back to memory. 

I personally like the 2nd way. 
You can choose a file to maintain your iptables, Git it, and leave comments in it.
What's more, next admin will have clues that how you reach this long list of confs.
Don't make others life too hard.
Any file is OK, but I suggest `/etc/sysconfig/iptables`. 
This is default iptables confs that will be loaded at system bootup.

There is one element in iptables you must know before proceed. 
iptables have several "tables": `filter`, `nat`, `mangle`, `raw`. 
We use `filter` and `nat` in this note. 

When you read others' posts on the Internet, 
you will encounter two notations. 
People using the 1st way will arrive at 

```
iptables -t {table} {the rest options}
```

People using the 2nd way will arrive at

```
*{table1}
{the rest options of cmd1-1}
{the rest options of cmd1-2}
...
*{table2}
{the rest options of cmd2-1}
{the rest options of cmd2-2}
...
```

Knowing this alone, you should be able to parse others' notes. 

### Host/Port Forwarding Configuration

The complete `iptables` confs with explanation in comments: 

```
*filter
# Allow forwarding TO {H2}:{P2}
-A FORWARD -d {H2} -p tcp --dport {P2} -j ACCEPT
# Allow forwarding FROM {H2}:{P2}
-A FORWARD -s {H2} -p tcp --sport {P2} -j ACCEPT
# This line was written by the former admins. Prohibit any forwarding by default.
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
*nat
# Use DNAT to modify headers "dHost:dPort" from {H1}:{P1} to {H2}:{P2}
# Note that after modifying the headers, system will find destination 
# is not itself. According to the rule of IP, the system should forward
# it rather than deliver to upper layers. That is why this packet has
# to pass the "FORWARD" chain of "filter" table.
-A PREROUTING -p tcp --dport {P1} -j DNAT --to-destination {H2}:{P2}
# Use MASQUERADE to modify headers "sHost:sPort" to {H2}:{some port}
# If you don't do this, "sHost:sPort" remains the same. {H2}:{P2}
# is able to receive this packet but the protocol fails when it 
# replies to "sHost:sPort". 
-A POSTROUTING -j MASQUERADE
```

### Only Port Forwarding

If you only want to do port forwarding on the same host, things are much easier. 
Just use the following conf. 

```
*nat
-A PREROUTING -p tcp -m tcp --dport {P1} -j REDIRECT --to-ports {P2}
```

Note that you don't have to configure "FORWARD" chain of "filter" table. 
We must distinguish between the "Forwarding" in the section header 
and what the system means by "FORWARD". 
As explained in the comments in the above section, 
the packets should be "forwarded" when the "dHost" is not the current system.
In this section, we only modify "dPort" and "dHost" remains the same. 
In this case, the behaviour of IP layer is to **deliver to upperlayers** 
rather than **forward to another host**.

To be more precise, you still have to configure something in "filter" table. 
When a packet is delivered to upper layer, iptables will filter it through "INPUT" chain. 
You will find something like the followings:

```
*filter
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport {P2} -j ACCEPT
```

I didn't include it in the notes by default, because they are supposed be there before.
Or else, you can not access that port, letting alone forwarding another port to it.
Is it? 

## Exploration

It turns out the references are not complete. 
Some time is spent on analyzing the problem and learning the principle of iptables. 
It's fun. 

   * I get the basics from [1], including `DNAT`, `MASQUERADE`, and `/proc/sys/net/ipv4/ip_forward`
   * [2] hint me that the `FORWARD` chain matters. 
   However, it only specifies the `ACCEPT` for one side (`H1->H2`). 
   * Use `tcpdump host {H1}` to monitor the forwarding result. 
   We find packets do reach H2 but it gets the result
   `11:08:06.868561 IP {H1} > {H2}: ICMP host {H1} unreachable - admin prohibited, length 68`. 
   Check the iptables of H1 and find 
   `-A FORWARD -j REJECT --reject-with icmp-host-prohibited`. 
   That's it. 
   So we should allow forwarding for both `H1->H2` and `H2->H1` in the iptables of H1. 

## Reference

   * [1] <http://www.debuntu.org/how-to-redirecting-network-traffic-to-a-new-ip-using-iptables/>
   * [2] <http://www.linuxquestions.org/questions/linux-networking-3/iptables-forward-port-to-another-host-844467/>
   * [3] <http://ramblings.narrabilis.com/ip-forward-using-iptables-port-and-host-redirect>
