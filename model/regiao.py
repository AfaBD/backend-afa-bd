from database import Base
from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship

class Regiao(Base):
    __tablename__ = "regiao"

    id = Column("reg_id",Integer, primary_key=True,index=True)
    descricao = Column("reg_descricao",String(255),nullable=False)
    cidades = relationship("Cidade",back_populates="regiao",lazy="selectin")