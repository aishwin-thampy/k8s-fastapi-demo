from fastapi import FastAPI

app = FastAPI(title="K8s FastAPI Demo", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello from Kubernetes!", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def get_item(item_id: int, name: str = "unknown"):
    return {"item_id": item_id, "name": name}
