#!/usr/bin/env python3

import threading
import platform
import socket
import sys
import os

# adapted from Python Penetration for Developers - Duffy et al # 

# Threaded OS Based Ping Sweep #

print("<-- Threaded OS Ping Sweep --> ")
#
net = input("[+] Enter the netwok address-> ")
#
net_segments = net.split('.')
#
join_char = '.'
#
network = net_segments[0]+join_char+net_segments[1]+join_char+net_segments[2]+join_char
#
st1 = int(input("[+] Enter the starting host-> "))
#
en1 = int(input("[+] Enter the last host-> "))
#
op_sys = platform.system()
#
if(op_sys == "Windows"):
    #
    cmd = "ping -n 1 "
    #
elif(op_sys == "Linux"):
    #
    cmd = "ping -c 1 "
    #
class MyThread(threading.Thread):
    #
    def __init__(self,st,en):
        #
        threading.Thread.__init__(self)
        #
        self.st = st
        #
        self.en = en
        #
    def run(self):
        #
        run_one(self.st,self.en)

def run_one(st1,en1):
    #
    for i in range(int(st1),int(en1)):
        #
        host = network+str(i)
        #
        tx = cmd+host
        #
        rx = os.popen(tx)
        #
        for line in rx.readlines():
            #
            if(line.count("ttl")):
                #
                print("[*] Host alive at-> %s " % host)
                #
total_hosts = en1-st1
#
tn = 20
#
total_thread = total_hosts / tn
#
total_thread = total_thread+1
#
threads = []
#
try:
    #
    for i in range(0,int(total_thread)):
        #
        en = st1+tn
        #
        if(en > en1):
            #
            en = en1
            #
        thread = MyThread(st1,en)
        #
        thread.start()
        #
        threads.append(thread)
        #
        st1 = en
        #
except:
     #
     print("[!] Error: failed to start thread ")
     #
print("[+] Threads Active: ", threading.activeCount())
#
for t in threads:
    #
    t.join()
