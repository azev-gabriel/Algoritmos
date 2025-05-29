# A prefeitura de uma cidade está fazendo uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:

# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário
# d) percentual de pessoas com salário até R$1000,00.

# O final da leitura de dados se dará com a entrada de um salário negativo.


## WHILE É MELHOR PARA USAR QUANDO NÃO HÁ UM NÚMERO ESPECÍFICO DE VEZES QUE O LOOP DEVE RODAR. GERALMENTE O LOOP SE ENCERRA COM ALGUMA CONDIÇÃO. EXEMPLO: QUANDO UM NÚMERO NEGATIVO É USADO.


# Variáveis
contador_habitantes = 0
soma_salario = 0
soma_filhos = 0
contador_baixa_renda = 0

# Inicia o programa com uma entrada de dados:
salario = int(input('Digite o salário: '))

# Estrutura para ENCERRAR o programa; -------------------
if salario < 0:
    print('PROGRAMA ENCERRADO')
else:
# -------------------------------------------------------

# INÍCIO do LOOP; ---------------------------------------------------------------------------------------------------------
    while salario > 0:

        # Adiciona um valor ao contador de habitantes TODA VEZ que um salário for contabilizado;
        contador_habitantes += 1    
        
        # Faz a soma de todos os salários (PRA DEPOIS TIRAR A MÉDIA);
        soma_salario = soma_salario + salario
        media_salarios = soma_salario / contador_habitantes      # RESPONDE A LETRA A;

        # Estrutura para encontrar o MAIOR SALÁRIO; -----------------------
        if salario > 0:
            maior_salario = salario
        if salario > maior_salario:
            maior_salario = salario     # RESPONDE A LETRA C;
        # -----------------------------------------------------------------

        # Estrutura para encontrar a população baixa renda: ----------------------
        if salario <= 1000:
            contador_baixa_renda += 1
            
        percentual_baixa_renda = (contador_baixa_renda / contador_habitantes) * 100      # RESPONDE A LETRA D;
        # ------------------------------------------------------------------------

        # Mais uma entrada de dados:
        filhos = int(input('Digite a quantidade de filhos: '))

        # Faz a soma de todos os filhos (PRA DEPOIS TIRAR A MÉDIA)
        soma_filhos = soma_filhos + filhos
        media_filhos = soma_filhos / contador_habitantes       # RESPONDE A LETRA B;

        # Reinicia o loop:
        salario = int(input('Digite o salário: '))
# FIM do LOOP --------------------------------------------------------------------------------------------------------------

# SAÍDA de dados:
print(f'Quantidade de habitantes avaliados: {contador_habitantes}.')
print(f'Média salarial: R${media_salarios:.2f}')
print(f'Média de filhos: {media_filhos:.2f}')
print(f'Maior salário: R${maior_salario}')
print(f'Percentual de habitantes com baixa renda: {percentual_baixa_renda:.2f}%.')