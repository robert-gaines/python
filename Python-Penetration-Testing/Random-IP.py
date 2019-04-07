#!/usr/bin/env python3

import random

def RandomIP():
    #
    random_addr = ""
    #
    for i in range(1,4):
        #
        value = random.randint(1,255)
        #
        random_addr += str(value)+'.'
        #
    random_addr = random_addr+str(random.randint(1,255))
    #
    return random_addr

if(__name__ == '__main__'):
    #
    addr = RandomIP()
    #
    print("[*] Random IP-> %s " % (addr))
