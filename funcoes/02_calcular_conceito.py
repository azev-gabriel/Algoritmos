# Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:
# Nota Conceito
# De 0 a 49   D
# De 50 a 69  C
# De 70 a 89  B
# De 90 a 100 A


def calcularConceito(media):
    if media < 0 or media > 100:
        print('VALOR INVÁLIDO.')
    elif media <= 49:
        conceito = 'D'
    elif media <= 69:
        conceito = 'C'
    elif media <= 89:
        conceito = 'B'
    elif media <= 100:
        conceito = 'A'

    return conceito


media_final = float(input('Digite a média final: '))
print(f'Conceito: {calcularConceito(media_final)}')