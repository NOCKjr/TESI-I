import sqlite3
from sqlite3 import Error

class Conexao:
    def get_conexao(self):
        caminho = '/home/elias.cruz/Downloads/TESI-I/banco_de_dados/banco.db'
        try:
            con = sqlite3.connect(caminho)
            return con
        except Error as er:
            print(er)

#obj = Conexao()
#conexao = obj.get_conexao()
#if conexao:
    #try:
        #sql = 'SELECT * FROM CLIENTES'
        #cursor = conexao.cursor()
        #resultado = cursor.execute(sql).fetchall()
        #for i in cursor.execute(sql):
            #print(f'{i}')
    #except Error as er:
            #print(er)

