#!/usr/bin/env python

import http.server 

class HTTPHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        #
        command = input("[*]>>> ")
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
        length = int(self.headers['Content-length'])
        #
        postVariable = self.rfile.read(length)
        #
        print(postVariable.decode())

if(__name__ == '__main__'):
    #
    Server = http.server.HTTPServer 
    #
    httpd = Server(('127.0.0.1',8080), HTTPHandler)
    #
    try:
        #
        print("[*] HTTP Server Active [*]")
        #
        httpd.serve_forever() 
        #
    except KeyboardInterrupt:
        #
        print("[!] Server Process Terminated [!]")
        #
        httpd.server_close()