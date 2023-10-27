from datetime import datetime

from pydantic import BaseModel

class PyMovimento(BaseModel):
    vlr_transacao: float
    des_transacao: str
    data_movimento: datetime
    id_cartao: int