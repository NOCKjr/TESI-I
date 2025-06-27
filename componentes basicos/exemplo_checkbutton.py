import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x300')
        self.verifica = tk.IntVar()
        self.cbt1 = tk.Checkbutton(self.janela, text='Flamengo', command=self.clicou, variable=self.verifica)
        self.cbt2 = tk.Checkbutton(self.janela, text='Bayern')

        self.cbt1.pack()
        self.cbt2.pack()

    def clicou(self):
        print(self.verifica.get())

gui = tk.Tk()
Tela(gui)
gui.mainloop()