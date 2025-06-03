# Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que divididos por 11 dão resto igual a 5.


print('Lista de números entre 1000 e 1999 que possuem resto 5:')
for numero in range(1000, 2000):
    if numero % 11 == 5:
        print(f'Número: {numero}')