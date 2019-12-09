from flask_pymongo import PyMongo
from marshmellow import Schema, fields

mongo = PyMongo()

class CharacterSchema(Schema):
  firstName = fields.Str()
  lastName = fields.Str()
  
 class PartySchema(Schema):
  members = fields.List(fields.Nested(CharacterSchema), required=True)
