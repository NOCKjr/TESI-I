import tkinter as tk
from tkinter import messagebox


class Tela():

    def __init__(self, master):

        self.janela = master
        self.janela.geometry("300x300")

        self.lbl_nome = tk.Label(self.janela, text="Nome: ")
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_email = tk.Label(self.janela, text="Email: ")
        self.lbl_email.grid(row=1, column=0)

        self.ent_nome = tk.Entry(self.janela)
        self.ent_nome.grid(row=0, column=1, columnspan=2, sticky="we")
        self.ent_email = tk.Entry(self.janela)
        self.ent_email.grid(row=1, column=1, columnspan=2, sticky="we")

        self.var_cpp = tk.IntVar()
        self.var_java = tk.IntVar()
        self.var_python = tk.IntVar()

        self.frm_curso = tk.LabelFrame(self.janela, text="Curso(s): ")
        self.frm_curso.grid(row=2, column=1, sticky="w")
        self.cbt_cpp = tk.Checkbutton(self.frm_curso, text="C++", variable=self.var_cpp)
        self.cbt_cpp.pack(anchor='w')
        self.cbt_java = tk.Checkbutton(self.frm_curso, text="Java", variable=self.var_java)
        self.cbt_java.pack(anchor='w')
        self.cbt_python = tk.Checkbutton(self.frm_curso, text="python", variable=self.var_python)
        self.cbt_python.pack(anchor='w')

        self.var_rbt = tk.StringVar()

        self.frm_mod = tk.LabelFrame(self.janela, text="Modalidade: ")
        self.frm_mod.grid(row=2, column=2, sticky='w')
        self.rbt_ead = tk.Radiobutton(self.frm_mod, text="EAD", variable=self.var_rbt, value="ead")
        self.rbt_ead.pack(anchor='w')
        self.rbt_presencial = tk.Radiobutton(self.frm_mod, text="Presencial", variable=self.var_rbt, value="presencial")
        self.rbt_presencial.pack(anchor='w')

        self.btn_enviar = tk.Button(self.janela, text="Enviar", command=self.exibir)
        self.btn_enviar.grid(row=3, column=0, columnspan=3, sticky="we")

    def exibir(self):
        lista = []
        if(self.var_cpp.get()):
            lista.append("C++")
        if(self.var_java.get()):
            lista.append("Java")
        if(self.var_python.get()):
            lista.append("Pyhton")

        modalidade = self.var_rbt.get()

        messagebox.showinfo("Informação ", f"Linguagens: {", ".join(lista)}"
                                           f"\nModalidade: {modalidade}")



gui = tk.Tk()
tela = Tela(gui)
tela.janela.mainloop()
