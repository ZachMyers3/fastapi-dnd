from typing import Optional, List

from .PyObjectId import PyObjectId

from pydantic import BaseModel, Field

from bson import ObjectId


class SpellComponentSchema(BaseModel):
    verbal: Optional[bool]
    somatic: Optional[bool]
    material: Optional[bool]
    materials_needed: Optional[str]
    raw: Optional[str]


class SpellClassListSchema(BaseModel):
    class_: Optional[str] = Field(alias="class")


class SpellCastingSchema(BaseModel):
    range_: Optional[int] = Field(alias="range")
    self_: Optional[bool] = Field(alias="self")
    casting_time: Optional[int]
    action_type: Optional[str]
    duration: Optional[List[int]]
    ritual: Optional[bool]
    concentration: Optional[bool]
    touch: Optional[bool]
    sight: Optional[bool]


class SpellSchema(BaseModel):
    object_id: Optional[PyObjectId] = Field(alias="_id")
    name: Optional[str]
    desc: Optional[str]
    book: Optional[str]
    page: Optional[int]
    components: Optional[SpellComponentSchema]
    level: Optional[int]
    school: Optional[str]
    classes: Optional[List[SpellClassListSchema]]
    casting: Optional[SpellCastingSchema]
    id: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
