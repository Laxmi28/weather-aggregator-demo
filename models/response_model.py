# app/models/response_models.py

from pydantic import BaseModel
from typing import Any, Dict

class WeatherResponse(BaseModel):
    city: str
    coordinates: Dict[str, float]
    sources: Dict[str, Any]