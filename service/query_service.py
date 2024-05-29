from database import SessionLocal
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from model import UnidadeEscolar,Endereco,Cidade,Regiao,Categoria,TipoEscola
from schema import ResponseUnidadeEscolar,ResponseTipoEscola,ResponseEndereco,ResponseCategoriaEscola,Query201,Query202

class QueryService:

    def query201(self):
        with SessionLocal() as db:
            query_result = db.query(
            Regiao.descricao,
            UnidadeEscolar
            ).join(Cidade, Regiao.id == Cidade.id_regiao
            ).join(Endereco, Cidade.id == Endereco.id_cidade
            ).join(UnidadeEscolar, Endereco.id == UnidadeEscolar.id_endereco
            ).options(
                joinedload(UnidadeEscolar.tipo),
                joinedload(UnidadeEscolar.endereco).joinedload(Endereco.cidade).joinedload(Cidade.regiao)
            ).group_by(Regiao.descricao, UnidadeEscolar.id).all()
        result_dict = {}
        for regiao,unidade in query_result:
            if regiao not in result_dict:
                result_dict[regiao] = {'count': 0, 'unidades_escolares': []}
            result_dict[regiao]['count'] += 1
            result_dict[regiao]['unidades_escolares'].append(
                ResponseUnidadeEscolar(
                    nome=unidade.nome,
                    cod_inep=unidade.cod_inep,
                    id=unidade.id,
                    tipo=ResponseTipoEscola(
                        id=unidade.tipo.id,
                        descricao=unidade.tipo.description
                    ),
                    categoria=ResponseCategoriaEscola(
                        id = unidade.categoria.id,
                        descricao=unidade.categoria.description
                    ),
                    endereco=ResponseEndereco(
                        id=unidade.endereco.id,
                        rua=unidade.endereco.rua,
                        numero=unidade.endereco.numero,
                        cep=unidade.endereco.cep,
                        cidade=unidade.endereco.cidade.nome,
                        regiao=unidade.endereco.cidade.regiao.descricao
                    )
                )
            )
        return [
            Query201(regiao=regiao, count=data['count'], unidades_escolares=data['unidades_escolares'])
            for regiao, data in result_dict.items()
        ]
    
    def query202(self):
        with SessionLocal() as db:
            query_result = db.query(
                Regiao.descricao.label("regiao_nome"),
                Categoria.description.label("categoria"),
                TipoEscola.description.label("tipo_escola"),
                func.count(UnidadeEscolar.id).label("num_unidades")
            ).join(
                Cidade
            ).join(
                Endereco
            ).join(
                UnidadeEscolar
            ).join(
                Categoria
            ).join(
                TipoEscola
            ).group_by(
                Regiao.descricao,
                Categoria.description,
                TipoEscola.description
            ).all()
        return [
            Query202(regiao=result.regiao_nome,categoria=result.categoria,tipo=result.tipo_escola,num_escolas=result.num_unidades)
            for result in query_result
        ]

