# from flask import current_app as app
from dataclasses import dataclass
from pickle import FALSE
from src.models.Database import Database
from posix import environ
from src.models.Database import Database

class User():
    def __init__(self):
        self.database = Database().db
        # print(self.db.db)
        # print(Database.db)
        pass

    def write(self, user):
        self.database.users.insert_one(user)
        return False
