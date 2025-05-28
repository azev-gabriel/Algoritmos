# Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado, reprovado ou se fará prova final. O aluno será reprovado se faltou mais de 15 aulas. Será aprovado se não for reprovado por falta e sua média for maior que 6,0. Caso tenha média menor, deverá fazer prova final. O cálculo da média deve ser feito com peso 3 para a primeira prova, 5 para a segunda prova e 2 para o trabalho.

nome = input('Digite seu nome: ')
frequencia = int(input('Digite sua frequência: '))
if frequencia > 15:
    situacao = 'Reprovado'
    print(situacao)
else:
    prova1 = float(input('Digite a nota da primeira prova (De 0 a 10): '))
    if prova1 < 0 or prova1 > 10:
        print('Valor inválido.')
    else:
        prova2 = float(input('Digite a nota da segunda prova (De 0 a 10): '))
        if prova2 < 0 or prova2 > 10:
            print('Valor inválido.')
        else:
            trabalho = float(input('Digite a nota do trabalho (De 0 a 10): '))
            if prova2 < 0 or prova2 > 10:
                print('Valor inválido.')
            else:
                media = (prova1 * 3 + prova2 * 5 + trabalho * 2) / 10
                if media >= 6:
                    situacao = 'Aprovado'
                else:
                    situacao = 'Prova final'

print('----- RELATÓRIO -----')
print(f'Nome do aluno: {nome}.')
print(f'Frequência: {frequencia}.')
print(f'Nota da primeira prova: {prova1}.')
print(f'Nota da segunda prova: {prova2}.')
print(f'Nota do trabalho: {trabalho}.')
print(f'Sua média foi de {media:.2f}.')
print(f'Situação: {situacao}.')


