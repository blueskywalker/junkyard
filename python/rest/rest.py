#!/usr/bin/env python

import sys, os, re, shutil, json, urllib, urllib2, BaseHTTPServer
import urlparse

# Fix issues with decoding HTTP responses
reload(sys)
sys.setdefaultencoding('utf8')

here = os.path.dirname(os.path.realpath(__file__))

class RESTRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        ''' GET Request '''

        if re.match(r"^/request(.*)",self.path):
            parsed = urlparse.urlparse(self.path)
            try:
                input_dir =  urlparse.parse_qs(parsed.query)['inputdir']
                output_dir = urlparse.parse_qs(parsed.query)['outputdir']

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write('{ "message" : "kick off converting"}')
            
            except KeyError:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write('{ "error" : "need parameters"}')
        else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write('{ "error" : "It is not a request"}')




def rest_server(port):
    'Starts the REST server'
    http_server = BaseHTTPServer.HTTPServer(('', port), RESTRequestHandler)
    print 'Starting HTTP server at port %d' % port
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    print 'Stopping HTTP server'
    http_server.server_close()

def main(argv):
    rest_server(8080)

if __name__ == '__main__':
    main(sys.argv[1:])
