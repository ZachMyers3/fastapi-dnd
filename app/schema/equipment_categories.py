from typing import Optional, List
from .PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from bson import ObjectId


class EquipmentTypeEquipmentSchema(BaseModel):
    name: Optional[str]
    url: Optional[str]


class EquipmentTypeSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    index: Optional[int]
    name: Optional[str]
    equipment: Optional[List[EquipmentTypeEquipmentSchema]]
    url: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
