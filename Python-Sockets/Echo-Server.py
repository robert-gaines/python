#!/usr/bin/env python3

import socket
import random

def main():
    #
    print("<-- TCP Echo Server -->")
    #
    host = '127.0.0.1'
    #
    port = random.randint(1024,65535)
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    server_addr = (host,port)
    #
    s.bind(server_addr)
    #
    s.listen(5)
    #
    print("[*] Serving on: %s:%s " % (host,port))
    #
    while(True):
        #
        connection, address = s.accept()
        #
        if(connection):
            #
            print("[*] Connection from-> ", address)
            #
            while(True):
                #
                data = connection.recv(1024)
                #
                if(not data): break
                    #
                if(data):
                    #
                    print("[*] Host sends -> " ,data)
                    #
                connection.send(b'[*] Echo-> %s ' % data)
                #
        connection.close()

if(__name__ == '__main__'):
    #
    main()