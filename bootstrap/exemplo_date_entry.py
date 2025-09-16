import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.lbl = ttk.Label(self.janela, text='Bem vindo ao ttkbootstrap!')
        self.lbl.pack()
        self.ent = ttk.DateEntry(self.janela, dateformat = '%d-%m-%y')
        self.ent.pack()
        self.btn = ttk.Button(self.janela, text='Enviar', bootstyle='success')
        self.btn.pack()

app = ttk.Window(themename='litera')
Tela(app)
app.mainloop()