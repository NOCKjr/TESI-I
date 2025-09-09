import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='clicar')
        self.btn.pack()
        self.btn.bind('<Key>', self.clicou)

    def clicou(self, event):
        print(event.keysym)
gui = tk.Tk()
Tela(gui)
gui.mainloop()