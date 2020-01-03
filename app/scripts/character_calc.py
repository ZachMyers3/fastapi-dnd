from bson.objectid import ObjectId
import math

from ..models import mongo

def get_total_level(char):
    total_level = 0
    for cclass in char['class']:
        total_level += cclass['level']
    return total_level

def calc_skill_mods(character):
    # calc all mods 
    strmod = math.floor(character['strength'] / 2) - 5
    dexmod = math.floor(character['dexterity'] / 2) - 5
    conmod = math.floor(character['constitution'] / 2) - 5
    wismod = math.floor(character['wisdom'] / 2) - 5
    chamod = math.floor(character['charisma'] / 2) - 5
    # get proficiency bonus from level
    level = get_total_level(character)
    prof_bonus = math.ceil(level / 4) + 1
    for skill in character['skills']:
        # grab skill from skills db by skill id
        db_skill = mongo.db.skills.find_one({'index': skill['skill_id']})
        if db_skill['ability_score']['name'] == 'STR':
            skill['mod'] = strmod
        elif db_skill['ability_score']['name'] == 'DEX':
            skill['mod'] = dexmod
        elif db_skill['ability_score']['name'] == 'CON':
            skill['mod'] = conmod
        elif db_skill['ability_score']['name'] == 'WIS':
            skill['mod'] = wismod
        elif db_skill['ability_score']['name'] == 'CHA':
            skill['mod'] = chamod
        skill['mod'] += 1
        # add proficiency bonus if proficient
        if skill['proficiency']:
            skill['mod'] += prof_bonus
    # return updated character
    return character


def calc_spells_available(character):
    # loop through every class to gather spells
    for cclass in character['class']:
        print(f'{cclass["name"]}')
        class_spells = list(mongo.db.spells.find({
             "classes": [{
                 "class": cclass["name"]
             }]   
        }))
        for spell in class_spells:
            print(f'{spell["name"]} | {spell["classes"]}')
        print(f'{class_spells=}')

