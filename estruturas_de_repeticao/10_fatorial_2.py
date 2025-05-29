# Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial deste valor.

# Inicia o programa com uma entrada de dados:
n = int(input('Digite quantos valores serão lidos: '))

# Cria um loop com que vai rodar n vezes:
for i in range(1, n + 1):
    valor = int(input(f'Digite o {i}º de {n} valores: '))
    fatorial = 1

    # Cria um loop dentro de outro loop:
    for i in range(1, valor + 1):
        fatorial = fatorial * i
    print(f'Fatorial de {valor}: {fatorial}')