from .database import db


def retrieve_skills():
    return db.skills.find()
