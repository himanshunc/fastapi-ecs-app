from fastapi import FastAPI
from app.routes.health import router as health_router
from app.config import APP_NAME, APP_ENV, APP_VERSION

app = FastAPI(title=APP_NAME)

# Include routes
app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}",
        "environment": APP_ENV,
        "version": APP_VERSION
    }

@app.get("/info")
def info():
    return {
        "app_name": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)