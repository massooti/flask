# from flask import current_app as app
from dataclasses import dataclass
from pickle import FALSE
from src.database.Database import Database
from posix import environ
# import pyjwt



class GradeDocument():
    def __init__(self):
        self.database = Database().db
        self.schema = self.database['grade_document']

    # def signIn(self, user):

    #     # self.database.users.insert_one(user)
    #     return False
