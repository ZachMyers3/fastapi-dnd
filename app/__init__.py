from flask import Flask

from models import db

def create_app():
    # initialize app
    app = Flask(__name__)
    # load config
    app.config.from_object('config.Config')
    # initialize database with app
    db.init_app(app)

    return app
