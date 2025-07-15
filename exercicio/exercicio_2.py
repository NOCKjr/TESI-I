import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x400')
        self.lbl_nome = tk.Label(self.janela, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)

        self.lbl_email = tk.Label(self.janela, text='email:')
        self.lbl_email.grid(row=1, column=0)

        self.ent_nome = tk.Entry(self.janela)
        self.ent_nome.grid(row=0, column=1, columnspan=2, stick='we')

        self.ent_email = tk.Entry(self.janela)
        self.ent_email.grid(row=1, column=1, columnspan=2, stick='we')

        self.var_c = tk.IntVar()
        self.var_java = tk.IntVar()
        self.var_python = tk.IntVar()

        self.frm_curso = tk.LabelFrame(self.janela, text='Curso:')
        self.frm_curso.grid(row=2, column=1, stick='w')
        self.cbt_c = tk.Checkbutton(self.frm_curso, text='C++', variable=self.var_c)
        self.cbt_c.pack(anchor ='w')
        self.cbt_java = tk.Checkbutton(self.frm_curso, text='Java', variable=self.var_java)
        self.cbt_java.pack(anchor ='w')
        self.cbt_python = tk.Checkbutton(self.frm_curso, text='Python', variable=self.var_python)
        self.cbt_python.pack(anchor ='w')

        self.var_mod = tk.StringVar()
        self.frm_mod = tk.LabelFrame(self.janela, text='Modalidade:')
        self.frm_mod.grid(row=2, column=2, stick='n')
        self.rbt_ead = tk.Radiobutton(self.frm_mod, text='EAD', variable=self.var_mod, value='EAD')
        self.rbt_ead.pack(anchor='w')
        self.rbt_presencial = tk.Radiobutton(self.frm_mod, text='Presencial', variable=self.var_mod, value='Presencial')
        self.rbt_presencial.pack(anchor='w')

        self.btn_enviar = tk.Button(self.janela, text='enviar', command = self.exibir_dados)
        self.btn_enviar.grid(row=3, column=0, columnspan=3, stick='we')

    def exibir_dados(self):
        lista=[]
        if self.var_c.get():
            lista.append('C++')
        if self.var_java.get():
            lista.append('Java')
        if self.var_python.get():
            lista.append('Python')

        modalidade = self.var_mod.get()
        messagebox.showinfo('informação', f'Linguagens: {", ".join(lista)}\nModalidade: {modalidade}')


gui = tk.Tk()
Tela(gui)
gui.mainloop()