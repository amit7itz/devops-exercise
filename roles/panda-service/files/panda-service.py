#! /usr/bin/env python2.7

import BaseHTTPServer
import os

SERVER_ADDRESS = ('0.0.0.0', 8888)
RESOURCES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources'))

class PandaHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        real_path = os.path.join(RESOURCES_DIR, self.path[1:])
        if not os.path.isfile(real_path):
            self.send_header("Content-type", 'text/html')
            self.end_headers()
            self.wfile.write("<html><head><title>BigService cool page</title></head>")
            self.wfile.write("<body>")
            for f in os.listdir(RESOURCES_DIR):
                self.wfile.write("<a href=\"{path}\">{path}</a></br>".format(path=f))
            self.wfile.write("</body></html>")
        else:
            f = open(real_path, 'rb')
            self.send_header("Content-type", 'image/png')
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            self.wfile.write(f.read())
        
def main():
    http_server = BaseHTTPServer.HTTPServer(SERVER_ADDRESS, PandaHTTPHandler)
    print 'Server start'
    http_server.serve_forever()

if __name__ == '__main__':
    main()

