import json

import requests
from utils.config_loader import load_config, get_api_key

class APIClient:
    def __init__(self):
        self.config = load_config()
        self.base_url = self.config["base_url"]
        self.country_url = self.config["country_url"]
        self.api_key = get_api_key()
        self.timeout = self.config["timeout"]

    def get_weather(self, city):
        url = f"{self.base_url}/weather"
        params = {"q": city, "appid": self.api_key}
        print("DEBUG params:", params)
        response = requests.get(url, params=params, timeout=self.timeout)
        print("DEBUG URL:", response.url)  # 👈 will show the full request
        print("DEBUG Status:", response.status_code)
        try:
            body = response.json()
            print("DEBUG Body (JSON):", body)
            print("DEBUG Body (formatted):", json.dumps(body, indent=2))
        except ValueError:
            print("DEBUG body (raw):", response.text[:500])
        return response


    def get_country(self, country):
        url = f"{self.country_url}/name/{country}"
        return requests.get(url, timeout=self.timeout)