import json

JSON_FILE = "../spells.json"
NEW_FILE = "spells.json"


def main():
    with open(JSON_FILE, encoding="utf-8") as _f:
        with open(NEW_FILE, "w", encoding="utf-8") as _w:
            _json = json.load(_f)
            for _o in _json:
                comp = _o["components"]
                try:
                    mats = _o["material"]
                    _o.pop("material", None)
                except KeyError:
                    mats = ""
                comp_raw = comp
                comp_v = "V" in comp
                comp_s = "S" in comp
                comp_m = "M" in comp
                new_json = {
                    "material": comp_m,
                    "materials_needed": mats,
                    "raw": comp_raw,
                    "somantic": comp_s,
                    "verbal": comp_v,
                }
                _o["components"] = new_json
            json.dump(_json, _w, indent=2)


if __name__ == "__main__":
    main()
