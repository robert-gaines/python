#!/usr/bin/env python3

_AUTH_ = 'RWG'

from scapy.arch.windows import get_windows_if_list
from scapy.all import *
import datetime
import psutil
import time
import sys

class LightIDS():
    #
    def __init__(self,interface,ruleSet,addr):
        #
        self.interface = interface
        #
        self.ruleSet = ruleSet 
        #
        self.addr = addr
        #
        return
        #
    def ParsePacket(self,pkt):
        #
        # print(self.ruleSet)
        #
        try:
            #
            if(pkt):
                #
                if(len(ruleSet) == 0):
                    #
                    #print(pkt)
                    #
                    if('IP' in pkt):
                        #
                        destination = pkt[IP].dst
                        #
                        try:
                            #
                            if(destination == addr):
                                #
                                print(destination)
                                #
                        except:
                            #
                            print("[!] Packet Processing Failure [!]")
                            #
                else:
                    #
                    print("Packet Received")
                    #
        except:
            #
            pass
            #
    def Run(self):
        #
        sniff(filter="",store=False,iface=r'%s'%self.interface,prn=self.ParsePacket)

def PopulateRuleSet():
    #
    def PopulatePortList():
        #
        print("[*] List will consist of integer port values...") ; time.sleep(1)
        #
        sentinel = ""
        #
        while(sentinel is not 'Q' or sentinel is not 'q'):
            #
            port = input("[+] Enter a port number or (Q/q) to exit-> ")
            #
            if(port is 'q' or port is 'Q'):
                #
                break
                #
            port = int(port) ; ruleSet.append(port)
            #
    def PopulateIPPortList():
        #
        print("[*] Rule Format: <IP> <PORT>") ; time.sleep(1)
        #
        print("[*] Default direction is inbound for this HIDS...") ; time.sleep(1)
        #
        ip = ""; port = ""
        #
        while(ip is not 'Q' or ip is not 'q'):
            #
            ip = input("[+] Enter an IPv4 address or (Q/q) to exit-> ")
            #
            if(ip is 'q' or ip is 'Q'):
                #
                break
                #
            port = input("[+] Enter a port number-> ")
            #
            port = int(port) ; ruleSet.append([ip,port])
            #
            print("[*] Added: %s:%s " % (ip,port))
            #
    print("""
    Rule Set Options
    ----------------
    1) Port List 
    2) IP/Port
    3) Any
          """)
    #
    selection = int(input("[+] Selection-> "))
    #
    populatedRules = []
    #
    if(selection is 1):
        populatedRules.append(PopulatePortList())
    elif(selection is 2):
        populatedRules.append(PopulateIPPortList())
    else:
        populatedRules = None
        #
    return populatedRules
        
if(__name__ == '__main__'):
    #
    ruleSet = []
    #
    def RunDetection(activeInterface,ruleSet,addr):
        #
        L = LightIDS(activeInterface,ruleSet,addr)
        #
        L.Run()
    #
    print("<<< Lightweight IDS >>>")
    #
    time.sleep(1)
    #
    print("[*] Collecting interface data...") ; time.sleep(1)
    #
    interfaces = get_windows_if_list()
    #
    print("<<< Network Interfaces >>>")
    #
    print("--------------------------")
    #
    for i in range(0,len(interfaces)):
        #
        print(i,')',interfaces[i]['name'])
        #
    interface = int(input("[+] Enter the interface index-> "))
    #
    print("[*] Selected: %s " % interfaces[interface]['name'])
    #
    activeInterface = interfaces[interface]['name']
    #
    addrs = psutil.net_if_addrs()
    #
    addr = addrs[activeInterface][1][1]
    #
    print("[*] Interface address-> %s " % addr)
    #
    time.sleep(3)
    #
    while(True):
        #
        print("<<< Menu >>>")
        #
        print("------------")
        #
        print("""
        1) Populate Rule Set
        2) Run Detection
        3) Exit
            """)
        #
        option = int(input("[+] Selection-> "))
        #
        if(option is 1):
            PopulateRuleSet()
        elif(option is 2):
            RunDetection(activeInterface,ruleSet,addr)
        else:
            sys.exit(0)

