# Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação: 1,2,3,4 = voto para os respectivos candidatos; 5 = voto nulo; 6 = voto em branco.

# Elabore um algoritmo que leia o código do candidato em um voto. Calcule e escreva as seguintes informações;

# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco.

# Como finalizador do conjunto de votos, utilize o valor 0.

total_votos = 0
total_nulo = 0
total_branco = 0

total_joao = 0
total_maria = 0
total_jose = 0
total_chico = 0


print('----------------------------------------------------------------')
print('Candidatos disponíveis: [1] JOÃO, [2] MARIA, [3] JOSÉ, [4] CHICO')
print('----------------------------------------------------------------')

voto = int(input('Digite o número do seu candidado para votar. Digite 5 para VOTO NULO ou 6 para VOTO EM BRANCO. Digite 0 para FINALIZAR.\n'))        # \n serve para saltar de linha no print, apenas formatação.

while voto != 0:
    if voto == 1:
        total_votos += 1
        total_joao += 1

    if voto == 2:
        total_votos += 1
        total_maria += 1

    if voto == 3:
        total_votos += 1
        total_jose += 1
    
    if voto == 4:
        total_votos += 1
        total_chico += 1

    if voto == 5:
        total_votos += 1
        total_nulo += 1

    if voto == 6:
        total_votos += 1
        total_branco += 1

    print(f'Total de votos: {total_votos}')
    print(f'Candidato João: {total_joao}')
    print(f'Candidato Maria: {total_maria}')
    print(f'Candidato José: {total_jose}')
    print(f'Candidato Chico: {total_chico}')
    print(f'Votos NULOS: {total_nulo}')
    print(f'Votos em BRANCO: {total_branco}')

    print('Candidatos disponíveis: [1] JOÃO, [2] MARIA, [3] JOSÉ, [4] CHICO')
    print('----------------------------------------------------------------')

    voto = int(input('Digite o número do seu candidado para votar. Digite 5 para VOTO NULO ou 6 para VOTO EM BRANCO. Digite 0 para FINALIZAR.\n'))

print('---------')
print('RESULTADO')
print('---------')
print(f'Total de votos: {total_votos}')
print(f'Candidato João: {total_joao}')
print(f'Candidato Maria: {total_maria}')
print(f'Candidato José: {total_jose}')
print(f'Candidato Chico: {total_chico}')
print(f'Votos NULOS: {total_nulo}')
print(f'Votos em BRANCO: {total_branco}')