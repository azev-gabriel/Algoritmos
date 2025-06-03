# Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o código e o preço de custo de cada produto e calcule o preço novo. Calcule também, a média dos preços com e sem aumento. Mostre o código e o preço novo de cada produto e, no final, as médias. A entrada de dados deve terminar quando for lido um código de produto negativo.

codigo = int(input('Digite o código do produto: '))
preco_custo = float(input('Digite o preço do produto: '))

contador_preco_custo = 0
contador_preco_novo = 0

soma_custo = 0
soma_novo = 0


while codigo >= 0:
    contador_preco_custo += 1
    reajuste = preco_custo * 0.20
    preco_novo = preco_custo + reajuste
    contador_preco_novo += 1
    soma_custo = soma_custo + preco_custo
    media_custo = soma_custo / contador_preco_custo
    soma_novo = soma_novo + preco_novo
    media_novo = soma_novo / contador_preco_novo

    print(f'\nCódigo do produto: {codigo};')
    print(f'Preço de custo: {preco_custo}')
    print(f'Preço com reajuste: {preco_novo};')
    print(f'Valor do reajuste: {reajuste}')
    print(f'Média dos preços de custo: {media_custo}')
    print(f'Média dos preços reajustados: {media_novo}')

    codigo = int(input('\nDigite o código do produto: '))
    preco_custo = float(input('Digite o preço do produto: '))



