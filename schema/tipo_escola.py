from pydantic import BaseModel

class BaseTipoEscola(BaseModel):
    descricao: str

class ResponseTipoEscola(BaseTipoEscola):
    id: int