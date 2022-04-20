# from flask import current_app as app
from asyncio import selector_events
from dataclasses import dataclass
from pickle import FALSE
from src.database.Database import Database
from posix import environ
# import pyjwt
import numpy as np
import pandas as pd


class AzmoonGradeDocument():
    courseWeights = None

    coursesScore = None

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
        scores = {key: courses.get(key) for key in self.courseWeights}
        totalAverage = self.docFuck(scores)
        detail = {
            "username": courses["username"],
            # {'username': 'adasd', 'courses': {'math': 18, 'adab': 14}}
            "courses": scores,
            "totalAverage": totalAverage,
            "totalClassRank": "-",
            "totalGlobalRank": "-"

        }
        self.schema.insert_one(detail)
        print("check database")

    def Calculate(self, json):

        # print("\n", json[-1], "\n") {'courses': ['math', 'adab', 'pysics]}
        initialDictionary = {}
        insertedCourses = json[-1]["courses"]

        initialDf = pd.DataFrame(initialDictionary)  # initializing dataframe
        data = []
        users = []
        GlobalUnitsScope = []
        LocalUnitsScope = []
        localClassNames = []
        self.coursesScores = []
        # self.domesticScore = []
        scoreByCourse = {}
        pp = []
        data = {}
        for i, classObj in enumerate(json[0]):
            # users.append(classObj["users"])
            # data.append(self.coursesScores)
            for user in enumerate(classObj["users"]):
                scoresInArray = user[1][3]
                # pp.clear()
                i = pp.append(user[1][3])
                data[classObj["class_id"]] = 3213213
                # print(scoresInArray)
                # print(user[1][3][0][])
                # print(user, i, j, k, m, o)
                # exit()
                self.coursesScores.append(scoresInArray)
                for j, insertedCourse in enumerate(insertedCourses):
                    pass  # print(scoresInArray[0])
                    # pp.append(scoresInArray[j])
                    # print(pp)
                # exit()

        print(data)
        # exit()

        exit()
        pureScores = np.array(self.coursesScores)
        print(pureScores[..., 0])

        for pureScore in np.ndenumerate(pureScores):
            print(pureScore)

        # globalPureScores = np.array(self.coursesScores).transpose()


# """
#
# [
#     [
#             {
#             "class_id": "wersdf145",
#             "users": [
#                       ["name", "n_id", true, [15, 12, 23]],
#                       ["name", "n_id", true, [17, 13, 23]],
#                       ["name", "n_id", true, [16, 14, 23]]
#             ]
#     },
#     {
#             "class_id": "fdvg123",
#             "users": [
#                          ["name", "n_id", true, [36, 16, 23]],
#                          ["name", "n_id", true, [37, 18, 23]]
#             ]
#     }


# ],


# {
#     "courses": ["math", "adab", "physic"]
# }

# ]
#
#
#
#
#
#
#
#   """
