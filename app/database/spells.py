from .database import db


def retrieve_spells():
    return db.spells.find()
