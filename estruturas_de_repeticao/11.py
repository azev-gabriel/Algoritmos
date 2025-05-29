# Escrever um algoritmo que leia um número não determinado de valores e calcule a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos. Mostre os resultados.


contador_valores = 0
contador_positivos = 0
contador_negativos = 0

valor = int(input('Digite um valor (positivo ou negativo): '))

while valor != 0:
    contador_valores += 1
    if valor > 0:
        contador_positivo += 1
    if valor < 0:
        contador_negativo += 1
    
    