from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from database.bd_models import Associado, Conta, Cartao, Movimento
from database.data_generator import DataGenerator
from models.associado import PyAssociado
from models.cartao import PyCartao
from models.conta import PyConta
from models.movimento import PyMovimento

def insert_data():
    engine = create_engine("postgresql://sicredi:postgresql@localhost:5432/sicredi_data_challenge")
    Session = sessionmaker(bind=engine)
    session = Session()

    row_number = 100

    associado_data = DataGenerator().sample_associado(row_number=row_number)
    for data in associado_data:
        print(data)
        associado = PyAssociado(**data)
        db_associado = Associado(**associado.model_dump())
        session.add(db_associado)

    # Sample data for Conta
    conta_data = DataGenerator().sample_conta(row_number)
    for data in conta_data:
        print(data)
        conta = PyConta(**data)
        db_conta = Conta(**conta.model_dump())
        session.add(db_conta)

    # Sample data for Cartao
    cartao_data = DataGenerator().sample_cartao(row_number)
    for data in cartao_data:
        print(data)
        cartao = PyCartao(**data)
        db_cartao = Cartao(**cartao.model_dump())
        session.add(db_cartao)

    # Sample data for Movimento
    movimento_data = DataGenerator().sample_movimento(row_number)
    for data in movimento_data:
        print(data)
        movimento = PyMovimento(**data)
        db_movimento = Movimento(**movimento.model_dump())
        session.add(db_movimento)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()