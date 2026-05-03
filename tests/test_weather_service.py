# tests/test_weather_service.py

import pytest
from service.external_clients import get_aggregated_weather


@pytest.mark.asyncio
async def test_aggregated_weather_success(monkeypatch):

    async def mock_wttr(city):
        return {"status": "success", "data": {"temp": "30C"}}

    async def mock_meteo(lat, lon):
        return {"status": "success", "data": {"temp": 30}}

    async def mock_go(city):
        return {"status": "success", "data": {"temp": "30"}}

    monkeypatch.setattr("app.service.weather_service.get_wttr_weather", mock_wttr)
    monkeypatch.setattr("app.service.weather_service.get_open_meteo", mock_meteo)
    monkeypatch.setattr("app.service.weather_service.get_go_weather", mock_go)

    result = await get_aggregated_weather("Mumbai")

    assert result["city"] == "Mumbai"
    assert result["sources"]["wttr"]["status"] == "success"