#!/usr/bin/env python3
"""FastAPI application entrypoint"""
import os
from fastapi import FastAPI

app = FastAPI(title="Ubiquitous Couscous")


@app.get("/")
async def read_root():
    return {"message": "Hello from new-app"}

if __name__ == "__main__":
    # Run with: python src/main.py OR
    # uvicorn src.main:app --host 0.0.0.0 --port 8000
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
