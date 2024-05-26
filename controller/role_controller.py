from fastapi import APIRouter
from schema import ResponseRole
from service import RoleService
from typing import List

router = APIRouter(
    prefix='/role'
)

@router.get("/",response_model=List[ResponseRole])
def list_roles():
    service = RoleService()
    return service.list_role()