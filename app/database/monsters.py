from bson.objectid import ObjectId

from .database import db


def retrieve_monsters():
    return db.monsters.find()


def retrieve_monster(_id: str):
    try:
        _id = ObjectId(_id)
    except:
        return None
    finally:
        return db.monsters.find_one({"_id": _id})
