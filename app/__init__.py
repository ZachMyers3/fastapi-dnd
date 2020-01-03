from flask import Flask
from flask_cors import CORS

from .models import mongo
from .json import JSONEncoder

from .api.views import views
from .api.character import character
from .api.monster import monster
from .api.spell import spell
from .api.equipment import equipment

def create_app():
    # initialize app
    app = Flask(__name__)
    # load config
    app.config.from_object('config.Config')
    # initialize database with app
    mongo.init_app(app)
    # initialize CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS(app)
    # initialize blueprints
    app.register_blueprint(views)
    app.register_blueprint(character)
    app.register_blueprint(monster)
    app.register_blueprint(spell)
    app.register_blueprint(equipment)
    # use extended JSONEncoder
    app.json_encoder = JSONEncoder
    return app
