from os import environ
from flask import Flask, request, json, Response
from pymongo import MongoClient
from flask import current_app, g


# class MongoApi:
#     def __init__(self, data):
#         self.client = MongoClient(environ.get('DB_HOST'))

#         database = data['database']
#         collection = data["collection"]
#         cursor = self.client[database]
#         self.collection = cursor[collection]
#         self.data = data
