def wttr_fallback(city: str):
    return {
        "status": "fallback",
        "message": f"wttr service unavailable for {city}",
        "data": {}
    }

def open_meteo_fallback(lat: float, lon: float):
    return {
        "status": "fallback",
        "message": f"open-meteo unavailable for coordinates ({lat}, {lon})",
        "data": {}
    }

def go_weather_fallback(city: str):
    return {
        "status": "fallback",
        "message": f"goWeather service unavailable for {city}",
        "data": {}
    }