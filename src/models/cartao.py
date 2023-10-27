from datetime import datetime

from pydantic import BaseModel

class PyCartao(BaseModel):
    id: int
    num_cartao: int
    nom_impresso: str
    data_criacao: datetime
    id_conta: int
    id_associado: int
