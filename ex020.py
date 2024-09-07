import random
alunos = [0] * 4
a = 0
for a in range(4):
    alunos[a] = input('Nome do Aluno: ')
random.shuffle(alunos)
print(f'A ordem de apresentação será \n{alunos}')
