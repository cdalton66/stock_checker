import os

API_KEY = os.getenv("API_KEY", "your_api_key_here")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", os.getenv("MYSQL_ROOT_PASSWORD", "rootpass"))
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB", "stocks")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
)
