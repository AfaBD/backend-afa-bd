from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
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
    return service.create_session(form_data.username,form_data.password)