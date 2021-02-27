from typing import List
from fastapi import APIRouter
from ..schema.ability_scores import AbilityScoresSchema
from ..database.ability_scores import retrieve_ability_scores

router = APIRouter()


@router.get("/ability_scores/", response_model=List[AbilityScoresSchema])
def get_ability_scores():
    return list(retrieve_ability_scores())
