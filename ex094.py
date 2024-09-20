cadastro_pessoas = dict()
pessoas = list()

total_idade = 0

while True:
    cadastro_pessoas['Nome'] = str(input('Nome: ')).capitalize()
    cadastro_pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper()

    while cadastro_pessoas['Sexo'].strip()[0] not in "MF":
        cadastro_pessoas['Sexo'] = str(input('M para masculino, F para feminino: ')).upper()

    try:
        cadastro_pessoas['Idade'] = int(input('Idade: '))
    except ValueError:
        cadastro_pessoas['Idade'] = int(input('Digite a idade em número: '))

    pessoas.append(cadastro_pessoas.copy())
    total_idade += cadastro_pessoas['Idade']

    continuar = str(input('Continuar? [S/N]: ')).upper()
    while continuar.strip()[0] not in "NS":
        continuar = str(input('Digite "S" ou "N": ')).upper()

    if continuar.strip()[0] == 'N':
        break

media_idade = total_idade/len(pessoas)

print(f'A) Temos {len(pessoas)} Pessoas cadastradas')
print(f'B) A média de idade é de {media_idade:.1f} anos')

mulheres = [p['Nome'] for p in pessoas if p['Sexo'] == 'F']
print(f'C) As mulheres cadastradas foram: {", ".join(mulheres)}')
print('D) Lista de pessoas que estão acima da média: ')
for i in pessoas:
    if i['Idade'] > media_idade:
        for key, value in i.items():
            print(f'{key} = {value}', end='; ')
        print()

print('< ENCERRADO >')
