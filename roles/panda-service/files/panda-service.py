#! /usr/bin/env python2.7

import BaseHTTPServer
import SimpleHTTPServer
import os

RESOURCES_DIR_PATH = os.path.join(os.path.dirname(__file__),'resources')
SERVER_ADDRESS = ('0.0.0.0', 8888)

def start_http_server(dir_path, server_port):
    os.chdir(dir_path)
    http_server = BaseHTTPServer.HTTPServer(SERVER_ADDRESS, 
                                            SimpleHTTPServer.SimpleHTTPRequestHandler)
    http_server.serve_forever()


def main():
    start_http_server(RESOURCES_DIR_PATH, 8080)

if __name__ == '__main__':
    main()

