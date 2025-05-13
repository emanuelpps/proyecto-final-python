from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class LogServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            message = data.get("message", "Sin mensaje")

            with open("logs.txt", "a", encoding="utf-8") as f:
                f.write(f"{message}\n")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Log recibido correctamente.")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error al procesar log: {e}".encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Servidor de logs activo</h1>")

if __name__ == "__main__":
    server_address = ('localhost', 9090)
    httpd = HTTPServer(server_address, LogServer)
    print("Servidor de logs escuchando en http://localhost:9090")
    httpd.serve_forever()