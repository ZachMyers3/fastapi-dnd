from typing import Optional, List
from .PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from bson import ObjectId


class CharacterClassSchema(BaseModel):
    name: Optional[str]
    level: Optional[int]


class CharacterSavingThrowSchema(BaseModel):
    name: Optional[str]
    mod: Optional[int]
    ability_id: Optional[int]
    proficiency: Optional[bool]


class CharacterSkillsSchema(BaseModel):
    name: Optional[str]
    mod: Optional[int]
    skill_id: Optional[int]
    proficiency: Optional[bool]
    expertise: Optional[bool]


class CharacterAttacksSchema(BaseModel):
    name: Optional[str]
    desc: Optional[str]
    attack_bonus: Optional[int]
    damage_dice: Optional[str]
    damage_bonus: Optional[str]


class CharacterSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    firstName: Optional[str]
    lastName: Optional[str]
    alias: Optional[str]
    class_: Optional[List[CharacterClassSchema]] = Field(alias="class")
    background: Optional[str]
    alignment: Optional[str]
    maxHP: Optional[int]
    currentHP: Optional[int]
    strength: Optional[int]
    dexterity: Optional[int]
    constitution: Optional[int]
    intelligence: Optional[int]
    wisdom: Optional[int]
    charisma: Optional[int]
    race: Optional[str]
    gender: Optional[str]
    deity: Optional[str]
    Hair: Optional[str]
    Eyes: Optional[str]
    Height: Optional[int]
    Weight: Optional[int]
    saving_throws: Optional[List[CharacterSavingThrowSchema]]
    skills: Optional[List[CharacterSkillsSchema]]
    attacks: Optional[List[CharacterAttacksSchema]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
