# Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores são negativos.

# Função: 
def contar_negativos(numeros):
    contador_de_negativos = 0
    for i in range(len(numeros)):     # 'len' é uma função embutida que retorna o número de elementos de um vetor.
        if numeros[i] < 0:     # 'if numeros[i] é igual a: Se o número do índice atual...
            contador_de_negativos += 1
    return contador_de_negativos


# Programa:
numeros = []

for i in range(10):     # Loop de exatos 10 números.
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print(f'Dos valores digitados, {contar_negativos(numeros)} são negativos.')



# Se eu quisesse usar uma lista ao invés de um contador, eu poderia fazer isso:

def contar_negativos(numeros):
    contador_de_negativos = []     # 'contador_de_negativos' é criado como uma lista;
    for i in range(len(numeros)):
        if numeros[i] < 0:
            contador_de_negativos.append(numeros[i])   # 'append' para adicionar o valor na lista.
    return contador_de_negativos


# Programa:
numeros = []

for i in range(10):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print(f'Dos valores digitados, {contar_negativos(numeros)} são negativos.')