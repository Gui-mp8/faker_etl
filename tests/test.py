import pytest
from src.database.data_generator import DataGenerator
# from src.pipelines.load import insert_data_to_db

import findspark
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import FloatType, IntegerType, StringType, StructField, StructType, TimestampType



############### DataGenerator Class tests ############################################################

def test_DataGenerator_samples_returns_list():
    fake = DataGenerator()
    test_dict = {
        "instance1" : fake.sample_associado(1),
        "instance2" : fake.sample_cartao(1),
        "instance3" : fake.sample_conta(1),
        "instance4" : fake.sample_movimento(1)
    }

    for instance, result in test_dict.items():
        assert isinstance(result, list)


# ############### PySpark Class tests ##################################################################

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

