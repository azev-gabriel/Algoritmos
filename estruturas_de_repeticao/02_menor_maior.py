# Escreva um algoritmo que leia 20 valores e encontre o maior e o menor deles. Mostre o resultado.


for contagem in range(1, 21): # Isso é um loop de 20 vezes. (Mesma ideia do exercício 01.)
    valor = int(input(f'Digite o {contagem}º valor: '))
         
         # Apenas aplicando as condições para definir o menor e o maior valor.
    if contagem == 1:
        menor = valor
        maior = valor          
    
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    print(f'MENOR VALOR: {menor}. MAIOR VALOR: {maior}.')

print('FIM DO LOOP.')




## OUTRA FORMA DE SE FAZER... USANDO WHILE:

contador = 1 # Inicia-se uma variável como CONTADOR (com o valor inicial de 1)

while contador < 20: # ENQUANTO o contador for menor que 20, o loop será executado.
    valor = int(input(f'Digite o {contador}º valor: '))

    if contador == 1:
        menor = valor
        maior = valor          
    
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor
    
    contador += 1

    print(f'MENOR VALOR: {menor}. MAIOR VALOR: {maior}.')

print('FIM DO LOOP.')
