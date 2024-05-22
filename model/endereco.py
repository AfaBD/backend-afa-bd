from database import Base
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship

class Endereco(Base):
    __tablename__ = "endereco"

    id = Column("end_id",Integer, primary_key=True,index=True)
    rua = Column("end_rua",String(255),nullable=False)
    numero = Column("end_numero",Integer,nullable=False)
    cep = Column("end_cep",String(9),nullable=False)
    id_cidade = Column("cid_id",Integer,ForeignKey("cidade.cid_id"))
    cidade = relationship("Cidade",back_populates="enderecos")
    unidades = relationship("UnidadeEscolar",back_populates="endereco")