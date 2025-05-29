# Escrever o algoritmo que leia os valores n1 e n2 e imprima o intervalo fechado (incluindo os limites) entre esses dois valores.


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n2 < n1:
    print('O primeiro valor é maior que o segundo. Portando serão alternados.')

    troca = n2
    n2 = n1
    n1 = troca

for i in range(n1, n2 + 1):
    print(i)