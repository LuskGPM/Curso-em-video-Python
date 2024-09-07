sa = float(input('Salário: '))
if sa <= 1412:
    aumento = sa * 0.15
else:
    aumento = sa * 0.10
print(f'Com o aumento o novo salário será de  R${sa + aumento}.')