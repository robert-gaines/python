#!/usr/bin/env python3

from datetime import datetime
import platform
import time
import os

def SplitAndRejoin(network,split_char):
    #
    segments = network.split(split_char)
    #
    rejoin_char = split_char
    #
    rejoined = segments[0]+rejoin_char+segments[1]+rejoin_char+segments[2]+rejoin_char
    #
    return rejoined


def main():
    #
    print("<-- OS Based Ping Sweep -->")
    #
    subject_network = input("[+] Enter the network address-> ")
    #
    truncated = SplitAndRejoin(subject_network,'.')
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
    else:
        #
        cmd = "ping -c 1 "
        #
    start = datetime.now()
    #
    print("[*] Initiating Scan [*]")
    #
    time.sleep(1)
    #
    for i in range(1,255):
        #
        tgt = truncated+str(i)
        #
        tx = cmd+tgt
        #
        rx = os.popen(tx)
        #
        for line in rx.readlines():
            #
            if(line.count("ttl")):
                #
                print("[*] Host alive at-> %s " % tgt)
                #
    end = datetime.now()
    #
    net_time = end-start
    #
    print("[~] Scanning completed in: %s " % net_time)

if(__name__ == '__main__'):
    #
    main()
