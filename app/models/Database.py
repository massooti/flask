from flask import Flask
from flask import current_app as app


# app = Flask(__name__)

client = app.config["DATABASE"]

db = client.test_database

POSTS_COLLECTION = db.users
# USERS_COLLECTION = DATABASE.users
# SETTINGS_COLLECTION = DATABASE.settings
