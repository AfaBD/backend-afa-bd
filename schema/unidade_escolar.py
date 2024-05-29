from pydantic import BaseModel
from .tipo_escola import ResponseTipoEscola
from .endereco import ResponseEndereco,RequestEndereco
from .categoria import ResponseCategoriaEscola

class UnidadeEscolarBase(BaseModel):
    nome: str
    cod_inep: int

class ResponseUnidadeEscolar(UnidadeEscolarBase):
    id:int
    tipo: ResponseTipoEscola
    categoria:ResponseCategoriaEscola
    endereco: ResponseEndereco

class RequestUnidadeEscolar(UnidadeEscolarBase):
    tipo_id: int
    categoria_id: int
    endereco: RequestEndereco