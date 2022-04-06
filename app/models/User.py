# from flask import current_app as app
from dataclasses import dataclass
from pickle import FALSE
from app.models.Database import Database
from posix import environ

# db = Database()
# print(db.client)


class User():
    def __init__(self):
        self.db = Database()
        print(self.db.db)
        # print(Database.db)
        pass

    def write(self, user):
        res = self.db.insert()
        return False
