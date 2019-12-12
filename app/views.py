from flask import Blueprint, abort, jsonify, request

from bson.objectid import ObjectId

from .models import mongo

views = Blueprint('views', __name__)

@views.route('/api/character', methods=['GET'])
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

@views.route('/api/character', methods=['POST'])
def create_character():
    # TODO: verify player doesnt exist
    # go to characters store
    characters = mongo.db.characters
    # insert request
    pid = characters.insert(request.json)
    # find new player
    new_char = characters.find_one({'_id': pid})
    return jsonify(ok=True, character=new_char)

@views.route('/api/character', methods=['PUT'])
def update_character():
    if not request.json:
        return jsonify(ok=False, msg='JSON format required'), 400
    # need first name
    if not '_id' in request.json:
        return jsonify(ok=False, msg='ID is required to update'), 400
    # find the object by id and update from the rest of the json
    id_json = {'_id': request.json['_id']}
    update_char = mongo.db.characters.update_one(id_json, request.json['$set'])
    this_char = mongo.db.characters.find_one({'_id': request.json['_id']})

    return jsonify(ok=True, character=this_char)

@views.route('/api/characters', methods=['GET'])
def get_characters():
    # get all characters (return a max limit)
    results = list(mongo.db.characters.find())

    return jsonify(ok=True, characters=results)
