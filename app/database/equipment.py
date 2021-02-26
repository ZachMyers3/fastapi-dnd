from .database import db


def retrieve_equipment(equipment_category: str = ""):
    if equipment_category:
        params = {"equipment_category": equipment_category}
    else:
        params = {}
    print(params)
    return db.equipment.find(params)
