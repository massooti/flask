
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


def calRank(scoresList):

    sortedList = sorted(scoresList, reverse=True)
    sortedRank = [sortedList.index(x, 1) for x in sortedList]
    # rankBasesd = list(map(xPlus, sortedIndex))
    scores = []
    ranks = []
    counter = 1
    dicts = {}
    for score in sortedList:
        if len(scores) == 0:
            scores.append(score)
            ranks.append(counter)
        elif score == scores[0]:
            scores.append(score)
            ranks.append(ranks[-1])
        elif score != scores[0]:
            scores.clear()
            scores.append(score)
            ranks.append(counter)

        dicts[score] = counter
        counter += 1

    fetchedRank = []
    for i in scoresList:
        print(i, dicts[i])
        if i == dicts[i]:
            fetchedRank.append(dicts[i])

    # print( "\n", fetchedRank)

    arr = np.array([scoresList, fetchedRank], dtype="object")
    print(arr)
    exit()
    return arr
    # print(sortedList, "\n", "\n", ranks, "\n", dicts)
    # return dicts


@jwt_required()
def insert():

    json = request.get_json()
    # print(json[0]["math_scores"], 1111111111111111111111)
    myDict = {}
    # myDict["users"]
    # {'users': ['asd', 'asdasd', 'werwer', 'ertert', 'dfgdfg', 'cvbcvb', 'dfgd', 'dfgdfg'], 'math_scores': [18, 19, 20, 20, 15, 17, 18, 0], 'adab_scores': [10, 17, 18, 20, 15, 14, 20, 0], 'weights': {'math': 4, 'adab': 3}}
    ranks = []
    df = pd.DataFrame(myDict)
    df["users"] = json[0]["users"]
    df["math_scores"] = json[0]["math_scores"]
    fetchRankScores = calRank(json[0]["math_scores"])

    return jsonify({"hell": "d"})


def pu():
    pass
