from utils.api_client import APIClient
from utils.schema_validator import CountrySchema

client = APIClient()

def test_valid_country():
    response = client.get_country("India")
    assert response.status_code == 200
    data = response.json()[0]
    CountrySchema(**data)

def test_invalid_country():
    response = client.get_country("NoCountry123")
    assert response.status_code == 404
