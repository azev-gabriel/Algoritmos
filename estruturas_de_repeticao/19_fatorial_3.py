# Escrever um algoritmo que leia um valor N inteiro e positivo e que calcula o valor de E. Imprime o resultado de E ao final. E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!


i = int(input('Digite N: '))
e = 1
fatorial = 1
n = i

for i in range (1,n+1):
    fat = 1
    for fat in range(1,i):
        fat = fat * i
    print (f'Fatorial: {i}!= {fat} => Parcela: 1/{fat}')
    e = e + 1 / fat
    print (f'E = {1 / fat:.6f} ')

print (f'\nValor final de E:{e:.4f} ')
