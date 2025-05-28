#  Escreva um programa que receba dois números reais e um código de seleção do usuário. Se o código digitado for 1, faça o programa adicionar os dois números previamente digitados e mostrar o resultado; se o código de seleção for 2, os números devem ser multiplicados; se o código de seleção for 3, o primeiro número deve ser dividido pelo segundo. Se nenhuma das opções acima for escolhida, mostrar "Código inválido".

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
codigo = int(input('Digite o código de seleção (1 para soma, 2 para multiplicação, 3 para divisão): '))

if codigo == 1:
    resultado = numero1 + numero2
    print(f'O resultado da soma é {resultado}')
elif codigo == 2:
    resultado = numero1 * numero2
    print(f'O resultado da multiplicação é {resultado}')
elif codigo == 3:
    resultado = numero1 / numero2
    print(f'O resultado da divisão é {resultado}')
else:
    print('Código inválido')