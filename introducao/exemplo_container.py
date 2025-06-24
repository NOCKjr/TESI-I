import tkinter as tk

janela = tk.Tk()

janela.title("Primeira janela com Tkinter")
janela.geometry("400x200")
janela.resizable(width=False, height=True)
janela.maxsize(400, 500)

container = tk.Frame(janela, width=100, height=100, bg="green") # janela é pai de container

#gerenciador de layout
container.pack() # add container em janela

janela.mainloop()