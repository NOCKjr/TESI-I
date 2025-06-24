import tkinter as tk
janela = tk.Tk()
janela.title('Primeira janela com Tkinter')
janela.geometry('400x200')
janela.resizable(width=False, height=False)
janela.maxsize(400, 500)
#adicionando um componente do tipo frame
container = tk.Frame(janela, width=100, height=100, bg='red') #Declaração do frame com o parâmetro pai
#gerenciador de layout
container.pack()
janela.mainloop()