#!/usr/bin/env python3

import subprocess
import time
import sys
import os

def main():
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
    for user in other_users:
        #
        subprocess.call(['userdel','-r',user])
        #
        subprocess.call(['groupdel',user])
        #
        path = "/home/%s" % user
        #
        subprocess.call(['rm','-rf',path])
        #
        path = "/var/mail/%s" % user
        #
        subprocess.call(['rm','-rf',path])
main()
