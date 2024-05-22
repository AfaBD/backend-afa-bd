class Cidade(Base):
    __tablename__ = "Cidade"

    id = Column("cid_id",Integer, primary_key=True,index=True)
    nome = Column("cid_nome",String(255),nullable=False)
    id_regiao = Column("reg_id",Integer,ForeignKey("Regiao.reg_id"))
    regiao = relationship("Regiao",back_populates="cidades")
    enderecos = relationship("Endereco",back_populates="cidade")

class Endereco(Base):
    __tablename__ = "Endereco"

    id = Column("end_id",Integer, primary_key=True,index=True)
    rua = Column("end_rua",String(255),nullable=False)
    numero = Column("end_numero",Integer,nullable=False)
    cep = Column("end_cep",String(9),nullable=False)
    id_cidade = Column("cid_id",Integer,ForeignKey("Cidade.cid_id"))
    cidade = relationship("Cidade",back_populates="enderecos")
    unidades = relationship("UnidadeEscolar",back_populates="endereco")

class Login(Base):
    __tablename__ = "Funcionario"

    id = Column("fun_id",Integer, primary_key=True,index=True)
    first_name = Column("fun_primeiro_nome",String(256),nullable=False)
    second_name = Column("fun_segundo_nome",String(256),nullable=False)
    password = Column("fun_senha",String(256),nullable=False)
    username = Column("fun_usuario",String(11),nullable=False)
    email = Column("fun_email",String(256),nullable=False)
    id_manager = Column("fun_id_gerente",Integer,ForeignKey("Funcionario.fun_id"))
    manager = relationship("Login", remote_side=[id], backref="employees", lazy="selectin")
    id_role = Column("crg_id",Integer,ForeignKey("Cargo.crg_id"))
    role = relationship("Role", back_populates="logins",lazy="selectin")
    id_unidade = Column("uni_id",Integer,ForeignKey("Unidade_Escolar.uni_id"))
    unidade_escolar = relationship("UnidadeEscolar",back_populates="manager")

class Regiao(Base):
    __tablename__ = "Regiao"

    id = Column("reg_id",Integer, primary_key=True,index=True)
    descricao = Column("reg_descricao",String(255),nullable=False)
    cidades = relationship("Cidade",back_populates="regiao")

class Role(Base):
    __tablename__ = "Cargo"

    id = Column("crg_id",Integer,primary_key=True,index=True)
    description = Column("crg_descricao",String(256),nullable=False)
    logins = relationship("Login", back_populates="role",lazy="selectin")

class TipoEscola(Base):
    __tablename__ = "Tipo_Escola"

    id = Column("tip_id",Integer, primary_key=True,index=True)
    description = Column("tip_descricao",String(255),nullable=False)
    unidades = relationship("UnidadeEscolar", back_populates="tipo",lazy="selectin")

class UnidadeEscolar(Base):
    __tablename__ = "Unidade_Escolar"

    id = Column("uni_id",Integer, primary_key=True,index=True)
    cod_inep = Column("uni_codigo_inep",Integer,nullable=False)
    nome = Column("uni_nome",String(255),nullable=False)

    id_tipo = Column("tip_id",Integer,ForeignKey("Tipo_Escola.tip_id"))
    tipo = relationship("TipoEscola", back_populates="unidades",lazy="selectin")

    id_endereco = Column("end_id",Integer,ForeignKey("Endereco.end_id"))
    endereco = relationship("Endereco",back_populates="unidades",lazy="selectin")
    
    manager = relationship("Login",back_populates="unidade_escolar")

