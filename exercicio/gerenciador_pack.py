import tkinter as tk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x300')
        self.frm_cima = tk.Frame(self.janela)
        self.frm_cima.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        self.frm_baixo = tk.Frame(self.janela)
        self.frm_baixo.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

        self.lbl_esquerda = tk.Label(self.frm_baixo, text='gray', fg='white', bg="gray")
        self.lbl_esquerda.pack(fill=tk.Y, expand=True, side=tk.LEFT)

        self.lbl_direita = tk.Label(self.frm_baixo, text='gray', fg='white', bg="gray")
        self.lbl_direita.pack(fill=tk.Y, expand=True, side=tk.RIGHT)

        self.frm_meio = tk.Frame(self.frm_baixo)
        self.frm_meio.pack(fill=tk.BOTH, expand=True)

        self.lbl_meio_baixo = tk.Label(self.frm_baixo, text='black', fg='white', bg='black')
        self.lbl_meio_baixo.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

        self.lbl_red = tk.Label(self.frm_cima, bg='red', text='red', fg='white')
        self.lbl_red.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        self.lbl_green = tk.Label(self.frm_cima, bg='green', text='green', fg='white')
        self.lbl_green.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        self.lbl_blue = tk.Label(self.frm_cima, bg='blue', text='blue', fg='white')
        self.lbl_blue.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

gui = tk.Tk()
Tela(gui)
gui.mainloop()
