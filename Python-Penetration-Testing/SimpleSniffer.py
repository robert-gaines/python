#!/usr/bin/env python3

import binascii
import socket
import struct
import time
import sys
import os

def CheckUser():
    #
    user = os.geteuid()
    #
    print("[*] User: ", user)
    #
    if(user == 0):
        #
        print("[*] User is root, Proceed ")
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
    CheckUser()
    #
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    #
    while(True):
        #
        packet = s.recvfrom(2048)
        #
        ethernet_head = packet[0][0:14]
        #
        ethernet = struct.unpack("!6s6s2s",ethernet_head)
        #
        print("[*] -- Ethernet Frame -- [*]")
        #
        print("[*] -- Destination MAC: ", binascii.hexlify(ethernet[0]))
        #
        print("[*] -- Source MAC: ", binascii.hexlify(ethernet[1]))
        #
        header = packet[0][14:34]
        #
        ip_header = struct.unpack("!12s4s4s",header)
        #
        print("[*] -- IP -- [*]")
        #
        print("[*] -- Source IP: ", socket.inet_ntoa(ip_header[1]))
        #
        print("[*] -- Destination IP: ", socket.inet_ntoa(ip_header[2]))
        #
        print("[*] -- TCP -- [*]")
        #
        tcp_header = packet[0][34:54]
        #
        tcp_unpacked = struct.unpack("!HH9ss6s",tcp_header)
        #
        print("[*] Source Port: ", tcp_unpacked[0])
        #
        print("[*] Destination Port: ", tcp_unpacked[1])
        #
        print("[*] Flag ", binascii.hexlify(tcp_unpacked[3]))

if(__name__ == '__main__'):
    #
    main()
