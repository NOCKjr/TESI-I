import tkinter as tk

class MinhaTela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Primeira janela com Tkinter")
        self.janela.geometry("400x200")
        self.janela.resizable(width=False, height=True)
        self.janela.maxsize(400, 500)
        self.container = tk.Frame(self.janela, width=100, height=100, bg="green")  # janela é pai de container

        # gerenciador de layout
        self.container.pack()  # add container em janela

        self.nome = tk.Label(self.container, text="um texto aí")
        self.telefone = tk.Label(self.janela, text="marcos..@gmail.com")
        self.nome.place(x=10,y=10)
        self.telefone.pack()


gui = tk.Tk()
minhatela = MinhaTela(gui)
gui.mainloop()
