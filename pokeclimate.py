import requests
import random

def get_current_weather(latitude, longitude, api_key_openweathermap):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key_openweathermap}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_main = data['weather'][0]['main']
        return weather_main
    else:
        print(f"Erro ao obter informações de clima para a localização atual: {response.status_code}")
        return None

def get_strongest_type(weather):
    weather_mapping = {
        "Clear": "fire",
        "Clouds": "normal",
        "Rain": "water",
        "Snow": "ice"
        # Adicione mais mapeamentos conforme necessário
    }
    return weather_mapping.get(weather, "normal")

def get_random_pokemon(latitude, longitude, api_key_openweathermap):
    weather = get_current_weather(latitude, longitude, api_key_openweathermap)
    if weather:
        strongest_type = get_strongest_type(weather)
        url = f"https://pokeapi.co/api/v2/type/{strongest_type.lower()}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            pokemon_names = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
            filtered_pokemon_names = [name for name in pokemon_names if any(letter in name for letter in ['i', 'a', 'm'])]
            
            if filtered_pokemon_names:
                random_pokemon_name = random.choice(filtered_pokemon_names)
                return random_pokemon_name
            else:
                print("Não foram encontrados Pokémon com as letras 'I', 'A' ou 'M' em seus nomes.")
                return None
        else:
            print(f"Erro ao obter informações do tipo de Pokémon para {strongest_type}: {response.status_code}")
            return None
    else:
        print("Não foi possível obter as informações de clima.")
        return None
