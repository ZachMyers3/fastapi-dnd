import json

JSON_FILE = '../spells.json'
NEW_FILE = 'spells.json'

def main():
    with open(JSON_FILE, encoding='utf-8') as _f:
        with open(NEW_FILE, 'w', encoding='utf-8') as _w:
            _json = json.load(_f)
            for _o in _json:
                # archetype = tryValue(_o, 'archetype')
                patrons = tryValue(_o, 'patrons')
                school = tryValue(_o, 'school')
                domains = tryValue(_o, 'domains')
                oaths = tryValue(_o, 'oaths')
                circles = tryValue(_o, 'circles')
                print(f'{patrons=}\n{school=}\n{domains=}\n{oaths=}\n{circles=}')
                print('============================')

                
                new_json = {
                    
                }
                _o['components'] = new_json
            json.dump(_json, _w, indent=2)

def tryValue(jsonObject, inKey):
    # try and find key value from jsonObject
    try:
        ret = jsonObject[inKey]
        ret = ret.split(',')
    except KeyError:
        ret = None

    # scrub whitespace from lists
    if isinstance(ret, list):
        for i in range(len(ret)):
            ret[i] = ret[i].strip()

    return ret


if __name__ == "__main__":
    main()
