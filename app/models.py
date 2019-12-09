from flask_pymongo import PyMongo
from marshmellow import Schema, fields

mongo = PyMongo()

class CharacterSchema(Schema):
  firstName = fields.Str()
  lastName = fields.Str()
  # base stats
  strength = fields.Int()
  dexterity = fields.Int()
  constitution = fields.Int()
  intelligence = fields.Int()
  wisdom = fields.Int()
  charisma = fields.Int()
  # vitals
  currentHP = fields.Int()
  maxHP = fields.Int()
  currentAC = fields.Int()
  baseAC = fields.Int()
   
 class PartySchema(Schema):
  members = fields.List(fields.Nested(CharacterSchema), required=True)
