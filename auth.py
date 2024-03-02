from flask_jwt_extended import create_access_token
from users import users

def authenticate(username, password):
    # Verifica se o usuário existe e a senha está correta
    if username in users and users[username] == password:
        # Retorna o token de acesso se a autenticação for bem-sucedida
        return create_access_token(identity=username)
    else:
        return None