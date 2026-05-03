# app/routes/weather.py

from fastapi import APIRouter, Query

from core.logger import logger
from service.external_clients import get_aggregated_weather
from utils.validators import validate_city
from models.response_model import WeatherResponse

router = APIRouter()

@router.get("/weather", response_model=WeatherResponse)
async def fetch_weather(
    city: str = Query(...),
    latitude: float = Query(default=None),
    longitude: float = Query(default=None)
):
    logger.info(f"Incoming request | city={city}, lat={latitude}, lon={longitude}")
    validate_city(city)

    response = await get_aggregated_weather(city, latitude, longitude)
    logger.info(f"Response sent | city={city}")
    return response