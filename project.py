from flask import Flask, render_template, jsonify, make_response, request
from decorators.authorization_decorator import authorized
from database.dao import DAO
from model.game import Game
from model.character import Character
from decorators.json_converter_decorator import convert_json_to


app = Flask(__name__)
app.secret_key = "fd7f0e4ec56046e91c32ba18110a0540"


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/game/all', methods=['GET'])
@authorized
def get_games():
    games = DAO.find_all(Game)
    return make_response(jsonify(games=[game.serialize for game in games]))


@app.route('/game/<game_id>', methods=['GET'])
@authorized
def get_game(game_id):
    game = DAO.find(Game, id=game_id)
    return jsonify(game.serialize)


@app.route('/game/create', methods=['POST'])
@authorized
@convert_json_to(Game)
def create_game(game):
    DAO.create(game)
    return "Ok"


@app.route('/game/update', methods=['PUT'])
@authorized
@convert_json_to(Game)
def update_game(game):
    DAO.update(game)
    return "Ok"


@app.route('/game/remove/<game_id>', methods=['DELETE'])
@authorized
def remove_game(game_id):
    game = DAO.find(Game, id=game_id)
    DAO.delete(game)
    return "Ok"


@app.route('/game/<id>/character/all', methods=['GET'])
@authorized
def get_characters_by_game(id):
    characters = DAO.session().query(Character).filter(Character.id_game == id)
    return jsonify(characters=[character.serialize for character in characters])


@app.route('/character/all', methods=['GET'])
@authorized
def get_characters():
    characters = DAO.find_all(Character)
    return jsonify(characters=[character.serialize for character in characters])


@app.route('/character/<character_id>', methods=['GET'])
@authorized
def get_character(character_id):
    game_character = DAO.find(Character, id=character_id)
    return jsonify(game_character.serialize)


@app.route('/character/create', methods=['POST'])
@authorized
@convert_json_to(Character)
def create_character(game_character):
    DAO.create(game_character)
    return "Ok"

@app.route('/character/update', methods=['PUT'])
@authorized
@convert_json_to(Character)
def update_character(character):
    game = DAO.find(Game, id=character.game)
    character.game = game
    DAO.update(character)
    return "Ok"


@app.route('/character/remove/<character_id>', methods=['DELETE'])
@authorized
def remove_character(character_id):
    character = DAO.find(Character, id=character_id)
    DAO.delete(character)
    return "Ok"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)