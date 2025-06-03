# Escrever um algoritmo que gere e escreva os 3 primeiros números perfeitos. Um número perfeito é aquele que é igual a soma dos seus divisores. (Ex.: 6 = 1+2+3; 28= 1+2+4+7+14, etc).


contador_perfeito = 0
inicio = 1

while contador_perfeito < 3:
    soma_divisor = 0

    for i in range(1, inicio):
        if inicio % i == 0:
            soma_divisor += i

    if soma_divisor == inicio:
        print(f'Número perfeito: {inicio}')
        contador_perfeito += 1
    inicio += 1