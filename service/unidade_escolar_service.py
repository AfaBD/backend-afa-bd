from database import SessionLocal
from model import UnidadeEscolar,Endereco,Cidade
from exception import unidade_escolar_not_found
from schema import ResponseUnidadeEscolar, ResponseTipoEscola, ResponseEndereco, RequestUnidadeEscolar, ResponseCategoriaEscola
from sqlalchemy.orm import joinedload
from .endereco_service import EnderecoService

class UnidadeEscolarService:
    
    def find_unidade_escolar(self,id):
        with SessionLocal() as db:
            unidade_escolar = db.query(UnidadeEscolar).options(
                joinedload(UnidadeEscolar.endereco).joinedload(Endereco.cidade).joinedload(Cidade.regiao)
            ).where(UnidadeEscolar.id == id).first()
        if unidade_escolar is None:
            unidade_escolar_not_found
        tipo_escola = ResponseTipoEscola(
            id=unidade_escolar.tipo.id,
            descricao=unidade_escolar.tipo.description
        )
        categoria = ResponseCategoriaEscola(
            id=unidade_escolar.categoria.id,
            descricao=unidade_escolar.categoria.description
        )
        endereco = ResponseEndereco(
            rua=unidade_escolar.endereco.rua,
            numero=unidade_escolar.endereco.numero,
            cep=unidade_escolar.endereco.cep,
            id=unidade_escolar.endereco.id,
            cidade=unidade_escolar.endereco.cidade.nome,
            regiao=unidade_escolar.endereco.cidade.regiao.descricao
        )
        return ResponseUnidadeEscolar(
            id=unidade_escolar.id,
            nome= unidade_escolar.nome,
            cod_inep=unidade_escolar.cod_inep,
            tipo=tipo_escola,
            categoria=categoria,
            endereco=endereco
        )

    def create_unidade_escolar(self,unidade_escolar_request: RequestUnidadeEscolar):
        unidade_escolar = UnidadeEscolar()
        unidade_escolar.nome = unidade_escolar_request.nome
        unidade_escolar.cod_inep = unidade_escolar_request.cod_inep
        unidade_escolar.id_categoria = unidade_escolar_request.categoria_id
        unidade_escolar.id_tipo = unidade_escolar_request.tipo_id
        endereco_service = EnderecoService()
        endereco = endereco_service.create_endereco(unidade_escolar_request.endereco)
        unidade_escolar.id_endereco = endereco.id
        with SessionLocal() as db:
            db.add(unidade_escolar)
            db.commit()
            db.refresh(unidade_escolar)
        return self.find_unidade_escolar(unidade_escolar.id)
