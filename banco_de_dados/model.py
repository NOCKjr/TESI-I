from conexao import Conexao
from sqlite3 import Error
class Model:
    def __init__(self):
        self.con = Conexao()
    def get(self, sql):
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            resultado = cursor.execute(sql).fetchall()
            con.close()
            return resultado
        except Error as er:
            print(er)

    def insert(self, sql):
        #sql = 'INSERT INTO CLIENTES(nome, cpf) values("TESTES", "0000000007");'
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            cont = cursor.rowcount
            if cursor.rowcount == 1:
                con.commit()
            con.close()
            return cont
        except Error as er:
            print(er)

    def delete(self, sql):
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(er)