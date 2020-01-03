from bson.objectid import ObjectId
import math
import os

# from ..models import mongo
import pymongo
mongo = pymongo.MongoClient(os.environ.get('MONGODB_URI'))

def calc_skill_mods(cid):
    # get character from the given id
    character = mongo.db.characters.find_one({'id': cid})
    # calc all mods 
    strmod = math.floor(character.stength / 2) - 5
    dexmod = math.floor(character.dexterity / 2) - 5
    conmod = math.floor(character.constitution / 2) - 5
    wismod = math.floor(character.wisdom / 2) - 5
    chamod = math.floor(character.charisma / 2) - 5
    # get proficiency bonus from level
    prof_bonus = math.ceil(character.level / 4) + 1
    for skill in character.skills:
        # grab skill from skills db by skill id
        db_skill = mongo.db.skills.find_one({'index': skill.skill_id})
        if db_skill.ability_score.name == 'STR':
            skill.mod = strmod
        elif db_skill.ability_score.name == 'DEX':
            skill.mod = dexmod
        elif db_skill.ability_score.name == 'CON':
            skill.mod = conmod
        elif db_skill.ability_score.name == 'WIS':
            skill.mod = wismod
        elif db_skill.ability_score.name == 'CHA':
            skill.mod = chamod
        # add proficiency bonus if proficient
        if skill.proficiency:
            skill.mod += prof_bonus
    
if __name__ == "__main__":
    calc_skill_mods(1)