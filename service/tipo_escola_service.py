from database import SessionLocal
from model import TipoEscola
from schema import ResponseTipoEscola

class TipoEscolaService:
    def list_tipo_escola(self):
        res = []
        with SessionLocal() as db:
            tipos = db.query(TipoEscola).all()
        for tipo in tipos:
            res.append(
                ResponseTipoEscola(
                    id=tipo.id,
                    descricao=tipo.description
                )
            )
        return res
        