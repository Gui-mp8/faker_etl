from abc import ABC, abstractmethod

# from pyspark.sql import DataFrame
# from sqlalchemy import Table

class DBLoad(ABC):

    @abstractmethod
    def add_data_to_tables(self) -> None:
        pass


# from abc import ABC, abstractmethod

# from pyspark.sql import DataFrame
# from sqlalchemy import Table

# class DBLoad(ABC):
#     @abstractmethod
#     def associado_table(self) -> DataFrame:
#         pass

#     @abstractmethod
#     def cartao_table(self) -> DataFrame:
#         pass

#     @abstractmethod
#     def conta_table(self) -> DataFrame:
#         pass

#     @abstractmethod
#     def movimento_table(self) -> DataFrame:
#         pass

#     @abstractmethod
#     def write_data(self) -> Table:
#         pass
