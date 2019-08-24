import json
import random
import requests

beacon_url = "https://beacon.clcert.cl/beacon/2.0/pulse/last"


def random_funfact(data):
    """
    :param data:str con la direccion relativa del archivo JSON a abrir
    :return: str con el dato aleatorio
    """
    with open(data) as d:
        dict = json.load(d)
    content = requests.get(beacon_url)
    seed = content.json()['pulse']['outputValue']
    random.seed(seed)
    l = len(dict['datos_curiosos'])
    return dict['datos_curiosos'][random.randint(0, l - 1)]['content']
