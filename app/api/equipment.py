from flask import Blueprint, abort, jsonify, request
from bson.objectid import ObjectId
import math

from ..models import mongo

equipment = Blueprint('equipment', __name__)

API_STUB = '/api/v1'

@equipment.route(f'{API_STUB}/equipment/all', methods=['GET'])
def get_all_equipment():
    results = list(mongo.db.equipment.find())

    return jsonify(ok=True, data=results)

@equipment.route(f'{API_STUB}/equipment', methods=['GET'])
def get_equipment():
    _id = request.args.get('_id', default=None, type=str)
    if _id:
        data = get_equipment_by_id(_id)
    
    eq_category = request.args.get('equipment_category', default=None, type=str)
    if eq_category:
        data = get_equipment_by_category(eq_category)
    
    return jsonify(ok=True, data=data)

def get_equipment_by_id(_id):
    data = mongo.db.equipment.find_one({'_id': ObjectId(_id)})
    return data

def get_equipment_by_category(category):
    data = list(mongo.db.equipment.find({'equipment_category': category}))
    return data

@equipment.route(f'{API_STUB}/equipment-categories/all', methods=['GET'])
def get_all_equipment_categories():
    results = list(mongo.db.equipment_categories.find())

    return jsonify(ok=True, data=results)
