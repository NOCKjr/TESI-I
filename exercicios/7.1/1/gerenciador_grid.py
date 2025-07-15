import tkinter as tk

class GerenciadorGrid:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x150')

        self.bnt1 = tk.Button(self.janela, text="1")
        self.bnt1.pack()

        self.frm1 = tk.Frame(self.janela)
        self.bnt2 = tk.Button(self.frm1, text="2")
        self.bnt3 = tk.Button(self.frm1, text="3")

        self.frm1.pack()
        self.bnt2.grid(row = 0, column=1)
        self.bnt3.grid(row = 0, column=2)

        self.frm2 = tk.Frame(self.janela)
        self.bnt4 = tk.Button(self.frm2, text="4")
        self.bnt5 = tk.Button(self.frm2, text="5")
        self.bnt6 = tk.Button(self.frm2, text="6")

        self.frm2.pack()
        self.bnt4.grid(row=0, column=4)
        self.bnt5.grid(row=0, column=5)
        self.bnt6.grid(row=0, column=6)

gui = tk.Tk()
GerenciadorGrid(gui)
gui.mainloop()