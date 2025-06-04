# Escrever uma função calcularQuociente(dividendo, divisor), que retorna a divisão inteira (sem casas decimais) de dividendo por divisor e outra função calcularResto(dividendo, divisor) que retorna o resto.


def calcular_quociente(dividendo, divisor):
    return dividendo // divisor

def calcular_resto(dividendo, divisor):
    return dividendo % divisor


dividendo = int(input('Dividendo: '))
divisor = int(input('Digite o divisor: '))

print(f'Quociente inteiro: {calcular_quociente(dividendo, divisor)}')
print(f'Resto inteiro: {calcular_resto(dividendo, divisor)}')