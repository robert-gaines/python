#!/usr/bin/env python

import socket
import sys

def main():
    #
    host = "127.0.0.1"
    #
    port = 4444
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    s.bind((host,port))
    #
    s.listen(3)
    #
    msg = b"[*] Connection acknowledged..."
    #
    while(True):
        #
        conn, addr = s.accept()
        #
        print("[*] Connection from: ", addr)
        #
        while(True):
            #
            data = conn.recv(4096)
            #
            conn.send(msg)
            #
            print("[*] Received data-> ", data)
            #
            if(not data):
                #
                break
                #
        conn.close()

if(__name__ == '__main__'):
    #
    main()