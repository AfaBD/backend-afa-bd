from pydantic import BaseModel
from .role import ResponseRole

class UserBase(BaseModel):
    username: str

class ResponseManagerUser(UserBase):
    id: int
    first_name: str
    second_name: str
    email: str

class RequestUser(UserBase):
    first_name: str
    second_name: str
    password:str
    email: str
    role: ResponseRole

class ResponseUser(RequestUser):
    id: int
