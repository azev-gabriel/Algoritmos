# Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos, digitados pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.

contador_valores = 0
soma_valores = 0

valor = int(input('Digite um valor (inteiro e positivo): '))

while valor > 0:
    contador_valores += 1
    soma_valores = soma_valores + valor

    valor = int(input('Digite um valor (inteiro e positivo): '))

media = soma_valores / contador_valores

print(f'Você digitou {contador_valores} valores.')
print(f'A média dos valores é: {media:.2f}.')
