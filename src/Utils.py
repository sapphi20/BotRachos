import json


def json_save(db, key, value):
    with open(db, "r") as d:
        data = json.load(d)
    data[key] = value

    with open(db, "w+") as f:
        f.write(json.dumps(data))
