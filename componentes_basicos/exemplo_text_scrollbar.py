import tkinter as tk
from tkinter.scrolledtext import ScrolledText
class Tela:

    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x100')

        self.scb = tk.Scrollbar(self.janela)
        #self.scb.pack(side=tk.RIGHT, fill=tk.Y)
        self.scb.pack(side="right", fill="y")

        linhas= '''Linha 1
        Linha 2 
            .
            .
            .
        Linha n
                '''

        self.txt = tk.Text(self.janela, yscrollcommand=self.scb.set) #heihgt
        self.txt.insert(tk.END, linhas)
        #self.txt.pack(side=tk.LEFT)
        self.txt.pack(side="left")

        self.scb.config(command = self.txt.yview)

        self.stx = ScrolledText(self.janela)
        self.stx.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()