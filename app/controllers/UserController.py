from pickle import FALSE
from urllib import response
from flask import jsonify, request, url_for
from app.models.User import User
from app.models import Database

user = User()


def index():
    return jsonify({"data": "hello world"})


def create():
    # print(Database.connection_params)
    request1 = request.get_json()
    response = user.write(request, 2)
    return jsonify({"data": response}, status=201)
