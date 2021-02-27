from typing import List
from bson.objectid import ObjectId

from fastapi import Depends, APIRouter, HTTPException

from ..schema.spells import SpellSchema

from ..database.spells import retrieve_spell, retrieve_spells

router = APIRouter()


@router.get("/spells/", response_model=List[SpellSchema])
def get_spells():
    return list(retrieve_spells())


@router.get("/spells/{_id}/", response_model=SpellSchema)
def get_spell_by_id(_id: str):
    result = retrieve_spell(_id=_id)
    if result is None:
        HTTPException(status_code=404, detail="Object not found")
    return result
