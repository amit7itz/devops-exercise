#! /usr/bin/env python2.7

import BaseHTTPServer

SERVER_ADDRESS = ('0.0.0.0', 7777)
get_request_counter = 0


class BigHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    implements handler for cools website that count your access to it :)
    """
    PAGE_TEMPLATE = """
    <html>
        <head>
            <title>BigService cool page</title>
        </head>
        <body>
            <h1>AHOY! you are visitor number {visitor_number}!</h1>
        </body>
    </html>
    """

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()
        visitor_number = self._get_visitor_number()
        self.wfile.write(self.PAGE_TEMPLATE.format(visitor_number=visitor_number))

    @staticmethod
    def _get_visitor_number(self):
        """
        increase the get requests counter by one and return its value
        """
        if 'get_request_counter' not in globals():
            global get_request_counter
            get_request_counter = 0
        get_request_counter += 1
        return get_request_counter


def main():
    http_server = BaseHTTPServer.HTTPServer(SERVER_ADDRESS, BigHTTPHandler)
    print 'Server start on address ' + str(SERVER_ADDRESS)
    http_server.serve_forever()

if __name__ == '__main__':
    main()

