#! /usr/bin/env python2.7

import BaseHTTPServer

SERVER_ADDRESS = ('0.0.0.0', 7777)

class BigHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()

    def do_GET(self):
        if not 'get_request_counter' in globals():
            global get_request_counter
            get_request_counter = 0
        get_request_counter += 1
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()
        self.wfile.write("<html><head><title>BigService cool page</title></head>")
        self.wfile.write("<body>")
        self.wfile.write("<h1>AHOY! you are visitor number {0}!</h1>".format(get_request_counter))
        self.wfile.write("</body></html>")
        
def main():
    http_server = BaseHTTPServer.HTTPServer(SERVER_ADDRESS, BigHTTPHandler)
    print 'Server start'
    http_server.serve_forever()

if __name__ == '__main__':
    main()

