import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.d = {1:'Pudim', 2:'Bolo', 3:'Pavê', 4:'Mousse de Araçá boi'}
        self.var_rbt = tk.IntVar()
        for i, j in self.d.items():
            rbt = tk.Radiobutton(self.janela, text=j, value=i, command=self.verifica, variable=self.var_rbt)
            rbt.pack()
        self.label = tk.Label(self.janela)
        self.label.pack()

    def verifica(self):
        valor = self.var_rbt.get()
        self.label.config(text=f'{self.d[valor]}')
gui = tk.Tk()
Tela(gui)
gui.mainloop()