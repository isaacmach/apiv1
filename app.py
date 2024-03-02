from flask import Flask, request, jsonify
from pokename import get_pokemon_info_by_name
from pokerandon import get_random_pokemon_by_type
from biggername import get_longest_pokemon_name_by_type
from pokeclimate import get_random_pokemon
from auth import authenticate
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configuração do Flask JWT Extended
app.config['JWT_SECRET_KEY'] = 'ISAACMACHADO'  # Chave secreta para assinar os tokens
jwt = JWTManager(app)

# Rota para login e geração de token
@app.route('/login', methods=['POST'])

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    token = authenticate(username, password)
    if token:
        return jsonify(access_token=token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401

# Rota protegida que requer autenticação JWT
@app.route('/protected', methods=['GET'])
@jwt_required()

def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

#get_pokemon_info_by_name
@app.route('/get_pokemon_info_by_name', methods=['GET','POST'])
@jwt_required()

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
@app.route('/get_random_pokemon_by_type', methods=['GET','POST'])
@jwt_required()

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
@app.route('/get_longest_pokemon_name_by_type', methods=['GET','POST'])
@jwt_required()

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
@app.route('/get_random_pokemon_by_city', methods=['GET','POST'])
@jwt_required()

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
