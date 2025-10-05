import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

def load_config():
    with open("config/config.json") as f:
        return json.load(f)

def get_api_key():
    return os.getenv("API_KEY")