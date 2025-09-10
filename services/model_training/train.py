import argparse, json, os, joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import mlflow

def load_data(path):
    rows=[]
    with open(path) as f:
        for l in f:
            rows.append(json.loads(l))
    return pd.DataFrame(rows)

def train(args):
    df = load_data(args.data)
    if df.empty:
        print('no data'); return
    X = df[['soc','speed','temperature_c']].fillna(0)
    y = df['soh'].fillna(90)
    mlflow.set_tracking_uri(args.mlflow_uri)
    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=10)
        model.fit(X,y)
        mlflow.log_param('n_estimators', 10)
        mlflow.sklearn.log_model(model, 'model')
        # save local copy
        os.makedirs('ml/models', exist_ok=True)
        joblib.dump(model, 'ml/models/example_model.pkl')
        print('Saved model to ml/models/example_model.pkl')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--mlflow-uri', default='http://localhost:5000')
    p.add_argument('--data', default='data/sample_day.jsonl')
    args=p.parse_args()
    train(args)
