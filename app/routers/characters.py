from app.database.characters import retrieve_characters
from typing import List

from fastapi import Depends, APIRouter, HTTPException

from ..schema.characters import CharacterSchema

from ..database.characters import retrieve_characters, retrieve_character

router = APIRouter()


@router.get("/characters/", response_model=List[CharacterSchema])
def get_all_equipment():
    return list(retrieve_characters())


@router.get("/characters/{_id}/", response_model=CharacterSchema)
def get_character(_id: str):
    result = retrieve_character(_id=_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return result
