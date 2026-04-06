# -----------------------------
# Stage 1: Builder
# -----------------------------
    FROM python:3.11-slim AS builder

    WORKDIR /app
    
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    COPY requirements.txt .
    
    RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
    
    # -----------------------------
    # Stage 2: Runtime
    # -----------------------------
    FROM python:3.11-slim
    
    WORKDIR /app
    
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    COPY --from=builder /install /usr/local
    COPY app/ app/
    
    EXPOSE 8000
    
    CMD ["python", "-m", "app.main"]