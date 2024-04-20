from database import SessionLocal
from schema import ResponseSession,TokenSession
from jose import jwt
from datetime import timedelta,datetime
from model import Login
from exception import invalid_credentials,user_not_found
from configuration import OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES,OAUTH_SECRET_KEY,OAUTH_ALGORITHM
from passlib.context import CryptContext

from .user_service import UserService

class SessionService:

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
        token_data = TokenSession(user=user.username, expire=expire)

        jwt_token = jwt.encode(
            token_data.model_dump(),
            OAUTH_SECRET_KEY,
            algorithm=OAUTH_ALGORITHM,
        )
        return ResponseSession(username=user.username,access_token=jwt_token,token_type="Bearer",expire=expire,role=user.role.description)