from dotenv import find_dotenv, load_dotenv
import motor.motor_asyncio
import os

load_dotenv(find_dotenv())

if os.environ.get("MONGODB_URI") is None:
    raise ("MONGODB_URI environment variable required")

print(os.environ.get("MONGODB_URI"))

# connect to mongo server
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("MONGODB_URI"))
# connect to our dnd database
database = client.dnd

# generate collection objects
# characters_collection = database.get_collecttion("characters")
# equipment_collection = database.get_collection("equipment")
spells_collection = database.get_collection("spells")
