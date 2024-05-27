from fastapi import APIRouter, Depends
from schema import ResponseCidade,RequestCidade
from model import Login
from service import CidadeService,SessionService
from typing import List, Annotated

router = APIRouter(
    prefix='/cidade'
)

service = SessionService()

@router.get("/{regiao_id}",response_model=List[ResponseCidade])
async def list_cidade(regiao_id:int,user: Annotated[Login,Depends(service.validate_token)]):
    cidade_service = CidadeService()
    return cidade_service.list_cidade(regiao_id)

@router.post("/",response_model=ResponseCidade)
async def create_cidade(cidade:RequestCidade,user: Annotated[Login,Depends(service.validate_token)]):
    cidade_service = CidadeService()
    return cidade_service.create_cidade(cidade)
