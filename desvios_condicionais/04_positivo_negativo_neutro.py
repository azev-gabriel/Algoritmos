# Ler um número e informar se ele é positivo, negativo ou neutro (zero).

numero = int(input('Digite um número: '))

if numero == 0:
    print(f'O número {numero} é NEUTRO.')
elif numero > 0:
    print(f'O número {numero} é POSITIVO.')
else:
    print(f'O número {numero} é NEGATIVO.')
