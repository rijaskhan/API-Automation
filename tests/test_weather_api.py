import pytest
from utils.api_client import APIClient
from utils.custom_logger import Logger
from utils.schema_validator import WeatherSchema

client = APIClient()
custom_logger = Logger.log_gen()

@pytest.mark.parametrize("city", ["New York", "Los Angeles", "Chicago", "Kochi", "Idukki"])
def test_valid_city_weather(city):
    response = client.get_weather(city)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < client.timeout
    data = response.json()
    custom_logger.info(f"json response: {data}")
    WeatherSchema(**data)   # schema validation

def test_invalid_city_weather():
    response = client.get_weather("InvalidCityXYZ")
    assert response.status_code == 404

@pytest.mark.parametrize("city", ["London", "Paris", "Tokyo"])
def test_multiple_cities(city):
    response = client.get_weather(city)
    assert response.status_code == 200
