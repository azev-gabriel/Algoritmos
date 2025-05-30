# Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.


conta_valores = 0
soma_valores = 0
conta_par = 0
soma_par = 0
conta_impar = 0
media_par = 0

valor = int(input('Digite um valor POSITIVO (0 encerra o programa): '))

while valor != 0:

    conta_valores += 1
    soma_valores += valor

    if valor % 2 == 0:
        conta_par += 1
        soma_par += valor
        media_par = soma_par / conta_par
        media_valores = soma_valores / conta_valores
    else:
        conta_impar += 1
        media_valores = soma_valores / conta_valores

    print(f'Quantidade de valores: {conta_valores}')
    print(f'Quantidade pares: {conta_par}')
    print(f'Quantidade ímpares: {conta_impar}')
    print(f'Média pares: {media_par:.2f}')
    print(f'Média valores: {media_valores:.2f}')

    valor = int(input('Digite um valor (POSITIVO): '))