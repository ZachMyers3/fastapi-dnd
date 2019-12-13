from flask import Blueprint, abort, jsonify, request

from bson.objectid import ObjectId

from .models import mongo

views = Blueprint('views', __name__)

@views.route('/api/v1/character', methods=['GET'])
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

@views.route('/api/v1/character', methods=['POST'])
def create_character():
    # TODO: verify player doesnt exist
    # go to characters store
    characters = mongo.db.characters
    # insert request
    pid = characters.insert(request.json)
    # find new player
    new_char = characters.find_one({'_id': pid})
    return jsonify(ok=True, character=new_char)

@views.route('/api/v1/character', methods=['PUT'])
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
    update_char = mongo.db.characters.update_one({'_id': _id}, {'$set': request.json})
    this_char = mongo.db.characters.find_one({'_id': _id})

    return jsonify(ok=True, character=this_char)

@views.route('/api/v1/characters', methods=['GET'])
def get_characters():
    # get all characters (return a max limit)
    results = list(mongo.db.characters.find())

    return jsonify(ok=True, characters=results)

@views.route('/api/v1/character', methods=['DELETE'])
def delete_character():
    _id = request.args.get('_id', default=None, type=str)
    if not _id:
        return jsonify(ok=False, msg='_id field required'), 400
    del_char = mongo.db.characters.find_one({'_id': ObjectId(_id)})
    if not this_char:
        return jsonify(ok=False, msg='Character not found'), 404
    del_result = mongo.db.characters.delete_one({'_id': ObjectId(_id)})
    if this_char:
        return jsonify(ok=True, character=del_char)

@views.route('/api/v1/monsters', methods=['GET'])
def get_monsters():
    # get args for pagination
    start = request.args.get('start', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    count = mongo.db.monsters.count()
    # error if starting after the entire size of the collection
    if count < start:
        return jsonify(ok=False, 
                       msg=f'Start of {start} larger than collection size of {count}'), 404
    # gather url params for previous query 
    if start == 1:
        previous = ''
    else:
        start_copy = max(1, start - limit)
        previous = f'?start={start_copy}&limit={limit}'
    print(f'{previous=}')
    # gather url params for next query
    if start + limit > count:
        nxt = ''
    else:
        start_copy = start + limit
        nxt = f'?start={start_copy}&limit={limit}'
    print(f'{nxt=}')
    # use find() by parameters
    monsters = list(mongo.db.monsters.find().skip(start).limit(limit))
    # return gathered data
    return jsonify(
        ok=True,
        monsters=monsters,
        previous=previous,
        next=nxt,
        start=start,
        limit=limit,
        count=count
    )
