from flask import Blueprint, jsonify, request, url_for
from src.controllers import UserController

mainRoutes = Blueprint('routes', __name__, url_prefix='/v1')


mainRoutes.route('/', methods=['GET'])(UserController.index)
mainRoutes.route('/sign-in', methods=['POST'])(UserController.signIn)
mainRoutes.route('/sign-up', methods=['POST'])(UserController.signUp)
mainRoutes.route('/me', methods=['GET'])(UserController.profile)
