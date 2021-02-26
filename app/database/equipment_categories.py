from .database import db


def retrieve_equipment_categories():
    return db.equipment_categories.find()
