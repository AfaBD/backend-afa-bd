from pydantic import BaseModel

class SessionBase(BaseModel):
    username: str

class RequestSession(SessionBase):
    password: str

class ResponseSession(SessionBase):
    access_token: str
    token_type: str
    role: str
    expire: float

class TokenSession(BaseModel):
    expire: float
