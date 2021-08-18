import os

DEBUG = True
Host = "localhost"
MONGODB_SETTINGS = {
    "db": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
    "port": 27017,
    "MONGODB_CONNECT": False
}
SECRET_KEY = os.environ.get("SECRET_KEY")
