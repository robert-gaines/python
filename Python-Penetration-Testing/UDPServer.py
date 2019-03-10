#!/usr/bin/env python3

import socket
import sys

def main():
    #
    print("<-- UDP Server -->")
    #
    srv_host = "0.0.0.0"
    #
    srv_port = int(input("[+] Enter the service port-> "))
    #
    addr = (srv_host, srv_port)
    #
    print("[+] Server set to: ", addr )
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    s.bind(addr)
    #
    while(True):
        #
        d,a = s.recvfrom(4096)
        #
        if(d):
            #
            print("[+] Connection from-> ", a)
            #
            print("[+] Received: ", d, " from ", a)
            #
            s.sendto(b"[+] Message Received ", a)

if(__name__ == '__main__'):
    #
    main()
