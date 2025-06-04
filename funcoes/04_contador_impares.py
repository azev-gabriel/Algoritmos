# Escrever uma função contarImpar(n1, n2) que retorna o número de inteiros ímpares que existem entre n1 e n2 (inclusive ambos, se for o caso). A função deve funcionar inclusive se o valor de n2 for menor que n1.


def contar_impar(n1, n2):
    if n2 < n1:
        print('O segundo número é maior que o primeiro. Os valores serão reordenados em ordem crescente.')
        var_temp = n1
        n1 = n2
        n2 = var_temp

    contador_impar = 0

    for i in range(n1, n2 + 1):
        if i % 2 != 0:
            contador_impar += 1

    return contador_impar


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'Valores digitados: {n1, n2}')
resposta = contar_impar(n1, n2)
print(f'A quantidade de ímpares no intervalo digitado é: {resposta}')
