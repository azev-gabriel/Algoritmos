# Escrever uma função verificarEstacao(dia, mes), que retorna qual a estação do ano da data passada por parâmetro. Lembrando que a primavera começa no dia 23 de setembro, o verão em 21 de dezembro, o outono em 21 de março e o inverno em 21 de junho.


def verificar_estacao(dia, mes):
        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            estacao = 'Digite valores válidos.'
        elif mes == 9 and dia >= 23 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
            estacao = 'Primavera'
        elif mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 21:
            estacao = 'Verão'
        elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
            estacao = 'Outono'
        elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 23:
            estacao = 'Inverno'

        return estacao


dia = int(input('Digite o dia do mês (numeral): '))
mes = int(input('Digite o mês (numeral): '))

estacao = print(f'Estação: {verificar_estacao(dia, mes)}')