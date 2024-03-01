from flask import Flask, request, jsonify
from pokename import get_pokemon_info_by_name
from pokerandon import get_random_pokemon_by_type
from biggername import get_longest_pokemon_name_by_type
from pokeclimate import get_random_pokemon

app = Flask(__name__)

#get_pokemon_info_by_name
@app.route('/get_pokemon_info_by_name', methods=['POST'])
def get_pokemon():
    data = request.json
    if 'pokemon_name' in data:
        pokemon_name = data['pokemon_name']
        pokemon_info = get_pokemon_info_by_name(pokemon_name)
        if pokemon_info:
            return jsonify(pokemon_info)
        else:
            return jsonify({"error": f"Não foi possível encontrar informações para o Pokémon {pokemon_name}"}), 404
    else:
        return jsonify({"error": "Campo 'pokemon_name' não encontrado"}), 400
    
#get_random_pokemon_by_type
@app.route('/get_random_pokemon_by_type', methods=['POST'])
def random_pokemon():
    data = request.json
    if 'pokemon_type' in data:
        pokemon_type = data['pokemon_type']
        random_pokemon_name = get_random_pokemon_by_type(pokemon_type)
        if random_pokemon_name:
            return jsonify({"pokemon_name": random_pokemon_name})
        else:
            return jsonify({"error": f"Não foi possível encontrar um Pokémon do tipo {pokemon_type}"}), 404
    else:
        return jsonify({"error": "Campo 'pokemon_type' não encontrado"}), 400    

#get_longest_pokemon_name_by_type
@app.route('/get_longest_pokemon_name_by_type', methods=['POST'])
def longest_pokemon_name():
    data = request.json
    if 'pokemon_type' in data:
        pokemon_type = data['pokemon_type']
        longest_name = get_longest_pokemon_name_by_type(pokemon_type)
        if longest_name:
            return jsonify({"longest_pokemon_name": longest_name})
        else:
            return jsonify({"error": f"Não foi possível encontrar um Pokémon do tipo {pokemon_type}"}), 404
    else:
        return jsonify({"error": "Campo 'pokemon_type' não encontrado"}), 400

#get_random_pokemon_by_city
@app.route('/get_random_pokemon_by_city', methods=['GET'])
def get_random_pokemon_route():
    # Obter coordenadas de latitude e longitude da requisição
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    # Chave da API do OpenWeatherMap
    api_key_openweathermap = "24b7c1745c0606680c7aa976c759921e"

    # Obter um Pokémon aleatório com base nas coordenadas
    random_pokemon = get_random_pokemon(latitude, longitude, api_key_openweathermap)

    # Retornar o Pokémon aleatório em formato JSON
    if random_pokemon:
        return jsonify({'random_pokemon': random_pokemon}), 200
    else:
        return jsonify({'error': 'Não foi possível obter um Pokémon.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
