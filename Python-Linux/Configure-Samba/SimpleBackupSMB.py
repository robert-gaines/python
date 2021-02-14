#!/usr/bin/env python3

import subprocess
import shutil
import time
import sys
import os

def BackupOperation():
    #
    dateTime = time.ctime()
    #
    dateTimeReplaceOne = dateTime.replace(' ','_')
    #
    timeStamp = dateTimeReplaceOne.replace(':','_')
    #
    backupDirName = "FAIS019_Backup_"+timeStamp
    #
    backupDirPath = "/backup/"+backupDirName
    #
    #subprocess.call(['smbclient','//<IP Goes Here>/backup','-U','','-c','mkdir '+backupDirName])
    #
    time.sleep(1)
    #
    backupName = "Server_Backup_"+timeStamp
    #
    backupPath = backupDirPath+'/'+backupName
    #
    backupExclude = "/tmp/"+backupName
    #
    print("[*] Creating compressed backup on the remote share...")
    #
    subprocess.call(['tar','-cvzp','--exclude=/backup'+','+backupName,'-f',backupExclude,'--one-file-system','/'])
    #
    return backupName

def ConnectToShare():
    #
    print("Attempting to connect to the remote share...")
    #
    check_backup_dir = os.path.exists('/backup')
    #
    result = subprocess.call(['mount','-t','cifs','<unc>','/backup','-o','username=<username>,password=<password>'])
    #
    if(result == 0):
         #
         print("[*] Connected to the remote share")
         #
    else:
         #
         print("[!] Failed to connect to the remote share")
         #
         sys.exit(1)

def CheckBackups():
    #
    os.chdir('/backup')
    #
    backups = os.listdir('/backup')
    #
    oldest_backup = backups[0]
    #
    oldest_mtime = os.path.getmtime(backups[0])
    #
    if(len(backups) > 7):
        #
        for b in backups:
            #
            current_mtime = os.path.getmtime(b)
            #
            if(current_mtime < oldest_mtime):
                #
                oldest_mtime = os.path.getmtime(b)
                #
                oldest_backup = b
                #
        print("[*] Oldest backup: %s " % oldest_backup) ; time.sleep(3)
        #
        print("[*] Removing: %s " % oldest_backup)
        #
        os.remove(oldest_backup)
        #
        os.chdir('/tmp')
        #
    else:
        os.chdir('/tmp')
        #
        return

def main():
    #
    print("[*] Linux Backup Script ")
    #
    sourceDirectory = '/'
    #
    destinationDirectory = "/backup"
    #
    print("[*] Connecting to the remote share ")
    #
    ConnectToShare()
    #
    CheckBackups()
    #
    os.chdir('/tmp') ; print("[*] Current directory: ",os.getcwd())
    #
    print("[*] Source Directory set to: %s " % sourceDirectory )
    #
    print("[*] Destination Directory set to: %s " % destinationDirectory)
    #
    print("[~] Checking the validity of the source and destination paths ")
    #
    checkSource = os.path.exists(sourceDirectory)
    #
    checkDestination = os.path.exists(destinationDirectory)
    #
    print("[*] Source result: %s " % checkSource)
    #
    print("[*] Destination result: %s " % checkDestination)
    #
    backupName = BackupOperation()
    #
    print("[*] Transferring: %s to the remote share " % backupName)
    #
    shutil.copy2(backupName,'/backup')
    #
    print("[*] Backup created at -> %s " % backupName)
    #
    print("[*] Backup operations are complete, departing...")
    #
    localBackupPath = "/tmp/"+backupName
    #
    os.remove(localBackupPath)
    #
    subprocess.call(['umount','-a'])
    #
    time.sleep(3)

if(__name__ == '__main__'):
    #
    main()
