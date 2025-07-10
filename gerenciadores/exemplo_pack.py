import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x500")

        lbl1 = tk.Label(self.janela, text="Label 1", bg="black", fg="white")
        lbl1.pack(fill="both", expand=1, side="top")
        lbl2 = tk.Label(self.janela, text="Label 2", bg="red", fg="white")
        lbl2.pack(fill="both", expand=1, side="top")
        lbl3 = tk.Label(self.janela, text="Label 3", bg="yellow", fg="black")
        lbl3.pack(fill="both", expand=1, side="top")

gui = tk.Tk()
Tela(gui)
gui.mainloop()