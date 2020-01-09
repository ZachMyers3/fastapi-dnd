from flask import Blueprint, abort, jsonify, request
from bson.objectid import ObjectId
import math

from ..models import mongo

spell = Blueprint('spell', __name__)

API_STUB = '/api/v1'

@spell.route(f'{API_STUB}/spells/all', methods=['GET'])
def get_all_spells():
    results = list(mongo.db.spells.find())

    return jsonify(ok=True, data=results)

@spell.route(f'{API_STUB}/spell', methods=['GET'])
def get_spell():
    _id = request.args.get('_id', default=None, type=int)
    if not _id:
        return jsonify(ok=False, msg='id field required'), 400
    data = mongo.db.spells.find_one({'id': _id})
    if data:
        return jsonify(ok=True, data=data)
    else:
        return jsonify(ok=False, msg='Spell not found'), 404
