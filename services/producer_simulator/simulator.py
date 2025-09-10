#!/usr/bin/env python3
"""Simple Kafka producer simulator that emits JSON telemetry events."""
import argparse, asyncio, json, random, time, yaml, os
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

def generate_event(vehicle_id):
    t = datetime.now(timezone.utc).isoformat()
    soc = round(random.uniform(10, 100), 2)
    soh = round(80 + random.uniform(-5,5),2)
    lat = 37.77 + random.uniform(-0.05, 0.05)
    lon = -122.41 + random.uniform(-0.05, 0.05)
    return {
        "vehicle_id": vehicle_id,
        "timestamp": t,
        "soc": soc,
        "soh": soh,
        "lat": lat,
        "lon": lon,
        "speed": round(random.uniform(0,80),2),
        "temperature_c": round(15 + random.uniform(-10,20),2)
    }

def stream(args):
    # Simple loop that prints to stdout or writes to file OR sends to Kafka if confluent-kafka available.
    vehicles = [f"veh-{i:03d}" for i in range(1, args.fleet_size+1)]
    out_file = args.out or os.environ.get('OUT_FILE') or 'out/telemetry_sample.jsonl'
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    print(f"Streaming {args.rate} evt/s for {len(vehicles)} vehicles, output -> {out_file}")
    with open(out_file, 'a') as f:
        try:
            while True:
                for v in vehicles:
                    e = generate_event(v)
                    f.write(json.dumps(e) + '\n')
                    f.flush()
                    print(json.dumps(e))
                    time.sleep(1.0/args.rate)
        except KeyboardInterrupt:
            print("Stopped.")

def replay(args):
    # Read sample file once and print to stdout
    with open(args.scenario, 'r') as fh:
        cfg = yaml.safe_load(fh)
    # For convenience, create a small sample_day
    sample_out = 'out/replay_telemetry.jsonl'
    os.makedirs(os.path.dirname(sample_out), exist_ok=True)
    vehicles = cfg.get('vehicles', ['veh-001','veh-002','veh-003'])
    with open(sample_out,'w') as f:
        for ts in range(100):
            for v in vehicles:
                e = generate_event(v)
                f.write(json.dumps(e)+'\n')
    print(f"Wrote replay to {sample_out}")

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--scenario', required=False, default='examples/scenario_configs/sample.yaml')
    p.add_argument('--mode', choices=['stream','replay'], default='replay')
    p.add_argument('--fleet-size', type=int, default=3, dest='fleet_size')
    p.add_argument('--rate', type=float, default=1.0, help='events per second')
    p.add_argument('--out', default=None)
    args = p.parse_args()
    if args.mode == 'stream':
        stream(args)
    else:
        replay(args)
