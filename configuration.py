import os

ENV = os.environ.get("ENV","test")

DATABASE_URL_PROD = os.environ.get("DATABASE_URL_PROD","postgresql://postgres:root@localhost:5432/afabd")
DATABASE_URL_TEST = os.environ.get("DATABASE_URL_TEST","sqlite:///./database.db")

OAUTH_SECRET_KEY = os.getenv("OAUTH_SECRET_KEY", "SECRET")
OAUTH_ALGORITHM = os.getenv("OAUTH_ALGORITHM", "HS256")
OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("OAUTH_TOKEN_EXPIRE", "30"))