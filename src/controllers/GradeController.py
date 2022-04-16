
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



gDoc = GradeDocument()

def calRank(scoresList):

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
    for i in scoresList:
        if i in dicts:
            fetchedRank.append(dicts[i][0])

    return np.array([scoresList, fetchedRank], dtype="object")


def generateDoc(courses):
    print(courses.keys())
    exit()
    detail ={
        "username" : courses.users,
        "courses":{
            "math" : 13,

        }

    }

    # gDoc.schema.inser


# @jwt_required()
def insert():

    json = request.get_json()
    # print(json[0]["math_scores"], 1111111111111111111111)
    myDict = {}
    # myDict["users"]
    # {'users': ['asd', 'asdasd', 'werwer', 'ertert', 'dfgdfg', 'cvbcvb', 'dfgd', 'dfgdfg'], 'math_scores': [18, 19, 20, 20, 15, 17, 18, 0], 'adab_scores': [10, 17, 18, 20, 15, 14, 20, 0], 'weights': {'math': 4, 'adab': 3}}

    df = pd.DataFrame(myDict)
    df["users"] = json[0]["users"]
    for courseName, scores in json[0]["scores"].items():
        getRanks = calRank(scores)
        val ={"rank":1, "w":json[0]["weights"][courseName]}

        df[courseName] =   getRanks[0]
        df[courseName + "_rank"] = getRanks[1]
        df[courseName + "_weight"] = json[0]["weights"][courseName]

        
    # df["_meta"] = val

    # df.apply(generateDoc, axis="columns")
    # df.to_dict()
    print(df)
    # df = df.reset_index()  # make sure indexes pair with number of rows
    # for  index, rows in df.iterrows():
    #     # print(index, tuple(rows)[1])
    #     generateDoc(rows)

    exit()
    # print(df)
    # return jsonify({"hell": "d"})

