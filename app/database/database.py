from pymongo import MongoClient

from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

if os.environ.get("MONGODB_URI") is None:
    raise ("MONGODB_URI required to connect to database")

client = MongoClient(os.environ.get("MONGODB_URI"))

db = client["dnd"]

print(db.spells.find())