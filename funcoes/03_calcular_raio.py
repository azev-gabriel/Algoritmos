# Faça uma função que recebe por parâmetro o raio de uma esfera e calcule o seu volume (v = (4 x pi x R3)/3).


def calcular_volume(raio):
    volume = (4 * 3.14 * raio ** 3) / 3
    return volume

raio = int(input('Digite o valor do raio da esfera: '))
print(f'Volume da esfera = {calcular_volume(raio):.2f}')