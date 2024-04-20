from database import Base
from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "Cargo"

    id = Column("crg_id",Integer,primary_key=True,index=True)
    description = Column("crg_descricao",String(256),nullable=False)
    logins = relationship("Login", back_populates="role",lazy="selectin")
