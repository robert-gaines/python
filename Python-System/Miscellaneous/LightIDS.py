#!/usr/bin/env python3

_AUTH_ = 'RWG'

from scapy.arch.windows import get_windows_if_list
from datetime import datetime
from scapy.all import *
import subprocess
import logging
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
        n = datetime.now() ; t = n.strftime("%m:%d:%Y - %H:%M:%S") ; ts = n.strftime("%m_%d_%Y_%H_%M_%S")
        #
        logName = "IDS-"+ts+".log"
        #
        logging.basicConfig(filename=logName,level=logging.INFO)
        #
        try:
            #
            if(pkt):
                #
                if(len(self.ruleSet) == 0):
                    #
                    if('IP' in pkt):
                        #
                        src = pkt[IP].src ; dst = pkt[IP].dst ; destPort = "" ; srcPort = ""
                        #
                        try:
                            #
                            if(pkt.haslayer(TCP)):
                                #
                                destPort = pkt[TCP].dport ; srcPort = pkt[TCP].sport
                                #
                            elif(pkt.haslayer(UDP)):
                                #
                                destPort = pkt[UDP].dport ; srcPort = pkt[UDP].sport
                                #
                            else:
                                #
                                destPort = 0 ; srcPort = 0
                                #
                        except:
                            #
                            pass
                            #
                        try:
                            #
                            if(dst == self.addr):
                                #
                                print("<<<ALERT>>> [%s] Traffic from: %s:%s <<<ALERT>>>" % (t,src,int(destPort)))
                                #
                                logging.info("<<<ALERT>>> [%s] Traffic from: %s:%s <<<ALERT>>>" % (ts,src,int(destPort)))
                                #
                                time.sleep(3)
                                #
                                cls = subprocess.call('cls',shell=True)
                                #
                        except Exception as e:
                            #
                            print("[*] Error: %s " % e)
                            #
                            print("[!] Packet Processing Failure [!]")
                            #
                            time.sleep(1)
                            #
                            cls = subprocess.call('cls',shell=True)
                            #
                elif(len(self.ruleSet[0]) == 1):
                    #
                    if('IP' in pkt):
                        #
                        src = pkt[IP].src ; dst = pkt[IP].dst ; destPort = "" ; srcPort = ""
                        #
                        try:
                            #
                            if(pkt.haslayer(TCP)):
                                #
                                destPort = pkt[TCP].dport ; srcPort = pkt[TCP].sport
                                #
                            elif(pkt.haslayer(UDP)):
                                #
                                destPort = pkt[UDP].dport ; srcPort = pkt[UDP].sport
                                #
                            else:
                                #
                                destPort = 0 ; srcPort = 0
                                #
                            for r in range(0,len(self.ruleSet)):
                                #
                                if(int(self.ruleSet[r][0]) == int(destPort) or dst == self.addr):
                                    #
                                    print("<<<ALERT>>> [%s] Traffic from: %s:%s <<<ALERT>>>" % (t,src,srcPort))
                                    #
                                    logging.info("<<<ALERT>>> [%s] Traffic from: %s:%s <<<ALERT>>>" % (ts,src,int(destPort)))
                                    #
                                    time.sleep(3)
                                    #
                                    cls = subprocess.call('cls',shell=True)
                                    #
                        except Exception as e:
                            #
                            print("[*] Error: %s " % e)
                            #
                            print("[!] Packet Processing Failure [!]")
                            #
                            time.sleep(1)
                            #
                            cls = subprocess.call('cls',shell=True)
                            #
                elif(len(self.ruleSet[0]) == 2):
                    #
                    if('IP' in pkt):
                        #
                        src = pkt[IP].src ; dst = pkt[IP].dst ; destPort = ""
                        #
                        try:
                            #
                            if(pkt.haslayer(TCP)):
                                #
                                destPort = pkt[TCP].dport
                                #
                            elif(pkt.haslayer(UDP)):
                                #
                                destPort = pkt[UDP].dport
                                #
                            else:
                                #
                                destPort = 0
                                #
                            for r in range(0,len(ruleSet)):
                                #
                                if(str(src) == ruleSet[r][0] or int(ruleSet[r][1]) == int(destPort)):
                                    #
                                    print("<<<ALERT>>> [%s] Traffic from: %s:%s <<<ALERT>>>" % (t,src,destPort))
                                    #
                                    logging.info("<<<ALERT>>> [%s] Traffic from: %s:%s <<<ALERT>>>" % (ts,src,int(destPort)))
                                    #
                                    time.sleep(3)
                                    #
                                    cls = subprocess.call('cls',shell=True)
                                    #
                        except Exception as e:
                            #
                            print("[*] Error: %s " % e)
                            #
                            print("[!] Packet Processing Failure [!]")
                            #
                            time.sleep(1)
                            #
                            cls = subprocess.call('cls',shell=True)
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
            portValue = [int(port)] ; ruleSet.append(portValue)
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
        print("[*] Performing detection...")
        #
        L = LightIDS(activeInterface,ruleSet,addr)
        #
        L.Run()
        #
    print("<<< Lightweight IDS >>>")
    #
    print()
    #
    time.sleep(1)
    #
    print("""
    *****************************************************
    A lightweight Host Intrustion Detection System (HIDS)
    *****************************************************
          """)
    #
    print() ; time.sleep(1)
    #
    print("[*] Collecting interface data...") ; time.sleep(1)
    #
    print()
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
    print()
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

