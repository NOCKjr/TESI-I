import tkinter as tk

class PackSimples:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x500")

        lbl1 = tk.Label(self.janela, text="Topo", bg="yellow", fg="black")
        lbl1.pack(fill="both", expand=1, side="top")

        lbl4 = tk.Label(self.janela, text="Rodapé", bg="cyan", fg="black")
        lbl4.pack(fill="both", expand=1, side="bottom")

        lbl2 = tk.Label(self.janela, text="Direita", bg="red", fg="white")
        lbl2.pack(fill="x", expand=1, side="right")

        lbl3 = tk.Label(self.janela, text="Esquerda", bg="green", fg="white")
        lbl3.pack(fill="x", expand=1, side="left")

gui = tk.Tk()
PackSimples(gui)
gui.mainloop()