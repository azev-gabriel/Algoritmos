# Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado o cargo correspondente. Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem de código inválido. Utilize a tabela abaixo:

# Código     Cargo
# 101        Vendedor
# 102        Atendente
# 103        Auxiliar Técnico
# 104        Assistente
# 105        Coordenador de Grupo
# 106        Gerente

codigo = int(input('Digite um código de 101 a 106: '))

if codigo == 101:
    cargo = 'Vendedor'
elif codigo == 102:
    cargo = 'Atendente'
elif codigo == 103:
    cargo = 'Auxiliar Técnico'
elif codigo == 104:
    cargo = 'Assistente'
elif codigo == 105:
    cargo = 'Coordenador de Grupo'
elif codigo == 106:
    cargo = 'Gerente'
else:
    print('Código inválido')
    exit() # exit() serve para sair do programa e evitar erro.
print(f'O cargo correspondente ao código {codigo} é "{cargo}".')
