import json
from typing import List, Dict

import pathlib
import pymongo
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

test_file = """
{
  "_id": "5e0f90b99afe3de6cbbeb2cc",
  "name": "Magic Missile",
  "desc": "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.",
  "book": "Player's Handbook",
  "page": 257,
  "components": {
    "verbal": true,
    "somatic": true,
    "material": false,
    "materials_needed": "",
    "raw": "V, S"
  },
  "level": 1,
  "school": "Evocation",
  "classes": [
    {
      "class": "Sorcerer"
    },
    {
      "class": "Wizard"
    }
  ],
  "casting": {
    "range": 120,
    "self": false,
    "casting_time": 6,
    "action_type": "action",
    "duration": [
      0
    ],
    "ritual": false,
    "concentration": false,
    "touch": false,
    "sight": false
  },
  "id": 240
}
"""


def determine_spell_duration_value(base_spell_length: List[int]):
    # determine it's best served as inst / second / minute / hour /day
    if base_spell_length[0] == 0:
        return None
    else:
        return str(base_spell_length[0])


def determing_spell_duration_units(base_spell_length: List[int]):
    # Can be: inst, second, minute, hour, day
    if base_spell_length[0] == 0:
        return "inst"
    else:
        return "second"


def determine_spell_self_or_creature(self: bool):
    if self:
        return "self"
    else:
        return "creature"


def determine_spell_damage_parts_list() -> List[List[str]]:
    return [[]]


def determine_spell_save_dictionary():
    save = {
        "ability": "",
        "dc": None,
        "value": "",
        "scaling": "spell",
    }
    return save


def determine_fountry_compat_spell_school(base_school: str) -> str:
    return base_school[0:3].lower()


def determine_materials_dictionary(components: Dict) -> Dict:
    materials = {
        "value": "",
        "consumed": False,
        "cost": 0,
        "supply": 0
    }
    return materials


def determine_spell_level_string(spell_level: int) -> str:
    if spell_level == 0:
        return "cantrip"
    else:
        return "level"


def base_to_foundy(spell_json: dict):
    foundry_json = {}
    foundry_json["_id"] = str(spell_json["_id"])
    foundry_json["name"] = spell_json["name"]
    foundry_json["permission"] = {
        "default": 0
    }
    foundry_json["type"] = "spell"
    foundry_json["data"] = {
        "description": {
            "value": spell_json["desc"],
            "chat": "",
            "unidentified": ""
        },
        "source": f"{spell_json['book']} page {spell_json['page']}",
        "activation": {
            "type": spell_json["casting"]["action_type"],
            "cost": 1,
            "condition": ""
        },
        "duration": {
            "value":
                determine_spell_duration_value(
                    spell_json["casting"]["duration"]
                ),
            "units":
                determing_spell_duration_units(
                    spell_json["casting"]["duration"]
                )
        },
        "target": {
            "value": 1,
            "units": "",
            "type":
                determine_spell_self_or_creature(
                    spell_json["casting"]["self"]
                )
        },
        "range": {
            "value": spell_json["casting"]["range"],
            "long": 0,
            "units": "ft"
        },
        "uses": {
            "value": 0,
            "max": 0,
            "per": ""
        },
        "ability": "",
        "actionType": "other",
        "attackBonus": 0,
        "chatFlavor": "",
        "critical": None,
        "damage": {
            "parts": determine_spell_damage_parts_list(),
            "versatile": ""
        },
        "formula": "",
        "save": determine_spell_save_dictionary(),
        "level": spell_json["level"],
        "school": determine_fountry_compat_spell_school(spell_json["school"]),
        "components": {
            "value": "",
            "vocal": spell_json["components"]["verbal"],
            "somatic": spell_json["components"]["somatic"],
            "material": spell_json["components"]["material"],
            "ritual": spell_json["casting"]["ritual"],
            "concentration": spell_json["casting"]["concentration"],
        },
        "materials": determine_materials_dictionary(spell_json["components"]),
        "preparation": {
            "mode": "prepared",
            "prepared": False
        },
        "scaling": {
            "mode": determine_spell_level_string(spell_json["level"]),
            "formula": ""
        }
    }
    foundry_json["sort"] = 100001
    foundry_json["flags"] = {}
    foundry_json["img"] = "systems/dnd5e/icons/spells/fire-arrows-magenta-1.jpg",
    foundry_json["img"] = foundry_json["img"][0]
    foundry_json["effects"] = []

    return foundry_json


def entire_db_to_foundry_compat_file(file_name: pathlib.Path):
    print(os.environ.get("MONGODB_URI"))
    client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
    db = client["dnd"]
    foundry_json_list = []
    for spell in db.spells.find():
        foundy_json = base_to_foundy(spell)
        foundry_json_list.append(foundy_json)

    with open(file_name, "w") as _f:
        for foundry_json in foundry_json_list:
            _f.write(f"{foundry_json}\n")


def entire_db_to_foundry_compat_collection(collection_name: str):
    print(os.environ.get("MONGODB_URI"))
    client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
    db = client["dnd"]
    foundry_json_list = []
    for spell in db.spells.find():
        foundy_json = base_to_foundy(spell)
        foundry_json_list.append(foundy_json)

    for foundry_json in foundry_json_list:
        del foundry_json["_id"]

    foundry_collection = db[collection_name]
    foundry_collection.insert_many(foundry_json_list)


if __name__ == "__main__":
    # entire_db_to_foundry_compat_file(pathlib.Path("./spells.db"))
    entire_db_to_foundry_compat_collection("foundry_spells")
