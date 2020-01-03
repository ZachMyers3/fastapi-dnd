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

def determine_max_spell_level(level):
    if level['spellcasting']['spell_slots_level_9'] > 0:
        return 9
    elif level['spellcasting']['spell_slots_level_8'] > 0:
        return 8
    elif level['spellcasting']['spell_slots_level_7'] > 0:
        return 7
    elif level['spellcasting']['spell_slots_level_6'] > 0:
        return 6
    elif level['spellcasting']['spell_slots_level_5'] > 0:
        return 5
    elif level['spellcasting']['spell_slots_level_4'] > 0:
        return 4
    elif level['spellcasting']['spell_slots_level_3'] > 0:
        return 3
    elif level['spellcasting']['spell_slots_level_2'] > 0:
        return 2
    elif level['spellcasting']['spell_slots_level_1'] > 0:
        return 1
    else:
        return 0


def calc_spells_available(character):
    # the list of all available spells per class
    spell_list = []
    # loop through every class to gather spells
    for cclass in character['class']:
        # find the class level information for the given class
        class_level = mongo.db.levels.find_one({
            "level": cclass['level'],
            "class.name": cclass['name']
        })
        # get the max spell slot available at given class level
        lvl_req = determine_max_spell_level(class_level)
        # if the max spell slot is zero go to next class
        if lvl_req == 0:
            continue
        # find all spells for this given class
        class_spells = list(mongo.db.spells.find({
             "classes": {
                 "class": cclass["name"]
             }   
        }))
        for spell in class_spells:
            # ignore spells that are over level for given class
            if spell['level'] > lvl_req:
                continue

            spell_list.append({
                "name": spell["name"],
                "level": spell["level"],
                "id": spell["id"]
            })

        # add the generated spell list to the character and return result
        character['spells'] = spell_list
        return character

