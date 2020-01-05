from flask_apscheduler import APScheduler

from .models import mongo
from .scripts.character_calc import calc_skill_mods, calc_spells_available

scheduler = APScheduler()

@scheduler.task('cron', id='update_character_spell_list', day='*')
def update_character_spell_list():
    print(f'Calculating variuous attributes for characters...')
    characters = mongo.db.characters.find()
    for character in characters:
        print(f'Updating calculated attributes for {character["firstName"]} {character["lastName"]}...')
        character = calc_skill_mods(character, mongo)
        character = calc_spells_available(character, mongo)
        mongo.db.characters.update_one({'_id': character['_id']}, {'$set': character})
    print(f'Attributes finished calculating!')
