from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_ingest_ok():
    payload = {
        "vehicle_id":"veh-001",
        "timestamp":"2025-09-10T00:00:00Z",
        "soc":50.0,"soh":90.0,"lat":0.0,"lon":0.0,"speed":10.0,"temperature_c":25.0
    }
    r = client.post('/ingest/telemetry', json=payload)
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'
