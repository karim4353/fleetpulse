# Changelog

All notable changes to the FleetPulse prototype will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-09-10

### Added
- Initial prototype scaffold for FleetPulse EV Fleet Telematics & Charging Optimizer
- Complete microservices architecture with Docker Compose setup
- Producer simulator for synthetic EV telemetry data generation
- Real-time streaming ingestion service with Kafka integration
- TimescaleDB storage for time-series telemetry data
- Feature processing pipeline for rolling window computations
- MLflow-based model training and tracking for SoH/RUL prediction
- FastAPI model serving endpoints for battery health predictions
- Heuristic charging optimization service (recommendations only)
- Basic React/TypeScript frontend dashboard
- Integration with Prometheus and Grafana for monitoring
- CI/CD pipeline with GitHub Actions
- Comprehensive documentation and runbooks
- Sample synthetic data and example API requests
- Security and privacy guidance for PII handling
- Demo orchestration scripts for end-to-end flow demonstration

### Technical Components
- Kafka + Zookeeper for event streaming
- TimescaleDB (PostgreSQL extension) for time-series storage
- MLflow server with local artifact store
- FastAPI services for ingestion, model serving, and optimization
- React frontend with basic fleet visualization
- Prometheus metrics collection
- Grafana dashboards for monitoring
- Docker containerization for all services
- Terraform and Kubernetes deployment examples

### Notes
- This is a CPU-only prototype for demonstrations and interviews
- No real-world vehicle or charger actuation - optimizer produces recommendations only
- Includes synthetic sample data only (< 10MB)
- Local development environment via Docker Compose
- Security best practices documented but implementation is demo-grade
