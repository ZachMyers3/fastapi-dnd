from typing import Optional, List
from .PyObjectId import PyObjectId
from pydantic import BaseModel, Field
from bson import ObjectId

from .ability_scores import AbilityScoresSkillSchema


class SkillsSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    index: Optional[int]
    name: Optional[str]
    desc: Optional[List[str]]
    ability_score: Optional[AbilityScoresSkillSchema]
    url: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
