from typing import Optional, List
from .PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from bson import ObjectId


class AbilityScoresSkillSchema(BaseModel):
    url: Optional[str]
    name: Optional[str]


class AbilityScoresSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    index: Optional[int]
    name: Optional[str]
    full_name: Optional[str]
    desc: Optional[List[str]]
    skills: Optional[List[AbilityScoresSkillSchema]]
    url: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
