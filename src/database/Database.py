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
        )  # configure db url
        # configure db name
        self.db = self.client[connection_params.get("name")]

    # def insert(self, element, collection_name):
    #     element["created"] = datetime.now()
    #     element["updated"] = datetime.now()
    #     inserted = self.db[collection_name].insert_one(
    #         element)  # insert data to db
    #     return str(inserted.inserted_id)
