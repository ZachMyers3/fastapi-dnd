""" Flask config class """
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config(object):
    # general config
    TESTING = bool(os.environ.get("TESTING"))
    DEBUG = bool(os.environ.get("DEBUG"))
    FLASK_ENV = os.environ.get("FLASK_ENV")
    # flask-pymongo
    MONGO_URI = os.environ.get("MONGODB_URI")
    # MONGO_URI = os.environ.get('MONGO_URI')

    SCHEDULER_API_ENABLED = True
