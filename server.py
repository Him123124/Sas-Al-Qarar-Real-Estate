"""Tiny server for the Sas Al-Qarar site (Python standard library only).
Serves the static pages and saves contact-form messages to data/messages.jsonl.
Run:  python3 server.py   then open http://localhost:8000
"""
import json, os, re, time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "data", "messages.jsonl")
PORT = int(os.environ.get("PORT", 8000))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def _json(self, code, obj):
        data = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != "/api/contact":
            return self._json(404, {"error": "not found"})
        try:
            size = int(self.headers.get("Content-Length", 0))
            if not 0 < size < 10_000:
                raise ValueError
            d = json.loads(self.rfile.read(size))
            name, phone, msg = (str(d.get(k, "")).strip() for k in ("name", "phone", "message"))
            if len(name) < 2 or len(msg) < 2 or not re.fullmatch(r"[0-9+\s-]{7,16}", phone):
                raise ValueError
        except (ValueError, json.JSONDecodeError):
            return self._json(400, {"error": "invalid data"})
        rec = {"time": time.strftime("%Y-%m-%d %H:%M:%S"), "type": str(d.get("type", ""))[:20],
               "name": name[:100], "phone": phone, "message": msg[:2000]}
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self._json(200, {"ok": True})

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def do_GET(self):
        if self.path.startswith("/data") or self.path.endswith((".py", ".md")):
            return self.send_error(404)  # keep messages and source private
        super().do_GET()

if __name__ == "__main__":
    print(f"Serving on http://localhost:{PORT}  (Ctrl+C to stop)")
    ThreadingHTTPServer(("", PORT), Handler).serve_forever()
