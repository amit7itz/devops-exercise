#! /usr/bin/env python2.7

import BaseHTTPServer
import os
import mimetypes

SERVER_ADDRESS = ('0.0.0.0', 8888)
RESOURCES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources'))


class PandaHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    implements files http server. serves all the files in the resources directory
    """
    PAGE_TEMPLATE = """
    <html>
        <head>
            <title>BigService cool page</title>
        </head>
        <body>
            {body}
        </body>
    </html>
    """

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()

    def do_GET(self):
        real_path = os.path.join(RESOURCES_DIR, self.path[1:])
        if os.path.isfile(real_path):
            self._send_file(real_path)
        else:
            self._send_main_page()

    def _send_main_page(self):
        self.send_response(200)
        # sending headers for html
        self.send_header("Content-type", 'text/html')
        self.end_headers()

        # create links for all files in resources folder
        links_str = ''
        for f in os.listdir(RESOURCES_DIR):
            links_str += '<a href="{path}">{path}</a></br>'.format(path=f)

        # sending the html content
        self.wfile.write(self.PAGE_TEMPLATE.format(body=links_str))

    def _send_file(self, file_path):
        self.send_response(200)
        f = open(file_path, 'rb')

        # find out the proper content type for this file
        _, file_extension = os.path.splitext(file_path)
        content_type = self._get_content_type(file_extension)

        # sending headers - type, length, last modified
        self.send_header("Content-type", content_type)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()

        # sending the file itself
        self.wfile.write(f.read())

    @staticmethod
    def _get_content_type(extension):
        if not mimetypes.inited:
            mimetypes.init()
        extension_map = mimetypes.types_map.copy()
        return extension_map[extension]


def main():
    http_server = BaseHTTPServer.HTTPServer(SERVER_ADDRESS, PandaHTTPHandler)
    print 'Server start on address' + str(SERVER_ADDRESS)
    http_server.serve_forever()

if __name__ == '__main__':
    main()
