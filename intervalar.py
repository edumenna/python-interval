import pilha as p 
from interval import interval
import matematica_intervalar

class Intervalar:

    def __init__(self, obj_pilha):

        if p.Pilha.pilha_tamanho_1(obj_pilha):
            intervalo = interval[p.Pilha.desempilha(obj_pilha)]
        elif p.Pilha.pilha_tamanho_2_ou_mais(obj_pilha):
            ultimo = p.Pilha.desempilha(obj_pilha)
            penultimo = p.Pilha.desempilha(obj_pilha)
            if type(penultimo) is interval:
                p.Pilha.empilha(obj_pilha, penultimo)
                intervalo = interval[ultimo]
            else:
                intervalo = interval[penultimo,ultimo]
        p.Pilha.empilha(obj_pilha, intervalo)
        print("intervalo: ", intervalo)
        p.Pilha.imprime_pilha(obj_pilha)

    def transforma_em_porcentagem(valor):
        return valor / 100

    def coeficiente_de_financiamento(self, n, i):
        i = self.transforma_em_porcentagem(i)
        return i / (1 - (1 / matematica_intervalar.calcula_potencia((1 + i),n)))

    # botao da calculadora
    def calcula_pmt(self, n, i, pv):
        return self.coeficiente_de_financiamento(n, i) * pv


    # botao de valor futuro
    def calcula_valor_futuro(self, n, i, pv):
        i = self.transforma_em_porcentagem(i)
        return pv * ( matematica_intervalar.calcula_potencia((1 + i),n) )

    # botao de valor presente
    def calcula_valor_presente(self, n, i, fv):
        i = self.transforma_em_porcentagem(i)
        return fv / ( matematica_intervalar.calcula_potencia((1 + i),n) )

    # botao taxa de juros compostos
    def calcula_taxa_juros_compostos(n, pv, fv):
        return (matematica_intervalar.calcula_raiz(fv/-pv, n) - 1) * 100

    # botao do i (tempo)
    def calcula_tempo(self, i, pv, fv):
        i = self.transforma_em_porcentagem(i)

        dividendo = matematica_intervalar.calcula_log(fv/-pv)
        divisor = matematica_intervalar.calcula_log(1 + i)

        return dividendo / divisor