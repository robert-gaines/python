#!/usr/bin/env python3

import random
import socket
import time
import sys 
import os 

def CullChildProcess(ActiveChildProcesses):
    #
    while(ActiveChildProcesses):
        #
        pid,stat = os.waitpid(0, os.WNOHANG)
        #
        if(not pid): break 
        #
        ActiveChildProcesses.remove(pid)

def HandleClientConnection(connection):
    #
    time.sleep(3)
    #
    while(True):
        #
        data = connection.recv(1024)
        #
        if(not data): break 
        #
        reply = "[+] Echo-> %s at %s " % (data,time.ctime(time.time()))
        #
        connection.send(reply.encode())
        #
    connection.close()
    #
    os._exit(0)

def main():
    #
    print("<-- Forked Server -->")
    #
    host = '127.0.0.1'
    #
    port = random.randint(1024,65535)
    #
    address = (host,port)
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    try:
        #
        s.bind(address)
        #
    except Exception as e:
        #
        print("[!] Bind operation failed, error-> ", e)
        #
    s.listen(5)
    #
    print("[*] Serving on %s:%i" % (host,port))
    #
    ActiveChildProcesses = []
    #
    while(True):
        #
        connection, address = s.accept()
        #
        print("[*] Connection from-> ", address,' @ ', time.ctime(time.time()))
        #
        CullChildProcess(ActiveChildProcesses)
        #
        SubordinatePid = os.fork()
        #
        if(SubordinatePid == 0):
            #
            HandleClientConnection(connection)
            #
        else:
            #
            ActiveChildProcesses.append(SubordinatePid)
        
if(__name__ == '__main__'):
    #
    main()



