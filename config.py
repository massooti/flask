# Statement for enabling the development environment
import os
from pickle import TRUE
from posix import environ
from pymongo import MongoClient


class Config(object):

    DEBUG = True

    DB_NAME = "production-db"
    DB_USERNAME = environ.get("DB_USER")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_PORT = environ.get("DB_PORT")
    DB_HOST = environ.get("DB_HOST")
    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the database - we are working with
    # SQLite for this example
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    # DATABASE_CONNECT_OPTIONS = {}

    DATABASE = MongoClient(host=environ.get("DB_HOST"),
                           port=environ.get("DB_PORT"),
                           username=environ.get("DB_USER"),
                           password=environ.get("DB_PASSWORD"),
                           )

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"
