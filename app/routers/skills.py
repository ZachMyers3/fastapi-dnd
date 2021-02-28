from typing import List
from fastapi import APIRouter
from ..schema.skills import SkillsSchema
from ..database.skills import retrieve_skills

router = APIRouter()


@router.get("/skills/", response_model=List[SkillsSchema])
def get_skills():
    return list(retrieve_skills())
