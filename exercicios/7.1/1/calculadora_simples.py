import tkinter as tk

class CalculadoraSimples:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("455x520")

        self.frm_visor = tk.Frame(self.janela, padx=13, pady=13)
        self.frm_visor.pack(fill="x")
        self.ent = tk.Entry(self.frm_visor, bd=7)
        self.ent.pack(fill="x")

        self.frm_botoes = tk.Frame(self.janela, pady=3, padx=5)
        self.frm_botoes.pack(fill="both", expand=1, side="top")

        self.botoes = [['7', '8', '9', '+'], ['4', '5', '6', '-'], ['1', '2', '3', '*'], ['0', '.', 'C', '/']]

        for i in range(4):
            for j in range(4):
                btn = tk.Button(self.frm_botoes, text=self.botoes[i][j], width=10, height=4)
                btn.grid(row=i, column=j)

        self.bnt = tk.Button(self.frm_botoes, text="=", bg="green", height=4, width=52, fg="white")
        self.bnt.grid(row=4, columnspan=4)

gui = tk.Tk()
CalculadoraSimples(gui)
gui.mainloop()