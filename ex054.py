from datetime import datetime
anoA = datetime.today().year
cvelho = 0
cnovo = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu: '))
    if anoA - ano <= 18:
        cnovo += 1
    else:
        cvelho += 1
print(f'{cnovo} Pessoas são menores ou iguais a 18 anos.\n{cvelho} pessoas são maiores de 18 anos.')