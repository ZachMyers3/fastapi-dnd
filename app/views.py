from flask import Blueprint, abort, jsonify, request

from .models import mongo

views = Blueprint('views', __name__)

@views.route('/character', methods=['GET'])
def get_character():
    # need JSON
    if not request.json:
        return jsonify(ok=False, msg='JSON format required'), 400
    # need first name
    if not 'firstName' in request.json:
        return jsonify(ok=False, msg='First name required'), 400
    print(f'{jsonify(request.args)=}')
    # based off of the JSON find character
    this_char = mongo.db.characters.find_one(request.json)
    print(f'{this_char=}')
    return jsonify(ok=True, character=this_char)

@views.route('/character', methods=['POST'])
def create_character():
    # TODO: verify player doesnt exist
    # go to characters store
    characters = mongo.db.characters
    # insert request
    pid = characters.insert(request.json)
    # find new player
    new_char = characters.find_one({'_id': pid})
    print(f'{new_char}')
    return jsonify(ok=True, character=new_char)

