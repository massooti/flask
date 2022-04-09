from flask import Blueprint, jsonify, request, url_for
from src.controllers import UserController

mainRoutes = Blueprint('routes', __name__, url_prefix='/')


mainRoutes.route('/', methods=['GET'])(UserController.index)
mainRoutes.route('/register', methods=['POST'])(UserController.register)
