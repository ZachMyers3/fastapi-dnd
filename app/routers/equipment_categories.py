from typing import List

from fastapi import Depends, APIRouter, HTTPException

from ..schema.equipment_categories import EquipmentTypeSchema

from ..database.equipment_categories import retrieve_equipment_categories

router = APIRouter()


@router.get("/equipment_categories/", response_model=List[EquipmentTypeSchema])
def get_equipment_categories():
    return list(retrieve_equipment_categories())
