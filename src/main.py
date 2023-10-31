from database.tables import PostgreSQL
from etl.load import PostegresqlLoad
from etl.transformation import PostgresqlTransformation
from etl.extraction import PostgresqlExtraction
from utils.config import load_config

def main(config):
    db = PostgreSQL()
    # db.conn = "postgresql://sicredi:postgresql@localhost:5432/sicredi_data_challenge"
    db.conn = "postgresql://sicredi:postgresql@postgres/sicredi_data_challenge"
    print("Droping tables..")
    db.drop_table()
    print("Tables dropped!!! \nCreating Tables...")
    db.create_table()
    print("Tables Created!!!")

    print("Inserting data...")
    PostegresqlLoad(config).add_data_to_tables()
    print("Data Inserted!")

    print("Writing the tables that will be queried...")

    table_name_list = [
        "associado",
        "conta",
        "cartao",
        "movimento"
    ]

    print("Quering the tables...")

    query = """
                SELECT
                    t1.nome as nome_associado,
                    t1.sobrenome as sobrenome_associado,
                    t1.idade as idade_associado,
                    t2.vlr_transacao as vlr_transacao_movimento,
                    t2.des_transacao as des_transacao_movimento,
                    t2.data_movimento,
                    t3.num_cartao as numero_cartao,
                    t3.nom_impresso as nome_impresso_cartao,
                    t3.data_criacao as data_criacao_cartao,
                    t4.tipo as tipo_conta,
                    t4.data_criacao as data_criacao_conta
                FROM
                    associado as t1
                JOIN
                    movimento as t2,
                    cartao as t3,
                    conta as t4
                WHERE
                    t1.id = t4.id_associado and
                    t4.id = t3.id_associado and
                    t3.id = t2.id_cartao
            """
    print("Query Sucess!!!")

    print("Writing the dataframe...")
    df = PostgresqlTransformation(config).query_tables(table_name_list, query)
    print("Dataframe Writed!!!")

    print("Extracting dataframe to csv...")
    PostgresqlExtraction(config).extract_to_csv(df)
    print('csv file was created in the specified path')
if __name__ == "__main__":
    config = load_config()
    main(config)