# Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado. Funcionários com até 1 ano de empresa, receberão aumento de 10%. Funcionários com mais de um ano de tempo de serviço, receberão aumento de 20%.

salario_atual = int(input('Digite seu salário atual: '))
tempo_servico = int(input('Digite o tempo de serviço (em anos): '))

if tempo_servico <= 1:
    reajuste = salario_atual * 0.10

else:
    reajuste = salario_atual * 0.20

salario_reajustado = salario_atual + reajuste

print(f'Seu novo salário é R${salario_reajustado}')
print(f'Valor do reajuste: R${reajuste}')