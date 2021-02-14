#!/usr/bin/env python3

from getpass import getpass
import subprocess
import shutil
import time
import sys
import os

def ConfigureFirewall():
    #
    '''
    -> Check the firewall status
    '''
    #
    try:
        #
        firewall_status = subprocess.check_output(['systemctl','status','firewalld']) ; firewall_status = str(firewall_status)
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
        print("[!] Firewall is not active ")
        #
        print("[~] Attempting to install the firewall service...")
        #
        try:
            #
            subprocess.call(['yum','install','firewalld','-y'])
            #
        except Exception as e:
            #
            print("[!] Error: Failed to install the firewall service: %s " % e)
            #
            return
            #
        print("[*] Attempting to start the firewall...") ; time.sleep(1)
        #
        try:
            #
            subprocess.call(['systemctl','start','firewalld'])
            #
        except Exception as e:
            #
            print("[!] Failed to start the firewall: %s " % e)
            #
            return
            #
    print("[*] Firewall is active ") ; time.sleep(1)
    #
    print("[~] Configuring firewall rules...")
    #
    try:
        #
        print("[+] Adding: 80 | Public | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--add-port=80/tcp'])
        #
        print("[+] Adding: 443 | Public | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--add-port=443/tcp'])
        #
        print("[+] Adding: 22 | Internal | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=internal','--add-port=22/tcp'])
        #
        print("[+] Adding: 5902 | Internal | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=internal','--add-port=5902/tcp'])
        #
        print("[+] Adding: HTTP | Public | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--add-service=http'])
        #
        print("[+] Adding: HTTPS | Public | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--add-service=https'])
        #
        print("[+] Adding: SSH | Internal | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=internal','--add-service=ssh'])
        #
        print("[*] Removing: SSH | External | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--remove-service=ssh'])
        #
        print("[-] Removing: RPC | Public | Accept ")
        #
        subprocess.call(['firewall-cmd','--permanent','--zone=public','--remove-port=111/tcp'])
        #
        print("[*] Reloading the firewall daemon...") ; time.sleep(1)
        #
        subprocess.call(['firewall-cmd','--reload'])
        #
        print("[*] Finished firewall configuration subroutine ") ; time.sleep(1)
        #
    except Exception as e:
        #
        print("[!] ERROR: Firewall rule configuration sequence hit a snag: %s " % s)
        #
    return

def ConfigureWhitelisting():
    #
    print("[*] Configuring IP based access control measures...") ; time.sleep(1)
    #
    try:
        #
        administrative_addr = input("[+] Enter the IP for the administrator's workstation-> ")
        #
        print("[*] Adding the administrator's workstation IP to the firewall rules...") ; time.sleep(1)
        #
        try:
            #
            subprocess.call(['firewall-cmd','--permanent','--zone=internal','--add-source='+f'{administrative_addr}'])
            #
            print("[*] Administrator's workstation added to the firewall rules ") ; time.sleep(1)
            #
        except Exception as e:
            #
            print("[!] ERROR: Failed to add administrator's IP to the firewall rules: %s " % e)
            #
        fileObject = open("/etc/hosts.allow",'w')
        #
        fileObject.write("sshd: %s" % administrative_addr) ; fileObject.write('\n')
        #
        fileObject.close()
        #
        fileObject = open("/etc/hosts.deny",'w')
        #
        fileObject.write("sshd: All\n")
        #
        fileObject.close()
        #
        print("[*] Reloading the firewall...")
        #
        try:
            #
            subprocess.call(['firewall-cmd','--reload'])
            #
        except Exception as e:
            #
            print("[!] Failed to reload firewall ")
            #
            return
            #
    except Exception as e:
        #
        print("[!] ERROR: Failed to implement access control measure(s): %s " % e)
        #
        return
        #
    print("[*] Finished configuring IP based access control measures ") ; time.sleep(1)
    #
    return

def InstallSoftware():
    #
    print("[*] Software installation sequence initiated ")
    #
    '''
    print("[*] Performing updates and upgrades as required...")
    #
    try:
        #
        subprocess.call(['yum','update','-y'])
        #
        subprocess.call(['yum','upgrade','-y'])
        #
    except Exception as e:
        #
        print("[!] ERROR: Update/Upgrade sequence failed: %s " % e)
        #
    print("[*] Update/Upgrade Sequence Completed ") ; time.sleep(1)
    #
    '''
    print("[~] Installing Tiger-VNC Server")
    #
    try:
        #
        subprocess.call(['yum','install','tigervnc-server','-y'])
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to install Tiger-VNC ")
        #
    print("[*] Tiger-VNC Server installation sequence complete ")
    #
    '''
    print("[~] Installing the Apache Web Server")
    #
    try:
        #
        subprocess.call(['yum','install','httpd','-y'])
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to install the web server: %s " % e)
        #
    print("[*] Apache Web Server installation sequence complete")
    #
    print("[*] Enabling the web server service...")
    #
    try:
        #
        subprocess.call(["systemctl","enable","httpd"])
        #
        print("[*] Enabled HTTPD ")
        #
    except Exception as e:
        #
        print("[!] ERROR: Failed to enable the HTTPD service: %s " % e)
        #
    print("[~] Updating... ") ; subprocess.call(['yum','update','-y'])
    #
    '''
    print("[*] Software update/upgrade/installation sequence complete")

def ConfigureBackups():
    #
    print("[*] Beginning scheduled backups configuration subroutine ")
    #
    time.sleep(1)
    #
    CheckCrontab = os.path.exists("/etc/crontab")
    #
    if(CheckCrontab):
        #
        print("[*] Located crontab file in: /etc/crontab ")
        #
    else:
        #
        print("[!] Failed to locate crontab file ")
        #
        return
        #
    print("[*] Checking for the presence of the backup script...")
    #
    CheckBackupScript = os.path.exists("SimpleBackup.py")
    #
    if(CheckBackupScript):
        #
        print("[*] Confirmed presence of the backup script in the current directory")
        #
        print("[~] Attempting to export the script...")
        #
        try:
            #
            copy_status = subprocess.check_output(['cp','SimpleBackup.py','/tmp/SimpleBackup.py'])
            #
            if(copy_status == 0):
                #
                print("[*] Backup script successfully copied to the /tmp directory")
                #
        except Exception as e:
            #
            print("[!] Failed to copy the backup script: %s " % e)
            #
        print("[*] Attempting to add a job in the crontab file...")
        #
        try:
            #
            fileObject = open('/etc/crontab','a')
            #
            fileObject.write("0 22 * * * /usr/bin/env python3 /tmp/SimpleBackup.py\n")
            #
            fileObject.close()
            #
            print("[*] Backup operation scheduled! ")
            #
        except Exception as e:
            #
            print("[!] ERROR: Failed to schedule the backup: %s " % e)
            #
            return
            #
        print("[*] Finished scheduling the backup ") ; time.sleep(1)
        #
        return
        #
    else:
        #
        print("[!] Failed to locate the backup script ")
        #
        return

def AddUsers():
    #
    print("[*] Adding the user addition subroutine ")
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
                    'robert.gaines'
                  ]
    #
    print("[*] Preparing to add the following users: ")
    #
    for user in other_users:
        #
        print("-> %s" % user)
        #
    password = getpass("[*] Enter the default password to be used with each account-> ")
    #
    password = subprocess.check_output(['openssl','passwd','-1',password])
    #
    password = str(password)
    password = password.lstrip("b'")
    password = password.rstrip("\\n'")
    parsed_password = password
    #
    for user in other_users:
        #
        try:
            #
            print("[*] Adding: %s " % user) ; time.sleep(1)
            #
            subprocess.call(['useradd','-p',parsed_password,user])
            #
            print("[*] Adding: %s to the administrators group " % user) ; time.sleep(1)
            #
            subprocess.call(['usermod','-aG','root',user])
            #
            subprocess.call(['usermod','-g','root',user])
            #
            print("[*] Setting account to disabled")
            #
            subprocess.call(['chage','-E0',user])
            #
        except Exception as e:
            #
            print("[*] ERROR: Failed to add the user -> %s <-> %s " % (user,e))
            #
    option = input("[*] Add another administrative user (y/n) ?")
    #
    option = option.lower()
    #
    if(option == 'y'):
        #
        username = input("[+] Enter the username-> ")
        #
        password = getpass("[+] Enter the password-> ")
        #
        try:
            #
            print("[*] Attempting to add: %s " % username)
            #
            subprocess.call(['adduser',username,"-p",password])
            #
            print("[*] Attempting to add the user to the administrators group...")
            #
            subprocess.call(['usermod','-aG',username,'root'])
            #
            print("[*] Added: %s to the administrators group " % username)
            #
        except Exception as e:
            #
            print("[!] ERROR: Failed to add another user: %s " % e)
            #
            return
    else:
        #
        return
        #
    return

def InstallGUI():
    #
    print("[*] Entering the X-Window installation subroutine ") ; time.sleep(1)
    #
    groups = subprocess.check_output(['dnf','group','list'])
    #
    groups = groups.decode('utf-8')
    #
    if('Server with GUI' in groups):
        #
        print("[*] Installing the default GUI environment is an option!")
        #
        subprocess.call(['dnf','groupinstall','Server with GUI','-y'])
        #
        print("[~] Setting the X-Window environment as the default ")
        #
        subprocess.call(['systemctl','set-default','graphical'])
        #
        return
        #
    else:
        #
        print("[!] Installing the default X-Window environment does not appear to be an option ")
        #
        return

def CheckIfRoot():
    #
    user_uid = os.getuid()
    #
    if(user_uid == 0):
        #
        print("[*] User is root, proceed ")
        #
    else:
        #
        print("[!] User is not root, aborting ")
        #
        sys.exit(1)

def main():
    #
    print("[*] Linux Server Configuration Script - Please run this as root! ")
    #
    CheckIfRoot()
    #
    ConfigureFirewall()
    #
    #ConfigureWhitelisting()
    #
    InstallSoftware()
    #
    #ConfigureBackups()
    #
    #InstallGUI()
    #
    AddUsers()
    #
    print("[*] Configuration complete -> Restarting ")
    #
    time.sleep(1)
    #
    #subprocess.call(["reboot"])
    #


if(__name__ == '__main__'):
    #
    main()
