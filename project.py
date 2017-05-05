from flask import Flask, request, render_template
from oauth2.authorization_decorator import authorized


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/login', methods=['POST'])
@authorized
def login(self):
    return None


@app.route('/logout', methods=['POST'])
def logout():
    return None


@app.route('/game/all', methods=['GET'])
def list_games():
    return "SELECT * FROM GAME"


@app.route('/game/{id}', methods=['GET'])
def get_game():
    return "SELECT * FROM GAME WHERE ID = {id}"


@app.route('/game/create', methods=['POST'])
@authorized
def create_game(self):
    return ""


@app.route('/game/remove', methods=['DELETE'])
@authorized
def remove_game():
    return ""


@app.route('/game/{id}/character/all', methods=['GET'])
def list_characters():
    return ""


@app.route('/character/{id}', methods=['GET'])
def get_character():
    return ""


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