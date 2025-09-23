import model

class ControllerCliente:
    def __init__(self):
        self.model = model.Model()

    def criar_tabelas(self):
        self.model.create_db()
    def inserir_clientes(self, nome='', cpf=''):
        sql = f"INSERT INTO CLIENTES(nome, cpf) VALUES ('{nome}', '{cpf}');"
        return self.model.insert(sql)

    def listar_clientes(self, nome=''):
        sql = f'SELECT * FROM CLIENTES WHERE nome LIKE "%{nome}%";'
        return self.model.get(sql)

    def excluir_clientes(self, id):
        sql = f'DELETE FROM CLIENTES WHERE id = {id}'
        return self.model.delete(sql)

    def editar_clientes(self, id, nome, cpf):
        sql = f'UPDATE CLIENTES SET nome = "{nome}", cpf = "{cpf}" WHERE id = {id};'
        return self.model.update(sql)