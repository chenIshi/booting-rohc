#! /usr/bin/env python3

from scapy.all import sr1, IP, ICMP

pingr = IP(src="192.168.7.1", dst="192.168.8.1")/ICMP()

num_of_failures = 0

for i in range(10):
    pingr[ICMP].seq = i
    res = sr1(pingr, timeout=2)
    if res is None:
        num_of_failures += 1

print(str(num_of_failures) + " out of 10 packets failed!")

