
def test_get_weather_success(client):
    response = client.get("/weather?city=Mumbai")
    assert response.status_code == 200
    data = response.json()

    assert data["city"] == "Mumbai"
    assert "sources" in data


def test_get_weather_invalid_city(client):
    response = client.get("/weather?city=12345")
    assert response.status_code == 400