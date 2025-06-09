# Escrever a função que recebe por parâmetro uma string e um número. A função deve retornar os primeiros caracteres da string de acordo com o número passado por parâmetro.


def extrair_caracteres(string, numero):     # Passando os parâmetros pra função.
    resposta = ''
    if numero > len(string):     # Se o número de caracteres for maior do que o tamanho da string, esse if ajusta o número para o tamanho da string.
        numero = len(string)     # numero = tamanho da string.
    for i in range(numero):
        resposta = resposta + string[i]
    return resposta



print(extrair_caracteres('UniAcademia', 12))

