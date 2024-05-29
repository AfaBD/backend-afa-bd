from database import Base
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import Mapped,relationship

class Categoria(Base):
    __tablename__ = "categoria_escolar"

    id = Column("cat_id",Integer, primary_key=True,index=True)
    description = Column("cat_descricao",String(255),nullable=False)
    unidades = relationship("UnidadeEscolar", back_populates="categoria",lazy="selectin")