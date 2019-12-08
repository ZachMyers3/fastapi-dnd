from flask import Flask

from .models import db
from .views import views

def create_app():
    # initialize app
    app = Flask(__name__)
    # load config
    app.config.from_object('config.Config')
    # initialize database with app
    db.init_app(app)
    # initialize blueprint
    app.register_blueprint(views)

    return app
