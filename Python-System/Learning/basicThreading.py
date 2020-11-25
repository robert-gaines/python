#!/usr/bin/env python

import threading

def ThreadFunction(name):
    #
    print("[*] Executing threaded function %s \n" % name)

def main():
    #
    threads = []
    #
    for i in range(3):
        #
        t = threading.Thread(target=ThreadFunction,args=(i,))
        #
        threads.append(t)
        #
        t.start()
        #
    for j in threads:
        #
        print("Joining: %s \n" % j)
        #
        j.join()

if(__name__ == '__main__'):
    #
    main()
