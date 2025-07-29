import tkinter as tk
from tkinter import ttk, messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        #self.janela.geometry('800x300')
        colunas = ['nome', 'cpf', 'email']
        self.tvw = ttk.Treeview(self.janela, height=5, columns=colunas, show='headings')
        #Configurar o cabaçalho das colunas
        self.tvw.heading('nome', text='NOME')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='EMAIL')
        #Preencher a tabela
        self.tvw.insert('', 'end', values=('Limeira', '00000000000', 'limeira@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Manoel', '00000000000', 'manoel@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste1', '00000000000', '1@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste2', '00000000000', '2@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste3', '00000000000', '3@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste4', '00000000000', '4@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste5', '00000000000', '5@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste6', '00000000000', '6@ufac.br'))
        self.tvw.insert('', 'end',
                        values=('Teste7', '00000000000', '7@ufac.br'))
        self.tvw.grid(row=0, column=0)
        self.brl = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.brl.grid(row=0, column=1, sticky='ns')
        self.tvw.configure(yscrollcommand=self.brl.set)
        #Botôes
        self.frm_botoes = ttk.Frame(self.janela)
        self.frm_botoes.grid(row=1, column=0)
        self.btn_cadastrar = ttk.Button(self.frm_botoes, text='Cadastrar', command=self.cadastrar)
        self.btn_cadastrar.grid(row=0, column=0)
        self.btn_excluir = ttk.Button(self.frm_botoes, text='Excluir', command=self.excluir)
        self.btn_excluir.grid(row=0, column=1)
        self.btn_editar = ttk.Button(self.frm_botoes, text='Editar', command=self.editar)
        self.btn_editar.grid(row=0, column=2)

        self.centralizar(self.janela)

    def centralizar(self, master):
        largura_monitor = master.winfo_screenwidth()
        altura_monitor = master.winfo_screenheight()
        #print(largura_monitor, altura_monitor)
        master.update_idletasks()
        largura_janela = master.winfo_width()
        altura_janela = master.winfo_height()
        #print(largura_janela, altura_janela)
        x = largura_monitor//2 - largura_janela//2
        y = altura_monitor//2 - altura_janela//2
        master.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

    def cadastrar(self):
        self.top_cadastrar = tk.Toplevel(self.janela)
        self.top_cadastrar.grab_set()
        self.lbl_nome = ttk.Label(self.top_cadastrar, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_cpf = ttk.Label(self.top_cadastrar, text='CPF:')
        self.lbl_cpf.grid(row=1, column=0)
        self.lbl_email = ttk.Label(self.top_cadastrar, text='Email:')
        self.lbl_email.grid(row=2, column=0)

        self.ent_nome = ttk.Entry(self.top_cadastrar)
        self.ent_nome.grid(row=0, column=1)
        self.ent_cpf = ttk.Entry(self.top_cadastrar)
        self.ent_cpf.grid(row=1, column=1)
        self.ent_email = ttk.Entry(self.top_cadastrar)
        self.ent_email.grid(row=2, column=1)

        self.btn_confirmar_cadastro = ttk.Button(self.top_cadastrar, text="Confirmar Cadastro", command=self.confirmar_cadastro)
        self.btn_confirmar_cadastro.grid(row=3, column=0, columnspan=2, stick='we')
        self.centralizar(self.top_cadastrar)
    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        if not nome or not cpf or not email:
            messagebox.showwarning('Aviso', 'Todos os campos são obrigatórios.', parent=self.top_cadastrar)
        else:
            self.tvw.insert('', 'end', values=(nome, cpf, email))
            self.top_cadastrar.destroy()
            self.janela.deiconify()

    def excluir(self):
        itens = self.tvw.selection()
        if not itens:
            messagebox.showwarning('Aviso', 'Selecione algo!')
        else:
            resposta = messagebox.askquestion('Confirmar', 'Tem certeza da exclusão?', parent=self.janela)
            if resposta=='yes':
                for item in itens:
                    self.tvw.delete(item)

        #for i in itens:
            #print(self.tvw.item(i, 'values'))
    def editar(self):
        self.item_selecionado = self.tvw.selection()
        if len(self.item_selecionado) != 1:
            messagebox.showwarning("Aviso", "Selecione um item")
        else:
            dados = self.tvw.item(self.item_selecionado, 'values')
            self.top_editar = tk.Toplevel(self.janela)
            self.top_editar.grab_set()
            self.lbl_nome = ttk.Label(self.top_editar, text='Nome:')
            self.lbl_nome.grid(row=0, column=0)
            self.lbl_cpf = ttk.Label(self.top_editar, text='CPF:')
            self.lbl_cpf.grid(row=1, column=0)
            self.lbl_email = ttk.Label(self.top_editar, text='Email:')
            self.lbl_email.grid(row=2, column=0)

            self.ent_nome = ttk.Entry(self.top_editar)
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert('end', dados[0])
            self.ent_cpf = ttk.Entry(self.top_editar)
            self.ent_cpf.grid(row=1, column=1)
            self.ent_cpf.insert('end', dados[1])
            self.ent_email = ttk.Entry(self.top_editar)
            self.ent_email.grid(row=2, column=1)
            self.ent_email.insert('end', dados[2])

            self.btn_confirmar_edicao = ttk.Button(self.top_editar, text="Confirmar edição",
                                                     command=self.confirmar_edicao)
            self.btn_confirmar_edicao.grid(row=3, column=0, columnspan=2, stick='we')
    def confirmar_edicao(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        if not nome or not cpf or not email:
            messagebox.showwarning('Aviso', 'Todos os campos são obrigatórios.', parent=self.top_editar)
        else:
            self.tvw.item(self.item_selecionado, values=(nome, cpf, email))
            self.top_editar.destroy()
            self.janela.deiconify()

gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()