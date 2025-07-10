import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        
        
        
        self.lbl_login = tk.Label(self.janela, text='Login:')
        self.lbl_login.grid(row=0, column=0)
        self.ent_login = tk.Entry(self.janela, width=20)
        self.ent_login.grid(row=0, column=1)

        self.lbl_senha = tk.Label(self.janela, text='Senha:')
        self.lbl_senha.grid(row=1, column=0)
        self.ent_senha = tk.Entry(self.janela, width=20, show='º')
        self.ent_senha.grid(row=1, column=1)

        self.bnt_enviar = tk.Button(self.janela, text="enviar")
        self.bnt_enviar.grid(row=2, column=0, sticky="we")

        self.bnt_enviar = tk.Button(self.janela, text="limpar")
        self.bnt_enviar.grid(row=2, column=1, columnspan=2, sticky="we")
        # self.bnt_enviar.grid(row=2, column=1, columnspan=2, sticky="we")

gui = tk.Tk()
Tela(gui)
gui.mainloop()