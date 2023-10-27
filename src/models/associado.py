from pydantic import BaseModel, EmailStr

class PyAssociado(BaseModel):
    id: int
    nome: str
    sobrenome: str
    idade: int
    email: EmailStr