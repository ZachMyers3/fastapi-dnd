from typing import List

from fastapi import Depends, APIRouter, HTTPException

from ..schema.equipment import EquipmentSchema

from ..database.equipment import (
    retrieve_equipment,
    retrieve_singular_equipment,
)

router = APIRouter()


@router.get("/equipment/", response_model=List[EquipmentSchema])
def get_all_equipment(equipment_category: str = ""):
    return list(retrieve_equipment(equipment_category=equipment_category))


@router.get("/equipment/{_id}/", response_model=EquipmentSchema)
def get_equipment_by_id(_id: str):
    result = retrieve_singular_equipment(_id=_id)
    if result is None:
        HTTPException(status_code=404, detail="Object not found")
    return result
