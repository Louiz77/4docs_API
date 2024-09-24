import os
from dotenv import load_dotenv

load_dotenv()

class APIConfig:
    BASE_URL = os.getenv("BASE_URL")
    EMAIL = os.getenv("EMAIL")
    SENHA = os.getenv("SENHA")
