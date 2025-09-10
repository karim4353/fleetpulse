#!/usr/bin/env bash
set -e
echo "Starting demo orchestration (local, assumes docker-compose up done)"
echo "Run simulator in another shell: python services/producer_simulator/simulator.py --mode replay"
echo "Backfill features:"
python services/feature_processor/processor.py || true
echo "Train model (tiny):"
python services/model_training/train.py --mlflow-uri http://localhost:5000 --data data/sample_day.jsonl || true
echo "Check model server (mock if no model):"
curl -s -X POST http://localhost:8001/predict/soh -H 'Content-Type: application/json' -d @examples/sample_vehicle_state.json || true
echo "Request optimizer:"
curl -s -X POST http://localhost:8002/optimize/charging -H 'Content-Type: application/json' -d @examples/sample_optimize_request.json || true
echo "Demo finished. Open frontend: http://localhost:3001"
