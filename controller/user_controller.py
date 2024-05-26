from fastapi import APIRouter, Depends
from schema import ResponseUser,RequestUser,ResponseRole
from service import SessionService,UserService
from model import Login
from typing import Annotated

router = APIRouter(
    prefix='/user'
)

service = SessionService()

@router.post("/",response_model=ResponseUser)
async def register(body_data: RequestUser):
    service = UserService()
    return service.create_user(body_data)

@router.get("/",response_model=ResponseUser)
async def get_user(user: Annotated[Login,Depends(service.validate_token)]):
    return user