#!/usr/bin/env python3

import socket

def SplitAndRejoin(network,split_char):
    #
    segments = network.split(split_char)
    #
    rejoin_char = split_char
    #
    rejoined = segments[0]+rejoin_char+segments[1]+rejoin_char+segments[2]+rejoin_char
    #
    return rejoined

def ScanHost(addr,port):
    #
    tgt = (addr,port)
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    socket.setdefaulttimeout(1)
    #
    result = s.connect_ex(tgt)
    #
    s.close()
    #
    if(result == 0):
        #
        return 1
        #
    else:
        #
        return 0

def main():
    #
    print("<-- TCP Ping Sweep -->")
    #
    network = input("[+] Enter the network address-> ")
    #
    port = int(input("[+] Enter the scan port-> "))
    #
    truncated = SplitAndRejoin(network,'.')
    #
    for i in range(1,255):
        #
        tgt = truncated+str(i)
        #
        rx = ScanHost(tgt,port)
        #
        if(rx == 1):
            #
            print("[*] Host alive at-> %s " % tgt)

if(__name__ == '__main__'):
    #
    main()
