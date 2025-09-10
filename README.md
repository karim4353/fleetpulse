# FleetPulse — Real-time EV Fleet Telematics & Charging Optimizer (Prototype)

**Elevator pitch:** FleetPulse is a prototype platform demonstrating end-to-end EV fleet telematics: simulator -> streaming ingestion -> timescale storage -> streaming feature pipeline -> offline training (MLflow) -> model serving -> charging optimizer -> dashboard. This repo is a CPU-only prototype for demos and hiring interviews. **No real-world actuation** — optimizer produces recommendations only.

## Architecture (placeholder)
```
[Simulator] -> Kafka -> [Ingestion] -> TimescaleDB
                         -> [Feature Processor] -> Feature Tables
                         -> [Model Training (MLflow)] -> [Model Server]
[Frontend] -> API Gateway -> Model Server / Optimizer
Monitoring: Prometheus + Grafana
```

## Quickstart (local)
Requirements: Docker, Docker Compose, Node (optional for frontend), Python 3.10+ (for local venv tasks).

1. Build & start stack:
   ```bash
   make up
   ```
   or
   ```bash
   docker-compose up --build
   ```

2. Stream simulator (in a new shell):
   ```bash
   python services/producer_simulator/simulator.py --scenario examples/scenario_configs/sample.yaml --mode stream
   ```

3. POST a sample event to ingestion HTTP endpoint:
   ```bash
   curl -X POST http://localhost:8000/ingest/telemetry -H 'Content-Type: application/json' -d @examples/sample_event.json
   ```

4. Train a tiny model and log to MLflow:
   ```bash
   python services/model_training/train.py --mlflow-uri http://localhost:5000 --data data/sample_day.jsonl
   ```

5. Predict SoH (model_server default port 8001):
   ```bash
   curl -X POST http://localhost:8001/predict/soh -H 'Content-Type: application/json' -d @examples/sample_vehicle_state.json
   ```

6. Request charging optimization:
   ```bash
   curl -X POST http://localhost:8002/optimize/charging -H 'Content-Type: application/json' -d @examples/sample_optimize_request.json
   ```

7. Run demo orchestration:
   ```bash
   make demo
   ```

## Project layout
See the repository top-level for folders and files. This prototype includes minimal, documented implementations for each component and sample data.

For developer run instructions, CI, monitoring notes, and security checklist see `docs/`.

