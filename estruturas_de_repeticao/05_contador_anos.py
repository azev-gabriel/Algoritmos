# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,30 metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.


altura_chico = 150
altura_ze = 130
contador_anos = 0
ano_atual = 2025
ano_parcial = ano_atual + contador_anos


while altura_ze <= altura_chico:
    altura_chico += 2
    altura_ze += 3
    contador_anos += 1
    ano_atual += 1
    ano_parcial += 1

    print(f'Ano: {ano_parcial} - Altura do Chico: {altura_chico} | Altura Zé: {altura_ze}.')


print(f'Em {ano_parcial}, ({contador_anos} anos) Zé estará mais alto que Chico.')