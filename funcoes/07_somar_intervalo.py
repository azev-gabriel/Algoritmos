# Escrever uma função somarIntervalo(n1, n2) que retorna a soma dos números inteiros que existem entre n1 e n2 (inclusive ambos). A função deve funcionar inclusive se o valor de n2 for menor que n1.


def somar_intervalo (n1, n2):
    if n2 < n1:
        print('O segundo número é maior que o primeiro. Os valores serão reordenados em ordem crescente.')
        var_temp = n1 # n1 ficou vazio...
        n1 = n2 # n2 foi pra n1...
        n2 = var_temp # n2 foi pra var_temp que é o n1.

    soma_inteiros = 0

    for i in range(n1, n2 + 1):
        soma_inteiros = i + soma_inteiros

    return soma_inteiros

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

resultado = print(f'Soma dos valores: {somar_intervalo(n1, n2)}')