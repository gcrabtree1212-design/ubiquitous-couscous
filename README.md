# Ubiquitous Couscous

A minimal FastAPI web application with Docker support and CI/CD.

## Quick Start

### Run locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python src/main.py
# OR
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

Visit http://localhost:8000 to see the app.

### Run with Docker
```bash
# Build the image
docker build -t ubiquitous-couscous .

# Run the container
docker run -p 8000:8000 ubiquitous-couscous
```

### Run tests
```bash
pytest -q
```

### Run linting
```bash
flake8
```

## CI/CD

The project uses GitHub Actions to:
- Run tests on Python 3.9, 3.10, and 3.11
- Run flake8 linting (non-blocking)
- Verify the app builds and tests pass on every push and pull request
