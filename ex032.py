import datetime
ano = int(input('Ano (0 para o ano atual): '))
anoat = datetime.date.today().year
if ano == 0:
    ano = anoat
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é Bissexto.')
else:
    print(f'{ano} não é Bissexto')
