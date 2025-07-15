import tkinter as tk

class GerenciadorPack:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x500")

        self.frm1 = tk.Frame(self.janela)
        self.frm1.pack(fill="both", expand=1, side="top")

        self.lbl_red = tk.Label(self.frm1, text="red", bg="red", fg="white")
        self.lbl_red.pack(fill="both", expand=1, side="top")
        self.lbl_green = tk.Label(self.frm1, text="green", bg="green", fg="white")
        self.lbl_green.pack(fill="both", expand=1, side="top")
        self.lbl_blue = tk.Label(self.frm1, text="blue", bg="blue", fg="white")
        self.lbl_blue.pack(fill="both", expand=1, side="top")

        self.frm2 = tk.Frame(self.janela, bg="purple")
        self.frm2.pack(fill="both", expand=1, side="bottom")

        self.lbl_grayL = tk.Label(self.frm2, text="gray", bg="gray", fg="white", padx=25)
        self.lbl_grayL.pack(side="left", fill="y")
        self.lbl_grayR = tk.Label(self.frm2, text="gray", bg="gray", fg="white", padx=25)
        self.lbl_grayR.pack(side="right", fill="y")
        self.lbl_black = tk.Label(self.frm2, text="black", bg="black", fg="white")
        self.lbl_black.pack(side="bottom", fill="both", expand=1)


        self.frm2_1 = tk.Frame(self.frm2, bg="red")
        self.frm2_1.pack(side="top", fill="both")

        self.lbl_cyan = tk.Label(self.frm2_1, text="cyan", bg="cyan", fg="black", pady=15)
        self.lbl_cyan.pack( side="left", fill="both", expand=1)
        self.lbl_yellow = tk.Label(self.frm2_1, text="yellow", bg="yellow", fg="black", pady=15)
        self.lbl_yellow.pack(side="right", fill="both", expand=1)
        self.lbl_magenta = tk.Label(self.frm2_1, text="magenta", bg="magenta", fg="black", pady=15, padx=19)
        self.lbl_magenta.pack(side="top", fill="both", expand=1)

gui = tk.Tk()
GerenciadorPack(gui)
gui.mainloop()