import tkinter as tk
from calcular_idade import Calcular_idade
from preferencias_cadastro import Preferencias_cadastro

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
        Calcular_idade(tk.Tk())

    def cad(self):
        # bugando
        Preferencias_cadastro(tk.Tk())

gui = tk.Tk()
tela = Tela(gui)
tela.janela.mainloop()