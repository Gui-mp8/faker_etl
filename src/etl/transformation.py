from typing import IO

from pyspark.sql import SparkSession, DataFrame, DataFrameReader
import findspark

from abstraction.db_tranform import DBTransform

class PostgresqlTransformation(DBTransform):
    """
        This class extracts data from a PostgreSQL database

        Args:
            config (dict): _description_
            findspark (function): initialize spark
            spark (class): starts a spark session using the PostgreSQL jar

        Methods:
            read_tables(): reads a table in database
            query_tables(): transform the query in a dataframe
    """
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
                .option("url", "jdbc:postgresql://postgres:5432/sicredi_data_challenge") \
                .option("driver", "org.postgresql.Driver") \
                .option("user", "sicredi") \
                .option("password", "postgresql") \
                # .option("url", "jdbc:postgresql://postgres:5432/sicredi_data_challenge") \
                # .option("url", "jdbc:postgresql://localhost:5432/sicredi_data_challenge") \
        return reader

    def query_tables(self, table_name_list: list, query: str) -> DataFrame:
        # Create TempView using base tables
        for table_name in table_name_list:
            self.read_tables().option("dbtable", table_name).load().createTempView(table_name)

        # Create movimento_flat dataframe
        df = self.spark.sql(query)
        return df
