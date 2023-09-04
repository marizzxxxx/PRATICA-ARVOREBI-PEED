class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)
#A
    def altura(self):
        return self.calcula_altura(self.raiz)

    def calcula_altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self.calcula_altura(no.esquerda)
        altura_direita = self.calcula_altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def contar_nos(self):
        return self.conta_nos_recursivo(self.raiz)

    def conta_nos_recursivo(self, no):
        if no is None:
            return 0
        return 1 + self.conta_nos_recursivo(no.esquerda) + self.conta_nos_recursivo(no.direita)

    def contar_folhas(self):
        return self.conta_folhas_recursivo(self.raiz)

    def conta_folhas_recursivo(self, no):
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        return self.conta_folhas_recursivo(no.esquerda) + self.conta_folhas_recursivo(no.direita)

    def buscar(self, valor):
        return self.buscar_recursivo(valor, self.raiz)

    def buscar_recursivo(self, valor, no):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self.buscar_recursivo(valor, no.esquerda)
        else:
            return self.buscar_recursivo(valor, no.direita)

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        if no is not None:
            print(no.valor, end=" ")
            self.mostrar_pre_ordem_recursivo(no.esquerda)
            self.mostrar_pre_ordem_recursivo(no.direita)

#T

arvore = ArvoreBinaria()
numeros = [50, 30, 70, 20, 40, 60, 80]

for numero in numeros:
    arvore.inserir_em_nivel(numero)

print("\nAltura:", arvore.altura())
print("Nós internos:", arvore.contar_nos() - arvore.contar_folhas())
print("Folhas:", arvore.contar_folhas())

numero_a_buscar = 6
if arvore.buscar(numero_a_buscar):
    print(f"{numero_a_buscar} está na árvore.")
else:
    print(f"{numero_a_buscar} não está na árvore.")

print("\nPre-ordem:")
arvore.mostrar_pre_ordem()