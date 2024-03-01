import requests

def get_longest_pokemon_name_by_type(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        longest_name = ""
        for pokemon in data["pokemon"]:
            pokemon_name = pokemon["pokemon"]["name"]
            if len(pokemon_name) > len(longest_name):
                longest_name = pokemon_name
        return longest_name
    else:
        print(f"Erro ao obter lista de Pokémon do tipo {pokemon_type}: {response.status_code}")
        return None