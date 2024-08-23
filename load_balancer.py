from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Backend server URLs
backend_servers = ["http://backend1:5000", "http://backend2:5001"]
server_index = 0

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def load_balance(path):
    global server_index
    backend_url = backend_servers[server_index]
    server_index = (server_index + 1) % len(backend_servers)

    response = requests.get(f"{backend_url}/{path}")
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)