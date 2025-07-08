import tkinter as tk
from datetime import date

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("400x350")

        self.lbl_nome = tk.Label(self.janela, text="Nome: ").pack()
        self.ent_nome = tk.Entry(self.janela)
        self.ent_nome.pack()

        self.lbl_ano_nas = tk.Label(self.janela, text="Ano de nascimento: ").pack()
        self.ent_ano_nas = tk.Entry(self.janela)
        self.ent_ano_nas.pack()

        self.lbl_mes_nas = tk.Label(self.janela, text="Mês de nascimento: ").pack()
        self.ent_mes_nas = tk.Entry(self.janela)
        self.ent_mes_nas.pack()

        self.lbl_dia_nas = tk.Label(self.janela, text="Dia de nascimento: ").pack()
        self.ent_dia_nas = tk.Entry(self.janela)
        self.ent_dia_nas.pack()

        self.bnt_calcular =tk.Button(self.janela, text="Calcular Idade", command=self.calcular_idade).pack()

        self.lbl_idade = tk.Label(self.janela, text="T")
        self.lbl_idade.pack()

    def calcular_idade(self):
        dia = date.today().day
        mes = date.today().month
        ano = date.today().year

        try:
            dia_nas = int(self.ent_dia_nas.get())
            mes_nas = int(self.ent_mes_nas.get())
            ano_nas = int(self.ent_ano_nas.get())
        except ValueError as va:
            self.lbl_idade["text"] = "Digite apenas valores numéricos!"

        anos = ano - ano_nas
        meses = mes - mes_nas
        dias = dia - dia_nas

        if(dias < 0):
            meses -= 1
            dias += 30

        if(meses < 0):
            anos -= 1
            meses += 12

        self.lbl_idade["text"] = f"Idade: {anos} anos, {meses} meses e {dias} dias ou {(date.today() - date(ano_nas, mes_nas, dia_nas)).days} dias"

gui = tk.Tk()
tela = Tela(gui)
tela.janela.mainloop()