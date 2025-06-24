import tkinter as tk

class MinhaTela:
    def __init__(self, tela):
        self.janela = tela
        self.janela.title('Primeira janela com Tkinter')
        self.janela.geometry('400x200')
        self.janela.resizable(width=False, height=False)
        self.janela.maxsize(400, 500)
        # adicionando um componente do tipo frame
        self.container = tk.Frame(self.janela, width=100, height=100, bg='red')  # Declaração do frame com o parâmetro pai
        # gerenciador de layout
        self.container.pack()
        self.nome = tk.Label(self.container, text='elias da cruz')
        self.email = tk.Label(self.janela, text='elias.cruz@sou.ufac.br')
        self.nome.place(x=10, y=10)
        self.email.pack()

gui = tk.Tk()
minhatela = MinhaTela(gui)
gui.mainloop()