import os
from fastapi import FastAPI

app = FastAPI(title="Docker Health Demo")

# Read application environment from environment variables
ENVIRONMENT = os.getenv("APP_ENV", "development")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": ENVIRONMENT
    }