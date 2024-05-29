from pydantic import BaseModel

class BaseCategoriaEscola(BaseModel):
    descricao: str

class ResponseCategoriaEscola(BaseCategoriaEscola):
    id: int