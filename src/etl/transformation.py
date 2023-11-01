from typing import IO

from pyspark.sql import SparkSession, DataFrame, DataFrameReader
import findspark

from abstraction.db_tranform import DBTransform

class PostgresqlTransformation(DBTransform):
    """
        This class extracts data from a PostgreSQL database

        Args:
            config (dict): configuration file
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
            This method reads a table from the database
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
        """
            This method let you to make any query based on the database tables

            Args:
                table_name_list (list): a list that needs one or more tables.
                query (str): the query that you want to make

        """
        # Create TempView using base tables
        for table_name in table_name_list:
            self.read_tables().option("dbtable", table_name).load().createTempView(table_name)

        df = self.spark.sql(query)
        return df
