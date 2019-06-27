#!/usr/bin/env python 

import _thread as thread 
import socket
import time
import sys 

host = '127.0.0.1'
#
port = 4444
#
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
try:
    s.bind((host,port))
except:
    sys.exit("[!] Error [!]")
    #
s.listen(3)

def Now():
    #
    return time.ctime(time.time())

def HandleClient(connection):
    #
    time.sleep(5)
    #
    while(True):
        #
        data = connection.recv(1024)
        #
        if(not data):
            #
            break
            #
        reply = "[*] Connection acknowledged at-> %s " % Now()
        #
        connection.send(reply.encode())
        #
    connection.close()

def Dispatcher():
    #
    while(True):
        #
        connection, address = s.accept()
        #
        print("[*] Connection from: ", address, " at ", Now())
        #
        thread.start_new_thread(HandleClient, (connection,))

Dispatcher()