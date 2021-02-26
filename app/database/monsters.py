from .database import db


def retrieve_monsters():
    return db.monsters.find()
