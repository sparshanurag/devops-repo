from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Blue/Green - Deployment"}

@app.get("/health")
def health():
    return {"status": "ok"}