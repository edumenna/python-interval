class Pilha(object):

    def __init__(self) -> None:
        self.pilha = []

    def empilha(self, valor):
        self.pilha.append(valor)

    def desempilha(self):
        return self.pilha.pop(-1)

    def pilha_vazia(self):
        if len(self.pilha) == 0:
            return True
        return False

    def pilha_tamanho_1(self):
        return len(self.pilha) == 1

    def pilha_tamanho_2_ou_mais(self):
        return len(self.pilha) > 1

    def limpa_pilha(self):
        return self.pilha.clear()

    def imprime_pilha(self):
        print("Pilha: ",self.pilha)

    def mostra_topo(self):
        return self.pilha[-1]