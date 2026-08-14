# Sistema de Controle de Contas

Projeto desenvolvido em **Python** para praticar lógica de programação, organização de código, funções, manipulação de arquivos e persistência de dados utilizando JSON.

O sistema permite cadastrar, visualizar e remover contas, mantendo os dados salvos mesmo após o encerramento do programa.

## Funcionalidades atuais

* Cadastro de contas
* Validação de dia e mês de vencimento
* Identificação de contas fixas
* Validação da resposta de conta fixa
* Cálculo do valor total das contas
* Contagem de contas cadastradas
* Contagem de contas fixas
* Remoção de contas cadastradas
* Verificação de conta existente durante a remoção
* Armazenamento dos dados em `contas.json`
* Leitura automática das contas já salvas
* Listagem formatada das contas
* Organização da lógica do sistema utilizando funções
* Separação entre o fluxo principal e as funções do sistema

## Tecnologias utilizadas

* Python 3
* Módulo `json`

## Estrutura do projeto

```text
controle-contas/
│
├── main.py
├── contas.py
├── contas.json
└── README.md
```

### `main.py`

Responsável pelo fluxo principal do programa e pela interação com o usuário.

### `contas.py`

Contém as funções responsáveis pelas operações do sistema, como:

* carregar contas;
* salvar contas;
* cadastrar contas;
* listar contas;
* remover contas;
* calcular o resumo das contas.

### `contas.json`

Arquivo utilizado para armazenar as contas cadastradas e manter os dados entre diferentes execuções do programa.

## Como executar

Certifique-se de possuir o Python 3 instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

## Próximas melhorias

* Marcar contas como pagas
* Separar contas pagas e pendentes
* Interface gráfica para facilitar a utilização do sistema
* Relatórios mensais
* Melhorar as validações de entrada
* Tratamento específico de erros
* Melhorar a organização e padronização do código

## Objetivo do projeto

Este projeto faz parte do meu portfólio de estudos em **Python** e tem como objetivo desenvolver conhecimentos em:

* lógica de programação;
* funções;
* listas;
* dicionários;
* módulos;
* manipulação de arquivos;
* JSON;
* persistência de dados;
* organização e modularização de código.

O projeto está sendo desenvolvido de forma incremental, adicionando novas funcionalidades conforme novos conceitos de Python são estudados e aplicados.
