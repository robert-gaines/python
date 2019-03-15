#!/usr/bin/env python3

import socket
import sys
import os

def CheckUser():
    #
    print("[~] Checking User ")
    #
    user = os.geteuid()
    #
    print("[+] User ", user)
    #
    if(user == 0):
        #
        print("[*] User is root, continue ")
        #
        return
        #
    else:
        #
        print("[!] User is not root, exit ")
        #
        sys.exit()

def main():
    #
    print('''
            <-- Crafted Packet Transmission -->
          ''')
    #
    CheckUser()
    #
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    #
    # Consult /usr/include/linux/if_ether.h -> for protocol codes
    #
    s.bind(("eth0",socket.htons(0x0800)))
    #
    source = '\x00\x0c\x29\x4f\x8e\x35'
    #
    destination = '\x00\x0c\x29\x2E\x84\x7A'
    #
    code = '\x08\x00'
    #
    ethernet_packet = str.encode(destination+source+code)
    #
    try:
        #
        s.send(ethernet_packet)
        #
        print("[*] Packet Sent ")
        #
    except:
        #
        sys.exit("[!] Transmission Failed ")

if(__name__=='__main__'):
    #
    main()
