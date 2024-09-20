alunos = dict()
alunos['Nome'] = str(input('Nome do aluno: '))
alunos['Média'] = float(input(f'Média do {alunos["Nome"]}: '))
print('=-' * 15)
for key, value in alunos.items():
    print(f' - {key} é {value}')
print(' - Situação: ', end='')
if alunos['Média'] >= 7:
    print('Aprovado')
elif 6 <= alunos['Média'] < 7:
    print('Recuperação')
else:
    print('Reprovado')
