from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_optimize():
    payload = {"vehicles":[{"vehicle_id":"veh-1","soc":20.0,"location":{"lat":0,"lon":0}},{"vehicle_id":"veh-2","soc":80.0,"location":{"lat":0,"lon":0}}],"charging_points":1}
    r = client.post('/optimize/charging', json=payload)
    assert r.status_code == 200
    assert 'schedule' in r.json()
