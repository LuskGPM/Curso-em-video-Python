from datetime import datetime

ano_atual = datetime.today().year
pessoa_aposentadoria = dict()

pessoa_aposentadoria['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
pessoa_aposentadoria['Idade'] = ano_atual - ano_nascimento
pessoa_aposentadoria['CTPS'] = int(input('Carteira de trabalho (Digite 0 se não tiver): '))

if pessoa_aposentadoria['CTPS'] != 0:
    pessoa_aposentadoria['Ano de Contratação'] = int(input('Ano de contratação: '))
    pessoa_aposentadoria['Salário'] = float(input('Salário: '))
    pessoa_aposentadoria['Aposentadoria'] = (pessoa_aposentadoria['Ano de Contratação'] - ano_nascimento) + 35

print('_'*35)
for key, value in pessoa_aposentadoria.items():
    print(f'{key} tem valor {value}')
