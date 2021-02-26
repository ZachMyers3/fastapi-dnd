from bson.objectid import ObjectId

from .database import db


def retrieve_spells():
    return db.spells.find()


def retrieve_spell(_id: ObjectId):
    return db.spells.find_one({"_id": _id})
