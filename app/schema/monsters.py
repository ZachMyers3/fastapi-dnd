from typing import Optional, List
from .PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from bson import ObjectId


class MonsterActionsSchema(BaseModel):
    name: Optional[str]
    desc: Optional[str]
    attack_bonus: Optional[int]
    damage_dice: Optional[str]
    damage_bonus: Optional[str]


class MonsterSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    name: Optional[str]
    size: Optional[str]
    type_: Optional[str] = Field(alias="type")
    subtype: Optional[str]
    alignment: Optional[str]
    armor_class: Optional[int]
    hit_points: Optional[int]
    hit_dice: Optional[str]
    speed: Optional[str]
    strength: Optional[int]
    dexterity: Optional[int]
    constitution: Optional[int]
    intelligence: Optional[int]
    wisdom: Optional[int]
    charisma: Optional[int]
    constitution_save: Optional[int]
    intelligence_save: Optional[int]
    wisdom_save: Optional[int]
    history: Optional[int]
    perception: Optional[int]
    damage_vulterability: Optional[str]
    damage_resistances: Optional[str]
    condition_immunities: Optional[str]
    senses: Optional[str]
    languages: Optional[str]
    challenge_rating: Optional[str]
    special_abilites: Optional[List[MonsterActionsSchema]]
    actions: Optional[List[MonsterActionsSchema]]
    legendary_actions: Optional[List[MonsterActionsSchema]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
