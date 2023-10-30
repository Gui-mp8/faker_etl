# Faker ETL

Este projeto tem como objetivo resolver o desafio técnico,  no qual ocorre a ingestão de dados aleatórios em um banco PostgreSQL,  a extração desses dados é a união dos mesmos para uma tabela final em csv.

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

## Pré Requisitos
- E necessaria a instalacao do [Python](https://www.python.org/downloads/)
- 'E necessaria a instalacao do [Docker](https://docs.docker.com/engine/install/ubuntu/) e instalar o [docker compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

**OBS**: Este banco pode ser visualizado usando o [DBeaver](https://dbeaver.io/download/).

[Tutorial para a Conexão entre o Dbeaver e o PostgreSQL.](https://alexdepaula18.medium.com/conectando-no-banco-de-dados-postgresql-utilizando-dbeaver-community-1275f4c9bcba)

## Rodando o Codigo

Para rodar o codigo basta rodar os comandos a seguir
### Linux:
```
make build
make run
```
### Windows
```
docker build --tag=faker_etl .
docker compose up -d
```
