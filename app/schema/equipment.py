from typing import Optional, List, Union
from .PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from bson import ObjectId


class EquipmentCostSchema(BaseModel):
    quantity: Optional[int]
    unit: Optional[str]


class EquipmentDamageTypeSchema(BaseModel):
    url: Optional[str]
    name: Optional[str]


class EquipmentDamageSchema(BaseModel):
    damage_dice: Optional[str]
    damage_bonus: Optional[int]
    damage_type: Optional[EquipmentDamageTypeSchema]


class EquipmentRangeSchema(BaseModel):
    normal: Optional[int]
    long_: Optional[Union[int, None]] = Field(alias="long")


class EquipmentPropertyScehma(BaseModel):
    url: Optional[str]
    name: Optional[str]


class EquipmentSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    index: Optional[int]
    name: Optional[str]
    equipment_category: Optional[str]
    weapon_category: Optional[str]
    weapon_range: Optional[str]
    category_range: Optional[str]
    cost: Optional[EquipmentCostSchema]
    damage: Optional[EquipmentDamageSchema]
    range_: Optional[EquipmentRangeSchema] = Field(alias="range")
    weight: Optional[int]
    properties: Optional[List[EquipmentPropertyScehma]]
    desc: Optional[List[str]]
    url: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
