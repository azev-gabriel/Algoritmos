# Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n. O algoritmo deve escrever cada termo gerado e o valor final de S.


n = int(input('Digite um valor INTEIRO E POSITIVO: '))
if n < 0:
    print('VALOR INVÁLIDO.')
else:
    s = 0

    for i in range(1, n + 1):    # Se não tiver + 1 no for, o valor original digitado não será somado.
        s = s + 1 / i
        
        print(f'1/{i} = {1 / i:.3f}')
        print(f'Soma total = {s:.3f}')