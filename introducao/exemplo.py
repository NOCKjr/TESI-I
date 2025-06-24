import tkinter as tk

janela = tk.Tk()

janela.title("Primeira janela com Tkinter")
janela.geometry("400x200")
janela.resizable(width=False, height=False)
janela.maxsize(400, 500)

janela.mainloop()