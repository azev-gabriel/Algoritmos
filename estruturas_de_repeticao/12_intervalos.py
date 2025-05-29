# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um número negativo.


intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

valor = int(input('Digite um valor positivo (negativo encerra o programa): '))
if valor < 0:
    print('PROGRAMA ENCERRADO.')
else:

    while valor > 0:
        if valor >= 0 and valor <= 25:              
            intervalo1 += 1
        elif valor >= 26 and valor <= 50:
            intervalo2 += 1
        elif valor >= 51 and valor <= 75:
            intervalo3 += 1
        elif valor >= 76 and valor <= 100:
            intervalo4 += 1
        else:
            print('Valor fora dos intervalos. Será descartado.')
    
        print(f'INTERVALO [0, 25]: {intervalo1}')                   # PRINTS DENTRO DO LOOP: Resultados em tempo real.
        print(f'INTERVALO [26, 50]: {intervalo2}')
        print(f'INTERVALO [51, 75]: {intervalo3}')                  # PRINTS FORA DO LOOP: Resultados no fim do loop.
        print(f'INTERVALO [76, 100]: {intervalo4}\n')

        valor = int(input('Digite um valor positivo (negativo encerra o programa): '))

