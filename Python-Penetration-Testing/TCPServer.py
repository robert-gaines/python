#!/usr/bin/env python3

import threading
import socket
import sys

def HandleClient(s):
    #
    request = s.recv(1024)
    #
    print("[*] Received: %s " % request)
    #
    s.send(b"[*] Connection Acknowledged ")
    #
    s.close()

def main():
    #
    print("<-- TCP Server -->")
    #
    bind_addr = "0.0.0.0"
    #
    print("[+] Server set to %s " % bind_addr)
    #
    bind_port = int(input("[+] Enter the port-> "))
    #
    addr = (bind_addr, bind_port)
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    try:
        #
        print("[+] Binding socket to: ", addr)
        #
        s.bind(addr)
        #
        print("[*] Listening on-> ", addr)
        #
        s.listen(5)
        #
    except socket.error:
        #
        print("[+] Bind process failed ")
        #
        sys.exit(0)
        #
    while(True):
        #
        c,a = s.accept()
        #
        print("[*] Connection from: %s:%d " % (addr[0],addr[1]))
        #
        handler = threading.Thread(target=HandleClient,args=(c,))
        #
        handler.start()

if(__name__ == '__main__'):
    #
    main()
