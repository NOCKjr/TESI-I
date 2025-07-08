import tkinter as tk
from tkinter import messagebox

class Tela:

    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')

        self.var_rbt = tk.IntVar()
        self.d = {1:"Pudim", 2:"Bolo", 3:"Pavê", 4:"Mousse de Araça Boi"}
        for chave,valor in self.d.items():
            rbt = tk.Radiobutton(self.janela, text=valor, value=chave,
                                 variable=self.var_rbt, command=self.escolher)
            rbt.pack()

    def escolher(self):
        messagebox.showinfo("sobremesas", "Você escolheu: " + self.d[self.var_rbt.get()])
        #print(self.d[self.var_rbt.get()])

gui = tk.Tk()
Tela(gui)
gui.mainloop()