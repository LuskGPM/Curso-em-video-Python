import sty

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
med = (n1 + n2)/2
if med < 5.0:
    resultado = sty.fg.red + "reprovado"
elif 5.0 <= med < 7.0:
    resultado = sty.fg.li_red + "de recuperação"
else:
    resultado = sty.fg.li_green + "aprovado"
print(f'Sua média foi {med}, você está {resultado}.')
