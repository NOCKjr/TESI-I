import tkinter as tk
from tkinter import messagebox

class PackSimples:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("300x220")
        self.janela.title("Cadastro de Aluno")

        self.frm0 = tk.Frame(self.janela)
        self.frm0.pack(fill="x")

        self.lbl_nome = tk.Label(self.frm0, text="Nome: ", padx=11, pady=7)
        self.lbl_nome.grid(row=0, column=0)
        self.ent_nome = tk.Entry(self.frm0, width=27)
        self.ent_nome.grid(row=0, column=1)
        self.lbl_email = tk.Label(self.frm0, text="Email: ", padx=11, pady=7)
        self.lbl_email.grid(row=1, column=0)
        self.ent_email = tk.Entry(self.frm0, width=27)
        self.ent_email.grid(row=1, column=1)

        self.frm1 = tk.Frame(self.janela)
        self.frm1.pack()

        self.lbl_cursos = tk.Label(self.frm1, text="Curso(s): ", padx=11)
        self.lbl_cursos.grid(row=0, column=0)
        self.var_cpp = tk.IntVar()
        self.cbt_cpp = tk.Checkbutton(self.frm1, text="C++", variable=self.var_cpp)
        self.cbt_cpp.grid(row=1, column=0)
        self.var_java = tk.IntVar()
        self.cbt_java = tk.Checkbutton(self.frm1, text="Java", variable=self.var_java)
        self.cbt_java.grid(row=2, column=0)
        self.var_python = tk.IntVar()
        self.cbt_python = tk.Checkbutton(self.frm1, text="Python", variable=self.var_python)
        self.cbt_python.grid(row=3, column=0)


        self.lbl_modalidade = tk.Label(self.frm1, text="Modalidade: ", padx=11)
        self.lbl_modalidade.grid(row=0, column=1)
        self.var_rbt = tk.IntVar()
        self.rbt_ead = tk.Radiobutton(self.frm1, text="EAD", value=1, variable=self.var_rbt)
        self.rbt_ead.grid(row=1, column=1)
        self.rbt_presencial = tk.Radiobutton(self.frm1, text="Presencial", value=2, variable=self.var_rbt)
        self.rbt_presencial.grid(row=2, column=1)

        self.bnt_exibir = tk.Button(self.janela, text="Exibir Dados", command=self.click)
        self.bnt_exibir.pack(fill='x')

    def click(self):
        t = f"{self.ent_nome.get()} está\nnos Cursos:"
        if(self.var_cpp.get()): t += " C++;"
        if(self.var_java.get()): t += " java;"
        if(self.var_python.get()): t+= " python;"
        t+= '\nna Modalidade: '
        t += "EAD" if self.var_rbt.get() == 1 else "Presencial"
        messagebox.showinfo(message=t)

        print(t)
gui = tk.Tk()
PackSimples(gui)
gui.mainloop()