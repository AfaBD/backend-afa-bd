CREATE TABLE Cargo (
    crg_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crg_descricao varchar(256)  NOT NULL
);

CREATE TABLE Funcionario (
    fun_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fun_primeiro_nome varchar(256)  NOT NULL,
    fun_segundo_nome varchar(256)  NOT NULL,
    fun_senha varchar(256)  NOT NULL,
    fun_usuario varchar(11)  NOT NULL,
    fun_email varchar(256)  NOT NULL,
    crg_id integer  NOT NULL,
    fun_id_gerente integer  NULL,
    FOREIGN KEY (crg_id) REFERENCES Cargo (crg_id),
    FOREIGN KEY (fun_id_gerente) REFERENCES Funcionario (fun_id)  
);

insert into Cargo (crg_descricao) values ('ROLE_ADMIN');
insert into Cargo (crg_descricao) values ('ROLE_MANAGER');
insert into Cargo (crg_descricao) values ('ROLE_SUPERVISOR');