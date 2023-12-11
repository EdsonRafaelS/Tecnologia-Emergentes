CREATE DATABASE projeto_TE

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
-- Excluir tabelas

-- Criação da tabela "Cadastro de Semestre"
CREATE TABLE Semestre (
    id_semestre SERIAL PRIMARY KEY,
    ano INTEGER NOT NULL,
    semestre INTEGER NOT NULL
);

-- Criação da tabela "Cadastro de Disciplinas"
CREATE TABLE Disciplinas (
    id_disciplina SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    carga_horaria INTEGER NOT NULL,
    nivel_disciplina VARCHAR(50) NOT NULL
);

-- Criação da tabela "Cadastro de Datas Importantes"
CREATE TABLE Datas_Importantes (
    id_data_importante SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    tipo_data VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL
);

-- Criação da tabela "Cadastro de Ofertas"
CREATE TABLE Ofertas (
    id_oferta SERIAL PRIMARY KEY,
    id_semestre INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    nivel VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_semestre) REFERENCES Semestre(id_semestre),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplinas(id_disciplina)
);


-- Criação da tabela "Geração de Cronograma"
CREATE TABLE Cronograma (
    id_cronograma SERIAL PRIMARY KEY,
    id_semestre INTEGER NOT NULL,
    nome_disciplina INTEGER NOT NULL,
    dia_inicio DATE NOT NULL,
    FOREIGN KEY (id_semestre) REFERENCES Semestre(id_semestre),
    FOREIGN KEY (nome_disciplina) REFERENCES Disciplinas(id_disciplina)
);

-- Criação da tabela "Gestão de Conteúdo das Aulas"
CREATE TABLE Gestao_Aulas (
    id_conteudo_aula SERIAL PRIMARY KEY,
    id_semestre INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    data DATE NOT NULL,
    aulas INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    FOREIGN KEY (id_semestre) REFERENCES Semestre(id_semestre),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplinas(id_disciplina)
);
