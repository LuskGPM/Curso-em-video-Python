import random
alunos = [0] * 4
a = 0
for a in range(4):
    alunos[a] = input('Digite o nome do aluno: ')
    a += 1
print(f'O aluno sorteado para resolver a questão é {alunos[random.randint(0, 3)]}')
