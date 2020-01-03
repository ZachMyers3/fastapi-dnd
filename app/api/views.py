from flask import Blueprint, abort, jsonify, request
from bson.objectid import ObjectId
import math

from ..models import mongo
from ..scripts.character_calc import calc_skill_mods, calc_spells_available

views = Blueprint('views', __name__)

URL = 'https://flask-dnd.herokuapp.com/api/v1'
API_STUB = '/api/v1'

@views.route(f'{API_STUB}/skills/all', methods=['GET'])
def get_all_skills():
    results = list(mongo.db.skills.find())

    return jsonify(ok=True, data=results)

@views.route(f'{API_STUB}/magic-schools/all', methods=['GET'])
def get_all_magic_schools():
    results = list(mongo.db.magic_schools.find())

    return jsonify(ok=True, data=results)

@views.route(f'{API_STUB}/languages/all', methods=['GET'])
def get_all_languages():
    results = list(mongo.db.languages.find())

    return jsonify(ok=True, data=results)

@views.route(f'{API_STUB}/test', methods=['GET'])
def test():
    # get character from the given id
    _id = request.args.get('_id', default=None, type=str)
    character = mongo.db.characters.find_one({'_id': ObjectId(_id)})
    character = calc_spells_available(character)

    return jsonify(ok=True, data=character)
