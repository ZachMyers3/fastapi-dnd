from flask import Blueprint, abort, jsonify, request

from bson.objectid import ObjectId

import math

from ..models import mongo

character = Blueprint('character', __name__)

API_STUB = '/api/v1'

@character.route(f'{API_STUB}/character', methods=['GET'])
def get_character():
    _id = request.args.get('_id', default=None, type=str)
    if not _id:
        return jsonify(ok=False, msg='_id field required'), 400
    this_char = mongo.db.characters.find_one({'_id': ObjectId(_id)})
    print(f'{this_char=}')
    if this_char:
        return jsonify(ok=True, character=this_char)
    else:
        return jsonify(ok=False, msg='Character not found'), 404

@character.route(f'{API_STUB}/character', methods=['POST'])
def create_character():
    # TODO: verify player doesnt exist
    # go to characters store
    characters = mongo.db.characters
    # insert request
    pid = characters.insert(request.json)
    # find new player
    new_char = characters.find_one({'_id': pid})
    return jsonify(ok=True, character=new_char)

@character.route(f'{API_STUB}/character', methods=['PUT'])
def update_character():
    _id = ObjectId(request.json['_id'])
    if not request.json:
        return jsonify(ok=False, msg='JSON format required'), 400
    if not _id:
        return jsonify(ok=False, msg='ID is required to update'), 400
    # find the object by id and update from the rest of the json
    print(f'_id')
    update_json = {'_id': _id, '$set': request.json}
    print(f'{update_json=}')
    request.json.pop('_id', None)
    mongo.db.characters.update_one({'_id': _id}, {'$set': request.json})
    this_char = mongo.db.characters.find_one({'_id': _id})

    return jsonify(ok=True, character=this_char)

@character.route(f'{API_STUB}/characters', methods=['GET'])
def get_characters():
    # get all characters (return a max per_page)
    results = list(mongo.db.characters.find())

    return jsonify(ok=True, characters=results)

@character.route(f'{API_STUB}/character', methods=['DELETE'])
def delete_character():
    _id = request.args.get('_id', default=None, type=str)
    if not _id:
        return jsonify(ok=False, msg='_id field required'), 400
    del_char = mongo.db.characters.find_one({'_id': ObjectId(_id)})
    if not del_char:
        return jsonify(ok=False, msg='Character not found'), 404
    del_result = mongo.db.characters.delete_one({'_id': ObjectId(_id)})
    if del_result:
        return jsonify(ok=True, character=del_char)
