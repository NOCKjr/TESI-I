import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.mte = ttk.Meter(self.janela, amountused=10, interactive=True)
        self.mte.pack()

app = ttk.Window(themename='litera')
Tela(app)
app.mainloop()