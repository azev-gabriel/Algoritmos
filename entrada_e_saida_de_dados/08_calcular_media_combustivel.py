# Calcular a média de combustível gasto pelo usuário, sendo informado a quantidade de quilômetros rodados e a quantidade de combustível consumidos.

km_rodados = int(input('Digite quantos quilômetros você rodou: '))
consumo = int(input('Digite quantos litros de combustível você gastou: '))

media = km_rodados / consumo

print(f'Média de quilômetros por litro de combustível:{media:.2f}')