from src.models.User import User
import hashlib


def run(db):
    dummyUser = {"username": "ttop-super-admin",
                 "password":  hashlib.sha256("a123456".encode("utf-8")).hexdigest()}
    doc = db.find_one(
        {"username": dummyUser["username"]})  # check if user exist
    if not doc:
        db.insert_one(dummyUser)


db = User().schema
# data seed
run(db)
