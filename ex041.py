import datetime

anoN = int(input('Ano de nascimento: '))
anoA = datetime.datetime.today().year
idade = anoA - anoN
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
