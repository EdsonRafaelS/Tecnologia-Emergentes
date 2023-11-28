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
    id_oferta int primary key,
    ano int,
    semestre int,
    id_disciplina int references disciplina(id),
    foreign key (ano, semestre) references semestre(ano, semestre)
);

create table datas_importantes(
	id int primary key,
	data_importante date not null,
	descricao_data varchar(30) not null,
	tipo_data varchar(30) not null
);

create table cronograma(
	id_cronograma int primary key,
	data_inicio_semestre date not null,
	data_termino_semestre date not null,
	dias_de_aulas varchar[],
	id_oferta int references oferta(id_oferta)
);

create table conteudos(
	id int primary key, 
	id_cronograma int references cronograma(id_cronograma),
	quantidade_aulas int not null
);
