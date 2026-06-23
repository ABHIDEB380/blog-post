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
    POSTGRES_DB_URL= f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()