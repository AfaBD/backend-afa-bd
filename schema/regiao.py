from pydantic import BaseModel

class RegiaoBase(BaseModel):
    description: str

class ResponseRegiaoSchema(RegiaoBase):
    id: int