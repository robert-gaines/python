#!/usr/bin/env python3

from scapy.all import *
import subprocess
import time

def ARPMonitor(packet):
    #
    if ARP in packet and packet[ARP].op in (1,2):
        #
        return packet.sprintf("%ARP.psrc% %ARP.hwsrc%")

def main():
    #
    print("<-- ARP Monitor -->")
    #
    print()
    #
    print("[*] Host : MAC")
    #
    print("----------------------------")
    sniff(prn=ARPMonitor, filter='arp', store=0)

if(__name__ == '__main__'):
    #
    main()
