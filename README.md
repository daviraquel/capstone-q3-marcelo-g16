# Projeto capstone Q3 - Facilitador: Marcelo - Grupo: 16

Seja bem-vindo! Este é o repositório da API do projeto capstone do período Q3 da Kenzie Academy Brasil.
Nosso projeto é um marketplace de NFT's onde os usuários podem vender, comprar e registrar suas criações e coleções.

```
URL base: https://capstone-q3-marcelo-g16.herokuapp.com/api
```

# Endpoints

## POST /users/signup

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

## POST /users/signin

Deverá fazer o login do usuário.

Requisição padrão:

```json
{
  "email": "john@mail.com",
  "password": "abcd1234"
}
```

Resposta:
**201 - CREATED**

```json
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### **Possíveis erros:**

Email não cadastrado na API.

Resposta:
**404 - NOT FOUND**

```json
{
	"detail": "this email is not registered"
}
```

Senha ou email incorreta.

Resposta:
**401 - UNAUTHORIZED**

```json
{
	"detail": "email and password missmatch"
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

## GET /users/profile

Rota retorna a informação do usuário logado.

Resposta:
**200 - OK**

```json
{
	"id": 1,
	"user_name": "John_Test",
	"email": "johntest@mail.com",
	"balance": "0",
	"last_deposit": null,
	"create_date": "Wed, 04 May 2022 19:00:13 GMT",
	"update_date": "Wed, 04 May 2022 19:00:13 GMT",
	"NFT's": [
		"john_doe"
	]
}
```

### **Possíveis erros:**

Usuário não cadastrado na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "User not found"
}
```

## PATCH /users/

Rota para alterar os dados de um usuário logado. O usuário pode alterar a senha e o email mas não o user_name.

Requisição padrão:

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
	"user_name": "John_Test",
	"email": "test@mail.com",
	"balance": "0",
	"last_deposit": null,
	"create_date": "Wed, 04 May 2022 19:00:13 GMT",
	"update_date": "Thu, 05 May 2022 20:28:39 GMT"
}
```

### **Possíveis erros:**

Usuário não cadastrado na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "User not found"
}
```

Email para alteração já cadastrado em outro usuário.

Resposta:
**409 - CONFLICT**

```json
{
  "Error": "Email already exists"
}
```

## DELETE /users/

Rota para deletar os dados de um usuário logado.

Resposta:
**204 - NO CONTENT**

### **Possíveis erros:**

Usuário não cadastrado na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "User not found"
}
```

## POST /nfts

Deverá fazer o registro de uma nova NFT pela inserção dos dados na tabela nfts. A requisição deve contar o nome da NFT, valor para negociação, um booleano indicando se estará disponível para venda ou não, uma descrição, um arquivo de imagem e o id da coleção a que pertence.

Requisição padrão:

```json
{
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
	"id": 3,
	"creator": 1,
	"owner": 1,
	"name": "john_doe",
	"for_sale": true,
	"value": "2.4",
	"description": "nft para teste da api",
	"collection": 1,
	"image": "image.png",
	"created_at": "Thu, 05 May 2022 16:17:33 GMT"
}
```

### **Possíveis erros:**

collection não registrada na API.

Resposta:
**400 - BAD REQUEST**

```json
{
	"error": "insert a collection already registered."
}
```

Requisição com campos faltantes.

Requisição:

```json
{
  "value": 2.4,
  "for_sale": true,
  "description": "NFT para teste da API",
  "image": "image.png",
  "collection": 3
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
	"error": "wrong keys",
	"expected_keys": [
		"name",
		"value",
		"for_sale",
		"description",
		"image",
		"collection"
	]
}
```

## GET /nfts

Retorna todas as NFT's cadastradas na API.

Resposta:
**200 - OK**

```json
[
	{
		"id": 2,
		"creator": {
			"name": "John_Doe",
			"email": "john@mail.com"
		},
		"owner": 2,
		"name": "john_doe",
		"for_sale": true,
		"value": "2.4",
		"description": "nft para teste da api",
		"collection": 1,
		"image": "image.png",
		"created_at": "Wed, 04 May 2022 15:10:46 GMT"
	},
	{
		"id": 3,
		"creator": {
			"name": "John_Test",
			"email": "test@mail.com"
		},
		"owner": 1,
		"name": "john_doe",
		"for_sale": true,
		"value": "2.4",
		"description": "nft para teste da api",
		"collection": 1,
		"image": "image.png",
		"created_at": "Thu, 05 May 2022 16:17:33 GMT"
	}
]
```

## GET /nfts/\<id:int\>

Rota para buscar uma NFT específica com base no seu id.

```
GET api/nfts/2
```

Resposta:
**200 - OK**

```json
{
	"id": 2,
	"creator": {
		"name": "John_Doe",
		"email": "john@mail.com"
	},
	"owner": 2,
	"name": "john_doe",
	"for_sale": true,
	"value": "2.4",
	"description": "nft para teste da api",
	"collection": 1,
	"image": "image.png",
	"created_at": "Wed, 04 May 2022 15:10:46 GMT"
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
	"id": 3,
	"creator": 1,
	"owner": 1,
	"name": "john_doe",
	"for_sale": false,
	"value": "4.5",
	"description": "nft para teste da api",
	"collection": 1,
	"image": "image.png",
	"created_at": "Thu, 05 May 2022 16:17:33 GMT"
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

Usuário logado não é o dono da NFT a ser alterada.

Resposta:
**401 - UNAUTHORIZED**

```json
{
	"detail": "only the creator of the NFT can update"
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

Usuário logado não é o dono da NFT a ser deletada.

Resposta:
**401 - UNAUTHORIZED**

```json
{
	"detail": "only the creator of the NFT can delete"
}
```

## POST /collections

Deverá fazer o registro de uma nova collection pela inserção dos dados na tabela collections. A requisição deve contar nome da collection e sua descrição.

Requisição padrão:

```json
{
	"name": "teste",
	"description": "teste"
}
```

Resposta:
**201 - CREATED**

```json
{
	"id": 1,
	"creator": 1,
	"name": "Teste",
	"description": "teste"
}
```

### **Possíveis erros:**

Objeto com campos faltando ou em excesso.

Formato da requisição:

```json
{
	"description": "teste"
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
	"msg": {
		"expected keys": [
			"name",
			"description"
		],
		"entry keys": [
			"description"
		]
	}
}
```

nome da collection já cadastrado.

Resposta:
**409 - CONFLICT**

```json
{
	"Error": "Collection already on database"
}
```

## GET /collections

Retorna todos as collections cadastrados na API.

Resposta:
**200 - OK**

```json
[
  {
    "id": 1,
    "creator": 1,
    "name": "Teste",
    "description": "teste"
  },
  {
    "id": 2,
    "creator": 2,
    "name": "Teste 2",
    "description": "teste 2"
  }
]
```

### **Possíveis erros:**

Sem collections cadastradas na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "There are no collections on database"
}
```

## GET /collections/\<name:str\>

Rota para buscar uma collection específica com base no seu nome.

```
GET /users/teste
```

Resposta:
**200 - OK**

```json
{
	"id": 1,
	"creator": 1,
	"name": "Teste",
	"description": "teste"
}
```

### **Possíveis erros:**

Nome da collection não cadastrada na API.

Resposta:
**404 - NOT FOUND**

```json
{
	"Error": "Collection not found"
}
```

## PATCH /collections/\<name:str\>

Rota para alterar a descrição de uma collection.

Requisição padrão:

```
PATCH api/collections/teste
```

```json
{
	"description": "mudei a descrição"
}
```

Resposta:
**200 - OK**

```json
{
	"id": 1,
	"creator": 1,
	"name": "Teste",
	"description": "mudei a descrição"
}
```

### **Possíveis erros:**

Nome não cadastrado na API.

Requisição:

```
PATCH api/collections/outronome
```

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "Collection not found"
}
```

O usuario que está tentando alterar não é o dono da collection

Resposta:
**401 - NOT UNAUTHORIZED**

```json
{
	"detail": "only the creator of the collection can update"
}
```

Faltando a chave "description" na requisição

Resposta:
**400 - BAD REQUEST**

```json
{
	"msg": {
		"expected key": "description",
		"entry keys": []
	}
}
```

## DELETE /collections/\<name:str\>

Rota para deletar uma collection com base no seu nome.

Requisição padrão:

```
DELETE api/collections/teste
```

Resposta:
**204 - NO CONTENT**

### **Possíveis erros:**

collection não cadastrada na API.

Requisição:

```
DELETE api/collections/outronome
```

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "Collection not found"
}
```

O usuario que está tentando deletar não é o dono da collection

Resposta:
**401 - NOT UNAUTHORIZED**

```json
{
	"detail": "only the creator of the collection can delete"
}
```

## POST /categories

Deverá fazer o registro de uma nova categoria. A requisição deve contar nome da categoria e sua descrição.

Requisição padrão:

```json
{
	"name": "teste",
	"description": "teste"
}
```

Resposta:
**201 - CREATED**

```json
{
	"id": 1,
	"name": "Teste",
	"description": "teste"
}
```

### **Possíveis erros:**

Objeto com campos faltando ou em excesso.

Formato da requisição:

```json
{
	"name": "teste"
}
```

Resposta:
**400 - BAD REQUEST**

```json
{
	"msg": {
		"expected keys": [
			"name",
			"description"
		],
		"entry keys": [
			"name"
		]
	}
}
```

## GET /categories

Retorna todos as collections cadastrados na API.

Resposta:
**200 - OK**

```json
[
	{
		"id": 1,
		"name": "Teste",
		"description": "teste"
	},
	{
		"id": 2,
		"name": "Teste 2",
		"description": "teste 2"
	}
]
```

### **Possíveis erros:**

Sem categorias cadastradas na API.

Resposta:
**404 - NOT FOUND**

```json
{
  "Error": "There are no categories on database"
}
```

## GET /categories/\<name:str\>

Rota para buscar uma categoria específica com base no seu nome.

```
GET /users/teste
```

Resposta:
**200 - OK**

```json
{
	"id": 1,
	"name": "Teste",
	"description": "teste",
	"collection": []
}
```

### **Possíveis erros:**

Nome da collection não cadastrada na API.

Resposta:
**404 - NOT FOUND**

```json
{
	"Error": "Category not found"
}
```

## PATCH /categories/\<name:str\>

Rota para alterar a descrição de uma categoria.

Requisição padrão:

```
PATCH api/categories/teste
```

```json
{
	"description": "mudei a descrição"
}
```

Resposta:
**200 - OK**

```json
{
	"id": 1,
	"name": "Teste",
	"description": "mudei a descrição"
}
```

### **Possíveis erros:**

Nome não cadastrado na API.

Requisição:

```
PATCH api/categories/outronome
```

Resposta:
**404 - NOT FOUND**

```json
{
	"Error": "Category not found"
}
```

Faltando a chave "description" na requisição

Resposta:
**400 - BAD REQUEST**

```json
{
	"msg": {
		"expected key": "description",
		"entry keys": []
	}
}
```

## DELETE /categories/\<name:str\>

Rota para deletar uma categoria com base no seu nome.

Requisição padrão:

```
DELETE api/categories/teste
```

Resposta:
**204 - NO CONTENT**

### **Possíveis erros:**

categoria não cadastrada na API.

Requisição:

```
DELETE api/categories/outronome
```

Resposta:
**404 - NOT FOUND**

```json
{
	"Error": "Category not found"
}
```