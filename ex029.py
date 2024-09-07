from sty import fg, bg

v = int(input('Velocidade do veículo: '))
vr = int(input('Velocidade máxima da rodovia: '))
multa50 = (vr * 0.5) + vr
multa20 = (vr * 0.2) + vr
if v > multa50:
    print('Infração ' + fg.da_red + bg.white + 'Gravissíma 3x' + fg.rs + bg.rs)
    print('Multa de R$880,41 e 5 pontos na carteira.')
elif multa50 >= v >= multa20:
    print('Infração ' + fg.li_red + 'Grave' + fg.rs)
    print('Multa de R$195,23 e 5 pontos na carteira.')
else:
    print('Velocidade compatível com a via.')
