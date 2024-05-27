from fastapi import APIRouter, Depends
from model import Login
from schema import ResponseUnidadeEscolar,RequestUnidadeEscolar
from service import UnidadeEscolarService,SessionService
from typing import Annotated

router = APIRouter(
    prefix='/unidade_escolar'
)

service = SessionService()

@router.get("/{id}",response_model=ResponseUnidadeEscolar)
async def find_unidade_escolar(id:int,user: Annotated[Login,Depends(service.validate_token)]):
    unidade_escolar_service = UnidadeEscolarService()
    return unidade_escolar_service.find_unidade_escolar(id)

@router.post("/",response_model=ResponseUnidadeEscolar)
async def create_unidade_escolar(unidade_escolar: RequestUnidadeEscolar,user: Annotated[Login,Depends(service.validate_token)]):
    unidade_escolar_service = UnidadeEscolarService()
    return unidade_escolar_service.create_unidade_escolar(unidade_escolar)