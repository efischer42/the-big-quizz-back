import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    PROJECT_NAME = "SideProject"

settings = Settings()
