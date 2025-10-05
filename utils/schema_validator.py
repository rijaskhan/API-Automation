from pydantic import BaseModel
from typing import List, Optional

class MainData(BaseModel):
    temp: float
    feels_like: Optional[float]
    temp_min: Optional[float]
    temp_max: Optional[float]
    pressure: Optional[int]
    humidity: Optional[int]

class WeatherDescription(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class WeatherSchema(BaseModel):
    name: str
    weather: List[WeatherDescription]
    main: MainData
    sys: dict

class CountrySchema(BaseModel):
    name: dict
    cca2: str
    region: str
    population: int
