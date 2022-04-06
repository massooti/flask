from crypt import methods
from flask import Blueprint, jsonify, request, url_for
from app.controllers import UserController

mainRoutes = Blueprint('routes', __name__, url_prefix='/')


mainRoutes.route('/', methods=['GET'])(UserController.index)
mainRoutes.route('/create', methods=['POST'])(UserController.create)
