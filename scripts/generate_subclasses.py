import json

JSON_FILE = "../spells.json"
NEW_FILE = "spells.json"


def main():
    with open(JSON_FILE, encoding="utf-8") as _f:
        with open(NEW_FILE, "w", encoding="utf-8") as _w:
            _json = json.load(_f)
            for _o in _json:
                # gather all the subclass information into lists
                patrons = tryValue(_o, "patrons")
                domains = tryValue(_o, "domains")
                oaths = tryValue(_o, "oaths")
                circles = tryValue(_o, "circles")
                classes = _o["classes"]
                # create objects for all classes in list
                for i in range(len(classes)):
                    classes[i] = {"class": classes[i]}
                # go through all of the subclass lists and add if needed
                classes = add_subclass("Warlock", patrons, classes)
                classes = add_subclass("Cleric", domains, classes)
                classes = add_subclass("Paladin", oaths, classes)
                classes = add_subclass("Druid", circles, classes)
                # set objects classes attribute to new data
                _o["classes"] = classes
                # remove old attributes
                _o.pop("patrons", None)
                _o.pop("domains", None)
                _o.pop("oaths", None)
                _o.pop("circles", None)

            json.dump(_json, _w, indent=2)


def add_subclass(inName, inSubClass, classList):
    # exit if the list is empty
    if not inSubClass:
        return classList

    for i in range(len(classList)):
        if classList[i]["class"].lower() == inName.lower():
            classList[i]["subclasses"] = inSubClass

    return classList


def tryValue(jsonObject, inKey):
    # try and find key value from jsonObject
    try:
        ret = jsonObject[inKey]
        ret = ret.split(",")
    except KeyError:
        ret = None

    # scrub whitespace from lists
    if isinstance(ret, list):
        for i in range(len(ret)):
            ret[i] = ret[i].strip()

    return ret


if __name__ == "__main__":
    main()
