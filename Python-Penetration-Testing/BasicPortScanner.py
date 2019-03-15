#!/usr/bin/env python3

import subprocess
import socket
import sys

def ScanHost(host,start,finish):
    #
    open_ports = []
    #
    for p in range(int(start),int(finish)):
        #
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #
        socket.setdefaulttimeout(1)
        #
        response = s.connect_ex((host,int(p)))
        #
        if(response == 0):
            #
            open_ports.append(p)
            #
        else:
            #
            continue
            #
        s.close()
        #
    print("[*] Retrieving Open Ports [*]")
    #
    print("-"*29)
    #
    for p in open_ports:
        #
        print("[*] %s : %i" % (host,int(p)))


def main():
    #
    print("<- Basic Port Scanner -->")
    #
    subprocess.call('clear',shell=True)
    #
    subject_host = input("[+] Enter the host IP address-> ")
    #
    starting_port = int(input("[+] Enter the starting port-> "))
    #
    concluding_port = int(input("[+] Enter the last port-> "))
    #
    ScanHost(subject_host,starting_port,concluding_port)

if(__name__ == '__main__'):
    #
    main()
