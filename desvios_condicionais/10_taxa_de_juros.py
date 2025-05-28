# A taxa de juros aplicada em fundos depositados em um banco é determinada pelo tempo em que estes ficam depositados. Para um banco em particular, a seguinte tabela é usada:

# Tempo em depósito                                  Taxa de juros
# Maior ou igual a 5 anos                                0,95
# Menor que 5 anos mas maior ou igual a 4 anos           0,90
# Menor que 4 anos mas maior ou igual a 3 anos           0,85
# Menor que 3 anos mas maior ou igual a 2 anos           0,75
# Menor que 2 anos mas maior ou igual a 1 ano            0,65
# Menor que 1 ano                                        0,55

# Usando esta informação, escreva um programa que receba o tempo em que os fundos foram mantidos em depósito e informe a taxa de juros correspondente.


tempo = int(input('Digite o tempo que o dinheiro está em depósito: '))

if tempo >= 5:
    taxa = 0.95
elif tempo >= 4:
    taxa = 0.90
elif tempo >= 3:
    taxa = 0.85
elif tempo >= 2:
    taxa = 0.75
elif tempo >= 1:
    taxa = 0.65
else:
    tempo < 1
    taxa = 0.55

print(f'Seu dinheiro possui uma taxa de juros de {taxa}.')

