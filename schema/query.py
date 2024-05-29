from pydantic import BaseModel
from typing import List
from .unidade_escolar import ResponseUnidadeEscolar

class Query201(BaseModel):
    regiao:str
    count:int
    unidades_escolares: List[ResponseUnidadeEscolar]

class Query202(BaseModel):
    regiao:str
    categoria:str
    tipo:str
    num_escolas:int