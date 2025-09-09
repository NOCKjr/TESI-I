import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
from PIL import Image, ImageTk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn_abrir = tk.Button(self.janela, text='Abrir arquivo...')
        self.btn_salvar = tk.Button(self.janela, text='Salvar arquivo')
        self.btn_abrir.pack()
        self.lbl_imagem = tk.Label(self.janela)
        self.lbl_imagem.pack()
        self.btn_salvar.pack()
        self.stx = ScrolledText(self.janela)
        self.stx.pack()
        self.btn_abrir.bind('<Button-1>', self.abrir)
        self.btn_salvar.bind('<Button-1>', self.salvar)

    def salvar(self, event):
        arquivo = fd.asksaveasfile()
        print(arquivo)
        arquivo.write(self.stx.get(1.0, 'end'))

    def abrir(self, event):
        #caminho = fd.askopenfilename()
        #print(caminho)
        #with open(caminho, 'r') as arquivo:
            #for linha in arquivo:
                #self.stx.insert('end', linha)
        arquivo = fd.askopenfile()
        print(arquivo)
        for linha in arquivo:
            self.stx.insert('end', linha)

app = tk.Tk()
Tela(app)
app.mainloop()