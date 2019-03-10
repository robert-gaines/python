#!/usr/bin/env python3

import socket
import sys

def main():
    #
    subject_host = input("[+] Enter the host address-> ")
    #
    subject_host_port = input("[+] Enter the subject host port-> ")
    #
    message = input("[+] Enter a message-> ")
    #
    message = message.encode('utf-8')
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    address = (subject_host, int(subject_host_port))
    #
    try:
        #
        status = s.connect_ex(address)
        #
        if(status == 0):
            #
            print("[*] Connected to -> ", address)
            #
    except socket.error:
        #
        print("[!] Socket Error ")
        #
        sys.exit(1)
        #
    try:
        #
        print("[+] Sending: %s " % message)
        #
        s.send(message)
        #
    except socket.error:
        #
        print("[!] Message could not be sent ")
        #
        sys.exit(1)
        #
    response = s.recv(4096)
    #
    if(response):
        #
        print("[*] Received: %s " % response)
        #
    else:
        #
        print("[-] No data received  ")
    #
    print("[!] Closing connection ")
    #
    s.close()

if(__name__) == '__main__':
    #
    main()
