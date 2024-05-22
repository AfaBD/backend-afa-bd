from database import SessionLocal
from schema import ResponseRegiaoSchema
from model import Regiao

class RegiaoService:

    def list_regiao(self):
        res = []
        with SessionLocal() as db:
            regioes = db.query(Regiao).all()
        for regiao in regioes:
            res.append(ResponseRegiaoSchema(
                id=regiao.id,
                description=regiao.descricao
            ))
        return res

