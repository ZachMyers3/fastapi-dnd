from flask import Blueprint, abort, jsonify, request

from .models import mongo

views = Blueprint('views', __name__)

@views.route('/player', methods=['GET', 'POST'])
@views.route('/player/<int:player_id>', methods=['GET', 'POST'])
def player(player_id=0):
    if request.method == 'GET':
        return get_player(player_id)
    elif request.method == 'POST':
        return create_player(player_id)
    else:
        return '400 Invalid Request', 400


def get_player(player_id):
    players = mongo.db.players

    this_player = players.find_one({'firstName': player_id})

    print(f'{this_player=}')

    return jsonify(get='get')

def create_player(player_id):
    # TODO: verify player doesnt exist
    # go to players store
    players = mongo.db.players
    # insert request
    pid = players.insert(request.json)
    # find new player
    new_player = players.find_one({'_id': pid})
    print(f'{new_player}')
    return jsonify(new_player)


