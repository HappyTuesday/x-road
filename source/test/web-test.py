#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        buf = 'Hello world'
        self.protocal_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header('Welcome','Contect')
        self.end_headers()
        self.wfile.write(buf)

def start_service(port):
    http_server = HTTPServer(('',int(port)),HTTPRequestHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_service(80)

