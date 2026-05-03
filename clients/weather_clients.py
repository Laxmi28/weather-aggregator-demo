import httpx
from fallbacks.fallback import (
    wttr_fallback,
    open_meteo_fallback,
    go_weather_fallback
)
from core.logger import logger
from core.config import settings

TIMEOUT = settings.API_TIMEOUT


async def safe_api_call(api_func, fallback_func, api_name: str, *args):
    try:
        logger.info(f"Calling external API | {api_name} | args={args}")

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await api_func(client, *args)

        logger.info(f"Success response | {api_name}")
        return response

    except Exception as e:
        logger.error(f"API failed | {api_name} | error={str(e)}")

        fallback = fallback_func(*args)

        logger.warning(f"Fallback triggered | {api_name}")
        return fallback


# ---- API implementations ---- #

async def _get_wttr(client: httpx.AsyncClient, city: str):
    url = f"{settings.WTTR_BASE_URL}/{city}?format=j1"
    res = await client.get(url)
    res.raise_for_status()
    return {"status": "success", "data": res.json()}


async def _get_open_meteo(client: httpx.AsyncClient, lat: float, lon: float):
    url = f"{settings.OPEN_METEO_BASE_URL}?latitude={lat}&longitude={lon}&current_weather=true"
    res = await client.get(url)
    res.raise_for_status()
    return {"status": "success", "data": res.json()}


async def _get_go_weather(client: httpx.AsyncClient, city: str):
    url = f"{settings.GO_WEATHER_BASE_URL}/{city}"
    res = await client.get(url)
    res.raise_for_status()
    return {"status": "success", "data": res.json()}


# ---- Public methods ---- #

async def get_wttr_weather(city: str):
    return await safe_api_call(_get_wttr, wttr_fallback, "WTTR", city)


async def get_open_meteo(lat: float, lon: float):
    return await safe_api_call(_get_open_meteo, open_meteo_fallback, "OPEN_METEO", lat, lon)


async def get_go_weather(city: str):
    return await safe_api_call(_get_go_weather, go_weather_fallback, "GO_WEATHER", city)