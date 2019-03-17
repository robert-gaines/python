#!/usr/bin/env python3

import subprocess
import random
import time
import sys

def GenerateRandomMAC():
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
        RandomMAC += ':'
        #
    RandomMAC = RandomMAC[0:17]
    #
    return RandomMAC

def SetMAC(interface, mac_addr):
    #
    print("[-] %s -> down" % interface)
    #
    time.sleep(1)
    #
    subprocess.call(["ifconfig",interface,"down"])
    #
    print("[*] Changing MAC Address on: %s " % interface)
    #
    time.sleep(1)
    #
    subprocess.call(["ifconfig",interface,"hw", "ether",mac_addr])
    #
    print("[-] %s -> up " % interface)
    #
    time.sleep(1)
    #
    subprocess.call(["ifconfig",interface,"up"])

def main():
    #
    print("<-- MAC Changer -->")
    #
    time.sleep(1)
    #
    interface = input("[+] Enter the interface-> ")
    #
    mac_addr = GenerateRandomMAC()
    #
    print("[*] Changing MAC address on "+interface+" to "+mac_addr)
    #
    time.sleep(1)
    #
    try:
        #
        SetMAC(interface, mac_addr)
        #
        print("Here")
        #
    except:
        #
        print()
        #
        sys.exit("[!] Error - MAC Couldn't be changed ")
        #
        print()
        #
    finally:
        #
        print()
        #
        subprocess.call(["ifconfig", interface])
        #
        time.sleep(3)
        #
        subprocess.call('clear')
        #
        sys.exit()


if(__name__ == '__main__'):
    #
    main()
