# Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, o algoritmo deverá escrever "Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado".

salario = int(input('Digite o valor da sua renda: '))
financiamento = int(input('Digite o valor do financiamento pretendido: '))

if financiamento <= salario * 5:
    print('Financiamento concedido!')
else:
    print('Financiamento negado!')