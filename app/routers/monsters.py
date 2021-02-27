from typing import List
from fastapi import APIRouter, HTTPException
from ..schema.monsters import MonsterSchema
from ..database.monsters import retrieve_monster, retrieve_monsters

router = APIRouter()


@router.get("/monsters/", response_model=List[MonsterSchema])
def get_all_monsters():
    return list(retrieve_monsters())


@router.get("/monsters/{_id}/", response_model=MonsterSchema)
def get_monster(_id: str):
    result = retrieve_monster(_id=_id)
    if result is None:
        HTTPException(status_code=404, detail="Object not found")
    return result
