from abc import ABC, abstractmethod

from sqlalchemy import Table

class AlchemyDDL(ABC):
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