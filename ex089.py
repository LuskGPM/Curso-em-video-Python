nome_alunos = list()
nota_alunos = list()
media_alunos = list()

while True:
    print('=' * 20)
    nome = str(input('Nome: '))
    primeira_nota = float(input('Primeria nota: '))
    segunda_nota = float(input('Segunda nota: '))

    nome_alunos.append(nome)
    nota_alunos.append([primeira_nota, segunda_nota])
    media_alunos.append((primeira_nota + segunda_nota) / 2)

    continuar = input('Continuar? [S/N]: ')
    if continuar.strip().lower()[0] == 'n':
        break

print(f"{'N°':<5}{'NOME':^10}{'MÉDIA':>20}")
print('-'*40)
for i, nome in enumerate(nome_alunos):
    print(f'{i:<5}{nome:^10}{media_alunos[i]:>20}')

while True:
    aluno_solicitado = int(input('Qual aluno você quer ver? (DIGITE 999 PARA SAIR): '))
    if aluno_solicitado == 999:
        break
    print(nome_alunos[aluno_solicitado], nota_alunos[aluno_solicitado])
    print('-'*20)
