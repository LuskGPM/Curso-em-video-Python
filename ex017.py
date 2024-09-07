import math

cO = float(input('Cateto Oposto: '))
cA = float(input('Cateto Adjacente: '))
h = math.hypot(cO, cA)
print(f'Hipotenusa: {h:.1f}')
