from interval import interval
import matematica_intervalar

class Financiamento(object):

    def __init__(self):
        pass

    def __init__(self, n, i, pv, pmt, fv):
        self.n = n
        self.i = i
        self.pv = pv
        self.pmt = pmt
        self.fv = fv

    def transforma_em_porcentagem(self):
        return self.i / 100

    def coeficiente_de_financiamento(self):
        i = self.transforma_em_porcentagem()
        return i / (1 - (1 / matematica_intervalar.calcula_potencia((1 + i), self.n)))

    # botao da calculadora
    def calcula_parcela(self):
        return self.coeficiente_de_financiamento() * self.pv

    # botao de valor futuro
    def calcula_valor_futuro(self):
        i = self.transforma_em_porcentagem()
        return self.pv * ( matematica_intervalar.calcula_potencia((1 + i), self.n) )

    # botao de valor presente
    def calcula_valor_presente(self):
        i = self.transforma_em_porcentagem()
        return self.fv / ( matematica_intervalar.calcula_potencia((1 + i), self.n) )

    # botao taxa de juros compostos
    def calcula_taxa_juros_compostos(self):
        return (matematica_intervalar.calcula_raiz(self.fv/-self.pv, self.n) - 1) * 100

    # botao do i (tempo)
    def calcula_tempo(self):
        i = self.transforma_em_porcentagem()

        dividendo = matematica_intervalar.calcula_log(self.fv/-self.pv)
        divisor = matematica_intervalar.calcula_log(1 + i)

        return dividendo / divisor
        
    def eh_para_calcular_n(self):
        if self.i is not None and self.pv is not None and self.fv is not None:
            return True
        return False

    def eh_para_calcular_i(self):
        if self.n is not None and self.pv is not None and self.fv is not None:
            return True
        return False

    def eh_para_calcular_pv(self):
        if self.n is not None and self.i is not None and self.fv is not None:
            return True
        return False

    def eh_para_calcular_fv(self):
        if self.n is not None and self.i is not None and self.pv is not None:
            return True
        return False

    def eh_para_calcular_pmt(self):
        if self.n is not None and self.i is not None and self.pv is not None:
            return True
        return False

#print(calcula_pmt(interval[36],interval[3,4],interval[40000])) #OK
#print(calcula_valor_futuro(interval[12], interval[2], interval[15000])) #OK
#print(calcula_valor_presente(interval[7], interval[2.5], interval[37443.60])) #OK
#print(calcula_taxa_juros_compostos(interval[5], interval[-42000], interval[45245.93])) #OK
#print(calcula_tempo(interval[3], interval[-12500], interval[15834.63])) #OK

#finc = Financiamento(None, interval[1], interval[-1000], None, interval[2000]) #OK
#print(finc.calcula_tempo())
