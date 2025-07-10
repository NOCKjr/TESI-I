import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x500")

        lbl1 = tk.Label(self.janela, text="Label 1", bg="blue", fg="white")
        lbl1.place(x=250, y=250, anchor="center")
        lbl2 = tk.Label(self.janela, text="Label 2", bg="red", fg="white")
        lbl2.place(x=0, y=0, width=250)

gui = tk.Tk()
Tela(gui)
gui.mainloop()