from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os, asyncio, json
from datetime import datetime

app = FastAPI(title='FleetPulse Ingestion')

DATABASE_URL = os.environ.get('DATABASE_URL','postgresql://fleet:example@localhost:5432/fleetpulse')

class Telemetry(BaseModel):
    vehicle_id: str
    timestamp: datetime
    soc: float = Field(ge=0, le=100)
    soh: float = Field(ge=0, le=100)
    lat: float
    lon: float
    speed: float
    temperature_c: float

@app.post('/ingest/telemetry')
async def ingest(event: Telemetry):
    # Very small demo: accept and append to local file, and pretend to write to DB.
    out = 'out/ingested.jsonl'
    with open(out,'a') as f:
        f.write(event.json() + '\n')
    return {'status':'ok','written_to':'out/ingested.jsonl'}
