from typing import List

from fastapi import Depends, APIRouter, HTTPException

from ..schema.spells import SpellSchema

from ..database.spells import retrieve_spells

router = APIRouter()


@router.get("/spells/", response_model=List[SpellSchema])
def get_all_spells():
    return list(retrieve_spells())
