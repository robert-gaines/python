#!/usr/bin/env python3

import subprocess
import threading
import socket
import time
import sys

subprocess.call('clear',shell=True)

class ThisThread(threading.Thread):
    #
    def __init__(self,threadName,host,begin,end):
        #
        threading.Thread.__init__(self)
        #
        self.threadName = threadName
        #
        self.host = host
        #
        self.begin = begin
        #
        self.end = end
        #
    def run(self):
        #
        ScanHost(self.threadName,self.host,self.begin,self.end)

def ScanHost(threadName,host,start,end):
    #
    try:
        #
        for port in range(int(start),int(end)):
            #
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #
            socket.setdefaulttimeout(1)
            #
            response = s.connect_ex((host,port))
            #
            if(response == 0):
                #
                print("[*] %s : %i " % (host,port))
            #
    except socket.error:
        #
        print("[!] Socket Error ")

print("[*] Threaded TCP Port Scanner [*]")
#
host = input("[+] Enter the subject host IP-> ")
#
start = int(input("[+] Enter the first port-> "))
#
end = int(input("[+] Enter the last port-> "))
#
total_ports = end-start
#
ports_per_thread = 30
#
total_number = total_ports / ports_per_thread

if(total_ports % ports_per_thread != 0):
    #
    total_number = total_number+1
    #
if(total_number > 300):
    #
    ports_per_thread = total_ports / 300
    #
    ports_per_thread = ports_per_thread + 1
    #
    if(total_ports%ports_per_thread != 0):
        #
        total_number = total_number+1
        #
threads = []
#
for i in range(int(total_number)):
    #
    k = i
    #
    end_two = start+ports_per_thread
    #
    thread = ThisThread("T1",host,start,end_two)
    #
    thread.start()
    #
threads.append(thread)
#
end = end_two
#
for t in threads:
    #
    t.join()
