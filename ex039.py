import datetime

anoN = int(input('Ano que você nasceu: '))
anoA = datetime.datetime.today().year
if anoA - anoN < 18:
    print(f'Você nasceu em {anoN}, possuí {anoA - anoN} anos \ne seu alistamento será daqui a {18 - (anoA - anoN)}'
          f' anos em {(18 - (anoA - anoN)) + anoA}.')
else:
    print(f'Você nasceu em {anoN}, possuí {anoA-anoN} anos, você deveria ter se alistado a {(anoA - anoN) - 18} anos\n'
          f'seu alistamento foi em {anoA - ((anoA - anoN) - 18)}')
