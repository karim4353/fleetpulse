-- Minimal telemetry table for TimescaleDB
CREATE TABLE IF NOT EXISTS telemetry (
  id SERIAL PRIMARY KEY,
  vehicle_id TEXT,
  ts TIMESTAMPTZ,
  soc DOUBLE PRECISION,
  soh DOUBLE PRECISION,
  lat DOUBLE PRECISION,
  lon DOUBLE PRECISION,
  speed DOUBLE PRECISION,
  temperature_c DOUBLE PRECISION
);
