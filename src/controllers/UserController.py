import hashlib
from urllib import response
from flask import jsonify, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.User import User
from src.database.Database import Database
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
import datetime

user = User()


# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         token = None
#         if 'x-access-tokens' in request.headers:
#             token = request.headers['x-access-tokens']

#         if not token:
#             return jsonify({'message': 'a valid token is missing'})
#         try:
#             data = jwt.decode(
#                 token, app.config['SECRET_KEY'], algorithms=["HS256"])
#             current_user = Users.query.filter_by(
#                 public_id=data['public_id']).first()
#         except:
#             return jsonify({'message': 'token is invalid'})

#         return f(current_user, *args, **kwargs)
#     return decorator


def index():
    return jsonify({"data": "hello world"})


def signIn():
    new_user = request.get_json()  # store the json body request
    new_user["password"] = hashlib.sha256(
        new_user["password"].encode("utf-8")).hexdigest()  # encrpt password
    # print(user.schema)
    doc = user.schema.find_one(
        {"username": new_user["username"]})  # check if user exist
    if not doc:
        user.schema.insert_one(new_user)
        return jsonify({'msg': 'User created successfully'}), 201
    else:
        return jsonify({'msg': 'Username already exists'}), 409


def signUp():
    login_details = request.get_json()  # store the json body request
    user_from_db = user.schema.find_one(
        {'username': login_details['username']})  # search for user in database

    if user_from_db:
        encrypted_password = hashlib.sha256(
            login_details['password'].encode("utf-8")).hexdigest()
        if encrypted_password == user_from_db['password']:
            token = create_access_token(
                identity=user_from_db['username'], expires_delta=datetime.timedelta(hours=2))  # create jwt token
            return jsonify(token=token), 200

    return jsonify({'msg': 'The username or password is incorrect'}), 401


@jwt_required()
def profile():
    current_user = get_jwt_identity()  # Get the identity of the current user
    user_from_db = user.schema.find_one({'username': current_user})
    if user_from_db:
        # delete data we don't want to return
        del user_from_db['_id'], user_from_db['password']
        return jsonify({'profile': user_from_db}), 200
    else:
        return jsonify({'msg': 'Profile not found'}), 404


@jwt_required()
def signOut():
    jti = get_jwt()["jti"]
    jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
    return jsonify(msg="Access token revoked")
