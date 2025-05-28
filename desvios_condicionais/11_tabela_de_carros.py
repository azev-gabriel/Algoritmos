# Baseado no ano e peso do modelo de um automóvel, o estado de Nova Jersey determina a sua classe de peso e taxa de registro usando uma tabela... Usando as informações, escreva um programa que receba o ano e o peso do modelo de um automóvel e calcule e imprima a classe de peso e a taxa de registro para o carro.

ano = int(input('Digite o ano do carro: '))
peso = int(input('Digite o peso do modelo: '))

if ano <= 1970:
    if peso < 1200:
        classe = 1
        taxa = 16.50
    elif peso >= 1200 and peso <= 1700:
        classe = 2
        taxa = 26.50
    else:
        classe = 3
        taxa = 46.50

if ano >= 1971 and ano <= 1979:
    if peso < 1200:
        classe = 4
        taxa = 27.00
    elif peso >= 1200 and peso <= 1700:
        classe = 5
        taxa = 30.50
    else:
        classe = 6
        taxa = 52.50

if ano >= 1980:
    if peso < 1600:
        classe = 7
        taxa = 19.50
    else:
        classe = 8
        taxa = 55.50

print(f'Classe de peso: {classe}')
print(f'Taxa de registro: {taxa}')