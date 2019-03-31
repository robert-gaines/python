#!/usr/bin/env python3

import subprocess
import socket
import time
import sys

def FormatMac(MacAddr):
    #
    newMacAddr = ""
    #
    i = 0
    #
    while(i <= len(MacAddr)-2):
        #
        for j in range(0,2):
            #
            newMacAddr += MacAddr[i]
            #
            i += 1
            #
        newMacAddr += ":"
        #
    newMacAddr = newMacAddr[0:len(newMacAddr)-1]
    #
    return newMacAddr


def MonitorMode():
    #
    amng_chk = subprocess.check_output(['which','airmon-ng'])
    #
    if(bytes("airmon-ng",'utf-8') in amng_chk):
        #
        pass
        #
    else:
        #
        sys.exit("[!] This script requires airmon-ng")
        #
    print("[+] Gathering interface data... ")
    #
    time.sleep(1)
    #
    subprocess.call(['iwconfig'])
    #
    print()
    #
    iface = input("[+] Enter the interface for monitoring-> ")
    #
    try:
        #
        subprocess.call(['airmon-ng','start',iface])
        #
    except:
        #
        sys.exit("[!] Transition to monitor mode failed ")


def main():
    #
    print("<-- Wireless Sniffer -->")
    #
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 3)
    #
    print("[*] Setting monitor mode ")
    #
    time.sleep(3)
    #
    MonitorMode()
    #
    subprocess.call(['iwconfig'])
    #
    print()
    #
    bind_iface = input("[+] Enter the monitoring interface-> ")
    #
    try:
        #
        sniffer.bind((bind_iface,0x003))
        #
    except:
        #
        sys.exit("[!] Bind operation failed ")
        #
    print()
    #
    print("*** Sniffing Wireless Traffic ***")
    #
    while(True):
        #
        frames = sniffer.recvfrom(6000)
        #
        frame = frames[0]
        #
        if(frame[18] == 128):
            #
            bssid = frame[34:40].hex()
            #
            bssid = FormatMac(bssid)
            #
            ssid = frame[55:75]
            #
            print("[*] SSID -> ", ssid)
            #
            print("[*] BSSID -> ", bssid)
            #
            time.sleep(2)

if(__name__ == '__main__'):
    #
    main()
