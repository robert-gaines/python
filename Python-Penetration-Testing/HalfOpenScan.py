#!/usr/bin/env python3

from scapy.all import *

def CheckUser():
    #
    user = os.geteuid()
    #
    print("[*] User: ", user)
    #
    if(user == 0):
        #
        print("[*] User is root, Proceed ")
        #
        return
        #
    else:
        #
        print("[!] User is not root, exit ")
        #
        sys.exit()

def SendSYN(source,destination,source_port,destination_port):
    #
    ip_segment = IP(src=source,dst=destination)
    #
    tcp_segment = TCP(sport=source_port,dport=destination_port,flags="S",seq=12345)
    #
    packet = ip_segment/tcp_segment
    #
    print('''
            Sending SYN
            -----------
            Source           -> %s
            Destination      -> %s
            Source Port      -> %s
            Destination Port -> %s
          ''' % (source,destination,source_port,destination_port))
    #
    p = sr1(packet, inter=1)
    #
    if(p):
        #
        print()
        #
        print("[*] Response from-> ", p.src," on: ",p.sport," flag(s): ",p.flags)
        #
        return
        #
    else:
        #
        print("[!] No Response ")
        #
        return

def SendRST(source,destination,source_port,destination_port):
    #
    ip_segment = IP(src=source,dst=destination)
    #
    tcp_segment = TCP(sport=source_port,dport=destination_port,flags="R",seq=12347)
    #
    packet = ip_segment/tcp_segment
    #
    print('''
            Sending RST
            -----------
            Source           -> %s
            Destination      -> %s
            Source Port      -> %s
            Destination Port -> %s
          ''' % (source,destination,source_port,destination_port))
    #
    p = sr1(packet)
    #
    return

def main():
    #
    print("<-- Half Open Scan -->")
    #
    CheckUser()
    #
    source = input("[+] Enter the source IP-> ")
    #
    destination = input("[+] Enter the destination IP-> ")
    #
    source_port = int(input("[+] Enter the source port-> "))
    #
    destination_port = int(input("[+] Enter the destination port-> "))
    #
    SendSYN(source,destination,source_port,destination_port)
    #
    SendRST(source,destination,source_port,destination_port)

if(__name__ == '__main__'):
    #
    main()
