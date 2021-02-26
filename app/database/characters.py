from bson.objectid import ObjectId


from .database import db


def retrieve_characters():
    return db.characters.find()


def retrieve_character(_id: str):
    try:
        _id = ObjectId(_id)
    except:
        return None
    finally:
        return db.characters.find_one({"_id": _id})
