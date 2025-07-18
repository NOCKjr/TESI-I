import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.imagem = tk.PhotoImage(file='wpp.png')
        #self.imagem = self.imagem.subsample(2, 2)
        self.lbl = tk.Label(self.janela, image=self.imagem)
        self.lbl.image = self.imagem
        self.lbl.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()