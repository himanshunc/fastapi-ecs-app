import os

APP_NAME = os.getenv("APP_NAME", "fastapi-ecs-app")
APP_ENV = os.getenv("APP_ENV", "dev")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")