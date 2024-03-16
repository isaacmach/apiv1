# 1 - ESQUEMA DE AUTENTICAÇÃO JWT

1. **Início de Sessão do Usuário**: O usuário fornece credenciais de início de sessão.
2. **Verificação das Credenciais**: As credenciais são verificadas.
3. **Criação do Token JWT**: Se as credenciais forem válidas, é gerado um token JWT e enviado de volta para o cliente.
4. **Armazenamento do Token pelo Cliente**: O cliente armazena o token JWT.
5. **Envio do Token em Solicitações Futuras**: O token JWT é incluído em cada solicitação subsequente do cliente.
6. **Validação do Token JWT**: O token é validado pela API.
7. **Autorização de Acesso**: Se o token for válido, a API concede acesso aos recursos solicitados.
8. **Expiração e Renovação do Token JWT (Opcional)**: Os tokens podem ter uma data de expiração e pode ser implementado um mecanismo de renovação.

# 2 - ENDPOINTS - Para acessar todos os endpoints, é necessário incluir um token de validação JWT no cabeçalho de autenticação (Authentication Header).

## 2.1 - Login: Obter um token JWT válido usando as credenciais corretas.
- **Endpoint**: `http://localhost:5000/login`
- **Método**: POST
- **Corpo da Requisição**:
```json
{
    "username": "isaac",
    "password": "123456"
}
Retorno
{
    "access_token": "JWTTOKEN"  
}
Use JWT token for authorization in the authentication header (Authorization).
```
## 2.2 - Obter o tipo de um Pokémon (fogo, água, terra, ar, etc…) pelo seu nome.
- **Endpoint**: `http://localhost:5000/get_pokemon_info_by_name`
- **Método**: POST
- **Corpo da Requisição**:
```json
{
    "pokemon_name": "pikachu"
}
```
## 2.3 - Obter um Pokémon aleatório de um tipo específico.
- **Endpoint**: `http://localhost:5000/get_random_pokemon_by_type`
- **Método**: POST
- **Corpo da Requisição**:
```json
{
    "pokemon_type": "fire"
}
```
## 2.4 - Obter o Pokémon com o nome mais longo de um determinado tipo.
- **Endpoint**: `http://localhost:5000/get_longest_pokemon_name_by_type`
- **Método**: POST
- **Corpo da Requisição**:
```json
{
    "pokemon_type": "fire"
}
```
## 2.5 - Obter um Pokémon aleatório que contenha uma das letras ‘I’,’A’,’M’ em seu nome e que seja do tipo específico mais forte com base no clima atual da sua cidade.
- **Endpoint**: `http://localhost:5000/get_random_pokemon_by_city`
- **Método**: GET

# 3 - Instruções DockerHub
```bash
docker run -p 5000:5000 isaacmachado098/pokeflaskapi:main
```
# 5 - Fluxo 
![image](https://github.com/isaacmach/POKECHALLENGE_V2/assets/123345527/47a0d7f1-9765-4fad-9a9d-123887a050df)

# 6 - APIs externas 
- **PokeApi**
- **Openweathermap**

