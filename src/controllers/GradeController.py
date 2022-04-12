
from flask import jsonify, request, url_for
from markupsafe import re
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.User import User
from src.database.Database import Database
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
import numpy as np
import pandas


@jwt_required()
def insert():

    json = request.get_json()
    users, weights = np.array(json[0]["users"]), np.array(json[0]["weights"])

    print(users, "\n", "||||||||||||||||||||||||||||||||||||||||||||||",
          "\n")

    # array = np.array([4, 2, 7, 1])
    # temp = array.argsort()
    # ranks = np.empty_like(temp)
    # ranks[temp] = np.arange(len(array))
    # print(array, "\n", ranks)
    math_marks = []
    for courses in users:
        scores = courses[4]
        # print(scores[0])
        math_marks.append(scores[0])
    current_rank = 0
    global_rank = 0
    current_mark = 0
    print(math_marks)
    for mark in math_marks:
        global_rank += 1
        if mark != current_rank:
            current_mark = mark
            current_rank = global_rank
        print(current_mark, current_rank)

##[18, 17, 20, 20, 17, 17, 18, 0]
# 18 1
# 17 2
# 20 3
# 20 4
# 17 5
# 17 6
# 18 7
# 0 8
#
#
#
        return jsonify({"hell": "d"})


def pu():
    pass
