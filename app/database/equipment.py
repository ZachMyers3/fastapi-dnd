from .database import db


def retrieve_equipment():
    return db.equipment.find()
