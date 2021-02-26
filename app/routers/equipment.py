from typing import List

from fastapi import Depends, APIRouter, HTTPException

from ..schema.equipment import EquipmentSchema

from ..database.equipment import retrieve_equipment

router = APIRouter()


@router.get("/equipment/", response_model=List[EquipmentSchema])
def get_all_equipment(equipment_category: str = ""):
    return list(retrieve_equipment(equipment_category=equipment_category))
