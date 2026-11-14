# Sistema de Controle de Contas

Projeto desenvolvido para praticar programação e desenvolvimento de aplicações, começando com Python e evoluindo para uma aplicação web com integração entre frontend e backend.

O Sistema de Controle de Contas permite cadastrar, visualizar, editar e remover contas, além de acompanhar informações como valores, vencimentos e contas fixas.

## Funcionalidades

- Cadastro de contas;
- Listagem de contas cadastradas;
- Edição completa dos dados de uma conta;
- Atualização parcial de informações;
- Exclusão de contas;
- Validação dos dados cadastrados;
- Identificação de contas fixas;
- Cálculo do valor total das contas;
- Contagem de contas cadastradas;
- Contagem de contas fixas;
- Armazenamento dos dados em arquivo JSON;
- Persistência dos dados mesmo após reiniciar o servidor.

## Tecnologias utilizadas

**Backend**
- Python 3
- FastAPI
- Pydantic
- JSON

**Frontend**
- React
- JavaScript
- Vite
- CSS

## Estrutura do projeto

```text

Sistema-controle-de-contas/
│
├── Backend/
│   ├── main.py
│   ├── contas.py
│   └── contas.json
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── requirements.txt
└── README.md

```

## Como executar o projeto

### 1. Backend

Na pasta principal do projeto, execute:

```bash
fastapi dev Backend/main.py
```

O backend ficará disponível em:

`http://127.0.0.1:8000`

A documentação interativa da API pode ser acessada em:

`http://127.0.0.1:8000/docs`

### 2. Frontend

Abra outro terminal e entre na pasta frontend:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

Execute a aplicação:

```bash
npm run dev
```

O frontend ficará disponível no endereço informado pelo Vite, normalmente:

`http://localhost:5173`

## API — Rotas disponíveis

| Método | Rota | Descrição |
|---|---|---|
| GET | `/contas` | Lista as contas |
| POST | `/contas` | Cadastra uma conta |
| PUT | `/contas/{nomeConta}` | Atualiza todos os dados |
| PATCH | `/contas/{nomeConta}` | Atualiza dados específicos |
| DELETE | `/contas/{nomeConta}` | Remove uma conta |

## Persistência de dados

Os dados das contas são armazenados no arquivo `Backend/contas.json`, utilizando o módulo JSON do Python.

Dessa forma, as informações permanecem salvas mesmo após o encerramento ou reinicialização do servidor.

## Objetivo do projeto

Este projeto faz parte do meu processo de aprendizagem em programação e desenvolvimento de software.

Foi iniciado como uma aplicação de terminal em Python e evoluiu gradualmente para uma aplicação web, permitindo aplicar conhecimentos em:

- Lógica de programação;
- Funções e modularização;
- Listas e dicionários;
- Manipulação de arquivos;
- Persistência de dados;
- Desenvolvimento de APIs;
- Integração entre frontend e backend;
- Desenvolvimento de interfaces com React;
- Operações CRUD.

O desenvolvimento acontece de forma incremental, com implementação e testes de novas funcionalidades conforme os conhecimentos são adquiridos.