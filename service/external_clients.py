# app/service/weather_service.py
from core.logger import logger

from clients.weather_clients import (
    get_wttr_weather,
    get_open_meteo,
    get_go_weather
)
from core.config import settings


import asyncio

async def get_aggregated_weather(city: str, latitude: float = None, longitude: float = None):
    logger.info(f"Incoming request | city={city}, lat={latitude}, lon={longitude}")

    lat = latitude if latitude else settings.DEFAULT_LATITUDE
    lon = longitude if longitude else settings.DEFAULT_LONGITUDE

    # Parallel API calls (IMPORTANT for performance)
    wttr_task = get_wttr_weather(city)
    meteo_task = get_open_meteo(lat, lon)
    go_weather_task = get_go_weather(city)

    wttr_res, meteo_res, go_res = await asyncio.gather(
        wttr_task, meteo_task, go_weather_task, return_exceptions=True
    )

    return {
        "city": city,
        "coordinates": {
            "latitude": lat,
            "longitude": lon
        },
        "sources": {
            "wttr": wttr_res,
            "open_meteo": meteo_res,
            "go_weather": go_res
        }
    }