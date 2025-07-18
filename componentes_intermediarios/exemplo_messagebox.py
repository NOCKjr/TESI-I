import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text = 'Abrir Toplevel', command=self.mensagem)
        self.btn.pack()

    def mensagem(self):
        retorno = messagebox.showerror('Aviso', 'Cuidado')
        print(retorno)
        retorno2 = messagebox.askyesno('aviso', 'sua mãe sabe que você é viado?')


gui = tk.Tk()
Tela(gui)
gui.mainloop()