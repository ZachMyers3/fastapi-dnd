from .database import db


def retrieve_ability_scores():
    return db.ability_scores.find()
