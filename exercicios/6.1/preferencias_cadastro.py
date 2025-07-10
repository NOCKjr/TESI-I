import tkinter as tk

class Preferencias_cadastro:
    def __init__(self, master):

        self.janela = master
        self.janela.geometry("400x350")

        self.lbl_radio = tk.Label(self.janela, text="Aceita receber conteúdo por email?").pack()

        self.var_rbt = tk.IntVar()

        tk.Radiobutton(self.janela, text="Sim", value=1, variable=self.var_rbt, command=self.n).pack()

        tk.Radiobutton(self.janela, text="Não", value=0, variable=self.var_rbt, command=self.n).pack()


        self.lbl_check = tk.Label(self.janela, text="Escolha as opções de conteúdo")

        self.var_cbt0 = tk.IntVar()  # Teoria da Computação
        self.var_cbt1 = tk.IntVar()  # Desenvolvimento e Engenharia de Software
        self.var_cbt2 = tk.IntVar()  # Desenvolvimento Web e Mobile
        self.var_cbt3 = tk.IntVar()  # IA e Data Science
        self.var_cbt4 = tk.IntVar()  # Segurança da Informação
        self.var_cbt5 = tk.IntVar()  # IoT

        self.cbt0 = tk.Checkbutton(self.janela, text="Teoria da Computação", variable=self.var_cbt0)

        self.cbt1 = tk.Checkbutton(self.janela, text="Desenvolvimento e Engenharia de Software", variable=self.var_cbt1)

        self.cbt2 = tk.Checkbutton(self.janela, text="Desenvolvimento Web e Mobile", variable=self.var_cbt2)

        self.cbt3 = tk.Checkbutton(self.janela, text="IA e Data Science", variable=self.var_cbt3)

        self.cbt4 = tk.Checkbutton(self.janela, text="Segurança da Informação", variable=self.var_cbt4)

        self.cbt5 = tk.Checkbutton(self.janela, text="IoT", variable=self.var_cbt5)

    def n(self):
        if(self.var_rbt.get()):

            self.lbl_check.pack()
            self.cbt0.pack()
            self.cbt1.pack()
            self.cbt2.pack()
            self.cbt3.pack()
            self.cbt4.pack()
            self.cbt5.pack()
        else:
            # destroy: apaga o elemento da memória
            # pack_forget: apenas faz com que não seja exibido,
            # mas continua na memória e pode reaparecer
            self.lbl_check.pack_forget()
            self.cbt0.pack_forget()
            self.cbt1.pack_forget()
            self.cbt2.pack_forget()
            self.cbt3.pack_forget()
            self.cbt4.pack_forget()
            self.cbt5.pack_forget()

# gui = tk.Tk()
# Preferencias_cadastro(gui)
# gui.mainloop()