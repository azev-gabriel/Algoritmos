# Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial de N (N!).

fatorial = 1
valor = 0

valor = int(input('Digite um valor inteiro e positivo: '))

for contador in range(1, valor + 1): # 'valor + 1' é usado por que a variável fatorial já é inicializada com 1.
    fatorial = fatorial * contador

print(f'O fatorial de {valor} é {fatorial}')


# EXEMPLO DE USO: 
# Usuário digita o valor 5 > Esse valor é usado para o range do contador > Inicia-se o loop > Atribui a variável 'fatorial' com o valor de fatorial * contador que é igual a 1 * 1 = fatorial = 1 > Refaz o loop > fatorial = 1 * 2 = 2 > Refaz o loop > fatorial = 2 * 3 = 6 > Refaz o loop > fatorial = 6 * 4 = 24 > Refaz o loop > fatorial = 24 * 5 = 120 > Imprime o resultado.

