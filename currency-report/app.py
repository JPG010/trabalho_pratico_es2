from flask import Flask, request, jsonify
from datetime import datetime
import os
import threading
import time
import requests

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200


@app.route('/quote')
def quote():
    _from = request.args.get('from', 'USD')
    _to = request.args.get('to', 'BRL')
    base = 5.40
    variation = (int(time.time()) % 100) / 1000.0
    price = round(base + variation, 4)
    payload = {
        "from": _from,
        "to": _to,
        "price": price,
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }
    return jsonify(payload)

# função para registrar o serviço no naming server caso seja definido
def register_with_naming():
    naming = os.environ.get('NAMING_SERVER_URL')
    if not naming:
        return
    try:
        data = {"name": "currency-report", "url": f"http://{os.environ.get('SERVICE_HOST', 'currency-report')}:{os.environ.get('SERVICE_PORT', '8100')}"}
        requests.post(naming.rstrip('/') + '/register', json=data, timeout=2)
    except Exception:
        pass


if __name__ == '__main__':
    t = threading.Thread(target=register_with_naming, daemon=True)
    t.start()
    host = os.environ.get('SERVICE_HOST', '0.0.0.0')
    port = int(os.environ.get('SERVICE_PORT', 8100))
    app.run(host=host, port=port)

