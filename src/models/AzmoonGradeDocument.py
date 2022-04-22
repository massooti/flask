# from flask import current_app as app
from asyncio import selector_events
from dataclasses import dataclass
from pickle import FALSE
from src.database.Database import Database
from collections import defaultdict
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

        initialDictionary = {}
        insertedCourses = json[-1]["courses"]   # print("\n", json[-1], "\n") {'courses': ['math', 'adab', 'pysics]}

        initialDf = pd.DataFrame(initialDictionary)  # initializing dataframe
        GlobalUnitsScope = []
        LocalUnitsScope = []
        localClassNames = []
        self.coursesScores = []
        scoreByCourse = {}
        pp = []
        data = {}
        users = []
        colmns = ['', 'username', insertedCourses]
        for i, classObj in enumerate(json[0]):
            for user in enumerate(classObj["users"]):
                scoresInArray = user[1][3]
                self.coursesScores.append(scoresInArray)
                try:
                    users[i].append(user[1][0])
                    pp[i].append(scoresInArray)
                except:
                    pp.append([scoresInArray])
                    users.append([user[1][0]])

        pureScores = np.array(self.coursesScores ,ndmin=2)      

        globalPureScores = np.array(self.coursesScores).transpose()
        # print(globalPureScores)
        # exit()
        yu = [] # [[(15, 17, 16), (12, 13, 14), (23, 23, 23)], [(36, 37), (16, 18), (23, 23)]]
        for n,localScores in enumerate(pp):
            yu.append(list(zip(*localScores)))

        print(users, "\n",yu)
        exit()
        for localClassIndex, localClassScorseByCourse in enumerate(yu):
            for localClassUsersInsex,username in enumerate(users):
                for insertedCourseIndex, insertedCourse in enumerate(insertedCourses):
                    # print(localClassIndex, localClassScorseByCourse, localClassUsersInsex,username, localClassUsersInsex, insertedCourse)
                    # pass
                    self.userGen(username, localRankInCoures=localClassScorseByCourse[insertedCourseIndex], inCourse = insertedCourse)

        # for user in users:
        #     self.userGen(user)


    def userGen(self, username,localRankInCoures, inCourse, **kwargs):
        print(username, localRankInCoures, inCourse)
        # exit()

    def getRank(scoresList):
        sortedList = sorted(scoresList, reverse=True)

        scores = []
        globalRanks = []
        counter = 1
        dicts = defaultdict(list)
        for score in sortedList:
            if len(scores) == 0:
                scores.append(score)
                globalRanks.append(counter)
            elif score == scores[0]:
                scores.append(score)
                globalRanks.append(globalRanks[-1])
            elif score != scores[0]:
                scores.clear()
                scores.append(score)
                globalRanks.append(counter)

            dicts[score] .append(counter)
            counter += 1
        # TODO: should improve
        fetchedLocalRank = []
        for score in scoresList:
            if score in dicts:
                fetchedLocalRank.append(dicts[score][0])
        return fetchedLocalRank



