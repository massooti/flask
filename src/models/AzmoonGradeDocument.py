# from flask import current_app as app
from src.database.Database import Database
from collections import defaultdict
# import pyjwt
import numpy as np
import pandas as pd
import time


class AzmoonGradeDocument():
    courseWeights = None

    coursesScore = None
    insertedCourses = None
    globalPureScores = None

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
        start_time = time.time()
        initialDictionary = {}
        self.insertedCourses = json[-1]["courses"]   # print("\n", json[-1], "\n") {'courses': ['math', 'adab', 'pysics]}

        initialDf = pd.DataFrame(initialDictionary)  # initializing dataframe
        self.coursesScores = []
        personalPureScores = []
 
        colmns = ['', 'username', self.insertedCourses]
        for i, classObj in enumerate(json[0]):
            for user in enumerate(classObj["users"]):
                scoresInArray = user[1][3]
                self.coursesScores.append(scoresInArray)
                try:
                    personalPureScores[i].append(scoresInArray)
                except:
                    personalPureScores.append([scoresInArray])

        # pureScores = np.array(self.coursesScores ,ndmin=2)      
        self.globalPureScores = np.array(self.coursesScores).transpose()

        localPureScoresByCourse = [] # [[(15, 17, 16), (12, 13, 14), (23, 23, 23)], [(36, 37), (16, 18), (23, 23)]]
        for localScores in personalPureScores:
            localPureScoresByCourse.append(list(zip(*localScores)))

        for localClassIndex, localClassScorseByCourse in enumerate(localPureScoresByCourse):
    
            for usr in json[0][localClassIndex]["users"]:  
                self.userGen(usr, localRankInCourese=localClassScorseByCourse)




        print("--- %s seconds ---" % (time.time() - start_time))


    def userGen(self, username,localRankInCourese):
        arr = []
        for i,insertedCourse in enumerate(self.insertedCourses):
            ranks = self.getRank(username[3][i], localRankInCourese[i], self.globalPureScores[i])
            arr.append([{insertedCourse:{'score': username[3][i], "l-r":ranks[0], "g-r":ranks[1]}}])

        print(arr)



    def getRank(self, achivedScore, localScoresList, globalScoresList):
        def rankSorting(achivedScore, scoresList):
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

                dicts[score].append(counter)
                counter += 1
                


            return dicts[achivedScore][0]


        return [rankSorting(achivedScore,localScoresList), rankSorting(achivedScore, globalScoresList)]



