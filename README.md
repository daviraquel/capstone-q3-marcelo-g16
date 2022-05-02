# Projeto capstone Q3 - Facilitador: Marcelo - Grupo: 16

Seja bem-vindo! Este é o repositório da API do projeto capstone do período Q3 da Kenzie Academy Brasil.
Nosso projeto é um marketplace de NFT's onde os usuários podem vender, comprar e registrar suas criações e coleções.

```
URL base: https://capstone-q3-marcelo-g16.herokuapp.com/api
```

# Endpoints

## POST /users

Deverá fazer o registro de um novo usuário pela inserção dos dados na tabela users.

Requisição padrão:

```json
{
  "user_name": "john_doe",
  "email": "john@mail.com",
  "password": "abcd1234"
}
```

Resposta:
**201 - CREATED**

```json
{
  "id": "HashedId",
  "user_name": "John Doe",
  "email": "john@mail.com"
}
```

### **Possíveis erros:**

Objeto com campos faltando ou em excesso.

Formato da requisição:

```json
{
  "user_name": "john_doe",
  "email": "john@mail.com"
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
  "msg": {
    "entry keys": ["user_name", "email"],
    "expected keys": ["user_name", "email", "password"]
  }
}
```

Username ou email já cadastrado.

Formato da requisição:

```json
{
  "user_name": "john_doe",
  "email": "john@mail.com",
  "password": "abcd1234"
}
```

Resposta:
**409 - CONFLICT**

```json
{
  "Error": "Username or email already in database"
}
```

## GET /users

Retorna todos os usuários cadastrados na API.

Resposta:
**200 - OK**

```json
[
  {
    "id": 1,
    "user_name": "john_doe",
    "email": "john@mail.com",
    "create_date": "Mon, 02 May 2022 13:01:51 GMT",
    "update_date": null
  },
  {
    "id": 2,
    "user_name": "jane_doe",
    "email": "jane@mail.com",
    "create_date": "Mon, 02 May 2022 14:32:02 GMT",
    "update_date": null
  }
]
```

### **Possíveis erros:**

Sem usuários cadastrados na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "There are no users on database"
}
```

## GET /users/\<user_email:str\>

Rota para buscar um usuário específico com base no seu email.

```
GET /users/john@mail.com
```

Resposta:
**200 - OK**

```json
{
  "id": 1,
  "user_name": "john_doe",
  "email": "john@mail.com",
  "create_date": "Mon, 02 May 2022 13:01:51 GMT",
  "update_date": null
}
```

### **Possíveis erros:**

Email não cadastrado na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "User not found"
}
```

## PATCH /users/\<user_email:str\>

Rota para alterar os dados de um usuário específico com base no seu email. O usuário pode alterar a senha e o email mas não o user_name.

Requisição padrão:

```
PATCH /users/john@mail.com
```

```json
{
  "email": "test@mail.com",
  "password": "123456"
}
```

Resposta:
**200 - OK**

```json
{
  "id": 1,
  "user_name": "John Doe",
  "email": "test@mail.com",
  "create_date": "Mon, 02 May 2022 13:01:51 GMT",
  "update_date": "Mon, 02 May 2022 16:03:08 GMT"
}
```

### **Possíveis erros:**

Email não cadastrado na API.

Requisição:

```
PATCH /users/juanito@mail.com
```

```json
{
  "email": "test@mail.com",
  "password": "123456"
}
```

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "User not found"
}
```

Email para alteração já cadastrado em outro usuário.

```
PATCH /users/john@mail.com
```

```json
{
  "email": "jane@mail.com",
  "password": "123456"
}
```

Resposta:
**409 - CONFLICT**

```json
{
  "Error": "Email already exists"
}
```

## DELETE /users/\<user_email:str\>

Rota para deletar os dados de um usuário específico com base no seu email.

Requisição padrão:

```
DELETE /users/john@mail.com
```

Resposta:
**204 - NO CONTENT**

### **Possíveis erros:**

Email não cadastrado na API.

Requisição:

```
DELETE /users/juanito@mail.com
```

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "User not found"
}
```

## POST /nfts

Deverá fazer o registro de uma nova NFT pela inserção dos dados na tabela nfts. A requisição deve contar o id do criador da NFT, id do owner, nome da NFT, valor para negociação, um booleano indicando se estará disponível para venda ou não, uma descrição, um arquivo de imagem e o id da coleção a que pertence.

Requisição padrão:

```json
{
  "creator": 1,
  "owner": 1,
  "name": "john_doe",
  "value": 2.4,
  "for_sale": true,
  "description": "NFT para teste da API",
  "image": "image.png",
  "collection": 1
}
```

Resposta:
**201 - CREATED**

```json
{
  "id": 2,
  "creator": 1,
  "owner": 1,
  "name": "john_doe",
  "for_sale": true,
  "value": "2.4",
  "description": "nft para teste da api",
  "collection": 1,
  "image": "image.png",
  "created_at": "Mon, 02 May 2022 17:28:42 GMT",
  "creator_info": {
    "id": 1,
    "user_name": "John Doe",
    "email": "test@mail.com",
    "create_date": "Mon, 02 May 2022 13:01:51 GMT",
    "update_date": "Mon, 02 May 2022 16:03:08 GMT"
  }
}
```

### **Possíveis erros:**

id do creator, owner ou collection não registrada na API.

Requisição:

```json
{
  "creator": 44,
  "owner": 1,
  "name": "john_doe",
  "value": 2.4,
  "for_sale": true,
  "description": "NFT para teste da API",
  "image": "image.png",
  "collection": 1
}
```

Resposta:
**409 - CONFLICT**

```json
{
  "error": "insert a creator, owner or collection that is already registered."
}
```

Requisição com campos faltantes.

Requisição:

```json
{
  "creator": 1,
  "owner": 1,
  "name": "john_doe",
  "value": 2.4,
  "for_sale": true,
  "description": "NFT para teste da API"
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
  "error": {
    "mandatory keys": [
      "creator",
      "owner",
      "name",
      "value",
      "for_sale",
      "description",
      "image",
      "collection"
    ],
    "missing keys": ["image", "collection"]
  }
}
```

## GET /nfts

Retorna todas as NFT's cadastradas na API.

Resposta:
**200 - OK**

```json
[
  {
    "id": 1,
    "creator": 1,
    "owner": 1,
    "name": "john_doe",
    "for_sale": true,
    "value": "2.4",
    "description": "nft para teste da api",
    "collection": 1,
    "image": "image.png",
    "created_at": "Mon, 02 May 2022 17:28:42 GMT",
    "creator_info": {
      "id": 1,
      "user_name": "John Doe",
      "email": "test@mail.com",
      "create_date": "Mon, 02 May 2022 13:01:51 GMT",
      "update_date": "Mon, 02 May 2022 16:03:08 GMT"
    }
  },
  {
    "id": 2,
    "creator": 1,
    "owner": 1,
    "name": "john_doe2",
    "for_sale": true,
    "value": "2.4",
    "description": "nft para teste da api",
    "collection": 1,
    "image": "image.png",
    "created_at": "Mon, 02 May 2022 17:28:42 GMT",
    "creator_info": {
      "id": 1,
      "user_name": "John Doe",
      "email": "test@mail.com",
      "create_date": "Mon, 02 May 2022 13:01:51 GMT",
      "update_date": "Mon, 02 May 2022 16:03:08 GMT"
    }
  }
]
```

## GET /nfts/\<id:int\>

Rota para buscar uma NFT específica com base no seu id.

```
GET /nfts/2
```

Resposta:
**200 - OK**

```json
{
  "id": 2,
  "creator": 1,
  "owner": 1,
  "name": "john_doe",
  "for_sale": true,
  "value": "2.4",
  "description": "nft para teste da api",
  "collection": 1,
  "image": "image.png",
  "created_at": "Mon, 02 May 2022 17:28:42 GMT",
  "creator_info": {
    "id": 1,
    "user_name": "John Doe",
    "email": "test@mail.com",
    "create_date": "Mon, 02 May 2022 13:01:51 GMT",
    "update_date": "Mon, 02 May 2022 16:03:08 GMT"
  }
}
```

### **Possíveis erros:**

NFT não cadastrada na API.

```
GET /nfts/44
```

Resposta:
**404 - NOT FOUND**

```json
{
  "error": "ntf id 44 not found"
}
```

## PATCH /nfts/\<id:int\>

Rota para alterar os dados de uma NFT específica com base no id. O usuário pode alterar value, for_sale, description e image.

Requisição padrão:

```
PATCH /nfts/2
```

```json
{
  "value": 4.5,
  "for_sale": false
}
```

Resposta:
**200 - OK**

```json
{
  "id": 2,
  "creator": 1,
  "owner": 1,
  "name": "john_doe",
  "for_sale": false,
  "value": "4.5",
  "description": "nft para teste da api",
  "collection": 1,
  "image": "image.png",
  "created_at": "Mon, 02 May 2022 17:28:42 GMT",
  "creator_info": {
    "id": 1,
    "user_name": "John Doe",
    "email": "test@mail.com",
    "create_date": "Mon, 02 May 2022 13:01:51 GMT",
    "update_date": "Mon, 02 May 2022 16:03:08 GMT"
  }
}
```

### **Possíveis erros:**

NFT não cadastrada na API.

Requisição:

```
PATCH /nfts/44
```

```json
{
  "value": 4.5,
  "for_sale": false
}
```

Resposta:
**404 - NOT FOUND**

```json
{
  "error": "nft id 44 not foud"
}
```

Requisição com campos não permitidos.

Requisição:

```
PATCH /nfts/2
```

```json
{
  "owner": 2,
  "for_sale": false
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
  "error": {
    "correct keys": ["value", "for_sale", "description", "image"],
    "received": ["owner"]
  }
}
```

Requisição com campos com tipo errado.

Requisição:

```
PATCH /nfts/2
```

```json
{
  "value": "valor",
  "for_sale": false
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
  "error": "correct the values passed"
}
```

## DELETE /nfts/\<id:int\>

Rota para deletar os dados de uma NFT específica com base no id.

Requisição padrão:

```
DELETE /nft/2
```

Resposta:
**204 - NO CONTENT**

### **Possíveis erros:**

NFT não cadastrada na API.

Requisição:

```
DELETE /nft/44
```

Resposta:
**404 - NOT FOUND**

```json
{
  "error": "nft id 44 not found"
}
```
