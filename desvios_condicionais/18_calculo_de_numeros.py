# Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos, calcule e imprima: a média dos números caso a soma deles for menor que 8, seu produto caso a soma seja igual a 8 ou a divisão do maior pelo menor caso a soma dos valores for maior que 8.

numero1 = float(input('Digite o número 1 (entre 1 e 10): '))
if numero1 < 1 or numero1 > 10:
    print('Número inválido')
    exit()
else:
    numero2 = float(input('Digite o número 2 (entre 1 e 10): '))
    if numero2 < 1 or numero2 > 10:
        print('Número inválido')
        exit()
    else:
        if numero1 + numero2 < 8:
            print(f'A média dos números é {(numero1 + numero2) / 2}')
        elif numero1 + numero2 == 8:
            print(f'O produto dos números é {numero1 * numero2}')
        else:
            menor = numero1 if numero1 < numero2 else numero2
            maior = numero1 if numero1 > numero2 else numero2
            print(f'A divisão é {maior / menor}')