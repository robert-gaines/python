#!/usr/bin/env python3

import socket

def main():
    #
    print("<-- Banner Grabber -->")
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    url = input("[+] Enter the URL-> ")
    #
    port = int(input("[+] Enter the port-> "))
    #
    get_request = bytes('GET / HTTP/1.1\nHost:'+url+'\n\n','utf-8')
    #
    try:
        s.connect((url,port))
        #
    except:
        #
        sys.exit("[!] Connection failed ")
        #
    intake = ''
    #
    s.send(get_request)
    #
    print(s.recv(4096))
    #
    print(intake)
    #
    s.close()

if(__name__ == '__main__'):
    #
    main()
