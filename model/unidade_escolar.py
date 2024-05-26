from database import Base
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import Mapped,relationship

class UnidadeEscolar(Base):
    __tablename__ = "unidade_escolar"

    id = Column("uni_id", Integer, primary_key=True, index=True)
    cod_inep = Column("uni_codigo_inep", Integer, nullable=False)
    nome = Column("uni_nome", String(255), nullable=False)
    
    id_tipo = Column("tip_id", Integer, ForeignKey("tipo_escola.tip_id"))
    tipo = relationship("TipoEscola", back_populates="unidades", lazy="selectin")

    id_endereco = Column("end_id", Integer, ForeignKey("endereco.end_id"))
    endereco = relationship("Endereco", back_populates="unidades", lazy="selectin")
    
    funcionarios = relationship("Login", back_populates="unidade_escolar")
    