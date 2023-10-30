# Faker ETL

Este projeto visa resolver um desafio técnico que envolve a ingestão de dados aleatórios em um banco PostgreSQL e a extração desses dados para a criação de uma tabela final em formato CSV.

## Índice
- [Tecnologias](#tecnologias)
- [Pré-Requisitos](#pre-requisitos)
- [Execução](#execucao)
- [Resolução do Desafio](#resolucao-do-desafio)
- [Observações](#observações)



## Tecnologias
<table>
    <tr>
        <td>Linux</td>
        <td>Código</td>
        <td>Banco de Dados</td>
        <td>Container</td>
        <td>Outros</td>
    </tr>
    <tr>
        <td>Ubuntu</td>
        <td>Python/PySpark</td>
        <td>PostgreSQL</td>
        <td>Docker</td>
        <td>DBeaver/dbdiagram.io</td>
    </tr>
</table>

## Pré-Requisitos

Antes de executar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- [Python](https://www.python.org/downloads/)

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [docker compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository) atualizado

**OBS**: Você também pode visualizar o banco de dados utilizando o [DBeaver](https://dbeaver.io/download/).  Para instruções sobre como configurar a conexão entre o DBeaver e o PostgreSQL, consulte este [tutorial](https://alexdepaula18.medium.com/conectando-no-banco-de-dados-postgresql-utilizando-dbeaver-community-1275f4c9bcba)

## Execução

Siga os passos abaixo para executar o projeto:

1. Clone o repositório:

    ```
    $ git clone https://github.com/yourusername/faker-etl.git
    ```

2. Acesse o diretório do projeto:

    ```
    $ cd faker-etl
    ```

3. Execute os seguintes comandos para construir a imagem Docker e iniciar os containers:

    ```
    $ docker build --tag=faker_etl .
    $ docker compose up -d
    ```
## Resolução do Desafio

### Modelar a Estrutura

A estrutura foi modelada em um banco de dados PostgreSQL utilizando o arquivo `database.models.py`

### Agregação das Tabelas

Para a criação da tabela `movimento_flat`, utilizamos o PySpark para processar os dados, unir as tabelas e criar a tabela `movimento_flat`.

Este fluxo pode ser observado no arquivo **main.py**.

## Observações

### Por que optamos por este design?

Optamos por um design predominantemente em Python, pois isso facilita a adição de novas funcionalidades ao código. Além disso, permite a realização de testes de forma rápida e simples utilizando a biblioteca Pytest.

### O que faríamos se tivéssemos mais tempo para concluir o desafio?

Se tivéssemos mais tempo, integraríamos o Apache Airflow para uma melhor orquestração do fluxo de dados, proporcionando maior escalabilidade e gerenciamento.

### Dificuldades encontradas no desenvolvimento

A principal dificuldade durante o desenvolvimento foi a configuração do arquivo `docker-compose.yml` para permitir a execução de todos os containers e o código principal com um único comando.