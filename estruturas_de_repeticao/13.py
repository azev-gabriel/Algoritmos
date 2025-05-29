# Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.

contador_valores = 0
contador_pares = 0
contador_impares = 0
soma_pares = 0
soma_valores = 0

while True:
    valor = int(input('Digite um valor POSITIVO: : '))
    
    if valor == 0:
        print('PROGRAMA ENCERRADO.')
        break

    if valor % 2 == 0:         # Isso significa que se um valor dividido por 2 da resto 0, ele é par.
        contador_pares += 1
    else:
        contador_impares += 1

    soma_pares = soma_pares + valor
    media_pares = soma_pares / contador_pares

    soma_valores = soma_valores + valor
    media_valores = soma_valores / contador_valores



    print(contador_pares)
    print(contador_impares)
    print(media_pares)
    print(media_valores)