# Uma encomenda de unidades de disco contém unidades marcadas com um código de 1 a 4, que indica o tipo seguinte:

# Código        Tipo da unidade
# 1             CD-ROM (700MB)
# 2             DVD-ROM (4.7GB)
# 3             DVD-9 (8.54 GB)
# 4             Blu-Ray (25 GB)

# Escreva um programa que receba o número de um código como entrada e, baseado no valor digitado, informe o tipo correto de unidade de disco.

codigo = int(input('Digite um código de 1 a 4: '))

if codigo == 1:
    tipo = 'CD-ROM (700MB)'
elif codigo == 2:
    tipo = 'DVD-ROM (4.7GB)'
elif codigo == 3:
    tipo = 'DVD-9 (8.54 GB)'
elif codigo == 4:
    tipo = 'Blu-Ray (25 GB)'
else:
    print('Código inválido')
    exit() # exit() serve para sair do programa e evitar erro.
print(f'O tipo de unidade de disco correspondente ao código {codigo} é "{tipo}".')