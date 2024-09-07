s = input('Informe seu sexo: ').strip().upper()
while s[0] not in "FfMm":
    s = input('Dado inválido, por favor informe seu sexo: ')
print('Seu sexo é {}'.format(s).capitalize())
