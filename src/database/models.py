from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Associado(Base):
    """
        This class represents the associado table
    """
    __tablename__ = "associado"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String, nullable=False)
    sobrenome: str = Column(String, nullable=False)
    idade: int = Column(Integer, nullable=False)
    email: str = Column(String, nullable=False)


class Conta(Base):
    """
        This class represents the conta table
    """
    __tablename__ = "conta"

    id: int = Column(Integer, primary_key=True, index=True)
    tipo: str = Column(String, nullable=False)
    data_criacao: datetime = Column(DateTime, nullable=False)
    id_associado: int = Column(Integer, ForeignKey("associado.id"), nullable=False)


class Cartao(Base):
    """
        This class represents the cartao table
    """
    __tablename__ = "cartao"

    id: int = Column(Integer, primary_key=True, index=True)
    num_cartao: int = Column(String, nullable=False)
    nom_impresso: str = Column(String(100), nullable=False)
    data_criacao: datetime = Column(DateTime, nullable=False)
    id_conta: int = Column(Integer, ForeignKey("conta.id"), nullable=False)
    id_associado: int = Column(Integer, ForeignKey("associado.id"), nullable=False)


class Movimento(Base):
    """
        This class represents the movimento table
    """
    __tablename__ = "movimento"

    id: int = Column(Integer, primary_key=True, index=True)
    vlr_transacao: float = Column(Float(10,2), nullable=False)
    des_transacao: str = Column(String, nullable=False)
    data_movimento: datetime = Column(DateTime, nullable=False)
    id_cartao: int = Column(Integer, ForeignKey("cartao.id"),nullable=False)