# tests/test_validators.py

import pytest
from utils.validators import validate_city
from fastapi import HTTPException


def test_valid_city():
    validate_city("Mumbai")  # should pass


def test_city_numeric():
    with pytest.raises(HTTPException):
        validate_city("12345")


def test_city_too_short():
    with pytest.raises(HTTPException):
        validate_city("A")


def test_city_too_long():
    with pytest.raises(HTTPException):
        validate_city("A" * 51)


def test_city_invalid_chars():
    with pytest.raises(HTTPException):
        validate_city("Mumbai@123")