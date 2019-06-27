#!/usr/bin/env python

import socket
import random
import sys

def main():
    #
    host = '0.0.0.0'
    #
    port = random.randint(1024,65536)
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    print("[*] Binding: %s|%i " % (host,port))
    #
    s.bind((host,port))
    #
    s.listen(3)
    #
    while(True):
        #
        connection,address = s.accept()
        #
        print("[+] Connection from-> ", address)
        #
        while(True):
            #
            data = connection.recv(1024)
            #
            if(not data): 
                #
                break
                #
            connection.send(b"[*] Echo -> "+data)
            #
        connection.close()

if(__name__ == "__main__"):
    #
    main()