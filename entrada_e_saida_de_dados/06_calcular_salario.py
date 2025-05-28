# Calcular o salário líquido do funcionário sabendo que este é constituído pelo salário bruto mais o valor das horas extras subtraindo 8% de INSS do total. Serão lidos nesse problema o  salário bruto, o valor das horas extras e o número de horas extras. Apresentar ao final o salário líquido.

salario_bruto = int(input('Digite seu salário bruto: '))
valor_hora_extra = int(input('Digite o valor da sua hora extra: '))
horas_extras = int(input('Digite quantas horas extras você fez: '))
salario_bruto_final = salario_bruto + valor_hora_extra * horas_extras
desconto = 0.08 * salario_bruto_final
salario_liquido = salario_bruto_final - desconto


print(f'- Salário fixo: R${salario_bruto}.')
print(f'- Você fez {horas_extras} horas extras, com o valor de R${valor_hora_extra} para cada uma delas.')
print(f'- Portanto, seu salário bruto é de R${salario_bruto_final}.')
print(f'- Você teve um desconto de 8% do INSS no valor de R${desconto}.')
print(f'- Seu salário final é de R${salario_liquido}')
