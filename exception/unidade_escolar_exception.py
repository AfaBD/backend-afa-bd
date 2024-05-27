from fastapi import HTTPException, status

unidade_escolar_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Unidade Escolar não encontrada"
)