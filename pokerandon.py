import requests
import random

#Obter um Pokémon aleatório com base no tipo específico.
def get_random_pokemon_by_type(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_names = [pokemon["pokemon"]["name"] for pokemon in data["pokemon"]]
        random_pokemon_name = random.choice(pokemon_names)
        return random_pokemon_name
    else:
        print(f"Erro ao obter lista de Pokémon do tipo {pokemon_type}: {response.status_code}")
        return None