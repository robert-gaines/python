#!/usr/bin/env python3

import subprocess
import time
import sys
import os

def PurgeLogFiles():
    #
    try:
        #
        print("[*] Clearing event logs...")
        #
        time.sleep(1)
        #
        subprocess.call(['powershell.exe','Get-EventLog -LogName * | ForEach {Clear-EventLog $_.Log }']) ; print()
        #
        print("[*] Success [*]") ; time.sleep(1)
        #
    except: 
        #
        print("[!] Failed to clear log files [!]")
        #
        time.sleep(1)
        #
        sys.exit(0)

def main():
    #
    print("""         
********************
*   NT Log Wiper   *
********************
          """)
    #
    PurgeLogFiles()

if(__name__ == '__main__'):
    #
    main()