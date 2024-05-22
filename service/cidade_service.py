from database import SessionLocal
from model import Cidade
from schema import ResponseCidade

class CidadeService:

    def list_cidade(self,regiao_id:int):
        res = []
        with SessionLocal() as db:
            cidades = db.query(Cidade).where(Cidade.id_regiao == regiao_id)
        for cidade in cidades:
            res.append(ResponseCidade(id=cidade.id,nome=cidade.nome))
        return res
        