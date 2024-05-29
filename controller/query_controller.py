from fastapi import APIRouter, Depends
from model import Login
from schema import Query201,Query202
from service import QueryService,SessionService
from typing import Annotated,List

router = APIRouter(
    prefix='/query'
)

service = SessionService()

@router.get('/201',response_model=List[Query201])
def runquery201(user: Annotated[Login,Depends(service.validate_token)]):
    query_service = QueryService()
    return query_service.query201()

@router.get('/202',response_model=List[Query202])
def runquery202(user: Annotated[Login,Depends(service.validate_token)]):
    query_service = QueryService()
    return query_service.query202()