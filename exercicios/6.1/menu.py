import tkinter as tk
import cadastro
import idade

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("400x350")

        self.mnu_barra = tk.Menu(self.janela) # crio a barra

        self.mnu_item_op = tk.Menu(self.mnu_barra) # crio uma das opções da barra
        self.mnu_barra.add_cascade(label="Opções", menu=self.mnu_item_op)

        self.mnu_item_op.add_command(label="Calcular idade", command=self.idade) # crio uma subopção

        self.mnu_item_op.add_command(label="Selecionar preferência de cadastro", command=self.cad) #

        self.janela.config(menu=self.mnu_barra)

    def idade(self):
        t_info = tk.Tk()
        info.Tela(t_info)
        t_info.mainloop()

    def cad(self):
        t_cad = tk.Tk()
        cadastro.Tela(t_cad)
        t_cad.mainloop()

gui = tk.Tk()
tela = Tela(gui)
tela.janela.mainloop()