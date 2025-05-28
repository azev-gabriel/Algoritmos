# Calcular o aumento que será dado a um funcionário, obtendo do usuário as seguintes informações: salário atual e a porcentagem de aumento. Apresentar o novo valor do salário e o valor do aumento.


salario_atual = float(input('Digite o seu salário atual: '))
aumento = int(input('Digite a porcentagem do seu aumento (Ex: 10 para 10%): '))

salario_novo = salario_atual + aumento * salario_atual / 100
# Exemplo: salario_novo = 1000 + 10 * 1000 / 100
valor_aumento = salario_novo - salario_atual

print(f'O valor do seu aumento é de R${valor_aumento:.2f}') # ":.2f" é para formatar o conteúdo printado. Serve para limitar o número de casas decimais em um valor printado.

print(f'O seu novo salário é de R${salario_novo:.2f}')