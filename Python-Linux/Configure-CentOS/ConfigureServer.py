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
            subprocess.call(["yum","install","firewalld","-y"])
            #
            subprocess.call(["systemctl","enable","firewalld"])
            #
            subprocess.call(["systemctl","start","firewalld"])
            #
            check_firewall_status = subprocess.check_output(["systemctl","status","firewalld"])
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
            segments = line.split(',')
            zone     = segments[0]
            port     = segments[1]
            protocol = segments[2]
            protocol = protocol.rstrip('\n')
            #
            try:
                #
                subprocess.call(["firewall-cmd","--permanent","--zone={0}".format(zone),"--add-port={0}/{1}".format(port,protocol)])
                #

                #
            except Exception as e:
                #
                print("[!] Failed to add firewall rule: %s " % e)
                #
        print("[*] Removing SSH from the public zone..."); time.sleep(1)
        #
        subprocess.call(["firewall-cmd","--permanent","--zone=public","--remove-port=22/tcp"])
        #
        subprocess.call(["firewall-cmd","--permanent","--zone=public","--remove-service=ssh"])
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
            segments = line.split(',')
            zone = segments[0]
            service = segments[1]
            service = service.rstrip('\n')
            #
            try:
                #
                subprocess.call(["firewall-cmd","--permanent","--zone={0}".format(zone),"--add-service={0}".format(service)])
                #
            except Exception as e:
                #
                print("[!] Failed to add firewall rule: %s " % e)
                #
        print("[*] Firewall Services Configured ")
        #
    else:
        #
        print("[!] Failed to locate the service configuration file ")
        #
    check_hosts_allow = os.path.exists('/etc/hosts.allow')
    #
    check_hosts_deny = os.path.exists('/etc/hosts.deny')
    #
    if(not check_hosts_allow and not check_hosts_deny):
        #
        print("[*] Host files are not present in /etc ")
        #
        print("[*]Configuring hosts.allow & hosts.deny...") ; time.sleep(1)
        #
        fileObject = open("/etc/hosts.allow",'w')
        #
        fileObject.close()
        #
        fileObject = open("/etc/hosts.deny",'w')
        #
        fileObject.write("sshd: All\n")
        #
        fileObject.close()
    else:
        #
        print("[*] Host files are already present in /etc -> Configure this part manually")
        #
    print("[*] Adding approved IPs ")
    #
    check_addr_file = os.path.exists("WhitelistedAddresses.txt")
    #
    if(check_addr_file):
        #
        print("[*] Located the configuration file ")
        #
        fileObject = open("WhitelistedAddresses.txt",'r')
        #
        allowFile = open("/etc/hosts.allow","w")
        #
        for line in fileObject.readlines():
            #
            segments = line.split(",")
            zone     = segments[0]
            ip       = segments[1]
            ip       = ip.rstrip('\n')
            #
            allowFile.write("sshd: %s " % ip) ; allowFile.write('\n')
            #
            subprocess.call(['firewall-cmd','--permanent',"--zone={0}".format(zone),"--add-source={0}".format(ip)])
            #
        fileObject.close()
        #
        allowFile.close()
        #
    else:
        #
        print("[!] Failed to locate the configuration file for IP addresses")
    #
    try:
        print("[*] Reloading the firewall one last time ") ; time.sleep(1)
        #
        subprocess.call(['firewall-cmd','--reload'])
        #
        print("[*] Firewall configuration complete")
        #
    except:
        #
        print("[!] Failed to reload the firewall ") ; time.sleep(1)
    #
    return

def ConfigureUsers():
    #
    print("[*] Adding Users ")
    #
    check_user_files = os.path.exists("ServerUsers.txt")
    #
    if(check_user_files):
        #
        print("[*] Located user configuration file ")
        #
        fileObject = open("ServerUsers.txt",'r')
        #
        for line in fileObject.readlines():
            #
            segments = line.split(',')
            username = segments[0]
            password = segments[1]
            group    = segments[2]
            group    = group.rstrip('\n')
            #
            password = subprocess.check_output(['openssl','passwd','-1',password])
            #
            password = str(password)
            password = password.lstrip("b'")
            password = password.rstrip("\\n'")
            parsed_password = password
            #
            try:
                #
                print("[*] Adding: %s " % username) ; time.sleep(1)
                #
                subprocess.call(['useradd','-p',parsed_password,username])
                #
                print("[*] Adding: %s to the administrators group " % username) ; time.sleep(1)
                #
                subprocess.call(['usermod','-aG','root',username])
                #
                subprocess.call(['usermod','-L',username])
                #
            except Exception as e:
                #
                print("[*] ERROR: Failed to add the user -> %s <-> %s " % (user,e))
                #
        print("[*] Finished adding users ") ; time.sleep(1)
        #
    else:
        #
        print("[!] Failed to locate user configuration file ")
        #
    return

def PerformUpdates():
    #
    print("[*] Installing updates... ")
    #
    try:
        #
        subprocess.call(["yum","update","-y"])
        #
    except Exception as e:
        #
        print("[!] Failed to install updates: %s " % e)
        #
    return

def CheckIfRoot():
    #
    print("[~] Checking to see if the user is root...")
    #
    RootTest = os.getuid()
    #
    if(RootTest == 0):
        #
        print("[*] User is root ")
        #
    else:
        #
        print("[!] Run this script as root ")
        #
        sys.exit(1)

def main():
    #
    print("[*] Linux Server Configuration Script - CentOS/RHEL ")
    #
    CheckIfRoot()
    #
    ConfigureNetworkInterfaces()
    #
    ConfigureFirewall()
    #
    ConfigureUsers()
    #
    PerformUpdates()

if(__name__ == '__main__'):
    #
    main()
