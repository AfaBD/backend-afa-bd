from database import Base
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import Mapped,relationship

class TipoEscola(Base):
    __tablename__ = "tipo_escola"

    id = Column("tip_id",Integer, primary_key=True,index=True)
    description = Column("tip_descricao",String(255),nullable=False)
    unidades = relationship("UnidadeEscolar", back_populates="tipo",lazy="selectin")