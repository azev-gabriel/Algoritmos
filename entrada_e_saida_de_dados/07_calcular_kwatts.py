# Efetuar a leitura do número de quilowatts consumidos e calcular o valor a ser pago de energia  elétrica, sabendo-se que o valor a pagar por quilowatt é de 0,12. Apresentar o valor total a ser pago pelo usuário acrescido de 18% de ICMS.

quilowatts = float(input('Digite a quantidade de quilowatts: '))
valor_consumo = quilowatts * 0.12
icms = valor_consumo * 0.18
valor_final = valor_consumo + icms

print(f'O valor da sua conta é: R${valor_final:.2f}')