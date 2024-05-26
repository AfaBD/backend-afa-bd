from pydantic import BaseModel

class RoleBase(BaseModel):
    description: str

class ResponseRole(RoleBase):
    id:int