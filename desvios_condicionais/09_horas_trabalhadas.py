# Escreva um programa para calcular e mostrar o salário semanal de uma pessoa, determinado pelas condições que seguem. Se o número de horas trabalhadas for inferior ou igual a 40, a pessoa recebe R$15,00 por hora, senão a pessoa recebe R$600,00 mais R$21,00 para cada hora trabalhada acima de 40 horas. O programa deve pedir o número de horas trabalhadas como entrada e deve dar o salário como saída.

horas_trabalhadas = int(input('Digite quantas horas você trabalhou na semana: '))

if horas_trabalhadas <= 40:
    salario = 15 * horas_trabalhadas
else:
    salario = 600 + (horas_trabalhadas - 40) * 21

print(f'Você trabalhou {horas_trabalhadas} horas na semana. Totalizando um salário semanal de R${salario}.')
