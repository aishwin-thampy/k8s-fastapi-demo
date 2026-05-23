FastAPI on Kubernetes (Kind)

A REST API built with FastAPI, containerized with Docker, and deployed to a local Kubernetes cluster using Kind.

## Tech Stack
- **Python / FastAPI** — REST API
- **Docker** — Containerization
- **Kubernetes (Kind)** — Local cluster orchestration
- **kubectl** — Cluster management

### Prerequisites
- Docker, Kind, kubectl installed

### Run locally
docker build -t fastapi-demo:latest .
docker run -p 8000:8000 fastapi-demo:latest

### Deploy to Kubernetes
kind create cluster --name fastapi-cluster
kind load docker-image fastapi-demo:latest --name fastapi-cluster
kubectl apply -f k8s/
kubectl port-forward service/fastapi-service 8080:80

Visit http://localhost:8080/docs for the interactive API docs.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Root message |
| GET | /health | Health check |
| GET | /items/{id} | Get item by ID |
