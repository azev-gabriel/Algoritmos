# Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até n. Mostre a tabuada na forma:

# 1 x n = n
# 2 x n = 2n
# 3 x n = 3n


n = int(input('Digite um número: '))    # n serve para definir até onde o i (índice) vai chegar. Exemplo: 5

print(f'Tabuada do {n}')    # Formatação;

for i in range(1, n + 1):    # 1, n +1 serve pra pular a multiplicação por zero.
    print(f'{i} x {n} = {i * n}')

print('Fim da tabuada.')