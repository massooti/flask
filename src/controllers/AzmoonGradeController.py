
from flask import jsonify, request
import numpy as np
import pandas as pd
from collections import defaultdict
from src.models.AzmoonGradeDocument import AzmoonGradeDocument


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
# @jwt_required()


def insertAzmoon():
    agDoc = AzmoonGradeDocument()
    json = request.get_json()
    # print("\n", json[-1], "\n") {'courses': ['math', 'adab', 'pysics]}
    initialDictionary = {}
    insertedCourses = json[-1]["courses"]
    initialDf = pd.DataFrame(initialDictionary)  # initializing dataframe
    data = []
    users = []
    GlobalUnitsScope = []
    LocalUnitsScope = []
    for i, classObj in enumerate(json[0]):
        users.extend(classObj["users"])
        for j, insertedCourse in enumerate(classObj["scores"]):
            LocalUnitsScope.append(classObj["scores"].get(insertedCourse))
            try:
                GlobalUnitsScope[j].extend(
                    classObj["scores"].get(insertedCourse))
            except:
                GlobalUnitsScope.append(classObj["scores"].get(insertedCourse))

    gU = np.asarray(GlobalUnitsScope)
    uU = np.asarray(users)
    lU = np.asarray(LocalUnitsScope)
    mat_f = np.column_stack((gU, lU))
    print(mat_f.tolist())
    # print(users)
    return jsonify({"hekpp": "hi"})
