#!/usr/bin/env python3
import argparse, time, json, requests
p=argparse.ArgumentParser()
p.add_argument('--file', default='data/sample_day.jsonl')
p.add_argument('--url', default='http://localhost:8000/ingest/telemetry')
args=p.parse_args()
with open(args.file) as f:
    for l in f:
        j=json.loads(l)
        try:
            r=requests.post(args.url, json=j, timeout=2)
            print(r.status_code, r.text)
        except Exception as e:
            print('err', e)
        time.sleep(0.1)
