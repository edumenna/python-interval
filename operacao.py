from pilha import Pilha

class Operacao(object):

    def __init__(self) -> None:
        pass    
    
    def soma(self, obj_pilha, valor_display):
        if Pilha.pilha_tamanho_1(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            return ultimo + float(valor_display)
        elif Pilha.pilha_tamanho_2_ou_mais(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            penultimo = Pilha.desempilha(obj_pilha)
            return ultimo + penultimo

    def subtracao(self, obj_pilha, valor_display):
        if Pilha.pilha_tamanho_1(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            return ultimo - valor_display
        elif Pilha.pilha_tamanho_2_ou_mais(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            penultimo = Pilha.desempilha(obj_pilha)
            return penultimo - ultimo

    def multiplicacao(self, obj_pilha, valor_display):
        if Pilha.pilha_tamanho_1(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            return ultimo * valor_display
        elif Pilha.pilha_tamanho_2_ou_mais(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            penultimo = Pilha.desempilha(obj_pilha)
            return penultimo * ultimo

    def divisao(self, obj_pilha, valor_display):
        if Pilha.pilha_tamanho_1(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            return ultimo / valor_display
        elif Pilha.pilha_tamanho_2_ou_mais(obj_pilha):
            ultimo = Pilha.desempilha(obj_pilha)
            penultimo = Pilha.desempilha(obj_pilha)
            return penultimo / ultimo

    def divide_1_por_x(self, obj_pilha, valor_display):
        if Pilha.pilha_vazia(obj_pilha):
            ultimo = valor_display
        else:
            ultimo = Pilha.desempilha(obj_pilha)
        return 1 / ultimo

    def eh_negativo(self, valor):
        return valor < 0

    def troca_sinal(self, valor):
        valor = float(valor)
        if type(valor) is str:
            if self.eh_negativo(valor):
                valor = valor[:1]
            else:
                valor = "-" + valor
        else:
            valor = valor * (-1)
        return str(valor)