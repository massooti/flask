
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
    for i, classObj in enumerate(json[0]):
        for j, insertedCourse in enumerate(classObj["scores"]):

            initialDf["class"] = classObj["class_id"]
            initialDf["username"] = classObj["users"]
            initialDf[insertedCourse] = classObj["scores"].get(insertedCourse)
            initialDf[insertedCourse +
                      "-l-Rank"] = getRank(classObj["scores"].get(insertedCourse))
            dfcloned = initialDf.copy()
        data.append(dfcloned)

    # generate final dataframe
    totalAzmoonScore = pd.concat([df.set_index("class")
                                  for df in data])
    # print(totalAzmoonScore.head())
    # exit()
    newCli = len(insertedCourses)  # set target  step for new indexes
    try:
        for i, insertedCourse in enumerate(insertedCourses):
            # print(newCli+1)
            totalAzmoonScore.insert(newCli+1, insertedCourse + "-g-Rank", getRank(
                totalAzmoonScore[insertedCourse].values.tolist()))
            newCli += newCli
    except:
        print(totalAzmoonScore.iloc[:, 1])
    print(totalAzmoonScore)


# """
#        username  math  math-l-Rank  math-g-Rank  adab  adab-g-Rank  adab-l-Rank
# class
# classA       a1    18            2            4    10            7            2
# classA       a2    19            1            3    17            3            1
# classB       b1    20            1            1    18            2            2
# classB       b2    20            1            1    20            1            1
# classC       c1    15            2            7    15            4            1
# classC       c2    17            1            6    14            6            2
# classD       d1    18            1            4    15            4            1
# classD       d2     0            2            8     0            8            2
#
#  """

    return jsonify({"hekpp": "hi"})
