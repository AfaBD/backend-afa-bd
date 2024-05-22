from database import SessionLocal
from typing import List
from schema import ResponseRole
from model import Role

class RoleService:

    def list_role(self) -> List[ResponseRole]:
        res = []
        with SessionLocal() as db:
            roles = db.query(Role).all()
        for role in roles:
            res.append(ResponseRole(id=role.id,description=role.description))
        return res 