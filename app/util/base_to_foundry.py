import json
from typing import List, Dict

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
    return base_school[0:3]


def determine_materials_dictionary(components: Dict) -> Dict:
    materials = {
        "value": "",
        "consumed": False,
        "cost": 0,
        "supply": 0
    }
    return materials


def base_to_foundy(spell_json: dict):
    print(spell_json)
    foundry_json = {}
    foundry_json["_id"] = spell_json["_id"]
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
        "source":f"{spell_json['book']} page {spell_json['casting']['duration']}",
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
            "model": "level",
            "formulat": ""
        }
    }
    foundry_json["sort"] = 100001
    foundry_json["flags"] = {}
    foundry_json["img"] = str(""),
    foundry_json["effects"] = []

    print(foundry_json)


if __name__ == "__main__":
    test_json = json.loads(test_file)
    base_to_foundy(test_json)
