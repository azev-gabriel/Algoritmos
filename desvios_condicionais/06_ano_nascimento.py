# Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exiba sua idade. A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos), adolescente (12 a 17 anos), adulta (18 a 64 anos) ou idosa (65 anos em diante).

ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
if ano_nascimento >= ano_atual: # Evita que a pessoa tenha menos de 1 ano de idade.
    print('Valor inválido!')
else:
    idade = ano_atual - ano_nascimento

    print(f'O indivíduo tem {idade} anos de idade.')

    if idade <= 3:
        classificacao = 'Bebê'
    elif idade <= 11:
        classificacao = 'Criança'
    elif idade <= 17:
        classificacao = 'Adolescente'
    elif idade <= 64:
        classificacao = 'Adulto'
    else:
        classificacao = 'Idoso'

    print(f'Classificação de acordo com a idade: {classificacao}')
