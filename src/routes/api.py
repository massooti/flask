from crypt import methods
from flask import Blueprint, jsonify, request, url_for
from src.controllers import UserController, GradeController

mainRoutes = Blueprint('routes', __name__, url_prefix='/v1')


mainRoutes.route('/', methods=['GET'])(UserController.index)
mainRoutes.route('/sign-in', methods=['POST'])(UserController.signIn)
mainRoutes.route('/sign-up', methods=['POST'])(UserController.signUp)
mainRoutes.route('/sign-out', methods=['POST'])(UserController.signOut)
mainRoutes.route('/me', methods=['GET'])(UserController.profile)


mainRoutes.route('/grade/insert', methods=["POST"])(GradeController.insert)
