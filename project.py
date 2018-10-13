from flask import Flask, render_template, jsonify, make_response, \
    request, abort
from decorators.authentication_decorator import authenticated
from database.dao import DAO
from model.game import Game
from model.user import User
from model.character import Character
from decorators.json_converter_decorator import convert_json_to


app = Flask(__name__)
app.secret_key = "fd7f0e4ec56046e91c32ba18110a0540"


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/user/create', methods=['POST'])
@authenticated
def create_user():
    auth_user = request.headers.get('auth_user')

    user = DAO.find(User, email=auth_user)
    if user is None:
        user = User()
        user.email = auth_user
        DAO.create(user)
    return "Ok"


@app.route('/game/all', methods=['GET'])
@authenticated
def get_games():
    games = DAO.find_all(Game)
    return make_response(jsonify(games=[game.serialize for game in games]))


@app.route('/game/<game_id>', methods=['GET'])
@authenticated
def get_game(game_id):
    game = DAO.find(Game, id=game_id)
    return jsonify(game.serialize)


@app.route('/game/create', methods=['POST'])
@authenticated
@convert_json_to(Game)
def create_game(game):
    auth_user = request.headers['auth_user']
    user = DAO.find(User, email=auth_user)
    game.user = user
    DAO.create(game)
    return "Ok"


@app.route('/game/update', methods=['PUT'])
@authenticated
@convert_json_to(Game)
def update_game(game):
    auth_user = request.headers['auth_user']
    game = DAO.find(Game, id=game.id)
    if (game.is_same_user(auth_user)):
        DAO.update(game)
        return "Ok"
    else:
        return abort(401)


@app.route('/game/remove/<game_id>', methods=['DELETE'])
@authenticated
def remove_game(game_id):
    auth_user = request.headers['auth_user']
    game = DAO.find(Game, id=game_id)
    if (game.is_same_user(auth_user)):
        DAO.delete(game)
        return "Ok"
    else:
        return abort(401)


@app.route('/game/<game_id>/character/all', methods=['GET'])
@authenticated
def get_characters_by_game(game_id):
    characters = DAO.session().query(Character)\
        .filter(Character.id_game == game_id)
    return jsonify(
        characters=[character.serialize for character in characters])


@app.route('/character/all', methods=['GET'])
@authenticated
def get_characters():
    characters = DAO.find_all(Character)
    return jsonify(
        characters=[character.serialize for character in characters])


@app.route('/character/<character_id>', methods=['GET'])
@authenticated
def get_character(character_id):

    game_character = DAO.find(Character, id=character_id)
    return jsonify(game_character.serialize)


@app.route('/character/create', methods=['POST'])
@authenticated
@convert_json_to(Character)
def create_character(game_character):
    DAO.create(game_character)
    return "Ok"


@app.route('/character/update', methods=['PUT'])
@authenticated
@convert_json_to(Character)
def update_character(character):
    auth_user = request.headers['auth_user']
    game = DAO.find(Game, id=character.game)
    if (game.is_same_user(auth_user)):
        character.game = game
        DAO.update(character)
        return "Ok"
    else:
        return abort(401)


@app.route('/character/remove/<character_id>', methods=['DELETE'])
@authenticated
def remove_character(character_id):
    auth_user = request.headers['auth_user']
    character = DAO.find(Character, id=character_id)
    if (character.game.is_same_user(auth_user)):
        DAO.delete(character)
        return "Ok"
    else:
        return abort(401)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)