from flask_mongoalchemy import MongoAlchemy

db = MongoAlchemy()

class Character(db.Document):
    firstName = db.StringField()
    lastName = db.StringField()
    maxHP = db.IntField()
    currentHP = db.IntField()
    baseAC = db.IntField()
    currentAC = db.IntField()

    def __repr__(self):
        return (f'\n===========================\n'
               f'{self.firstName} {self.lastName}\n'
               f'HP: {self.currentHP}/{self.maxHP}\n'
               f'AC: {self.currentAC} ({self.baseAC})\n'
                  f'===========================')
