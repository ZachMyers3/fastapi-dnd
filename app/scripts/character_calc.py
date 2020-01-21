from bson.objectid import ObjectId
import math

def get_total_level(character):
    total_level = 0
    for cclass in character['class']:
        total_level += cclass['level']
    return total_level

def calc_skill_mods(character, mongo):
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
    max_lvl = 0
    for key, value in level['spellcasting'].items():
        if 'spell_slots_level' in key:
            if value > 0:
                lvl = int(key[-1])
                if lvl > max_lvl:
                    max_lvl = lvl

    return max_lvl

# 3rd level spell slot for druid
# see call lightning to debug
# {
#     "_id": {
#         "$oid": "5e0f90b99afe3de6cbbeb20f"
#     },
#     "name": "Call Lightning",
#     "desc": "<p>A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius, centered on a point you can see within range directly above you. The spell fails if you can\u2019t see a point in the air where the storm cloud could appear (for example, if you are in a room that can\u2019t accommodate the cloud).<\/p><p>When you cast the spell, choose a point you can see under the cloud. A bolt of lightning flashes down from the cloud to that point. Each creature within 5 feet of that point must make a Dexterity saving throw. A creature takes 3d10 lightning damage on a failed save, or half as much damage on a successful one. On each of your turns until the spell ends, you can use your action to call down lightning in this way again, targeting the same point or a different one.<\/p><p>If you are outdoors in stormy conditions when you cast this spell, the spell gives you control over the existing storm instead of creating a new one. Under such conditions, the spell\u2019s damage increases by 1d10.<\/p>",
#     "higher_level": "When you cast this spell using a spell slot of 4th or higher level, the damage increases by 1d10 for each slot level above 3rd.",
#     "book": "Player's Handbook",
#     "page": 220,
#     "components": {
#         "material": false,
#         "materials_needed": "",
#         "raw": "V, S",
#         "somatic": true,
#         "verbal": true
#     },
#     "level": 3,
#     "school": "Conjuration",
    # "classes": [
    #     {
    #         "class": "Cleric",
    #         "subclasses": [
    #             "Tempest"
    #         ],
    #         "class_level": 5
    #     },
    #     {
    #         "class": "Druid",
    #         "subclasses": [
    #             "Forest"
    #         ],
    #         "class_level": 5
    #     }
    # ],
#     "casting": {
#         "range": 120,
#         "self": false,
#         "casting_time": 6,
#         "action_type": "action",
#         "duration": [
#             600
#         ],
#         "ritual": false,
#         "concentration": true,
#         "touch": false,
#         "sight": false
#     },
#     "id": 47
# }

def calc_spells_available(character, mongo):
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
            "classes.class": cclass["name"]
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

