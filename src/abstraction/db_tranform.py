from abc import ABC, abstractmethod

from pyspark.sql import DataFrame, DataFrameReader

class DBTransform(ABC):
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