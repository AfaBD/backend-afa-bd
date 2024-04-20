from fastapi import APIRouter
from schema import ResponseUser,RequestUser
from service import UserService

router = APIRouter(
    prefix='/user'
)

@router.post("/",response_model=ResponseUser)
async def register(body_data: RequestUser):
    service = UserService()
    return service.create_user(body_data)