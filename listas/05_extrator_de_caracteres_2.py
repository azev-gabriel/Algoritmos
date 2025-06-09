# Escrever a função que recebe por parâmetro uma string e um caractere. E a função deve retornar os primeiros caracteres da string até encontrar o caractere passado por parâmetro.


def extrair_primeiros_caracteres(string, caractere):
    resposta = ''
    i = 0
    letra_encontrada = False
    while i < len(string) and not letra_encontrada:
        if string[i] == caractere:
            letra_encontrada = True
        else:
            resposta = resposta + string[i]
        i = i + 1
    return resposta

print(extrair_primeiros_caracteres('UniAcademia', 'e'))