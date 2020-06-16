from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import socket

address = ('localhost', 8080)

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('path = {}'.format(self.path))

        parsed_path = urlparse(self.path)
        
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        ip = ip.encode()
  
        self.send_header('Hello', 'BasicHTTP!')
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(ip)
        
server =  HTTPServer(address, MyHTTPRequestHandler)
server.serve_forever()
