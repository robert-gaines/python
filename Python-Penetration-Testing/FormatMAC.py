#!/usr/bin/env python3

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

FormatMac("d18e5558b03f")
