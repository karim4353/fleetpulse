"""Simple offline feature materializer that reads out/ingested.jsonl and computes rolling features."""
import pandas as pd, json, os

def backfill(infile='out/ingested.jsonl', out_table='out/features.jsonl'):
    if not os.path.exists(infile):
        print('No input file', infile); return
    rows=[]
    with open(infile) as f:
        for l in f:
            rows.append(json.loads(l))
    df = pd.DataFrame(rows)
    if df.empty:
        print('empty')
        return
    # simple rolling avg soc per vehicle
    out=[]
    for vid, g in df.groupby('vehicle_id'):
        g = g.sort_values('timestamp')
        g['soc_roll3'] = g['soc'].rolling(3,min_periods=1).mean()
        out.append(g.to_dict(orient='records'))
    flat = [r for grp in out for r in grp]
    with open(out_table,'w') as f:
        for r in flat:
            f.write(json.dumps(r)+'\n')
    print('Wrote features to', out_table)

if __name__=='__main__':
    backfill()
