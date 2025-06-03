# Escrever um algoritmo que lê 10 valores, um de cada vez, e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.

contador_dentro = 0
contador_fora = 0

for i in range(1, 11):
    valor = float(input('Digite um valor: '))
    if valor >= 10 and valor <= 20:
        print('Esse valor está no intervalo de 10 a 20.')
        contador_dentro += 1
    else:
        print('Esse valor está fora do invervalo de 10 a 20.')
        contador_fora += 1
    print(f'Valores digitados: {i} de 10')
    print(f'Valores dentro do intervalo: {contador_dentro}')
    print(f'Valores fora do intervalo: {contador_fora}')
