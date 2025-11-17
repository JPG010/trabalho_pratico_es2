import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_health():
    client = app.test_client()
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json.get('status') == 'UP'


def test_history():
    client = app.test_client()
    r = client.get('/history?from=USD&to=BRL')
    assert r.status_code == 200
    assert r.json['from'] == 'USD'
    assert r.json['to'] == 'BRL'
    assert isinstance(r.json['values'], list)
    assert len(r.json['values']) > 0
    assert 'timestamp' in r.json['values'][0]
    assert 'price' in r.json['values'][0]

