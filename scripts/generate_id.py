import json
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Add ID number to all json objects in list')
    parser.add_argument('-f', '--file', required=True, type=str, help='Directory to input file')
    parser.add_argument('-o', '--out', required=True, type=str, help='Directory to save file')
    return parser.parse_args()

def main():
    # get the file from command args
    args = get_args()
    json_id = 0
    with open(args.file, encoding='utf-8') as _f:
        with open(args.out, 'w', encoding='utf-8') as _w:
            _json = json.load(_f)
            for _o in _json:
                _o['id'] = json_id
                json_id += 1
                # print(f'{_o}')
            json.dump(_json, _w, indent=2)

if __name__ == "__main__":
    main()
