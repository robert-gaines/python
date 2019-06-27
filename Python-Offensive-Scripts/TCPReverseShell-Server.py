#!/usr/bin/env python

import socket

def Connect():
    #
    host = '127.0.0.1' ; port = 4444
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
    #
    s.bind((host,port))
    #
    s.listen(1)
    #
    print("[*] Listening on: %s:%i ..." % (host,port))
    #
    connection,address = s.accept()
    #
    print("[*] Connection from: %s " % str(address))
    #
    while(True):
        #
        command = input("[*]>>> ")
        #
        if('exit' in command):
            #
            connection.send('exit'.encode())
            #
            connection.close()
            #
        else:
            #
            connection.send(command.encode())
            #
            print(connection.recv(1024).decode())

def main():
    #
    Connect()

if(__name__ == '__main__'):
    #
    main()
