from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType, IntegerType, StringType, StructField, StructType, TimestampType
import findspark

from database.data_generator import DataGenerator
from abstraction.db_load import DBLoad

class PostegresqlLoad(DBLoad):
    def __init__(self, config: dict) -> None:
        self.config = config
        self.data_gen = DataGenerator()
        self.spark_init = findspark.init()
        self.spark = SparkSession \
                        .builder \
                        .appName("base_tables") \
                        .config("spark.jars", "src/drivers/postgresql-42.5.0.jar") \
                        .getOrCreate()

    def add_data_to_tables(self) -> None:
        associado_schema = StructType(
            [
                StructField(name='id', dataType=IntegerType()),
                StructField(name='nome', dataType=StringType()),
                StructField(name='sobrenome', dataType=StringType()),
                StructField(name='idade', dataType=IntegerType()),
                StructField(name='email', dataType=StringType())
            ]
        )

        conta_schema = StructType(
            [
                StructField(name='id', dataType=IntegerType()),
                StructField(name='tipo', dataType=StringType()),
                StructField(name='data_criacao', dataType=TimestampType()),
                StructField(name='id_associado', dataType=IntegerType())
            ]
        )

        cartao_schema = StructType(
            [
                StructField(name='id', dataType=IntegerType()),
                StructField(name='num_cartao', dataType=StringType()),
                StructField(name='nom_impresso', dataType=StringType()),
                StructField(name='data_criacao', dataType=TimestampType()),
                StructField(name='id_conta', dataType=IntegerType()),
                StructField(name='id_associado', dataType=IntegerType())
            ]
        )

        movimento_schema = StructType(
            [
                StructField(name='id', dataType=IntegerType()),
                StructField(name='vlr_transacao', dataType=FloatType()),
                StructField(name='des_transacao', dataType=StringType()),
                StructField(name='data_movimento', dataType=TimestampType()),
                StructField(name='id_cartao', dataType=IntegerType())
            ]
        )

        tables_to_load = {
            "associado": self.spark.createDataFrame(
                schema=associado_schema,
                data=self.data_gen.sample_associado(self.config["row_number"])
            ),
            "conta": self.spark.createDataFrame(
                schema=conta_schema,
                data=self.data_gen.sample_conta(self.config["row_number"])
            ),
            "cartao": self.spark.createDataFrame(
                schema=cartao_schema,
                data=self.data_gen.sample_cartao(self.config["row_number"])
            ),
            "movimento": self.spark.createDataFrame(
                schema=movimento_schema,
                data=self.data_gen.sample_movimento(self.config["row_number"])
            )
        }
        for table in tables_to_load.items():
            table[1].write \
                .format("jdbc") \
                .option("url", "jdbc:postgresql://localhost:5432/sicredi_data_challenge") \
                .option("driver", "org.postgresql.Driver") \
                .option("dbtable", str(table[0])) \
                .option("user", "sicredi") \
                .option("password", "postgresql") \
                .mode("append") \
                .save()
#container:
# .option("url", "jdbc:postgresql://postgres:5432/sicredi_data_challenge") \
#local:
# .option("url", "jdbc:postgresql://localhost:5432/sicredi_data_challenge") \
