#!/usr/bin/env python

import socket

def main():
    #
    host = input("[+] Enter the host IP-> ")
    #
    port = int(input("[+] Enter the server port-> "))
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    msg = b"[*] Hello server! "
    #
    s.connect((host,port))
    #
    s.send(msg)
    #
    data = s.recv(4096)
    #
    if(data):
        #
        print("[*] Received data-> ", data)
        #
    s.close()

if(__name__ == '__main__'):
    #
    main()