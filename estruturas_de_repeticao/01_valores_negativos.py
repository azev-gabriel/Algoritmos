# Escrever um algoritmo que lê 10 valores e conte quantos destes valores são negativos, escrevendo esta informação.



## FOR É MELHOR PARA SITUAÇÕES EM QUE HÁ UMA QUANTIDADE EXATA DE VEZES QUE O LOOP DEVE SER RODADO.


contador_de_negativos = 0 # Criei uma variável que serve de contador;
valor = 0 # Inicio a variável valor com valor 0.

for i in range (1, 11): # Repete o loop 10 vezes, com 'i' indo de 1 até 10.
    valor = int(input('Digite um valor: '))

    if valor < 0: # Se o valor for menor que 0, adicione 1 ao contador.
        contador_de_negativos += 1     # '+=' é um operador de atribuição.


print(f'Você digitou {contador_de_negativos} números negativos.')


