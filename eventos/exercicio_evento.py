import tkinter as tk
from tkinter import scrolledtext

class Tela:
    texto = ''
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Pressione qualquer tecla')
        self.btn.pack()
        self.janela.bind('<Key>', self.clicou)
        self.label = tk.Label(self.janela, text=Tela.texto)
        self.label.pack()

    def clicou(self, event):
        if event.char() == ' ' or '':
            self.label.config(text=Tela.texto+f'Tecla especial: {event.keysym}\n')
        else:
            self.label.config(text=Tela.texto+f'Tecla normal: {event.keysym}\n')
gui = tk.Tk()
Tela(gui)
gui.mainloop()