from src.database.data_generator import DataGenerator

import findspark
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

def test_spark_connection():
    findspark.init()
    spark = SparkSession \
        .builder \
        .appName("base_tables") \
        .config("spark.jars", "src/drivers/postgresql-42.5.0.jar") \
        .getOrCreate()
    assert spark is not None

def test_if_returns_dataframe():
    findspark.init()
    spark = SparkSession \
                            .builder \
                            .appName("base_tables") \
                            .config("spark.jars", "src/drivers/postgresql-42.5.0.jar") \
                            .getOrCreate()

    fake = DataGenerator()

    associado_schema = StructType(
        [
            StructField(name='id', dataType=IntegerType()),
            StructField(name='nome', dataType=StringType()),
            StructField(name='sobrenome', dataType=StringType()),
            StructField(name='idade', dataType=IntegerType()),
            StructField(name='email', dataType=StringType())
        ]
    )

    associado_data = fake.sample_associado(10)
    associado_dataframe = spark.createDataFrame(schema=associado_schema, data=associado_data)

    assert isinstance(associado_dataframe, DataFrame)



def test_if_dataframe_returns_valid_row_numbers():
    findspark.init()
    spark = SparkSession \
                            .builder \
                            .appName("base_tables") \
                            .config("spark.jars", "src/drivers/postgresql-42.5.0.jar") \
                            .getOrCreate()
    fake = DataGenerator()

    associado_schema = StructType(
        [
            StructField(name='id', dataType=IntegerType()),
            StructField(name='nome', dataType=StringType()),
            StructField(name='sobrenome', dataType=StringType()),
            StructField(name='idade', dataType=IntegerType()),
            StructField(name='email', dataType=StringType())
        ]
    )

    associado_data = fake.sample_associado(5)
    df_test = spark.createDataFrame(schema=associado_schema, data=associado_data)

    assert df_test.count() == 5

