"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    
    result = User.query.all()
    all_users = list(map(lambda x: x.serialize(),result))

    return jsonify(all_users), 200
    
#ADD PEOPLE
@app.route('/addpeople', methods=['POST'])
def add_people():
    request_body = request.get_json()
    people = Character(name=request_body["name"],height=request_body["height"],
    mass=request_body["mass"],hair=request_body["hair"],
    gender=request_body["gender"],skin=request_body["skin"],eye=request_body["eye"],
    birth=request_body["birth"])
    db.session.add(people)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /add user response "
    }
    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def get_people():
    result = Character.query.all()
    all_people = list(map(lambda x: x.serialize(),result))

    return jsonify(all_people), 200





@app.route('/planets', methods=['GET'])
def get_planets():

    result = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(),result))

    return jsonify(all_planets), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
