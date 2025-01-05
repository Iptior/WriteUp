# NETWORK - Day 02 - Wrapped Packet

## Description

<img align="center" src="screens/01-Description.png" alt="Description of the challenge" />

We have 1 network file (PCAP) to analyze.

## Wireshark

In first, i search in conversations statistics because it's an exfiltration.

<img align="center" src="screens/02-Conversations.png" alt="Conversations in wireshark interface" />

But exchanges are in HTTPS, encrypted packets, so i swap my technique.
Let's see DNS traffic !

<img align="center" src="screens/03-DNS.png" alt="DNS traffic" />

Why root-me is in request DNS?
I investigate about the IP...

<img align="center" src="screens/04-IP-info-212.png" alt="IP info" />

2 protocoles : SSH and ICMP, one is encrypted, the other not.

<img align="center" src="screens/05-ICMP-packet.png" alt="ICMP packet" />

Some data is present in this ICMP packet.

## Extraction of data 

I use tshark and this command line (filter on ICMP protocol and the destination IP is the root-me IP):

```tshark.exe" -r chall.pcapng -Y "icmp && ip.dst == 212.129.38.224" -T fields -e data.data```

To work on data, i use cyberchef.

<img align="center" src="screens/06-Cyberchef.png" alt="CyberChef" />



## The Flag 

I concatenated the date and found the flag:

<img align="center" src="screens/07-Flag.png" alt="Flag" />

*RM{M3rry_Chr1stM4s_R00T-M3}*

