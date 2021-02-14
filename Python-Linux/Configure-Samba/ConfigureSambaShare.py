#!/usr/bin/env python3

from getpass import getpass
import subprocess
import time
import sys
import os

def CheckIfRoot():
    #
    user_uid = os.getuid()
    #
    if(user_uid == 0):
        #
        print("[*] User is root, proceed")
        #
    else:
        #
        print("[!] User is not root, aborting")
        #
        sys.exit(1)

def InstallSamba():
    #
    print("[*] Installing Samba Components ")
    #
    try:
        #
        subprocess.call(['yum','install','samba','samba-client','-y'])
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to install Samba: %s " % e)
        #
        return
        #
    print("[*] Installed Samba components ")
    #
    print("[*] Enabling supporting services ")
    #
    try:
        #
        subprocess.call(['systemctl','start','smb.service'])
        #
        subprocess.call(['systemctl','start','nmb.service'])
        #
        subprocess.call(['systemctl','enable','smb.service'])
        #
        subprocess.call(['systemctl','enable','nmb.service'])
        #
        print("[*] Started and enabled supporting service ")
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to start or enable supporting services: %s " % e)

def ConfigureFirewallRules():
    #
    print("[*] Configuring firewall rules to support the share ") ; time.sleep(1)
    #
    try:
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--add-service=samba'])
        #
        subprocess.call(['firewall-cmd','--zone=public','--add-service=samba'])
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to configure the firewall rules -> %s " % e)
        
def ConfigureShareDirectory():
    #
    print("[*] Configuring the share directory ") ; time.sleep(1)
    #
    try:
        #
        print("[*] Creating the backup share at-> /backup ") ; time.sleep(1)
        #
        os.mkdir('/backup')
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to create the backup directory: %s " % e)
        #
    print("[*] Adding share permissions on the backup directory ") ; time.sleep(1)
    #
    try:
        #
        subprocess.call(['chmod','2770','/backup'])
        #
        subprocess.call(['chown','-R','root','/backup'])
        #
        subprocess.call(['chcon','-t','samba_share_t','/backup','-R'])
        #
        print("[*] Permissions configured on the share directory ")
        #
    except:
        #
        print("[!] ERROR: Failed to set permissions on the backup directory ")
        #
    print("[*] Adding a share group ...") ; time.sleep(1)
    #
    try:
        #
        subprocess.call(['groupadd','share_admins'])
        #
        time.sleep(3)
        #
        subprocess.call(['chgrp','root','/backup'])
        #
        print("[*] Share group is: share_admins ")
        #
    except:
        #
        print("[!] ERROR: Failed to configure share administrators group ")
        #
    finally:
        #
        print("[*] Basic share configuration complete") ; time.sleep(1)

def ConfigureShareUsers():
    #
    print("[*] Configuring user permissions for the share ") ; time.sleep(1)
    #
    other_users = [
                    'den.bowker',
                    'qin.wang',
                    'dave.anderson',
                    'colin.pringle',
                    'steve.price',
                    'cori.huggins',
                    'josh.arp',
                    'eric.parker',
                    'robert.gaines',
                  ]
    #
    print("[*] Adding users to the share administrators group...") ; time.sleep(1)
    #
    for user in other_users:
        #
        print("[*] Adding: %s " % user)
        #
        try:
            #
            subprocess.call(['usermod','-aG','share_admins',user])
            #
        except Exception as e:
            #
            print("[!] ERROR: Failed to add user to the share administrators group: %s " % e)
            #
    print("[*] Configure the Samba credential database...") ; time.sleep(1)
    #
    for user in other_users:
        #
        print("[*] Configuring: %s " % user)
        #
        subprocess.call(['smbpasswd','-a',user])
        #
    for user in other_users:
        #
        print("[*] Enabling: %s " % user)
        #
        subprocess.call(['smbpasswd','-e',user])
        #
    print("[*] SMB User configuration sequence complete ")

def ConfigureShareParameters():
    #
    print("[*] Configuring the Samba share path ")
    #
    test_smb_conf = os.path.exists('/etc/samba/smb.conf')
    #
    if(test_smb_conf):
        #
        print("[*] Located configuration file ")
        #
        fileObject = open("/etc/samba/smb.conf",'a')
        #
        fileObject.write('\n')
        #
        fileObject.write("[backup]\n")
        #
        conf_parameters = ['path=/backup','browseable = yes','read only = no','writeable = yes','guest ok = no']
        #
        for c in conf_parameters:
            #
            fileObject.write('\t'+c+'\n')
            #
        authorized_users = [
                              'root',
                              'den.bowker',
                              'qin.wang',
                              'dave.anderson',
                              'colin.pringle',
                              'steve.price',
                              'cori.huggins',
                              'josh.arp',
                              'eric.parker',
                              'robert.gaines'
                           ]
        #
        auth_user_string = 'valid users = '
        #
        for a in authorized_users:
            #
            value = a
            #
            auth_user_string += value+' '
            #
        auth_user_string += "@share_admins"
        #
        fileObject.write('\t'+auth_user_string+'\n')
        #
        fileObject.write('\n')
        #
        fileObject.close()
        #
    else:
        #
        print("[*] Failed to locate smb configuration file ") ; time.sleep(1)
        #
    print("[*] Finished appending configuration paramters to smb.conf ") ; time.sleep(1)

def main():
    #
    print("[*] SAMBA Share configuration script ")
    #
    CheckIfRoot()
    #
    InstallSamba()
    #
    ConfigureFirewallRules()
    #
    ConfigureShareDirectory()
    #
    #ConfigureShareUsers()
    #
    ConfigureShareParameters()
    #
    print("[*] Restarting relevant services ")
    #
    subprocess.call(['systemctl','restart','smb.service'])
    #
    subprocess.call(['systemctl','restart','nmb.service'])
    #
    print("[*] Script complete, departing ") ; time.sleep(1) ; sys.exit(0)

if(__name__ == '__main__'):
    #
    main()
