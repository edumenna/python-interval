from tkinter import *
from pilha import Pilha
from hp_funcoes import Financiamento
from operacao import Operacao
import intervalar as intervalar

class Application:
    def __init__(self, master=None):
        self.pilha = Pilha()
        self.op_basica = Operacao()
        self.financiamento = Financiamento(None,None,None,None,None)
        self.f = False
        self.g = False
        
        self.monta_interface(master)

    def monta_interface(self, master):
        self.define_titulo(master)

        self.cria_frame1(master)
        self.cria_frame2(master)
        self.cria_frame3(master)
        self.cria_frame4(master)
        self.cria_frame5(master)

    def cria_frame1(self, master):
        self.frame1 = Frame(master)
        self.monta_frame1()
        self.frame1.pack()

    def cria_frame2(self, master):
        self.frame2 = Frame(master)
        self.monta_frame2()        
        self.frame2.pack()

    def cria_frame3(self, master):
        self.frame3 = Frame(master)
        self.monta_frame3()
        self.frame3.pack()

    def cria_frame4(self, master):
        self.frame4 = Frame(master)
        self.monta_frame4()
        self.frame4.pack()

    def cria_frame5(self, master):
        self.frame5 = Frame(master)
        self.monta_frame5()
        self.frame5.pack()

    def monta_frame1(self):
        self.display_auxiliar = Label(self.frame1, text="")
        self.display_auxiliar.grid(row=0,column=5)
        self.display = Label(self.frame1, text="0.00", fg="black", bg="white", width=35)
        self.display.grid(row=0,column=6, columnspan=4, padx=5, pady=5)

    def monta_frame2(self):
        linha = 1 
        self.cria_botao(self.frame2, "n", linha, 0, self.bt_n)
        self.cria_botao(self.frame2, "i", linha, 1, self.bt_i)
        self.cria_botao(self.frame2, "PV", linha, 2, self.bt_pv)
        self.cria_botao(self.frame2, "PMT", linha, 3, self.bt_pmt)
        self.cria_botao(self.frame2, "FV", linha, 4, self.bt_fv)
        self.cria_botao(self.frame2, "CHS", linha, 5, self.troca_sinal)
        self.cria_botao(self.frame2, "7", linha, 6, self.concatena_7)
        self.cria_botao(self.frame2, "8", linha, 7, self.concatena_8)
        self.cria_botao(self.frame2, "9", linha, 8, self.concatena_9)
        self.cria_botao(self.frame2, "/", linha, 9, self.divisao)

    def monta_frame3(self):
        linha = 2 
        self.cria_botao(self.frame3, "x^y", linha, 0, "")
        self.cria_botao(self.frame3, "1/x", linha, 1, self.divide_1_por_x)
        self.cria_botao(self.frame3, "%T", linha, 2, "")
        self.cria_botao(self.frame3, "DD%", linha, 3, "")
        self.cria_botao(self.frame3, "%", linha, 4, "")
        self.cria_botao(self.frame3, "EEX", linha, 5, "")
        self.cria_botao(self.frame3, "4", linha, 6, self.concatena_4)
        self.cria_botao(self.frame3, "5", linha, 7, self.concatena_5)
        self.cria_botao(self.frame3, "6", linha, 8, self.concatena_6)
        self.cria_botao(self.frame3, "x", linha, 9, self.multiplicacao)

    def monta_frame4(self):
        linha = 3
        self.cria_botao(self.frame3, "R/S", linha, 0, "")
        self.cria_botao(self.frame3, "SST", linha, 1, "")
        self.cria_botao(self.frame3, "Rv", linha, 2, "")
        self.cria_botao(self.frame3, "x<>y", linha, 3, "")
        self.cria_botao(self.frame3, "CLX", linha, 4, self.limpa_display_e_ou_pilha)
        self.cria_botao(self.frame3, "IVAL", linha, 5, self.cria_intervalo)
        self.cria_botao(self.frame3, "1", linha, 6, self.concatena_1)
        self.cria_botao(self.frame3, "2", linha, 7, self.concatena_2)
        self.cria_botao(self.frame3, "3", linha, 8, self.concatena_3)
        self.cria_botao(self.frame3, "-", linha, 9, self.subtracao)
        
    def monta_frame5(self):
        linha = 4
        self.cria_botao(self.frame3, "ONOFF", linha, 0, self.reset)
        self.cria_botao(self.frame3, "f", linha, 1, self.ativa_desativa_tecla_f)
        self.cria_botao(self.frame3, "g", linha, 2, "")
        self.cria_botao(self.frame3, "STO", linha, 3, "")
        self.cria_botao(self.frame3, "RCL", linha, 4, "")
        self.cria_botao(self.frame3, "ENT", linha, 5, self.tecla_enter)
        self.cria_botao(self.frame3, "0", linha, 6, self.concatena_0)
        self.cria_botao(self.frame3, ".", linha, 7, self.concatena_ponto)
        self.cria_botao(self.frame3, "S+", linha, 8, "")
        self.cria_botao(self.frame3, "+", linha, 9, self.soma)

    def cria_botao(self, frame, label, linha, coluna, metodo):
        botao = Button(frame, text=label, command=metodo)
        botao.grid(padx=5, pady=5, row=linha, column=coluna)
        botao.config(width=4)

    def define_titulo(self, master):
        master.title("HP12C")

    def le_display(self):
        return self.display["text"]
        #return self.converte_para_float(self.display["text"])

    def imprime_display(self, valor):
        try:
            self.display["text"] = str(valor)
        except:
            pass

    def tecla_enter(self):
        self.pilha.empilha(self.converte_para_float(self.display["text"]))
        self.limpa_display()
        self.pilha.imprime_pilha()

    def reset(self):
        self.pilha = Pilha()
        self.op_basica = Operacao()
        self.financiamento = Financiamento(None,None,None,None,None)
        self.f = False
        self.g = False

    def converte_para_float(self, valor_display):
        try:
            return float(valor_display)
        except:
            pass

    def limpa_display(self):
        self.display["text"] = "0.00"

    def limpa_display_e_ou_pilha(self):
        if self.f is True:
            self.pilha.limpa_pilha()
            self.f = False
            self.display_auxiliar["text"] = ""
        self.limpa_display()

    def ativa_desativa_tecla_f(self):
        if self.f is True:
            self.f = False
            self.display_auxiliar["text"] = ""
        else:    
            self.f = True
            self.display_auxiliar["text"] = "f"

    def eh_primeira_digitacao(self):
        return self.display["text"] == "0.00"

    def concatena(self, valor):
        if self.eh_primeira_digitacao():
            self.display["text"] = str(valor)
        else:
            self.display["text"] += str(valor)

    def concatena_0(self):
        self.concatena(0)

    def concatena_1(self):
        self.concatena(1)
        
    def concatena_2(self):
        self.concatena(2)
        
    def concatena_3(self):
        self.concatena(3)

    def concatena_4(self):
        self.concatena(4)

    def concatena_5(self):
        self.concatena(5)

    def concatena_6(self):
        self.concatena(6)

    def concatena_7(self):
        self.concatena(7)

    def concatena_8(self):
        self.concatena(8)

    def concatena_9(self):
        self.concatena(9)

    def concatena_ponto(self):
        if self.eh_primeira_digitacao():
            self.display["text"] = "."
        else:
            if "." not in self.display["text"]: 
                self.display["text"] += "."

    def bt_n(self):
        if self.financiamento.eh_para_calcular_n():
            self.display["text"] = self.financiamento.calcula_tempo()
        else:
            self.financiamento.n = self.pilha.desempilha()
            print(self.financiamento.n)

    def bt_i(self):
        if self.financiamento.eh_para_calcular_i():
            self.display["text"] = self.financiamento.calcula_taxa_juros_compostos()
        else:
            self.financiamento.i = self.pilha.desempilha()
            print(self.financiamento.i)

    def bt_pv(self):
        if self.financiamento.eh_para_calcular_pv():
            self.display["text"] = self.financiamento.calcula_valor_presente()
        else:
            self.financiamento.pv = self.pilha.desempilha()
            print(self.financiamento.pv)

    def bt_pmt(self):
        if self.financiamento.eh_para_calcular_pmt():
            self.display["text"] = self.financiamento.calcula_parcela()
        else:
            self.financiamento.pmt = self.pilha.desempilha()
            print(self.financiamento.pmt)
    
    def bt_fv(self):
        if self.financiamento.eh_para_calcular_fv():
            self.display["text"] = self.financiamento.calcula_valor_futuro()
        else:
            self.financiamento.fv = self.pilha.desempilha()
            print(self.financiamento.fv)

    def cria_intervalo(self):
        intervalar.Intervalar(self.pilha)
        self.display["text"] = self.pilha.mostra_topo()

    def troca_sinal(self):
        self.display["text"] = self.op_basica.troca_sinal(self.display["text"])

    def soma(self):
        self.imprime_display(self.op_basica.soma(self.pilha, self.le_display()))
    
    def subtracao(self):
        self.imprime_display(self.op_basica.subtracao(self.pilha, self.le_display()))
    
    def multiplicacao(self):
        self.imprime_display(self.op_basica.multiplicacao(self.pilha, self.le_display()))

    def divisao(self):
        self.imprime_display(self.op_basica.divisao(self.pilha, self.le_display()))

    def divide_1_por_x(self):
        self.imprime_display(self.op_basica.divide_1_por_x(self.pilha, self.le_display()))