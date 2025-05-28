# Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela "APROVADO".

# nota = float(input('Digite sua nota: '))

# if nota >= 60:     # SE a nota for MAIOR OU IGUAL que 60...
#     print('APROVADO!')




# Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela "APROVADO", se for menor, imprimir reprovado.
# Testar ainda se o valor lido foi maior do que 100 ou menor do que zero. Neste caso, imprimir "NOTA INVÁLIDA".

nota = float(input('Digite sua nota: '))

# Se a nota for menor que zero ou maior que 100: Imprime nota inválida e finaliza o programa.
if nota < 0 or nota > 100:
    print('NOTA INVÁLIDA!')

# Se a nota for digitada da forma certa, o programa continua a rodar os códigos...
# Se a nota for maior que 60: Imprime aprovado;
elif nota >= 60:
    print('APROVADO!')
else: # SENÃO: Imprime reprovado.
    print('REPROVADO!')


