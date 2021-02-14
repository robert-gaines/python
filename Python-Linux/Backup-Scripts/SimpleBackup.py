#!/usr/bin/env python3

import subprocess
import shutil
import time
import sys
import os

def MakeBackupDirectory(destination):
    #
    dateTime = time.ctime()
    #
    dateTimeReplaceOne = dateTime.replace(' ','_')
    #
    timeStamp = dateTimeReplaceOne.replace(':','_')
    #
    dirName = "Backup_"+timeStamp
    #
    if(not (destination.endswith('/'))):
        #
        destination = destination+"/"+dirName
        #
        print("[*] Creating backup directory in the specified location: %s " % destination)
        #
        '''
        try:
            #
            os.mkdir(destination)
            #
        except Exception as e:
            #
            print("[!] Failed to create backup directory: %s " % e)
            #
            sys.exit(1)
            #
        '''
    else:
        #
        destination = destination+dirName
        #
        print("[*] Creating backup directory in the specified location: %s " % destination)
        #
        '''
        try:
            #
            os.mkdir(destination)
            #
        except Exception as e:
            #
            print("[!] Failed to create backup directory: %s " % e)
            #
            sys.exit(1)
            #
        '''
    #
    print("[*] Backup operation will utilize: %s " % destination )
    #
    destination = destination+'/'
    #
    return destination

def BackupOperation(source,destination):
    #
    print("[*] File copy sequence initiated ")
    #
    print("[*] The script will exit when complete...")
    #
    try:
        #
        shutil.copytree(source,destination,copy_function=shutil.copy)
        #
    except Exception as e:
        #
        print("[!] ERROR | Backup Operation Failed: %s " %  e)
        #
        time.sleep(3)
        #
        sys.exit(1)
        #
    timeStamp = str(time.ctime())
        #
    print("[*] Backup complete: %s " % timeStamp)
    #
    return

def main():
    #
    print("[*] Linux Backup Script ")
    #
    sourceDirectory = input("[+] Enter the path to the source directory (Default is the filesystem root) -> ")
    #
    if(sourceDirectory is ''):
        #
        sourceDirectory = '/'
        #
    destinationDirectory = input("[+] Enter the path to the destination directory-> ")
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
    backupDirectory = MakeBackupDirectory(destinationDirectory)
    #
    print("[*] Backup directory created at -> %s " % backupDirectory)
    #
    BackupOperation(sourceDirectory,backupDirectory)
    #
    print("[*] Backup operations are complete, departing...")
    #
    time.sleep(3)
    
if(__name__ == '__main__'):
    #
    main()
