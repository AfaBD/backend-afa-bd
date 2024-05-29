from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from schema import ResponseSession
from typing import Annotated
from service import SessionService
from model import Login

router = APIRouter(
    prefix='/session'
)

service = SessionService()

@router.post("/",response_model=ResponseSession)
async def login(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    service = SessionService()
    session_data = service.create_session(form_data.username,form_data.password)
    response = JSONResponse(content=session_data.dict())
    response.set_cookie(
        key='token',
        value=session_data.access_token,
        httponly=False,
        secure=False
    )
    return response