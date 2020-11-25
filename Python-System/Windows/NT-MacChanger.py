#!/usr/bin/env python3

_AUTH_ = 'RWG'

from scapy.arch.windows import get_windows_if_list
import subprocess
import psutil
import random
import string
import time
import sys

def AddPrintBuffer(tgtStr):
    #
    i = 0
    #
    if(len(tgtStr) < 30):
        #
        while(len(tgtStr) < 30):
            #
            tgtStr = tgtStr + " "
            #
    return tgtStr

def RandomMAC():
    #
    # MAC Format: XX:XX:XX:XX:XX:XX
    #
    RandomMAC = ''
    #
    for i in range(0,6):
        #
        for j in range(0,2):
            #
            RandomMAC += random.choice('0123456789abcdef')
            #
        RandomMAC += '-'
        #
    RandomMAC = RandomMAC[0:17]
    #
    return RandomMAC

def CheckForHex(candidateMAC):
    #
    hexChars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    #
    for c in candidateMAC:
        #
        if(c.upper() not in hexChars):
            #
            return 1
            #
        else:
            #
            return 0

def ManualMAC():
    #
    macStr = "" ; macChars = ""
    #
    print("[*] Enter hex pairs as prompted...")
    #
    for i in range(0,6):
        #
        macChars = ''
        #
        for j in range(0,2):
            #
            macChars += input("[+] Enter a hex character-> ")
            #
        macStr += macChars
        #
        macStr += '-'
        #
    macStr = macStr[0:17]
    #
    return macStr

def DisplayAdapters():
    #
    print("[*] Displaying network adapters...") ; time.sleep(1)
    #
    print()
    #
    interfaces = get_windows_if_list()
    #
    print("<<< Network Adapters >>>  \t MAC \t IPV4 \t IPV6")
    #
    print("------------------------  \t --- \t ---- \t ----")
    #
    for i in range(0,len(interfaces)):
        #
        single_intf = AddPrintBuffer(interfaces[i]['name'])
        #
        macAddr = AddPrintBuffer(interfaces[i]['mac'])
        #
        ip_addr_v4 = AddPrintBuffer(interfaces[i]['ips'][1])
        #
        ip_addr_v6 = interfaces[i]['ips'][0]
        #
        print(i,')',single_intf,' ',macAddr,' ',ip_addr_v4,' ',ip_addr_v6)
        #
    print()
    #
    time.sleep(3)
    #
    return

def GetAdapters():
    #
    print("[*] Identifying network interfaces...") ; time.sleep(1)
    #
    print()
    #
    interfaces = get_windows_if_list()
    #
    print("<<< Network Adapters >>>  \t     MAC \t\t\t      IPV4 \t\t\t       IPV6")
    #
    print("------------------------  \t     --- \t\t\t      ---- \t\t\t       ----")
    #
    for i in range(0,len(interfaces)):
        #
        single_intf = AddPrintBuffer(interfaces[i]['name'])
        #
        macAddr = AddPrintBuffer(interfaces[i]['mac'])
        #
        ip_addr_v4 = AddPrintBuffer(interfaces[i]['ips'][1])
        #
        ip_addr_v6 = interfaces[i]['ips'][0]
        #
        print(i,')',single_intf,' ',macAddr,' ',ip_addr_v4,' ',ip_addr_v6)
        #
    print()
    #
    interface = int(input("[+] Enter the interface index-> "))
    #
    print("[*] Selected: %s " % interfaces[interface]['name'])
    #
    activeInterface = interfaces[interface]['name']
    #
    activeMAC = interfaces[interface]['mac']
    #
    subjectInterface = [activeInterface,activeMAC]
    #
    return subjectInterface

def ChangeMAC(newMac,interface):
    #
    cmd_str = ['powershell.exe','Set-NetAdapter','-Name '+interface,'-MacAddress '+newMac]
    #
    try:
        #
        result = subprocess.call(cmd_str)
        #
        print(result)
        #
    except:
        #
        print("[!] Failed to Change MAC Address [!]")
        #
        sys.exit(0)
        #
    return

def main():
    #
    print("""
<<< NT MAC Address Changer >>>
    """)
    #
    print() ; time.sleep(1)
    #
    print("[~] You should probably run this as an administrator [~]")
    #
    print()
    #
    time.sleep(1)
    #
    newMac = ""
    #
    interface = GetAdapters() ; curMAC = interface[1] ; curInt = interface[0]
    #
    print("[*] Network Adapter: %s | Layer 2 Address: %s " % (curInt,curMAC))
    #
    print("""
MAC Modification Options
------------------------

1) Manual MAC Entry
2) Auto-generate a Random MAC

    """)
    #
    subroutine = int(input("[+] Selection-> "))
    #
    newMac = ""
    #
    if(subroutine == 1):
        #
        newMac = ManualMAC()
        #
        check = CheckForHex(newMac)
        #
        if(check == 1):
            #
            print("[!] Invalid MAC Entered [!]")
            #
            sys.exit(0)
            #
        else:
            #
            print("[*] Manual MAC Generated as: %s " % newMac)
            #
            print("[*] Attempting to change the MAC on the selected interface...")
            #
            time.sleep(1)
            #
            ChangeMAC(newMac,curInt)
            #
            DisplayAdapters()
            #
    elif(subroutine == 2):
        #
        newMac = RandomMAC() ; print("[*] Random MAC Generated as: %s " % newMac)
        #
        check = CheckForHex(newMac)
        #
        if(check == 1):
            #
            print("[!] Invalid MAC Entered [!]")
            #
            sys.exit(0)
            #
        else:
            #
            print("[*] Attempting to change the MAC on the selected interface...")
            #
            time.sleep(1)
            #
            ChangeMAC(newMac,curInt)
            #
            DisplayAdapters()
            #
    else:
        print("[!] Undefined option. Departing [!]")
        #
        sys.exit(0)
        #
    cls = subprocess.call(['powershell.exe','cls'])
    #
    return

if(__name__ == '__main__'):
    #
    main()