# Implemente uma função que retorne a média dos valores armazenados em um vetor de inteiros.


def media(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
        if len(vetor) == 0:
            return 0
        else:
            media = soma / len(vetor)
    return media

vetor = [2, 4, 8, 14, 20, 26, 32, 38, 44, 50]
print(f'A média do dos valores do vetor é = {media(vetor)}')