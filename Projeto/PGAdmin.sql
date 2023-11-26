create database projeto_II

create table disciplina(
	id int PRIMARY KEY,
	nome varchar(40) not null,
	carga_horaria int not null,
	nivel_de_ensino varchar not null
);

create table semestre(
	ano int not null,
	semestre int not  null,
	primary key(ano, semestre)
);

create table oferta(
    id int primary key,
    ano int,
    semestre int,
    id_disciplina int references disciplina(id),
    foreign key (ano, semestre) references semestre(ano, semestre)
);
