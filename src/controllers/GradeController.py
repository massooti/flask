
from flask import jsonify, request, url_for
from markupsafe import re
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.User import User
from src.database.Database import Database
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
import numpy as np


@jwt_required()
def insert():

    json = request.get_json()

    users, weights = np.array(json[0].get(
        "users")), np.array(json[0].get("weights"))
    users = json[0].get(
        "users")
    print("*********************", "\n", "\n", "*********************", )
    # print(users, "\n", weights)
    print(np.array(users[0:2]))
    print("*********************", "\n", "\n", "*********************", )
    for courses in users:
        # print(courses["name"])
        numpy_2d_arrays = np.array([courses['name'], courses["courses"]])
        # numpy_2d_arrays = arr.append(arr)

    # print(numpy_2d_arrays)
    current_rank = 0
    global_rank = 0
    current_mark = 0

    # print(json[0]["users"])
    # print(numpy_2d_arrays)
    # print(1111111111111)
    return jsonify({"hell": "d"})


def pu():
    pass
