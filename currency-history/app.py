from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import os
import threading

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200


@app.route('/history')
def history():
    _from = request.args.get('from', 'USD')
    _to = request.args.get('to', 'BRL')
    now = datetime.utcnow()
    values = []
    base = 5.40
    for i in range(6):
        ts = (now - timedelta(minutes=5 - i)).isoformat() + 'Z'
        price = round(base + (i * 0.01), 4)
        values.append({"timestamp": ts, "price": price})
    return jsonify({"from": _from, "to": _to, "values": values})


# função para registrar o serviço no naming server caso seja definido
def register_with_naming():
    naming = os.environ.get('NAMING_SERVER_URL')
    if not naming:
        return
    try:
        import requests
        data = {"name": "currency-history", "url": f"http://{os.environ.get('SERVICE_HOST', 'currency-history')}:{os.environ.get('SERVICE_PORT', '8101')}"}
        requests.post(naming.rstrip('/') + '/register', json=data, timeout=2)
    except Exception:
        pass


if __name__ == '__main__':
    t = threading.Thread(target=register_with_naming, daemon=True)
    t.start()
    host = os.environ.get('SERVICE_HOST', '0.0.0.0')
    port = int(os.environ.get('SERVICE_PORT', 8101))
    app.run(host=host, port=port)

