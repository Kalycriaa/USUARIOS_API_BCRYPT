# 🔐 API de Autenticação de Usuários com Flask + Bcrypt

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Flask-Bcrypt](https://img.shields.io/badge/Flask--Bcrypt-Password%20Hash-success)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)

---

# 📖 Sobre o Projeto

Este projeto foi desenvolvido durante meus estudos em desenvolvimento Backend utilizando **Python** e **Flask**.

O principal objetivo desta aplicação foi entender como funciona a segurança no armazenamento de senhas utilizando **Flask-Bcrypt**, aprendendo desde a geração da senha em Hash até sua validação durante o processo de autenticação.

Ao invés de salvar a senha original do usuário no banco de dados, a aplicação gera uma Hash criptográfica antes do cadastro, aumentando significativamente a segurança da aplicação.

Além disso, toda a estrutura foi organizada utilizando arquitetura em camadas, separando responsabilidades entre Models, Services e Routes.

---

# 🚀 Tecnologias Utilizadas

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- SQLite
- Postman

---

# 📁 Estrutura do Projeto

```text
USUARIOS/
│
├── usuarios/
│   ├── models/
│   │     └── usuarios_model.py
│   │
│   ├── services/
│   │     └── usuarios_services.py
│   │
│   └── routes/
│         └── usuarios_routes.py
│
├── extensions.py
├── app.py
└── usuarios.db
```

---

# 🧱 Arquitetura

O projeto foi dividido em camadas para facilitar manutenção, escalabilidade e organização do código.

### Models

Responsável pela representação da tabela do banco de dados.

Foi criado o modelo:

- Usuario

Campos:

- id
- nome
- email
- senha

Também foi implementado o método:

```python
to_dict()
```

Este método converte os objetos do SQLAlchemy em dicionários Python para que possam ser serializados como JSON nas respostas da API.

---

### Services

Toda a regra de negócio da aplicação foi concentrada nesta camada.

Ela possui duas responsabilidades principais:

## Cadastro

Durante o cadastro:

1. Recebe os dados enviados pela requisição;
2. Gera uma Hash da senha utilizando Flask-Bcrypt;
3. Converte a Hash para String (`decode("utf-8")`);
4. Salva o usuário no banco de dados;
5. Retorna o objeto cadastrado.

Exemplo da lógica utilizada:

```python
senha_hash = bcrypt.generate_password_hash(
    dados.get("senha")
).decode("utf-8")
```

Dessa forma, nenhuma senha é armazenada em texto puro no banco de dados.

---

## Login

Durante a autenticação:

1. Busca o usuário pelo email;
2. Caso não exista retorna erro;
3. Caso exista utiliza:

```python
bcrypt.check_password_hash()
```

Essa função compara a senha digitada com a Hash armazenada no banco.

Caso sejam compatíveis:

```python
True
```

Caso contrário:

```python
False
```

O processo acontece utilizando o Salt armazenado dentro da própria Hash, sem necessidade de descriptografar a senha.

---

### Routes

As rotas possuem apenas responsabilidade de comunicação HTTP.

Nelas ficam:

- request.get_json()
- validações
- chamadas da camada Service
- respostas JSON
- códigos HTTP

Toda a regra de negócio permanece isolada na camada Services.

---

# 🔐 Endpoints

## Cadastro

### POST

```http
POST /usuarios
```

Body

```json
{
    "nome":"Felipe Roseno Silva",
    "email":"felipe@gmail.com",
    "senha":"Felipe@123456"
}
```

Resposta

```json
{
    "id":1,
    "nome":"Felipe Roseno Silva",
    "email":"felipe@gmail.com"
}
```

Status

```
201 Created
```

---

## Login

### POST

```http
POST /usuarios/login
```

Body

```json
{
    "email":"felipe@gmail.com",
    "senha":"Felipe@123456"
}
```

Resposta

```json
{
    "id":1,
    "nome":"Felipe Roseno Silva",
    "email":"felipe@gmail.com"
}
```

Status

```
200 OK
```

---

### Usuário inexistente

```json
{
    "error":"usuario nao existe"
}
```

Status

```
404 Not Found
```

---

### Senha incorreta

```json
{
    "error":"senha incorreta."
}
```

Status

```
401 Unauthorized
```

---

### Campos obrigatórios

```json
{
    "error":"por favor preencher todos campos obrigatorio"
}
```

Status

```
400 Bad Request
```

---

# 🧠 O que aprendi neste projeto

Durante este projeto consegui compreender, na prática, como funciona o armazenamento seguro de senhas.

Entre os principais aprendizados estão:

- funcionamento do Hash de senha;
- diferença entre senha original e Hash;
- utilização do Salt automaticamente pelo Bcrypt;
- geração de Hash utilizando `generate_password_hash()`;
- validação utilizando `check_password_hash()`;
- separação de responsabilidades utilizando arquitetura em camadas;
- criação de APIs REST utilizando Flask;
- organização entre Models, Services e Routes;
- serialização de objetos utilizando `to_dict()`;
- testes completos da API utilizando Postman.

---

# 📌 Próximos passos

O próximo objetivo deste projeto será implementar autenticação baseada em **JWT (JSON Web Token)**.

Com isso será possível:

- gerar Tokens após login;
- proteger rotas privadas;
- autenticar usuários utilizando Bearer Token;
- criar um fluxo completo de autenticação Backend.

---

# 👨‍💻 Autor

**Kaio Silva Nascimento**

Estudante de Gestão da Tecnologia da Informação e Desenvolvedor Backend Python.

Atualmente focado em desenvolvimento de APIs REST, arquitetura em camadas, autenticação com JWT, bancos de dados relacionais e boas práticas no desenvolvimento Backend.
