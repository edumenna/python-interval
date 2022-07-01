from interval import interval
import math

def calcula_potencia(numero, potencia):
    pot_inf = 1
    pot_sup = 1
    i = 0
    
    while i < potencia[0].inf:
        pot_inf = pot_inf * numero
        i   = i + 1
    
    i = 0

    while i < potencia[0].sup:
        pot_sup = pot_sup * numero
        i   = i + 1

    return interval[pot_inf, pot_sup]

def calcula_raiz(numero, radical):
    ref = 1 / radical
    inf = pow(numero[0].inf,ref[0].inf)
    sup = pow(numero[0].sup,ref[0].sup)

    return interval[inf,sup]

def calcula_log(numero):
    inf = math.log(numero[0].inf)
    sup = math.log(numero[0].sup)

    return interval[inf,sup]