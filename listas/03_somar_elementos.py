# Escrever uma função que recebe por parâmetro um vetor de inteiros e retorna a soma de seus elementos.

def somador_de_vetor(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    # Aqui, eu poderia usar a função embutida 'sum' para somar todos os elementos de um vetor.
    # return sum(numeros)
    return soma


vetor = [2, 4, 6, 8, 10]

print(f'Soma dos números do vetor: {somador_de_vetor(vetor)}')