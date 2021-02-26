from bson.objectid import ObjectId

from .database import db


def retrieve_spells():
    return db.spells.find()


def retrieve_spell(_id: str):
    try:
        _id = ObjectId(_id)
    except:
        return None
    finally:
        return db.spells.find_one({"_id": _id})
