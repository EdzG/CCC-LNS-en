"""Serve the repo for local study. / redirects to the study dashboard; everything else
(the course site at /index.html, chapters, slides) is served as files.

    python3 study/serve.py [--port 8000] [--lan]

Standard library only. Binds to localhost unless --lan (to open it from a phone on the same
network). The professor's index.html stays untouched: the redirect lives here.
"""
import argparse
import functools
import http.server
import socket
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path.startswith('/?'):
            self.send_response(302)
            self.send_header('Location', '/study/')
            self.end_headers()
            return
        super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')    # see edits to strings.json etc. at once
        super().end_headers()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--port', type=int, default=8000)
    ap.add_argument('--lan', action='store_true', help='listen on all interfaces, not just localhost')
    args = ap.parse_args()
    host = '0.0.0.0' if args.lan else '127.0.0.1'
    srv = http.server.ThreadingHTTPServer((host, args.port), functools.partial(Handler, directory=str(REPO)))
    print(f'Study dashboard: http://localhost:{args.port}/')
    if args.lan:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('10.255.255.255', 1))
            print(f'On your network:  http://{s.getsockname()[0]}:{args.port}/')
        except OSError:
            pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
