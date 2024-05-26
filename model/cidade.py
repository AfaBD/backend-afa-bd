from database import Base
from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Cidade(Base):
    __tablename__ = "cidade"

    id = Column("cid_id",Integer, primary_key=True,index=True)
    nome = Column("cid_nome",String(255),nullable=False)
    id_regiao = Column("reg_id",Integer,ForeignKey("regiao.reg_id"))
    regiao = relationship("Regiao",back_populates="cidades")
    enderecos = relationship("Endereco",back_populates="cidade")