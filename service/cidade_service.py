from database import SessionLocal
from model import Cidade
from schema import ResponseCidade, RequestCidade

class CidadeService:

    def list_cidade(self,regiao_id:int):
        res = []
        with SessionLocal() as db:
            cidades = db.query(Cidade).where(Cidade.id_regiao == regiao_id)
        for cidade in cidades:
            res.append(ResponseCidade(id=cidade.id,nome=cidade.nome))
        return res
        
    def create_cidade(self,request_cidade:RequestCidade):
        cidade = Cidade()
        cidade.nome = request_cidade.nome
        cidade.id_regiao = request_cidade.regiao_id
        with SessionLocal() as db:
            db.add(cidade)
            db.commit()
            db.refresh(cidade)
        return ResponseCidade(
            id=cidade.id,
            nome=cidade.nome
        )        
