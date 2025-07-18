import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text = 'Abrir Toplevel', command=self.abrir_toplevel)
        self.btn.pack()

    def abrir_toplevel(self):
        #self.janela.withdraw()#iconify()
        def fechar():
            segunda_janela.destroy()
            self.janela.deiconify()

        self.janela.withdraw()
        segunda_janela = tk.Toplevel(self.janela)
        segunda_janela.grab_set()
        self.btn_sair = tk.Button(segunda_janela, text='Fechar janela',command=fechar)
        self.btn_sair.pack()



gui = tk.Tk()
Tela(gui)
gui.mainloop()