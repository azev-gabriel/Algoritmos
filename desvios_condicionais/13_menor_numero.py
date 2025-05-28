# Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numero4 = int(input('Digite o quarto número: '))

if numero1 < numero2:
    menor = numero1
else:
    menor = numero2
if numero3 < menor:
    menor = numero3
if numero4 < menor:
    menor = numero4

print(f'O menor número é {menor}.')