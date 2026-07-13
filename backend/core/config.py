# This file will be used to config the project configuration
# by using settings object from core.config file
import os
from dotenv import load_dotenv
from pathlib import Path

ENV_PATH = Path(".") / '.env'
load_dotenv(dotenv_path=ENV_PATH)

POSTGRES_USER= os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB=os.getenv("POSTGRES_DB")
POSTGRES_PORT= os.getenv("POSTGRES_PORT")
POSTGRES_SERVER= os.getenv("POSTGRES_SERVER")
class Settings():
    PROJECT_NAME: str = "Blog Post📪"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_DB_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    PRIVATE_KEY: str = os.getenv("PRIVATE_KEY")
    PUBLIC_KEY:str=os.getenv("PUBLIC_KEY")
    JWT_ALGO:str= os.getenv("JWT_ALGO")
    JWT_ISSUER:str= os.getenv("JWT_ISSUER")
    JWT_AUDIENCE:str = os.getenv("JWT_AUDIENCE")
    JWT_EXPIRE_MINUTES:int= os.getenv("JWT_EXPIRE_MINUTES")

settings = Settings()