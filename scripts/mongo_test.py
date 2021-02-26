from dotenv import find_dotenv, load_dotenv
import os
import pymongo

load_dotenv(find_dotenv())

client = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
db = client.dnd
collection = db.spells.find()
