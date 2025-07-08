import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x500')
        self.lbl1 = tk.Label(self.janela, text='Label1', fg='white', bg='green')
        self.lbl2 = tk.Label(self.janela, text='Label2', fg='white', bg='red')
        self.lbl3 = tk.Label(self.janela, text='Label3', fg='white', bg='blue')
        self.lbl1.pack(fill='both', expand=True)
        self.lbl2.pack(fill='both', expand=True)
        self.lbl3.pack(fill='both', expand=True)

gui = tk.Tk()
Tela(gui)
gui.mainloop()