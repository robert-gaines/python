#!/usr/bin/env python3

_auth_ = 'RWG'

import psutil

# The purpose of this script is to gather #
# core data on a host computer            #

def CPUData():
    cpuCount = psutil.cpu_count(logical=True)
    #
    print("[*] CPU Count: %i " % cpuCount)
    #
    print()
    #
    perCpu = psutil.cpu_percent(interval=1,percpu=True)
    #
    print("[*] CPU Data: % Utilization per Interval")
    #
    print("----------------------------------------")
    #
    for p in perCpu:
        #
        print(p)
        #
    print()
    #
    cpuStats = psutil.cpu_stats()
    #
    statLabels = ["Switches","Interrupts","Soft Interrupts","System Calls"]
    #
    print("[*] CPU Statistics ")
    #
    print("-------------------")
    #
    for s in range(0,len(statLabels)):
        #
        print(statLabels[s],":",cpuStats[s])
        #
    cpuFreq = psutil.cpu_freq(percpu=False)
    #
    print()
    #
    print("[*] Current CPU Frequency ")
    #
    print("--------------------------")
    #
    print(cpuFreq[0])
    #
    print()



def main():
    #
    print("[*] System Data Collection Script [*]")
    #
    print("-------------------------------------")
    #
    print()
    #
    CPUData()
    #
    return

if(__name__ == '__main__'):
    
    main()