from pydantic import BaseModel

class CidadeBase(BaseModel):
    nome: str

class ResponseCidade(CidadeBase):
    id: int