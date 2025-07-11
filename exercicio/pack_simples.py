import tkinter as tk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        self.lbl_topo = tk.Label(self.janela, text = 'TOPO', bg='yellow')
        self.lbl_esquerda = tk.Label(self.janela, text='ESQUERDA', bg='red')
        self.lbl_direita = tk.Label(self.janela, text='DIREITA', bg='green')
        self.lbl_rodape = tk.Label(self.janela, text='RODAPÉ', bg='cyan')

        self.lbl_topo.pack(fill=tk.BOTH, expand = True, side=tk.TOP)
        self.lbl_rodape.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)
        self.lbl_esquerda.pack(fill=tk.X, expand=True, side=tk.LEFT)
        self.lbl_direita.pack(fill=tk.X, expand=True, side = tk.RIGHT)

gui = tk.Tk()
Tela(gui)
gui.mainloop()
