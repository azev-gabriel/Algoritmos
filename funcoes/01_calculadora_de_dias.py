# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

# FUNÇÃO: ------------------------------------------
def calcularDias(ano, mes, dia):                    # DEF usado para criar funções |    ## calcularDias: nome da função
                                                    ### (ano, mes, dia): Parâmetros da função
    resultado = (ano * 365) + (mes * 30) + dia      
    return resultado                                # return: retorna o resultado dos cálculos
# FIM DA FUNÇÃO: -----------------------------------

# PROGRAMA: --------------------------------------
ano = int(input('Digite o ano de nascimento: '))
mes = int(input('Digite o mês de nascimento: '))
dia = int(input('Digite o dia de nascimento: '))

resultado = calcularDias(ano, mes, dia)             # Chama a função, passando os argumentos para os parâmetros.
print(f'Sua idade em dias = {resultado}')