# Implemente uma função que retorne o maior elemento de um vetor de inteiros. 
# Implemente uma função que retorne o menor elemento de um vetor de inteiros.
# Implemente uma função que ordene um vetor de inteiros de tamanho 10.

# Função para retornar o maior elemento de um vetor:

def retornar_maior_elemento(numeros):     
    maior_elemento = numeros[0]     # [0] é o primeiro elemento do vetor.
    for i in range(len(numeros)):
        if numeros[i] > maior_elemento:
            maior_elemento = numeros[i]
    return maior_elemento


# Função para retornar o menor elemento de um vetor:

def retornar_menor_elemento(numeros):
    menor_elemento = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] < menor_elemento:
            menor_elemento = numeros[i]
    return menor_elemento


# Função para ordenar um vetor de inteiros de tamanho 10:

def ordenar_vetor(numeros):
    for i in range(len(numeros)):
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[i]:
                var_temp = vetor[j]
                vetor[j] = vetor[i]
                vetor[i] = var_temp
    # No Python, eu poderia simplesmente usar a função embutida 'sort' para ordenar um vetor.
    # return sort(vetor)
    return vetor

# Programa: 

vetor = []

while True:
    numero = int(input('Adicione valores inteiro para o vetor (Pressione 0 para finalizar): '))
    if numero == 0:
        break
    vetor.append(numero)

print(f'Vetor: {vetor}')
print(f'Vetor ordenado: {ordenar_vetor(vetor)}')
print(f'O menor elemento do vetor é {retornar_menor_elemento(vetor)}')
print(f'O maior elemento do vetor é {retornar_maior_elemento(vetor)}')
