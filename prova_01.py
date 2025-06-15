# 01: Faça um programa que leia o cargo de um funcionário e o tempo de trabalho na empresa e escreva o percentual de participação dele no fundo de lucros da empresa, segundo a tabla abaixo:

# Cargo 1 = Programador          Tempo de trabalho < 2 anos             Percentual = 2%
#                                                 >= 2anos              Percentual = 3%

# Cargo 2 = Analista             Tempo de trabalho < 3 anos             Percentual = 4%
#                                                  >= 3anos             Percentual = 5% 

# Cargo 3 = Gerente              Tempo de trabalho <= 4 anos            Percentual = 6%
#                                                   > 4 anos            Percentual = 7%


# print('Cargos:')
# print('Programador: 1 | Analista: 2 | Gerente: 3')
# print('\n')

# cargo = int(input('Digite o seu cargo: '))
# if cargo != 1 and cargo != 2 and cargo != 3:
#     print('Cargo inválido. Tente novamente!')
#     exit()

# tempo_trabalho = int(input('Digite o tempo de trabalho na empresa: '))
# if tempo_trabalho < 0:
#     print('Tempo de trabalho inválido. Tente novamente!')
#     exit()

# if cargo == 1 and tempo_trabalho < 2:
#     percentual = 2
#     print(f'Percentual de participação: {percentual}%.')
# elif cargo == 1 and tempo_trabalho >= 2:
#     percentual = 3
#     print(f'Percentual de participação: {percentual}%.')
# elif cargo == 2 and tempo_trabalho < 3:
#     percentual = 4
#     print(f'Percentual de participação: {percentual}%.')
# elif cargo == 2 and tempo_trabalho >= 3:
#     percentual = 5
#     print(f'Percentual de participação: {percentual}%.')
# elif cargo == 3 and tempo_trabalho <= 4:
#     percentual = 6
#     print(f'Percentual de participação: {percentual}%.')
# elif cargo == 3 and tempo_trabalho > 4:
#     percentual = 7
#     print(f'Percentual de participação: {percentual}%.')





# 02: Uma empresa de telefonia tem cerca de vários clientes e 3 planos de comercialização, segundo a tabela abaixo. Faça um programa que leia para cada cliente o tipo de plano contratado do cliente ( 1, 2 ou 3) e o tempo de conversação, que será digitado em minutos. Para encerrar digite um plano com valor zero. Seu programa deve calcular e escrever para cada cliente o valor a pagar pela ligação considerando a tabela. O cálculo é feito multiplicando o tempo de conversação (lido pelo seu programa) pelo valor R$ de cada minuto, identificado na tabela em função do plano contratado pelo cliente.
# Plano contratado      Valor do minuto R$
# 1                         R$ 0,10
# 2                         R$ 0,20
# 3                         R$ 0,25


# while True:
#     print('\nPlanos: 1 | 2 | 3')
#     print('\n')
#     plano = int(input('Digite o plano contratado: '))
#     if plano != 1 and plano != 2 and plano != 3:
#         print('Plano inválido. Tente novamente!')
#         continue
#     if plano == 0:
#         break

#     tempo_conversacao = int(input('\nDigite o tempo de conversação em minutos: '))

#     if plano == 1:
#         valor_minuto = 0.10
#         print(f'Valor a pagar: R${valor_minuto * tempo_conversacao:.2f}.')
#     elif plano == 2:
#         valor_minuto = 0.20
#         print(f'Valor a pagar: R${valor_minuto * tempo_conversacao:.2f}.')
#     elif plano == 3:
#         valor_minuto = 0.25
#         print(f'Valor a pagar: R${valor_minuto * tempo_conversacao:.2f}.')
#     else:
#         print('Valor inválido. Tente novamente!')







# 03: Faça um programa que lei 4 números inteiros quaisquer e escreva os números em ordem crescente. Exemplo: se digitado : 9, 5, 2, 6 o programa deverá escrever; 2,5,6,9.


while True:
    print('\n')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))

    if n1 <= n2 and n1 <= n3 and n1 <= n4:
        menor = n1
        a = n2
        b = n3
        c = n4
    elif n2 <= n1 and n2 <= n3 and n2 <= n4:
        menor = n2
        a = n1
        b = n3
        c = n4
    elif n3 <= n1 and n3 <= n2 and n3 <= n4:
        menor = n3
        a = n1
        b = n2
        c = n4
    else:
        menor = n4
        a = n1
        b = n2
        c = n3

    if a <= b and a <= c:
        meio1 = a
        x = b
        y = c
    elif b <= a and b <= c:
        meio1 = b
        x = a
        y = c
    else:
        meio1 = c
        x = a
        y = b

    if x <= y:
        meio2 = x
        maior = y
    else:
        meio2 = y
        maior = x

    print(f'Ordem crescente: {menor}, {meio1}, {meio2}, {maior}')
