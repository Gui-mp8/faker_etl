from typing import IO

from pyspark.sql import SparkSession, DataFrame, DataFrameReader
import findspark

from abstraction.db_extraction import DBExtraction

class PostgresqlExtraction(DBExtraction):
    def __init__(self, config: dict) -> None:
        self.config = config
        self.findspark = findspark.init()
        self.spark: SparkSession = SparkSession \
                                    .builder \
                                    .appName("extract") \
                                    .config("spark.jars", "src/drivers/postgresql-42.5.0.jar") \
                                    .getOrCreate()

        self.spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")

    def read_tables(self) -> DataFrameReader:
        """
        Read base tables from database
        """
        reader = self.spark.read\
            .format("jdbc")\
                .option("url", "jdbc:postgresql://localhost:5432/sicredi_data_challenge") \
                .option("driver", "org.postgresql.Driver") \
                .option("user", "sicredi") \
                .option("password", "postgresql") \
                # .option("url", "jdbc:postgresql://postgres:5432/sicredi_data_challenge") \
        return reader

    def query_tables(self) -> DataFrame:
        tablename_list = [
            "associado",
            "conta",
            "cartao",
            "movimento"
        ]
        # Create TempView using base tables
        for tablename in tablename_list:
            self.read_tables().option("dbtable", tablename).load().createTempView(tablename)

        # Create movimento_flat dataframe
        movimento_flat = self.spark.sql(
            """
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
        )
        return movimento_flat

    def extract_to_csv(self) -> IO[str]:
        '''
            Extract data from database tables, create tempViews and merge in 'movimento_flat' dataframe
        '''
        # Write movimento_flat dataframe in a csv file
        return self.query_tables().coalesce(1).write.csv(path=f"data/{self.config['final_result_path']}", sep=';', header=True, mode='overwrite')