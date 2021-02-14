#!/usr/bin/env python3

import subprocess
import socket
import time
import sys
import os

def ConfigureNetworkInterfaces():
    #
    print("[*] Configuring the network interface(s) ") ; time.sleep(1)
    #
    subprocess.call(['nmtui'])
    #
    print("[*] Finished configuring the network interface(s) ")

def ConfigureFirewall():
    #
    try:
        #
        firewall_status = subprocess.check_output(['systemctl','status','firewall-cmd'])
        #
    except:
        #
        firewall_status = 'Inactive'
        #
    if('running' in firewall_status):
        #
        print("[*] Firewall is active ")
        #
    else:
        #
        print("[~] Firewall appears to be inactive. Installing/Configuring the firewall... ")
        #
        try:
            #
            print("[*] Installing the firewall daemon...") ; time.sleep(1)
            #
            # subprocess.call(["yum","install","firewalld","-y"])
            # #
            # subprocess.call(["systemctl","enable","firewalld"])
            # #
            # subprocess.call(["systemctl","start","firewalld"])
            # #
            # check_firewall_status = subprocess.check_output(["systemctl","status","firewalld"])
            #
            if("running" in check_firewall_status):
                #
                print("[*] Firewall is installed and running ") ; time.sleep(1)
                #
            else:
                #
                print("[!] The firewall doesn't appear to be running, consider a manual configuration ") ; time.sleep(3)
                #
        except Exception as e:
            #
            print("[!] Failed to install or configure the firewall ")
            #
    print("[*] Attempting to read firewall configuration parameters")
    #
    check_port_config = os.path.exists("FirewallConfigPorts.txt")
    #
    check_service_config = os.path.exists("FirewallConfigServices.txt")
    #
    if(check_port_config):
        #
        print("[*] Located the port configuration file ")
        #
        fileObject = open("FirewallConfigPorts.txt",'r')
        #
        for line in fileObject.readlines():
            #
            print(line)
            #
        print("[*] Firewall Ports Configured")
        #
    else:
        #
        print("[!] Failed to locate the port configuration file ")
        #
    if(check_service_config):
        #
        print("[*] Located the service configuration file ")
        #
        fileObject = open("FirewallConfigServices.txt")
        #
        for line in fileObject.readlines():
            #
            print(line)
            #
        print("[*] Firewall Services Configured ")
        #
    else:
        #
        print("[!] Failed to locate the service configuration file ")
        #
    return

def ConfigureUsers():
    #
    return

def PerformUpdates():
    #
    return

def main():
    #
    print("[*] Linux Server Configuration Script - CentOS/RHEL ")
    #
    #ConfigureNetworkInterfaces()
    #
    ConfigureFirewall()

if(__name__ == '__main__'):
    #
    main()
