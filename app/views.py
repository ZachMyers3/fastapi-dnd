from flask import Blueprint, abort, jsonify, request

from bson.objectid import ObjectId

import math

from .models import mongo

views = Blueprint('views', __name__)

URL = 'https://flask-dnd.herokuapp.com/api/v1'

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
    # get all characters (return a max per_page)
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

@views.route('/api/v1/monster', methods=['GET'])
def get_monster():
    _id = request.args.get('_id', default=None, type=str)
    if not _id:
        return jsonify(ok=False, msg='_id field required'), 400
    this_monster = mongo.db.monsters.find_one({'_id': ObjectId(_id)})
    if this_monster:
        return jsonify(ok=True, monster=this_monster)
    else:
        return jsonify(ok=False, msg='Character not found'), 404

@views.route('/api/v1/monsters', methods=['GET'])
def get_monsters():
    per_page = request.args.get('per_page', default=10, type=int)
    current_page = request.args.get('page', default=1, type=int)
    total = mongo.db.monsters.count()
    last_page = math.floor(total / per_page) + 1
    # gather url params for previous query 
    if current_page == 1:
        prev_page_url = None
    else:
        prev_page_url = f'{URL}/monsters?page={current_page-1}'
    # gather url params for next query
    if ((current_page * per_page) + per_page) > total:
        next_page_url = None
    else:
        next_page_url = f'{URL}/monsters?page={current_page+1}'
    # use find() by parameters
    page_from = (current_page * per_page) - per_page + 1
    monsters = list(mongo.db.monsters.find().skip(page_from).limit(per_page))
    page_to = page_from + len(monsters) - 1
    # return gathered data
    return jsonify(
        total=total,
        per_page=per_page,
        current_page=current_page,
        last_page=last_page,
        next_page_url=next_page_url,
        prev_page_url=prev_page_url,
        page_from=page_from,
        page_to=page_to,
        data=monsters
    )

@views.route('/api/v1/monsters/all', methods=['GET'])
def get_all_monsters():
    # get all characters (return a max per_page)
    results = list(mongo.db.monsters.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/spells/all', methods=['GET'])
def get_all_spells():
    results = list(mongo.db.spells.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/skills/all', methods=['GET'])
def get_all_skills():
    results = list(mongo.db.skills.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/magic-schools/all', methods=['GET'])
def get_all_magic_schools():
    results = list(mongo.db.magic_schools.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/languages/all', methods=['GET'])
def get_all_languages():
    results = list(mongo.db.languages.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/equipment/all', methods=['GET'])
def get_all_equipment():
    results = list(mongo.db.equipment.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/equipment', methods=['GET'])
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
    data = mongo.db.equipment_category.find({'equipment_category': category})
    return data

@views.route('/api/v1/equipment-categories/all', methods=['GET'])
def get_all_equipment_categories():
    results = list(mongo.db.equipment_categories.find())

    return jsonify(ok=True, data=results)

@views.route('/api/v1/spell', methods=['GET'])
def get_spell():
    _id = request.args.get('_id', default=None, type=str)
    if not _id:
        return jsonify(ok=False, msg='_id field required'), 400
    data = mongo.db.spells.find_one({'_id': ObjectId(_id)})
    if data:
        return jsonify(ok=True, data=data)
    else:
        return jsonify(ok=False, msg='Spell not found'), 404
