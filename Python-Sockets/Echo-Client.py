#!/usr/bin/env python

import socket
import sys

def main():
    #
    message = b"[+] Testing Connection [+]"
    #
    host = input("[+] Enter the server IP-> ")
    #
    port = int(input("[+] Enter the port-> "))
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    print("[*] Attempting connection to: %s|%i " % (host,port))
    #
    s.connect((host,port))
    #
    for m in message:
        #
        s.send(m)
        #
        data = s.recv(1024)
        #
        print("[*] Received: ", data)
        #
    s.close()

if(__name__ == '__main__'):
    #
    main()
