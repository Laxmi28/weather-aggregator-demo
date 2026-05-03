# app/utils/utils.py

import re
from fastapi import HTTPException

def validate_city(city: str):
    if not (2 <= len(city) <= 50):
        raise HTTPException(status_code=400, detail="City length must be between 2 and 50")

    if city.isnumeric():
        raise HTTPException(status_code=400, detail="City cannot be only numeric")

    if not re.match("^[a-zA-Z ]+$", city):
        raise HTTPException(status_code=400, detail="City must contain only alphabets and spaces")