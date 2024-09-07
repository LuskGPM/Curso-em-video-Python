d = int(input('Distância: '))
if d > 200:
    p = d * 0.45
    print('Você irá pagar R${}'.format(p))
else:
    p = d * 0.5
    print('Você irá pagar R${}'.format(p))
