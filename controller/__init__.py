from .session_controller import router as session_router
from .user_controller import router as user_router
from .role_controller import router as role_router
from .regiao_controller import router as regiao_router
from .cidade_controller import router as cidade_router
from .tipo_escola_controller import router as tipo_escola_router
from .unidade_escolar_controller import router as unidade_escolar_router
from .endereco_controller import router as endereco_router

__all__ = [
    'session_router',
    'user_router',
    'role_router',
    'regiao_router',
    'cidade_router',
    'tipo_escola_router',
    'unidade_escolar_router',
    'endereco_router'
]