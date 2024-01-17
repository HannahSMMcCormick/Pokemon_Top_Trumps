# CFG Pokemon Top Trumps python 

#Imported packages 
import random
import requests

#Generates random pokemon Id to select card
def get_random_pokemon_id():
    return random.randint(1,151)


#
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    responce = requests.get(url)
    if responce.status_code == 200:
        data = responce.json()
        return{
            'name': data['name'],
            'id':data['id'],
            'height': data['height'],
            'weight': data['weight']
        }
    else:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None