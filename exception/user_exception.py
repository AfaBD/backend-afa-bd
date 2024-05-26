from fastapi import HTTPException, status

user_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Usuário não encontrado"
)

user_already_exist = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Usuário ja cadastrado"
)