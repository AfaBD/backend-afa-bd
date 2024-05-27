from database import SessionLocal
from sqlalchemy.orm import joinedload
from model import Endereco,Cidade
from schema import ResponseEndereco,RequestEndereco
from exception import endereco_not_found

class EnderecoService:

    def find_endereco(self,id: int):
        with SessionLocal() as db:
            endereco = db.query(Endereco).options(
                joinedload(Endereco.cidade).joinedload(Cidade.regiao)
            ).where(Endereco.id == id).first()
        if endereco is None:
            raise endereco_not_found
        return ResponseEndereco(
            rua=endereco.rua,
            numero=endereco.numero,
            cep=endereco.cep,
            id=endereco.id,
            cidade=endereco.cidade.nome,
            regiao=endereco.cidade.regiao.descricao
        )

    def create_endereco(self, endereco_request:RequestEndereco):
        endereco = Endereco()
        endereco.rua = endereco_request.rua
        endereco.numero = endereco_request.numero
        endereco.cep = endereco_request.cep
        endereco.id_cidade = endereco_request.cidade_id
        with SessionLocal() as db:
            db.add(endereco)
            db.commit()
            db.refresh(endereco)
        return self.find_endereco(endereco.id)