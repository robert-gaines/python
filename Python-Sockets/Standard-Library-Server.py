#!/usr/bin/env python

import socketserver 
import time 

host = '127.0.0.1'
#
port = 4444


def Now():
    #
    return time.ctime(time.time())

class ClientHandler(socketserver.BaseRequestHandler):
    #
    def Handle(self):
        #
        print(self.client_address, Now())
        #
        time.sleep(5)
        #
        while(True):
            #
            data = self.request.recv(1024)
            #
            if(not data):
                #
                break
                #
            reply = "[*] Connection acknowledged at-> %s " % Now()
            #
            self.request.send(reply.encode())
            #
        self.request.close()

resource = (host,port)
#
s = socketserver.ThreadingTCPServer(resource,ClientHandler)
#
s.serve_forever()