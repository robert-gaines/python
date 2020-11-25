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
    #
    print("[*] Average system load ")
    #
    print("------------------------")
    #
    loadAverage = psutil.getloadavg()
    #
    print(loadAverage)
    #
    print()

def MemoryStats():
    #
    netMemory = psutil.virtual_memory()
    #
    memoryLabels = ['Total','Available','Percent','Used','Free']; i = 0
    #
    print("[*] Memory values: ")
    #
    print("-------------------")
    #
    for m in memoryLabels:
        #
        print(m,":",netMemory[i])
        #
        i = i+1
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
    MemoryStats()
    #
    return

if(__name__ == '__main__'):
    
    main()