lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 != lado2 == lado3 or lado2 != lado3 == lado1 or lado3 != lado2 == lado1:
        print('Triângulo Isósceles')
    elif lado1 != lado2 != lado3:
        print('Triângulo Escaleno')
else:
    print('Os segmentos não podem formar um triângulo')
