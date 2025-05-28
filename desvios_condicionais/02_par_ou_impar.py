# Ler um número inteiro e informar se o número lido é par ou impar.

numero = int(input('Digite um número: '))

if numero % 2 == 0:        # IMPORTANTE: == é IGUALDADE   //   = é ATRIBUIÇÃO DE VALOR!
    # % é DIVISÃO SEM RESTO!
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')