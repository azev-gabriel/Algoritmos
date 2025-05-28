# Faça um algoritmo que transforme a nota de um aluno em conceito. As notas 10 e 9 receberão conceito A, as notas 8 e 7 receberão conceito B, as notas 6 e 5 receberão conceito C e abaixo de 5 conceito D.

nota = int(input('Digite a nota do aluno: '))

if nota == 10 or nota == 9:
    conceito = 'A'
elif nota == 8 or nota == 7:
    conceito = 'B'
elif nota == 6 or nota == 5:
    conceito = 'C'
else:
    conceito = 'D'
print(f'A nota {nota} gera o conceito {conceito}')