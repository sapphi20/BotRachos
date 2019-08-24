import json
import random

import requests

beacon_url = "https://beacon.clcert.cl/beacon/2.0/pulse/last"
funfact_uri = "/json/datosCuriosos.json"


def json_save(db, key, value):
    with open(db, "r") as d:
        data = json.load(d)
    data[key] = value

    with open(db, "w+") as f:
        f.write(json.dumps(data))


def json_get(db, group, key):
    with open(db, "r")as d:
        data = json.load(d)
    if group in data:
        if key in group:
            return data[group][key]
    return None


def random_funfact(data):
    """
    :param data:str con la direccion relativa del archivo JSON a abrir
    :return: str con el dato aleatorio , str con el tipo
    """
    with open(data) as d:
        data_dict = json.load(d)
    content = requests.get(beacon_url)
    seed = content.json()['pulse']['outputValue']
    random.seed(seed)
    length = len(data_dict['datos_curiosos'])
    selected = random.randint(0, length - 1)
    return data_dict['datos_curiosos'][selected]['content'], data_dict['datos_curiosos'][selected]['type']
