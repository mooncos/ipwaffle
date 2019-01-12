#!/bin/bash

iptables -I INPUT -p udp --dport 111 -j REJECT
iptables -I INPUT -p tcp --dport 111 -j REJECT
iptables -I INPUT -p udp --dport 932 -j REJECT
iptables -I INPUT -p tcp --dport 932 -j REJECT
iptables -I INPUT -p udp --dport 3128 -j REJECT
iptables -I INPUT -p tcp --dport 3128 -j REJECT

iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 80 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 80 -j DNAT --to 192.168.1.4:80
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 8663 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 8663 -j DNAT --to 192.168.1.4:8663
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 8443 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 8443 -j DNAT --to 192.168.1.4:8443
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 8000 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 8000 -j DNAT --to 192.168.1.4:8000
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 6998 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 6998 -j DNAT --to 192.168.1.4:6998
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 443 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 443 -j DNAT --to 192.168.1.4:443
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 1337 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 1337 -j DNAT --to 192.168.1.4:1337
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 7331 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 7331 -j DNAT --to 192.168.1.4:7331
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 25 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 25 -j DNAT --to 192.168.1.4:25
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 465 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 465 -j DNAT --to 192.168.1.4:465
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 143 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 143 -j DNAT --to 192.168.1.4:143
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 993 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 993 -j DNAT --to 192.168.1.4:993
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 110 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 110 -j DNAT --to 192.168.1.4:110
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 995 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 995 -j DNAT --to 192.168.1.4:995
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 4190 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 4190 -j DNAT --to 192.168.1.4:4190
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 5555 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 5555 -j DNAT --to 192.168.1.1:5555
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 280 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 280 -j DNAT --to 192.168.1.2:80
iptables -A FORWARD -p tcp -d 5.9.100.11 --dport 28080 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp -d 5.9.100.11 --dport 28080 -j DNAT --to 192.168.1.2:8080
iptables -t nat -L -n