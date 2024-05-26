from fastapi import APIRouter,Depends
from schema import ResponseTipoEscola
from model import TipoEscola,Login
from service import TipoEscolaService, SessionService
from typing import List, Annotated

router = APIRouter(
    prefix='/tipo_escola'
)

service = SessionService()

@router.get("/",response_model=List[ResponseTipoEscola])
async def list_tipo_escola(user: Annotated[Login,Depends(service.validate_token)]):
    tipo_escola_service = TipoEscolaService()
    return tipo_escola_service.list_tipo_escola()