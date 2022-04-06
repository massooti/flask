# Statement for enabling the development environment
import os
from pickle import TRUE
from pymongo import MongoClient


class Config():

    DEBUG = False

    connection_params = {
        'name': os.environ.get('DB_NAME'),
        'user': os.environ.get("DB_USER"),
        'password': os.environ.get("DB_PASSWORD"),
        'host': os.environ.get("DB_HOST"),
        'port': os.environ.get("DB_PORT"),
        'namespace': '',
    }


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