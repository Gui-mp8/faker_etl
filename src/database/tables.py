from sqlalchemy import create_engine, Table

from abstraction.alchemy_ddl import AlchemyDDL
from .models import Base

class PostgreSQL(AlchemyDDL):

    def create_table(self) -> Table:
        engine = create_engine(self.conn)
        Base.metadata.create_all(engine)

    def drop_table(self):
        engine = create_engine(self.conn)
        Base.metadata.drop_all(engine)

    # def create_tables() -> Table:
    #     SQLALCHEMY_DATABASE_URL = "postgresql://sicredi:postgresql@localhost:5432/sicredi_data_challenge"
    #     # SQLALCHEMY_DATABASE_URL = "postgresql://sicredi:postgresql@postgres/sicredi_data_challenge"
    #     engine = create_engine(SQLALCHEMY_DATABASE_URL)
    #     Base.metadata.create_all(engine)

    # def drop_tables():
    #     SQLALCHEMY_DATABASE_URL = "postgresql://sicredi:postgresql@localhost:5432/sicredi_data_challenge"
    #     # SQLALCHEMY_DATABASE_URL = "postgresql://sicredi:postgresql@postgres/sicredi_data_challenge"
    #     engine = create_engine(SQLALCHEMY_DATABASE_URL)
    #     Base.metadata.drop_all(engine)