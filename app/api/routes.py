from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Game, game_schema, games_schema

api = Blueprint('api',__name__, url_prefix='/api')


# @api.route('/getdata')
# def getdata():
#     return {'yee': 'haw'}

# @api.route('/getdata', methods = ['GET'])
# @token_required
# def index():
#     games = Game.query
#     return render_template('bootstrap_table.html', title='Bootstrap Table',
#                            games=games)


@api.route('/games', methods = ['POST'])
@token_required
def create_game(current_user_token):
    game_id = request.json['game_id']
    title = request.json['title']
    thumbnail = request.json['thumbnail']
    short_description = request.json['short_description']
    game_url = request.json['game_url']
    genre = request.json['genre']
    platform = request.json['platform']
    publisher = request.json['publisher']
    developer = request.json['developer']
    release_date = request.json['release_date']
    freetogame_profile_url = request.json['freetogame_profile_url']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    game = Game(game_id, title, thumbnail, short_description,
                game_url,genre,platform,publisher,developer,
                release_date,freetogame_profile_url,
                user_token = user_token )

    db.session.add(game)
    db.session.commit()

    response = game_schema.dump(game)
    return jsonify(response)


@api.route('/games', methods = ['GET'])
@token_required
def get_game(current_user_token):
    a_user = current_user_token.token
    games = Game.query.filter_by(user_token = a_user).all()
    response = games_schema.dump(games)
    return jsonify(response)



@api.route('/games/<id>', methods = ['GET'])
@token_required
def get_single_game(current_user_token, id):
    game = Game.query.get(id)
    response = game_schema.dump(game)
    return jsonify(response)



@api.route('/games/<id>', methods = ['POST','PUT'])
@token_required
def update_game(current_user_token,id):
    game = Game.query.get(id)
    game.game_id = request.json['game_id']
    game.title = request.json['title']
    game.thumbnail = request.json['thumbnail']
    game.short_description = request.json['short_description']
    game.game_url = request.json['game_url']
    game.genre = request.json['genre']
    game.platform = request.json['platform']
    game.publisher = request.json['publisher']
    game.developer = request.json['developer']
    game.release_date = request.json['release_date']
    game.freetogame_profile_url = request.json['freetogame_profile_url']
    game.user_token = current_user_token.token

    db.session.commit()
    response = game_schema.dump(game)
    return jsonify(response)


@api.route('/games/<id>', methods = ['DELETE'])
@token_required
def delete_game(current_user_token, id):
    game = Game.query.get(id)
    db.session.delete(game)
    db.session.commit()
    response = game_schema.dump(game)
    return jsonify(response)