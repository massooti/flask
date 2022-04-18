
from enum import IntEnum
from pickle import TRUE
from flask import jsonify, request, url_for
from markupsafe import re
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.User import User
from src.database.Database import Database
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
import numpy as np
import pandas as pd
from collections import defaultdict
from src.models.GradeDocument import GradeDocument


def calRank(scoresList, courseName, courseWeight):

    sortedList = sorted(scoresList, reverse=True)
    # sortedRank = [sortedList.index(x, 1) for x in sortedList]
    # rankBasesd = list(map(xPlus, sortedIndex))
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
    fetchedRank = []
    meta = []
    for score in scoresList:
        if score in dicts:
            fetchedRank.append(dicts[score][0])
            meta.append(
                {"score": score, "rank": dicts[score][0], "w": courseWeight})

    return np.array([scoresList, fetchedRank, meta], dtype="object")


# @jwt_required()
def insert():
    gDoc = GradeDocument()
    json = request.get_json()
    # print(json[0]["math_scores"], 1111111111111111111111)
    myDict = {}
    # myDict["users"]
    # {'users': ['asd', 'asdasd', 'werwer', 'ertert', 'dfgdfg', 'cvbcvb', 'dfgd', 'dfgdfg'], 'math_scores': [18, 19, 20, 20, 15, 17, 18, 0], 'adab_scores': [10, 17, 18, 20, 15, 14, 20, 0], 'weights': {'math': 4, 'adab': 3}}

    df = pd.DataFrame(myDict)
    df["username"] = json[0]["users"]
    for courseName, scores in json[0]["scores"].items():
        getRanks = calRank(scores, courseName,
                           courseWeight=json[0]["weights"][courseName])
        val = {"rank": 1, "w": json[0]["weights"][courseName]}

        df[courseName] = getRanks[0]
        # df[courseName + "_rank"] = getRanks[1]
        # df[courseName + "_weight"] = json[0]["weights"][courseName]
        df[courseName] = getRanks[2]
        gDoc.courseWeights = json[0]["weights"]

    print(df)
    df = df.reset_index()  # make sure indexes pair with number of rows
    for index, rows in df.iterrows():
        gDoc.generateDoc(rows.to_dict())


def insertAgain():
    gDoc = GradeDocument()
    json = request.get_json()
    # print("\n", json[-1], "\n") {'courses': ['math', 'adab', 'pysics]}
    myDict = {}
    insertedCourses  = json[-1]["courses"]

    localScope = []
    localScores = []
    globalScores = []
    globalScope = []
    emptyList=[]
    exctractScoresTotal = []
    riazyScores = []
    df = pd.DataFrame(myDict)

    for i, key in enumerate(json[0]):
        exctractScoresViaClass = np.array(key["users"], dtype="object")
        # allArrays = np.append(allArrays, exctractScores[:, 3], axis = 0)
       
        # for j, val in enumerate(exctractScoresViaClass):
        #     print("i is {} and j is {}".format(i, j))
        #     if i ==j:
        #         localScope.append(val[3][0])
        #     elif 
        #     # print(globalScope)
        #     # exit()
        #     # globalScores
    



    print(exctractScoresViaClass)
    exit()


   

    return jsonify({"hekpp":"hi"})


   