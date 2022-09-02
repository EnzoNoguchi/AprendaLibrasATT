import webbrowser as wb
import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()
        self.db_connection = self.db_connection.conectar()
        self.con = self.db_connection.cursor() #navegação no banco de dados

    def inserir(self, nome , email, senha):
        try:
            sql = "insert into usuario(codigo, nome, email, senha) values('','{}','{}','{}')".format(nome, email, senha)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linhas afetadas".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "select * from usuario"
            self.con.execute(sql)
            msg = ""

            for (codigo, nome, email, senha) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Email: {}, Senha: {}".format(codigo, nome, email, senha)

            return msg
        except Exception as erro:
            return erro




    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update usuario set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro



    def excluir(self, cod):
        try:
            sql = "delete from usuario where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount)
        except Exception as erro:
            return erro





