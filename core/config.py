import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    WTTR_BASE_URL = os.getenv("WTTR_BASE_URL")
    OPEN_METEO_BASE_URL = os.getenv("OPEN_METEO_BASE_URL")
    GO_WEATHER_BASE_URL = os.getenv("GO_WEATHER_BASE_URL")

    DEFAULT_LATITUDE = float(os.getenv("DEFAULT_LATITUDE", 19.07))
    DEFAULT_LONGITUDE = float(os.getenv("DEFAULT_LONGITUDE", 72.87))

    API_TIMEOUT = float(os.getenv("API_TIMEOUT", 5))


settings = Settings()