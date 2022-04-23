# from flask import current_app as app
from src.database.Database import Database
from collections import defaultdict
# import pyjwt
import numpy as np
class AzmoonGradeDocument():

    coursesScore = None
    insertedCourses = None
    globalPureScores = None

    def __init__(self):
        self.database = Database().db
        self.schema = self.database['grade_document']

    def Calculate(self, json):

        self.insertedCourses = json[-1]["courses"]   # print("\n", json[-1], "\n") {'courses': ['math', 'adab', 'pysics]}

        self.coursesScores = []
        personalPureScores = []
 
        for i, classObj in enumerate(json[0]):
            for user in enumerate(classObj["users"]):
                scoresInArray = user[1][3]
                self.coursesScores.append(scoresInArray)
                try:
                    personalPureScores[i].append(scoresInArray)
                except:
                    personalPureScores.append([scoresInArray])

        self.globalPureScores = np.array(self.coursesScores).transpose()

        localPureScoresByCourse = [] # [[(15, 17, 16), (12, 13, 14), (23, 23, 23)], [(36, 37), (16, 18), (23, 23)]]
        for localScores in personalPureScores:
            localPureScoresByCourse.append(list(zip(*localScores)))


        ClassObjects = []
        for localClassIndex, localClassScorseByCourse in enumerate(localPureScoresByCourse):
    
            for usr in json[0][localClassIndex]["users"]:  
                users = self.participantDetails(usr, localRankInCourese=localClassScorseByCourse)
                ClassObjects.append({json[0][localClassIndex]["class_id"]:[users]}) #[{'A': []}, {'B': []}, {'C': []}, {'D': []}]


        azmoonDoc = self.schema.insert_one({"detail": ClassObjects})

        return azmoonDoc.inserted_id

         

    def participantDetails(self, user,localRankInCourese):
        courseDict = defaultdict(list)

        for i,insertedCourse in enumerate(self.insertedCourses):
            ranks = self.getRank(user[3][i], localRankInCourese[i], self.globalPureScores[i])
            score ={insertedCourse:{'score': user[3][i], "local-rank":ranks[0], "global-rank":ranks[1]}}
            courseDict["courses"].append(score)

        user[3] =  courseDict["courses"]

        return user


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



