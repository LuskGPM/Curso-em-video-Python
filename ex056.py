soma = 0
chomem = 0
cmulher = 0
mvelho = 0
nvelho = ''
for c in range(1, 5):
    print('-'*5, c, '° PESSOA', '-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().upper()
    soma += idade
    if sexo == 'M':
        chomem += 1
    elif sexo == 'F' and idade < 20:
        cmulher += 1
    if chomem == 1:
        mvelho = idade
        nvelho = nome
    else:
        if sexo == 'M' and idade > mvelho:
            mvelho = idade
            nvelho = nome
print(f'A média de idade do grupo é: {soma/4}')
if chomem == 0:
    print('Não temos homens no grupo.')
else:
    print(f'O homem mais velho é o sr {nvelho} que possuí {mvelho} anos.')
if cmulher == 0:
    print('Não temos mulher no grupo.')
else:
    print(f'{cmulher} mulheres possuem menos de 20 anos.')
