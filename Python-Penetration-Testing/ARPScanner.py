#!/usr/bin/env python3

import scapy.all as scapy
import time

def ARPScan(target):
    #
    request = scapy.ARP(pdst=target)
    #
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #
    broadcast_and_request = broadcast/request
    #
    print(broadcast_and_request.summary())
    #
    #broadcast_and_request.show()
    #


def main():
    #
    print("<-- ARP Scanner -->")
    #
    target = input("[+] Enter the target or target subnet-> ")
    #
    ARPScan(target)

if(__name__ == '__main__'):
    #
    main()
