FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN pip install flask gunicorn
COPY app.py .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]