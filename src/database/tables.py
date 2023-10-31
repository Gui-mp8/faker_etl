from sqlalchemy import create_engine, Table

from abstraction.alchemy_ddl import AlchemyDDL
from .models import Base

class PostgreSQL(AlchemyDDL):
    """
        This class can receive PostgreSQL database url connections
        to make DDL operations

        Attributes:
            The sames of the ALchemyDDL class

        Methods:
            create_table(): Creates the tables.
            drop_table(): Deletes the tables.

    """
    def create_table(self) -> Table:
        """
            This method creates the tables based on the Base.metadata of the models created at models.py.

        """
        engine = create_engine(self.conn)
        Base.metadata.create_all(engine)

    def drop_table(self) -> None:
        """
            This method Deletes the tables based on the Base.metadata of the models created at models.py.

        """
        engine = create_engine(self.conn)
        Base.metadata.drop_all(engine)
