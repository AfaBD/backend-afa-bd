from pydantic import BaseModel
from .tipo_escola import ResponseTipoEscola
from .endereco import ResponseEndereco,RequestEndereco

class UnidadeEscolarBase(BaseModel):
    nome: str
    cod_inep: int

class ResponseUnidadeEscolar(UnidadeEscolarBase):
    id:int
    tipo: ResponseTipoEscola
    endereco: ResponseEndereco

class RequestUnidadeEscolar(UnidadeEscolarBase):
    tipo_id: int
    endereco: RequestEndereco