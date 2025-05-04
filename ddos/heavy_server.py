from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class HeavyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Received request")
        time.sleep(3)  # Simulate slow processing
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Heavy load response")

server = HTTPServer(('127.0.0.1', 8000), HeavyHandler)
print("Heavy test server running on port 8000...")
server.serve_forever()
