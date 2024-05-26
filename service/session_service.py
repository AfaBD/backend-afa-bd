from database import SessionLocal
from schema import ResponseSession,TokenSession,ResponseUser,ResponseRole
from jose import jwt,JWTError
from datetime import timedelta,datetime
from model import Login
from exception import invalid_credentials,user_not_found
from configuration import OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES,OAUTH_SECRET_KEY,OAUTH_ALGORITHM
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Annotated

from .user_service import UserService

class SessionService:

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_session(self, username:str, password:str) -> ResponseSession:
        user_service = UserService()
        user: Login = user_service.get_user_by_username(username)
        if user is None:
            raise user_not_found
        if not self.pwd_context.verify(password,user.password):
            raise invalid_credentials
        return self.create_token(user)

    def create_token(self,user:Login) -> ResponseSession:
        interval = timedelta(
            minutes=OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES
        )
        expire = (datetime.utcnow() + interval).timestamp()
        token_data = TokenSession(username=user.username, expire=expire)

        jwt_token = jwt.encode(
            token_data.model_dump(),
            OAUTH_SECRET_KEY,
            algorithm=OAUTH_ALGORITHM,
        )
        return ResponseSession(username=user.username,access_token=jwt_token,token_type="Bearer",expire=expire,role=user.role.description)
    
    @staticmethod
    def validate_token(token: Annotated[str, Depends(oauth2_scheme)]) -> ResponseUser:
        try:
            payload = jwt.decode(
                token,
                OAUTH_SECRET_KEY,
                algorithms=[OAUTH_ALGORITHM],
            )

            token_data: TokenSession = TokenSession.model_validate(payload)

            if token_data.username is None or token_data.expire < datetime.utcnow().timestamp():
                raise invalid_credentials
            user_service = UserService()
            user: Login = user_service.get_user_by_username(token_data.username)
            if user is None:
                raise user_not_found
            return ResponseUser(
                id=user.id,
                username=user.username,
                first_name=user.first_name,
                second_name=user.second_name,
                password='',
                email=user.email,
                role=ResponseRole(
                    id=user.role.id,
                    description=user.role.description
                )
            )

        except JWTError:
            raise invalid_credentials
