#!/usr/bin/env python

import socket
import time
import sys
import os 

activeChildren = []

def Now():
    #
    return time.ctime(time.time())

def ReapChildren():
    #
    while(activeChildren):
        #
        pid,status = os.waitpid(0, os.WNOHANG)
        #
        if(not pid):
            #
            break
            #
        activeChildren.remove(pid)

def HandleClient(connection):
    #
    time.sleep(5)
    #
    while(True):
        #
        data = connection.rev(1024)
        #
        if(not data):
            #
            break
            #
        reply = "[*] Transmission-> %s @ %s " % (data,Now())
        #
        connection.send(reply)
        #
        connection.close()
        #
        os._exit(0)

def Dispatcher():
    #
    while(True):
        #
        connection,address = s.accept()
        #
        print("[*] Connection from: ", address, " at ", Now())
        #
        ReapChildren()
        #
        childPid = os.fork()
        #
        if(childPid == 0):
            #
            HandleClient(connection)
            #
        else:
            #
            activeChildren.append(childPid)


host = '127.0.0.1'
#
port = 4444
#
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
s.bind((host,port))
#
s.listen(3)
#
Dispatcher()