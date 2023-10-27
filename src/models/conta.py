from datetime import datetime

from pydantic import BaseModel

class PyConta(BaseModel):
    id: int
    tipo: str
    data_criacao: datetime
    id_associado: int
