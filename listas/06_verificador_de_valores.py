# Implemente uma função que, dado um valor, retorne se esse valor pertence ou não a um vetor de inteiros.


def verificador_de_valores(vetor, valor):
    achou = 'Não'     # False
    for i in range(len(vetor)):
        if vetor[i] == valor:
            achou = 'Sim'     # True
    return achou

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(verificador_de_valores(vetor, 5))
print(verificador_de_valores(vetor, 11))
print(verificador_de_valores(vetor, 7))