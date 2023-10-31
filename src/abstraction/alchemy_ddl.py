from abc import ABC, abstractmethod

from sqlalchemy import Table

class AlchemyDDL(ABC):
    """
        This class can receive any database url connections
        like PostgreSQL, MySQl, etc... to make DDL operations

        Attributes:
            conn (str): The connection string.

        Methods:
            create_table(): Creates the tables based on the models created.
            drop_table(): Deletes the tables based on the models created.

    """
    def __init__(self) -> None:
        self._conn = None

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, database_url: str):
        self._conn = database_url

    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def drop_table(self):
        pass