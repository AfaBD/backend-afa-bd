from database import Base
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import Mapped,relationship

class Login(Base):
    __tablename__ = "Funcionario"

    id = Column("fun_id",Integer, primary_key=True,index=True)
    first_name = Column("fun_primeiro_nome",String(256),nullable=False)
    second_name = Column("fun_segundo_nome",String(256),nullable=False)
    password = Column("fun_senha",String(256),nullable=False)
    username = Column("fun_usuario",String(11),nullable=False)
    email = Column("fun_email",String(256),nullable=False)
    id_manager = Column("fun_id_gerente",Integer,ForeignKey("Funcionario.fun_id"))
    manager = relationship("Login", remote_side=[id], backref="employees", lazy="selectin")
    id_role = Column("crg_id",Integer,ForeignKey("Cargo.crg_id"))
    role = relationship("Role", back_populates="logins",lazy="selectin")