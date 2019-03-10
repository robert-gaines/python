#!/usr/bin/env python3

# Basic UDP Client Program #

import socket

def main():
    #
    print("<-- UDP Client Program -->")
    #
    subject_host = input("[+] Enter the host address-> ")
    #
    subject_host_port = input("[+] Enter the host's port-> ")
    #
    message = input("[+] Enter a message-> ")
    #
    message = message.encode('utf-8')
    #
    address = (subject_host, int(subject_host_port))
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    s.sendto(message,address)
    #
    data, rx_address = s.recvfrom(4096)
    #
    if(data):
        #
        print("[+] Received-> ", data)
        #
    s.close()

if(__name__ == '__main__'):
    #
    main()
