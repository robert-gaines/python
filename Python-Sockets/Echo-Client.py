#!/usr/bin/env python3

import socket

def main():
    #
    print("<-- TCP Echo Client -->")
    #
    server = input("[+] Enter the server address-> ")
    #
    port = int(input("[+] Enter the server port-> "))
    #
    message = input("[+] Enter a message-> ")
    #
    message = str.encode(message)
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    server_addr = (server,port)
    #
    s.connect(server_addr)
    #
    s.send(message)
    #
    data = s.recv(1024)
    #
    print("[+] Client received: %s" % data)
    #
    s.close()

if(__name__ == '__main__'):
    #
    main()
