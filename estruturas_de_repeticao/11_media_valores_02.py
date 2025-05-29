# Escrever um algoritmo que leia um número não determinado de valores e calcule a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos. Mostre os resultados.


contador_valores = 0
contador_positivos = 0
contador_negativos = 0
soma_valores = 0

valor = int(input('Digite um valor (positivo ou negativo): '))
if valor == 0:
    print('PROGRAMA ENCERRADO.')
else:

    while valor != 0:
        contador_valores += 1

        if valor > 0:
            contador_positivos += 1
        if valor < 0:
            contador_negativos += 1
    
        soma_valores = soma_valores + valor
        media_valores = soma_valores / contador_valores
        porcentagem_positivos = (contador_positivos / contador_valores) * 100
        porcentagem_negativos = (contador_negativos / contador_valores) * 100

        print(f'Valor digitado: {valor}.')
        print(f'Soma dos valores digitados: {soma_valores}.')
        print(f'Total de valores digitados: {contador_valores}.')
        print(f'Quantidade de positivos: {contador_positivos}.')
        print(f'Quantidade de negativos: {contador_negativos}.')
        print(f'Média dos valores: {media_valores:.2f}.')
        print(f'Porcentagem de positivos: {porcentagem_positivos:.2f}')
        print(f'Porcentagem de negativos: {porcentagem_negativos:.2f}\n')

        valor = int(input('Digite outro valor (positivo ou negativo): ')) # Se não tiver essa linha no fim do loop, ele roda infinito.

    
    