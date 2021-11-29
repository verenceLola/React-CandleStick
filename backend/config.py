from starlette.config import Config
from databases import DatabaseURL

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URL = config("DATABASE_URL", cast=DatabaseURL)
