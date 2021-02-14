#!/usr/bin/env python3

import subprocess
import time
import sys
import os

def main():
    #
    print("[*] LAMP Server Configuration Script ")
    #
    CheckForRoot = os.getuid()
    #
    if(CheckForRoot == 0):
        #
        print("[*] User is root -> Proceed")
        #
    else:
        #
        print("[!] Run this as root! ")
        #
        sys.exit(1)
        #
    print("[*] Installing the Apache Web Server")
    #
    subprocess.call(['yum','install','httpd','-y'])
    #
    print("[*] Starting the web server ")
    #
    subprocess.call(['systemctl','start','httpd.service'])
    #
    print("[*] Enabling the web server as a service ")
    #
    subprocess.call(['systemctl','enable','httpd.service'])
    #
    print("[*] Installing the MariaDB server")
    #
    subprocess.call(['yum','install','mariadb-server','mariadb','-y'])
    #
    print("[*] Starting the MariaDB Server ")
    #
    subprocess.call(['systemctl','start','mariadb.service'])
    #
    print("[*] Starting the MySQL installation sequence")
    #
    subprocess.call(['sudo','mysql_secure_installation'])
    #
    print("[*] Enabling the DB service")
    #
    subprocess.call(['systemctl','enable','mariadb.service'])
    #
    print("[*] Installing PHP ")
    #
    subprocess.call(['yum','install','php','php-mysql','-y'])
    #
    print("[*] Installing the EPEL Release ")
    #
    subprocess.call(['yum','install','epel-release','-y'])
    #
    print("[*] Installing PHP MyAdmin ")
    #
    subprocess.call(['yum','install','phpmyadmin','-y'])
    #
    print("[*] Restarting the web server ...")
    #
    subprocess.call(['systemctl','restart','httpd.service'])
    #
    print("[*] Basic LAMP Stack installation complete, restarting ")
    #
    time.sleep(3)
    #
    subprocess.call(['reboot'])

if(__name__ == '__main__'):
    #
    main()

