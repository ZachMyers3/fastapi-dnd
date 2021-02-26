from bson.objectid import ObjectId


from .database import db


def retrieve_equipment(equipment_category: str = ""):
    if equipment_category:
        params = {"equipment_category": equipment_category}
    else:
        params = {}
    print(params)
    return db.equipment.find(params)


def retrieve_singular_equipment(_id: str):
    try:
        _id = ObjectId(_id)
    except:
        return None
    finally:
        return db.equipment.find_one({"_id": _id})
