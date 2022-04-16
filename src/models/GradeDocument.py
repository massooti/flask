# from flask import current_app as app
from asyncio import selector_events
from dataclasses import dataclass
from pickle import FALSE
from src.database.Database import Database
from posix import environ
# import pyjwt



class GradeDocument():
    courseWeights = None
    def __init__(self):
        self.database = Database().db
        self.schema = self.database['grade_document']


    def docFuck(self, scores):
        totalWeight = sum(self.courseWeights.values())
        finalScore = []
        for key in scores.items():
            finalScore.append(key[1]["score"] * key[1]["w"])


        return sum(finalScore) / totalWeight

    def generateDoc(self, courses):
        scores = {key:courses.get(key) for key in self.courseWeights}
        totalAverage = self.docFuck(scores)
        detail ={
            "username" : courses["username"],
            "courses": scores ,# {'username': 'adasd', 'courses': {'math': 18, 'adab': 14}}
            "totalAverage" : totalAverage,
            "totalClassRank" : "-",
            "totalGlobalRank": "-"

        }
        self.schema.insert_one(detail)
        print("check database")

