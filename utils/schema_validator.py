from pydantic import BaseModel
from typing import List, Optional

class WeatherSchema(BaseModel):
    name: str
    weather: List[dict]
    main: dict
    sys: dict

class CountrySchema(BaseModel):
    name: dict
    cca2: str
    region: str
    population: int
