import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x100')
        self.scb = tk.Scrollbar(self.janela)
        self.scb.pack(side='right', fill='y')
        self.txt = tk.Text(self.janela, height=5, yscrollcommand=self.scb.set)
        self.txt.pack(side='left')
        self.scb.config(command=self.txt.yview)
gui = tk.Tk()
Tela(gui)
gui.mainloop()