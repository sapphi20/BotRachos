import random

import requests

from config import BASE_PATH
# API URL
from src.utils import json_get, json_save

beacon_last_url = "https://beacon.clcert.cl/beacon/2.0/pulse/last"
beacon_url = "https://beacon.clcert.cl/beacon/2.0/chain/4/pulse/"

# Python dict containing the information of the last lottery
DATA = None
db = BASE_PATH + "/json/db.json"


def get_last_pulse():
    """
    obtiene el ultimo pulso generado por faro de aleatoridad de clcert
    :return: par con el indice del pulso y la seed para generar la aleatoridad
    """
    content = requests.get(beacon_last_url)

    # JSON containing all the pulse data
    pulse = content.json()["pulse"]

    # Random string of 512 bits obtained from the pulse
    seed = pulse["outputValue"]

    # This index will be used by the observer to verify the process
    pulse_index = pulse["pulseIndex"]

    return pulse_index, seed


# falta sacar el ultimo compa de la lista
def run_choice(participantes, id_grupo):
    """
    :param participantes: lista con la informacion de los participantes
    :param id_grupo: id del grupo para buscar
    :return: participante elegido
    """
    elegido = None
    vueltas = 1
    pulse_index, seed = get_last_pulse()

    last_boy = json_get(db, id_grupo, "ultimo_conductor")  # meter aqui el niño sacado del diccionario

    # Seed the PRNG
    random.seed(seed)
    if last_boy is not None:
        check = verify(id_grupo)
    else:
        check = True
    # The list to be shared
    if check:
        while True:
            elegido = participantes[(random.randint(0, len(participantes) - 1))]
            if elegido != last_boy:
                break
            else:
                vueltas += 1
                continue
    if elegido is not None:
        json_save(db, id_grupo, {"ultimo_pulso": pulse_index,
                                 "ultimo_conductor": elegido,
                                 "ultimo_grupo": participantes,
                                 "vueltas": vueltas})
    return elegido


def verify(id_grupo):
    """
    permite comprobar que la aleatoridad fue generada correctamente
    :param id_grupo: grupo de telegram al que se le va a consultar la aleatoridad
    :return: boolean true or false
    """

    seed = get_seed_by_pid(
        json_get(db, id_grupo, "ultimo_pulso"))  # aqui va la llamada al diccionario para la seed usada

    random.seed(seed)
    last_boy = json_get(db, id_grupo, "ultimo_conductor")  # aqui va el niño del diccionario
    grupo = json_get(db, id_grupo, "ultimo_grupo")
    vueltas = json_get(db, id_grupo, "vueltas")

    elegido = None

    for i in range(vueltas):
        elegido = grupo.get(random.randint(0, grupo.length - 1))

    if last_boy == elegido:
        return True
    return False


"""
def publish(pulse_id, initial_data, tries, result):
    global DATA
    DATA = dict(
        pulseId=pulse_id,
        initialData=initial_data,
        tries=tries,
        resultData=result
    )
    print("DATA =", DATA)
"""


def get_seed_by_pid(pulse_id):
    content = requests.get(beacon_url + str(pulse_id))

    # JSON containing all the pulse data
    pulse = content.json()["pulse"]

    # Random string of 512 bits obtained from the pulse
    seed = pulse["outputValue"]
    return seed


def rand_verify(id_group):
    beacon = json_get(db, id_group, "ultimo_pulso")
    gente = json_get(db, id_group, "ultimo_grupo")
    ultimo_conductor = json_get(db, id_group, "ultimo_conductor")
    if beacon is None:
        return "No han hecho un grupo"
    msg = "El ultimo sorteo se genero con las siguientes personas:\n" + \
        '\n'.join(gente) + \
        "Y el conductor designado fue " + ultimo_conductor + ".\n" + \
        "Reclamos a la FIFA a traves de " + beacon_url + beacon + "."
    return msg
