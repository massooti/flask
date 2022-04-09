from pickle import FALSE
from urllib import response
from flask import jsonify, request, url_for
from src.models.User import User
from src.models import Database
import jwt

user = User()


def index():
    return jsonify({"data": "hello world"})


def register():
    # print(Database.connection_params)
    username = request.json.get("username")
    password = request.json.get("password")
    # response = user.write(request1)
    print(response)
    return jsonify({"data": response}, status=201)
