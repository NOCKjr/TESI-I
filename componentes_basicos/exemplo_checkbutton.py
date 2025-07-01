import tkinter as tk

class Tela:

    def clicou(self):
        if(self.var_cbt1.get() and self.var_cbt2.get()):
            self.lbl_mostrar["text"] = "Empatou"
        elif(self.var_cbt1.get()):
            self.lbl_mostrar["text"] = "Flamengo"
        elif(self.var_cbt2.get()):
            self.lbl_mostrar["text"] = "Bayern"
        else:
            self.lbl_mostrar["text"] = "Aposte!"

    def __init__(self, master):
        self.janela = master
        self.janela.geometry("300x300")

        self.var_cbt1 = tk.IntVar()
        self.cbt1 = tk.Checkbutton(self.janela, text = "Flamengo", variable = self.var_cbt1)
        self.cbt1.pack()

        self.var_cbt2 = tk.IntVar()
        self.cbt2 = tk.Checkbutton(self.janela, text = "Bayern", variable = self.var_cbt2)
        self.cbt2.pack()

        self.bnt = tk.Button(self.janela, text="confirmar", command = self.clicou)
        self.bnt.pack()

        self.lbl_mostrar = tk.Label(self.janela)
        self.lbl_mostrar.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()