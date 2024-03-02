# 1 - ESQUEMA DE AUTENTICAÇÃO JWT

1. **Início de Sessão do Usuário**: O usuário fornece credenciais de início de sessão.
2. **Verificação das Credenciais**: As credenciais são verificadas.
3. **Criação do Token JWT**: Se as credenciais forem válidas, é gerado um token JWT e enviado de volta para o cliente.
4. **Armazenamento do Token pelo Cliente**: O cliente armazena o token JWT.
5. **Envio do Token em Solicitações Futuras**: O token JWT é incluído em cada solicitação subsequente do cliente.
6. **Validação do Token JWT**: O token é validado pela API.
7. **Autorização de Acesso**: Se o token for válido, a API concede acesso aos recursos solicitados.
8. **Expiração e Renovação do Token JWT (Opcional)**: Os tokens podem ter uma data de expiração e pode ser implementado um mecanismo de renovação.

# 2 - ENDPOINTS

## 2.1 - Login
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
