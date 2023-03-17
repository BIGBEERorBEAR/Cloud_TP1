import json
import random
import datetime
import time
import paho.mqtt.client as paho

# Chargement des données du fichier JSON
with open('tp1.json', 'r') as f:
    data = json.load(f)

def generate_random_coords():
    # Définir les limites géographiques de Toulouse
    min_lat, max_lat = 43.5291, 43.7075
    min_long, max_long = 1.3484, 1.5348
    
    # Générer des coordonnées GPS aléatoires
    latitude = round(random.uniform(min_lat, max_lat), 6)
    longitude = round(random.uniform(min_long, max_long), 6)    
    return latitude, longitude

def allure(vehicule):
    if vehicule == 'T.E.R':
        return '83.1'
    elif vehicule == 'Tramway':
        return '18.1'
    elif vehicule == 'Metro':
        return '35.1'

def conso(vehicule):
    if vehicule == 'T.E.R':
        return '140'
    elif vehicule == 'Tramway':
        return '120'
    elif vehicule == 'Metro':
        return '110'
    
def vitesse(vehicule):
    if vehicule == 'T.E.R':
        return '3'
    elif vehicule == 'Tramway':
        return '1'
    elif vehicule == 'Metro':
        return '2'


def create_trames(i):
# Boucle à travers les données pour créer les trames
    latitude, longitude = generate_random_coords()
    now = datetime.datetime.now()
    t = int(now.timestamp())

    # Détermination du constructeur
    # Création de la trame pour Alstom
    V_id = 0
    for j in range (0, 3):
        if data['VEHICULES'][i]['VEHICLE_TYPE_ID'] == data['VEHICULE_TYPE'][j]['ID']:
            V_id = j
    trame = f"{data['VEHICULES'][i]['VIN']}|{str(latitude)}|{str(longitude)}|{allure(data['VEHICULE_TYPE'][V_id]['NAME'])}|{str(t)}|{data['VEHICULE_TYPE'][V_id]['CAPACITY']}|{conso(data['VEHICULE_TYPE'][V_id]['NAME'])}|{vitesse(data['VEHICULE_TYPE'][V_id]['NAME'])}"
    print(trame)

def all_trames():
    nb_trames = round(random.uniform(1, 15))
    for i in range (0, nb_trames):
        init_tram = round(random.uniform(0, nb_trames))
        create_trames(init_tram)
# create client object
client = paho.Client("example")
    # establish connection
client.connect("localhost", 1883)
    # loop
for i in range(10):
        # send message
    client.publish("topic_ssie", all_trames())
        # sleep
    time.sleep(1)
    # disconnection
client.disconnect()