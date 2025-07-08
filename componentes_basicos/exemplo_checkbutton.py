import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x300')
        self.var_cbt1 = tk.IntVar()
        self.var_cbt2 = tk.IntVar()
        self.cbt1 = tk.Checkbutton(self.janela, text='Flamengo', variable=self.var_cbt1)
        self.cbt2 = tk.Checkbutton(self.janela, text='Bayern', variable=self.var_cbt2)
        self.btn_enviar = tk.Button(self.janela, text='Enviar', command=self.verificar)
        self.lbl_mostrar = tk.Label(self.janela)

        self.cbt1.pack()
        self.cbt2.pack()
        self.btn_enviar.pack()
        self.lbl_mostrar.pack()



    def verificar(self):
        if self.var_cbt1.get() and self.var_cbt2.get():
            self.lbl_mostrar.config(text='Flamengo e Bayern')
        elif self.var_cbt1.get():
            self.lbl_mostrar.config(text='Flamengo')
        elif self.var_cbt2.get():
            self.lbl_mostrar.config(text='Bayern')
        else:
            self.lbl_mostrar.config(text='Nenhum')

gui = tk.Tk()
Tela(gui)
gui.mainloop()