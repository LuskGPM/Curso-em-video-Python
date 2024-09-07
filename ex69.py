c18 = ch = cm = cm20 = 0
while True:
    print('     CADASTRE UMA PESSOA     ')
    print('=='*15)
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().upper()
    while sexo not in "FM":
        sexo = input('Sexo [F/M]: ').upper().strip()
    print('=='*15)
    if idade > 18:
        c18 += 1
    if sexo in "F" and idade < 20:
        cm20 += 1
    if sexo in "M":
        ch += 1
    if sexo in "F":
        cm += 1
    sn = input('Quer continuar? [S/N]: ').strip().upper()
    print('=='*15)
    while sn not in "SN":
        sn = input('Quer continuar? [S/N]: ').strip().upper()
    if sn in "N":
        break

print(f'{c18} Pessoas tem mais de 18 anos.')
if ch > 0:
    print(f'{ch} Homens foram cadastrados.')
else:
    print('Nenhum homem foi cadastrado.')
if cm > 0:
    print(f'{cm20} Mulheres tem menos de 20 anos')
else:
    print('Nenhuma mulher foi cadastrada.')
