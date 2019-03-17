#!/usr/bin/env python3

import subprocess
import binascii
import socket
import struct
import sys
import re

def ExtractMAC():
    #
    mac = subprocess.call('arp -a', shell=True)
    #
    filter = re.compile(u'([0-9a-fA-F]:?){12}')
    #
    output = re.findall(filter,mac)

def main():
    #
    ExtractMAC()

if(__name__ == '__main__'):
    #
    main()
