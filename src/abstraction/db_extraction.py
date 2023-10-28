from abc import ABC, abstractmethod
from typing import IO

from pyspark.sql import SparkSession, DataFrame, DataFrameReader

class DBExtraction():
    # def __init__(self) -> None:
    #     self._jar_file_path = None

    # @property
    # def jar_file_path(self):
    #     return self._jar_file_path

    # @jar_file_path.setter
    # def jar(self, path: str):
    #     self._jar_file_path = path
    @abstractmethod
    def read_tables(self) -> DataFrameReader:
        pass

    @abstractmethod
    def query_tables(self) -> DataFrame:
        pass

    def extract_to_csv(self) -> IO[str]:
        pass