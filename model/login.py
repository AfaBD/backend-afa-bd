from database import Base
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import Mapped,relationship

class Login(Base):
    __tablename__ = "funcionario"

    id = Column("fun_id", Integer, primary_key=True, index=True)
    first_name = Column("fun_primeiro_nome", String(256), nullable=False)
    second_name = Column("fun_segundo_nome", String(256), nullable=False)
    password = Column("fun_senha", String(256), nullable=False)
    username = Column("fun_usuario", String(11), nullable=False)
    email = Column("fun_email", String(256), nullable=False)

    id_role = Column("crg_id", Integer, ForeignKey("cargo.crg_id"))
    role = relationship("Role", back_populates="logins", lazy="selectin")

    id_unidade = Column("uni_id", Integer, ForeignKey("unidade_escolar.uni_id"))
    unidade_escolar = relationship("UnidadeEscolar", back_populates="funcionarios")

    id_manager = Column("fun_id_gerente", Integer, ForeignKey("funcionario.fun_id"))
    manager = relationship("Login", remote_side=[id], backref="employees", lazy="selectin")