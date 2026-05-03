# app/main.py

from fastapi import FastAPI
from routes.weather_routes import router as weather_router

app = FastAPI(title="Weather Aggregator API")

app.include_router(weather_router)