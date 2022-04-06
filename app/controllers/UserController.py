from flask import jsonify, request, url_for


def index():
    return jsonify({"data": "hello world"})


def create():
