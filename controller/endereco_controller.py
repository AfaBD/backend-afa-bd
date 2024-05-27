from fastapi import APIRouter, Depends
from schema import ResponseEndereco, RequestEndereco
from model import Login
from service import EnderecoService,SessionService
from typing import List, Annotated

router = APIRouter(
    prefix='/endereco'
)

service = SessionService()

@router.get("/{id}",response_model=ResponseEndereco)
async def find_endereco(id:int,user: Annotated[Login,Depends(service.validate_token)]):
    endereco_service = EnderecoService()
    return endereco_service.find_endereco(id)

@router.post("/",response_model=ResponseEndereco)
async def create_endereco(endereco: RequestEndereco,user: Annotated[Login,Depends(service.validate_token)]):
    endereco_service = EnderecoService()
    return endereco_service.create_endereco(endereco)

