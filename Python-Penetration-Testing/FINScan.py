#!/usr/bin/env python3

from scapy.all import *

def main():
    #
    print("<-- FIN Scan -->")
    #
    print()
    #
    source_ip_addr = input("[+] Source IP Address-> ")
    #
    destination_ip_address = input("[+] Destination IP Address-> ")
    #
    destination_port = int(input("[+] Destination port-> "))
    #
    ip_header = IP(src=source_ip_addr,dst=destination_ip_address)
    #
    transport_header = TCP(sport=1024, dport=destination_port, flags="F", seq=12345)
    #
    pkt = ip_header/transport_header
    #
    p = sr1(pkt,verbose=False)
    #
    p.show()

if(__name__ == '__main__'):
    #
    main()
