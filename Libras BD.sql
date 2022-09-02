create database ABCdasMaos;
use ABCdasMaos;



create table usuario(
    codigo int not null primary key auto_increment,
    nome varchar(120) not null,
    email varchar(15) not null,
    senha varchar(10) not null
)engine = InnoDB;



select* from usuario