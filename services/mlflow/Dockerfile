FROM python:3.10-slim
WORKDIR /app
RUN pip install mlflow[extras]
CMD mlflow server --host 0.0.0.0 --port 5000 --default-artifact-root /ml/artifacts
