from config import Config
from flask import current_app
from pymongo import MongoClient
from datetime import datetime
import os
# from serve import app


class Database(object):

    def __init__(self):
        connection_params = Config.connection_params
        self.client = MongoClient(
            'mongodb://{user}:{password}@{host}:'
            '{port}/{namespace}?retryWrites=true'.format(**connection_params)
        )
        # configure db name
        self.db = self.client[connection_params.get("name")]
