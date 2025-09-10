from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
import time
app = FastAPI(title='FleetPulse Optimizer')

class Vehicle(BaseModel):
    vehicle_id: str
    soc: float
    location: Dict[str,float]

class OptimizeRequest(BaseModel):
    vehicles: List[Vehicle]
    charging_points: int = 2
    start_time: str = None
    end_time: str = None

@app.post('/optimize/charging')
def optimize(req: OptimizeRequest):
    ts = time.time()
    # Simple heuristic: sort by lowest SOC and assign charging points round-robin.
    vehicles = sorted(req.vehicles, key=lambda v: v.soc)
    schedule = []
    for i, v in enumerate(vehicles):
        assigned_slot = i % req.charging_points
        schedule.append({'vehicle_id': v.vehicle_id, 'assigned_slot': int(assigned_slot), 'recommended_start': 'now+%dm' % (assigned_slot*15)})
    return {'schedule': schedule, 'latency_ms': int((time.time()-ts)*1000)}
