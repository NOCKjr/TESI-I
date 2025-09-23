import ttkbootstrap as ttk
from tkinter import messagebox
import control
class Tela:
    def __init__(self, master):
        self.janela = master
        colunas = ['id','nome', 'cpf']
        self.tvw = ttk.Treeview(self.janela, height=5,
                                columns=colunas, show='headings')
        #Configurar o cabaçalho das colunas
        self.tvw.heading('id', text='ID')
        self.tvw.heading('nome', text='NOME')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.grid(row=0, column=0)
        self.brl = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.brl.grid(row=0, column=1, sticky='ns')
        self.tvw.configure(yscrollcommand=self.brl.set)

        #listando clientes
        self.controle_clientes = control.ControllerCliente()
        self.controle_clientes.criar_tabelas()
        tuplas = self.controle_clientes.listar_clientes()
        for item in tuplas:
            print(item)
            self.tvw.insert('', 'end', values = item)

        #Botões
        self.frm_botoes = ttk.Frame(self.janela)
        self.frm_botoes.grid(row=1, column=0)
        self.btn_cadastrar = ttk.Button(self.frm_botoes, text='Cadastrar',
                                        command=self.cadastrar)
        self.btn_cadastrar.grid(row=0,column=0)
        self.btn_excluir = ttk.Button(self.frm_botoes, text='Excluir',
                                     command=self.excluir)
        self.btn_excluir.grid(row=0, column=1)
        self.btn_editar = ttk.Button(self.frm_botoes, text='Editar',
                                     command=self.editar)
        self.btn_editar.grid(row=0, column=2)
        self.centraliza(self.janela)

        self.btn_pesquisar = ttk.Button(self.frm_botoes, text='pesquisar...', command=self.atualizar_treeview)
        self.btn_pesquisar.grid(row=0, column=3)

        self.ent_pesquisar = ttk.Entry(self.frm_botoes)
        self.ent_pesquisar.grid(row=1, column=0, columnspan=4)


    def centraliza(self, master):
        # Criar uma forma de centralizar a janela

        largura_monitor = master.winfo_screenwidth()
        altura_monitor = master.winfo_screenheight()
        master.update_idletasks()
        largura_janela = master.winfo_width()
        altura_janela = master.winfo_height()
        x = largura_monitor // 2 - largura_janela // 2
        y = altura_monitor //2 - altura_janela // 2
        master.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

    def excluir(self):
        itens = self.tvw.selection()

        if len(itens) > 0:
            resposta = messagebox.askquestion('Confirmar', 'Tem certeza da '
                                                      'exclusão?')
            if resposta == 'yes':
                for i in itens:
                    id = self.tvw.item(i, 'values')[0]
                    self.controle_clientes.excluir_clientes(id)
                messagebox.showinfo('Informação', 'Cliente(s) excluidos com sucesso!')
        else:
            messagebox.showwarning('Aviso', 'Bicho seleciona aew')
        self.atualizar_treeview()
        # for item in itens:
        #     print(self.tvw.item(item, 'values'))
    def editar(self):
        self.item_selecionado = self.tvw.selection()
        if len(self.item_selecionado) != 1:
            messagebox.showwarning('Aviso', 'Selecione um item')
        else:
            self.dados = self.tvw.item(self.item_selecionado, 'values')
            self.top_editar = ttk.Toplevel(self.janela)
            self.top_editar.grab_set()
            self.lbl_nome = ttk.Label(self.top_editar, text='NOME:').grid(
                row=0, column=0)
            self.lbl_cpf = ttk.Label(self.top_editar, text='CPF:').grid(
                row=1, column=0)
            self.ent_nome = (ttk.Entry(self.top_editar))
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert('end', self.dados[1]) #Preenche o campo de entrada
            self.ent_cpf = (ttk.Entry(self.top_editar))
            self.ent_cpf.grid(row=1, column=1)
            self.ent_cpf.insert('end', self.dados[2]) #Preenche o campo de entrada
            self.btn_confirmar_edicao = ttk.Button(self.top_editar,
                                                     text='Confirmar '
                                                          'Edição',
                                                     command=self.confirmar_edicao).grid(
                row=3,
                column=0, columnspan=2, sticky='we')

    def confirmar_edicao(self):
        id = self.dados[0]
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        if nome == '' or cpf == '':
            messagebox.showwarning('Aviso', 'Todos os campos são obrigatórios')
        else:
            #leva a alteração do formulario para o banco de dados
            self.controle_clientes.editar_clientes(id, nome, cpf)
            #alteção do componente tree view
            #self.tvw.item(self.item_selecionado, values=(nome,cpf, email))
            self.atualizar_treeview()
            self.top_editar.destroy()
            self.janela.deiconify()

    def cadastrar(self):
        self.top_cadastrar = ttk.Toplevel(self.janela)
        self.top_cadastrar.grab_set()
        self.lbl_nome = ttk.Label(self.top_cadastrar, text='NOME:').grid(
            row=0, column=0)
        self.lbl_cpf = ttk.Label(self.top_cadastrar, text='CPF:').grid(
            row=1, column=0)
        self.ent_nome = (ttk.Entry(self.top_cadastrar))
        self.ent_nome.grid(row=0, column=1)
        self.ent_cpf = (ttk.Entry(self.top_cadastrar))
        self.ent_cpf.grid(row=1, column=1)
        self.btn_confirmar_cadastro = ttk.Button(self.top_cadastrar,
                                                 text='Confirmar '
                                                      'Cadastro',
                                                 command=self.confirmar_cadastro).grid(row=3,
                                                                       column=0, columnspan=2, sticky='we')
        self.centraliza(self.top_cadastrar)

    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        if nome == '' or cpf == '':
            messagebox.showwarning('Aviso', 'Todos os campos são '
                                            'obrigatórios.',
                                   parent=self.top_cadastrar)
        else:
            if self.controle_clientes.inserir_clientes(nome, cpf) == 1:
                messagebox.showinfo('informação', 'Cliente inserido com sucesso!')
            #self.tvw.insert('','end', values=(nome, cpf, email))
            self.atualizar_treeview()
            self.top_cadastrar.destroy()
            self.janela.deiconify()
    def atualizar_treeview(self):
        nome = self.ent_pesquisar.get()
        dados = self.tvw.get_children()
        for item in dados:
            self.tvw.delete(item)
        tuplas = self.controle_clientes.listar_clientes(nome)
        for item in tuplas:
            self.tvw.insert('', 'end', values=item)

gui = ttk.Window(themename='litera')
principal = Tela(gui)
gui.mainloop()