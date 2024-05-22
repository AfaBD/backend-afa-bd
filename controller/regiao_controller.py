from fastapi import APIRouter,Depends
from schema import ResponseRegiaoSchema
from model import Login
from service import RegiaoService, SessionService
from typing import List, Annotated

router = APIRouter(
    prefix='/regiao'
)

service = SessionService()

@router.get("/",response_model=List[ResponseRegiaoSchema])
async def list_regioes(user: Annotated[Login,Depends(service.validate_token)]):
    regiao_service = RegiaoService()
    return regiao_service.list_regiao()