from flask import Flask, render_template, request, jsonify, redirect
from oauth2.authorization_decorator import authorized
from database.dao import DAO
from model.game import Game
from model.game_character import GameCharacter

app = Flask(__name__)
app.secret_key = "fd7f0e4ec56046e91c32ba18110a0540"


@app.route('/')
def home():
    games = DAO.find_all(Game)
    return render_template('gameList.html', games=[game.serialize for game in games])


@app.route('/login', methods=['POST'])
@authorized
def login():
    redirect('/')


@app.route('/logout', methods=['POST'])
def logout():
    redirect('/')





@app.route('/game/<id>', methods=['GET'])
def get_game(id_game):
    game = DAO.find(Game, id=id_game)[0]
    return jsonify(game.serialize)


@app.route('/game/all', methods=['GET'])
def get_games():
    games = DAO.find_all(Game)
    return jsonify(games=[game.serialize for game in games])


@app.route('/game/list', methods=['GET'])
def list_games():
    games = DAO.find_all(Game)
    return render_template('gameList.html', games=[game.serialize for game in games])


@app.route('/game/new', methods=['GET'])
def new_game():
    return render_template('gameForm.html')


@app.route('/game/create', methods=['POST'])
#@authorized
def create_game():
    content = request.get_json(silent=True)
    return ""


@app.route('/game/remove', methods=['DELETE'])
@authorized
def remove_game():
    return ""






@app.route('/game/<id>/character/all', methods=['GET'])
def get_characters(id):
    characters = DAO.session().query(GameCharacter).filter(GameCharacter.id_game == id)
    return jsonify(characters=[character.serialize for character in characters])


@app.route('/game/<id>/character/list', methods=['GET'])
def list_characters(id):
    games = DAO.find_all(Game)
    characters = DAO.session().query(GameCharacter).filter(GameCharacter.id_game == id)
    return render_template('gameCharacterList.html', games=[game.serialize for game in games], characters=[character.serialize for character in characters])








@app.route('/character/<id_character>', methods=['GET'])
def get_character(id_character):
    game_character = DAO.find(GameCharacter, id=id_character)[0]
    return jsonify(game_character.serialize)


@app.route('/character/new', methods=['GET'])
def new_character():
    return render_template("gameCharacterForm.html")


@app.route('/character/create', methods=['POST'])
@authorized
def create_character():
    return ""


@app.route('/character/remove', methods=['DELETE'])
@authorized
def remove_character():
    return ""


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)