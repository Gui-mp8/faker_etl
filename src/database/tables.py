from sqlalchemy import create_engine, Table

from abstraction.alchemy_ddl import AlchemyDDL
from .models import Base

class PostgreSQL(AlchemyDDL):

    def create_table(self) -> Table:
        engine = create_engine(self.conn)
        Base.metadata.create_all(engine)

    def drop_table(self) -> None:
        engine = create_engine(self.conn)
        Base.metadata.drop_all(engine)
