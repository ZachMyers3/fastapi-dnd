from flask import Blueprint, abort, jsonify, request

from bson.objectid import ObjectId

import math

from ..models import mongo

monster = Blueprint('monster', __name__)

URL = 'https://flask-dnd.herokuapp.com/api/v1'
API_STUB = '/api/v1'

@monster.route(f'{API_STUB}/monster', methods=['GET'])
def get_monster():
    _id = request.args.get('_id', default=None, type=str)
    if not _id:
        return jsonify(ok=False, msg='_id field required'), 400
    this_monster = mongo.db.monsters.find_one({'_id': ObjectId(_id)})
    if this_monster:
        return jsonify(ok=True, monster=this_monster)
    else:
        return jsonify(ok=False, msg='Character not found'), 404

@monster.route(f'{API_STUB}/monsters', methods=['GET'])
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

@monster.route(f'{API_STUB}/monsters/all', methods=['GET'])
def get_all_monsters():
    # get all characters (return a max per_page)
    results = list(mongo.db.monsters.find())

    return jsonify(ok=True, data=results)