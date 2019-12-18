import json

JSON_FILE = '../spells.json'
NEW_FILE = 'spells.json'

MINUTES_TO_SECOND = 60
HOURS_TO_SECOND =  MINUTES_TO_SECOND * 60
ROUND_TO_SECOND = 6
DAYS_TO_SECOND = HOURS_TO_SECOND * 24

MILES_TO_FEET = 5280

def main():
    with open(JSON_FILE, encoding='utf-8') as _f:
        with open(NEW_FILE, 'w', encoding='utf-8') as _w:
            _json = json.load(_f)
            for _o in _json:
                cast_range = _o['range']
                cast_ritual = _o['ritual']
                cast_duration = _o['duration']
                cast_time = _o['casting_time']
                cast_concentration = _o['concentration']
                cast_duration = duration_parser(cast_duration)
                cast_time, action_type = time_parser(cast_time)
                cast_range, touch = range_parser(cast_range)
                # print(f'{cast_range=}')
                # print(f'{cast_ritual=}')
                # print(f'{cast_duration=}')
                # print(f'{cast_time=}')

                casting = {
                    "range": cast_range,
                    "affected": None,
                    "casting_time": cast_time,
                    "action_type": action_type,
                    "duration": cast_duration,
                    "ritual": cast_ritual,
                    "concentration": cast_concentration
                }
            # json.dump(_json, _w, indent=2)

def range_parser(rg):
    rg = rg.lower()
    print(f'{rg=}')

    if rg == 'touch':
        rg = '5'
        touch = True

    if rg == 'self':
        rg = '0'
        touch = True

    

    return '', True

def time_parser(in_time):
    in_time = in_time.lower()

    action_type = ''
    if 'action' in in_time:
        if 'bonus' in in_time:
            action_type = 'bonus'
        elif 'reaction' in in_time:
            action_type = 'reaction'
        else:
            action_type = 'action'

        in_time = in_time.replace('reaction', '')
        in_time = in_time.replace('action', '')
        in_time = in_time.replace('bonus', '')
        in_time = in_time.strip()
        if in_time == '':
            in_time = '1'
        in_time = str(int(in_time) * ROUND_TO_SECOND)
    
    if 'minute' in in_time or 'minutes' in in_time:
        in_time = in_time.replace('minutes', '')
        in_time = in_time.replace('minute', '')
        in_time = in_time.strip()
        in_time = int(in_time) * MINUTES_TO_SECOND
        in_time = str(in_time)

    if ('hour' in in_time or 'hours' in in_time):
        in_time = in_time.replace('hours', '')
        in_time = in_time.replace('hour', '')
        in_time = in_time.strip()
        in_time = int(in_time) * HOURS_TO_SECOND
        in_time = str(in_time)

    return in_time, action_type


def duration_parser(in_duration):
    durations = in_duration.split('/')
    for i in range(len(durations)):
        d = durations[i]
        d = d.lower()
        d = d.replace('up to', '')
        d = d.strip()

        if 'minute' in d or 'minutes' in d:
            d = d.replace('minutes', '')
            d = d.replace('minute', '')
            d = d.strip()
            d = int(d) * MINUTES_TO_SECOND
            d = str(d)

        if ('hour' in d or 'hours' in d):
            d = d.replace('hours', '')
            d = d.replace('hour', '')
            d = d.strip()
            d = int(d) * HOURS_TO_SECOND
            d = str(d)

        if ('instantaneous' in d):
            d = '0'

        if ('until dispelled' in d):
            d = '1'

        if ('special' in d):
            d = '2'

        if ('round' in d or 'rounds' in d):
            d = d.replace('rounds', '')
            d = d.replace('round', '')
            d = d.strip()
            d = int(d) * ROUND_TO_SECOND
            d = str(d)

        if ('days' in d or 'day' in d):
            d = d.replace('days', '')
            d = d.replace('day', '')
            d = d.strip()
            d = int(d) * DAYS_TO_SECOND
            d = str(d)

        durations[i] = int(d)

    return durations


if __name__ == "__main__":
    main()
