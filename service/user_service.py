from database import SessionLocal
from model import Login
from exception import user_not_found,user_already_exist
from schema import RequestUser,ResponseUser
from passlib.context import CryptContext

class UserService:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_user_by_username(self,username: str) -> Login:
        with SessionLocal() as db:
            user = db.query(Login).where(Login.username == username).first()
        return user
    
    def create_user(self,request_user: RequestUser) -> ResponseUser:
        user = self.get_user_by_username(request_user.username)
        if user is not None:
            raise user_already_exist
        user = Login()
        user.first_name = request_user.first_name
        user.second_name = request_user.second_name
        user.password = self.pwd_context.hash(request_user.password)
        user.email = request_user.email
        user.username = request_user.username
        user.id_role = request_user.role.id
        with SessionLocal() as db:
            db.add(user)
            db.commit()
            db.refresh(user)
        return ResponseUser(
            id=user.id,
            first_name=user.first_name,
            second_name=user.second_name,
            password= user.password,
            email=user.email,
            role= request_user.role,
            username=user.username   
        )


