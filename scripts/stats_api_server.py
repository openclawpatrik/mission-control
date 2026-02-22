#!/usr/bin/env python3
import json, os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = os.environ.get('STATS_API_HOST', '127.0.0.1')
PORT = int(os.environ.get('STATS_API_PORT', '8787'))
API_KEY = os.environ.get('STATS_API_KEY', '')
CORS_ORIGIN = os.environ.get('STATS_API_CORS', '*')
ROOT = '/Users/bob/.openclaw/workspace'

class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', CORS_ORIGIN)
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, x-api-key')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')

    def _auth_ok(self):
        if not API_KEY:
            return True
        return self.headers.get('x-api-key', '') == API_KEY

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path.split('?')[0] not in ['/system_stats', '/system_stats.json', '/healthz']:
            self.send_response(404); self._cors(); self.end_headers(); return
        if self.path.startswith('/healthz'):
            self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b'ok'); return
        if not self._auth_ok():
            self.send_response(401); self._cors(); self.end_headers(); self.wfile.write(b'unauthorized'); return
        try:
            with open(f'{ROOT}/system_stats.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            payload = json.dumps(data, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers(); self.wfile.write(str(e).encode('utf-8'))

if __name__ == '__main__':
    s = ThreadingHTTPServer((HOST, PORT), H)
    print(f'stats api on http://{HOST}:{PORT}')
    s.serve_forever()
