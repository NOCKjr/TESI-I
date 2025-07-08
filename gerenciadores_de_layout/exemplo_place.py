import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x500')
        self.lbl1 = tk.Label(self.janela, text='Label1', fg='white', bg='green')
        self.lbl2 = tk.Label(self.janela, text='Label2', fg='white', bg='red')
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')
        self.lbl2.place(x=0, y=0, width=250)

gui = tk.Tk()
Tela(gui)
gui.mainloop()