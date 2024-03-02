import requests

#Obter informações sobre um Pokémon com base no seu nome.
def get_pokemon_info_by_name(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "id": pokemon_data["id"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "types": [t["type"]["name"] for t in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None
