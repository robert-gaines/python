#!/usr/bin/env python3

import httplib2
import shelve

def main():
    #
    print("<-- Login Page Locator -->")
    #
    print()
    #
    subject_url = input("[+] Enter the URL-> ")
    #
    url_alt_one = subject_url.replace("http://","")
    #
    url_alt_two = url_alt_one.replace("/","")
    #
    shelf = shelve.open("page_data.txt",writeback=True)
    #
    for u in shelf['php']:
        #
        slash_char = "/"
        #
        url_alt_final = url_alt_two+slash_char+u
        #
        print("[*] Testing %s " % (url_alt_final))
        #
        req = httplib.HTTPConnection(url_alt_final)
        #
        req.request("GET",u)
        #
        reply = req.getresponse()
        #
        if(reply.status == 200):
            #
            print("[*] URL Found -> %s " % url_alt_final)
            #
            sentinel = input("[+] Press 'C' to continue-> ")
            #
            if(c in sentinel or C in sentinel):
                #
                continue
                #
            else:
                #
                break
                #
    shelf.close()

if(__name__ == '__main__'):
    #
    main()
