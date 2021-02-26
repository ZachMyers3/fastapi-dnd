from typing import List
from fastapi import APIRouter
from ..schema.monsters import MonsterSchema
from ..database.monsters import retrieve_monsters

router = APIRouter()


@router.get("/monsters/", response_model=List[MonsterSchema])
def get_all_equipment():
    return list(retrieve_monsters())
