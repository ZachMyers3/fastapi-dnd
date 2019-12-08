from flask import Flask

from .models import mongo
from .views import views
from .json import JSONEncoder

def create_app():
    # initialize app
    app = Flask(__name__)
    # load config
    app.config.from_object('config.Config')
    # initialize database with app
    mongo.init_app(app)
    # initialize blueprint
    app.register_blueprint(views)
    # use extended JSONEncoder
    app.json_encoder = JSONEncoder
    return app
