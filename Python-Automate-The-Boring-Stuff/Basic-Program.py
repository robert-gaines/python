#!/usr/bin/env python3 

# Simple greeting #


def main():
    #
    print("[*] Hello user...")
    #
    name = input("[+] What is your name? ")
    #
    print("[*] Greetings, %s " % (name))
    #
    return

if(__name__ == '__main__'):
    #
    main()