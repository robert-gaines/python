#!/usr/bin/env python

import _thread as thread 
import socket
import time
import sys 
import os

blockSize = 1024 
defaultHost = '127.0.0.1'
defaultPort = 4444

helpText = """
            server-> FTPServer.py -mode server [-port n] [-host h]
            client-> FTPServer.py -mode client -file [f] [-port n] [-host h]
           """

def Now():
    #
    return time.asctime()

def parseCommandLine():
    #
    d = {}
    #
    args = sys.argv[1:]
    #
    while(len(args) >= 2):
        #
        d[args[0]] = args[1]
        #
        args = args[2:]
        #
    return d

def Client(host,port,filename):
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    s.connect((host,port))
    #
    s.send((filename+'\n').encode())
    #
    depositDirectory = os.path.split(filename)[1]
    #
    fileObject = open(depositDirectory,'wb')
    #
    while(True):
        #
        data = s.recv(blockSize)
        #
        if(not data):
            #
            break
            #
        fileObject.write(data)
        #
    s.close()
    #
    fileObject.close()
    #
    print("[+] Received ", filename, ' at ', Now())

def serverThread(clientSocket):
    #
    s = clientSocket.makefile('r')
    #
    fileName = s.readline()[:-1]
    #
    try:
        #
        fileObject = open(fileName,'rb')
        #
        while(True):
            #
            bytes = fileObject.read(blockSize)
            #
            if(not bytes):
                #
                break
                #
            sent = clientSocket.send(bytes)
            #
            assert sent == len(bytes)
            #
    except:
        #
        print("[!] Error during download operation [!]")
        #
    clientSocket.close()

def Server(host,port):
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    s.bind((host,port))
    #
    s.listen(5)
    #
    while(True):
        #
        clientSocket,clientAddr = s.accept()
        #
        print("[*] Connection to server from-> ", clientAddr, ' at ', Now())
        #
        thread.start_new_thread(serverThread,(clientSocket,))

def main(args):
    #
    host = args.get('-host',defaultHost)
    #
    port = int(args.get('-port',defaultPort))
    #
    if(args.get('-mode')=='server'):
        #
        if(host == 'localhost'):
            #
            host = ''
            #
            Server(host,port)
            #
        elif(args.get('-file')):
            #
            Client(host,port,args['-file'])
            #
        else:
            #
            print(helpText)

if(__name__ == '__main__'):
    #
    args = parseCommandLine()
    #
    main(args)    


