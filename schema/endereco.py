from pydantic import BaseModel

class EnderecoBase(BaseModel):
    rua: str
    numero: int
    cep: str

class ResponseEndereco(EnderecoBase):
    id:int
    cidade: str
    regiao:str

class RequestEndereco(EnderecoBase):
    cidade_id: int