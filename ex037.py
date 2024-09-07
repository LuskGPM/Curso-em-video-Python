import sty

n = int(input('Número: '))
c = int(input('''Converter para Binário [ 1 ]
Converter para Octal [ 2 ]
Converter para Hexadecimal [ 3 ]
opção: '''))
if c == 1:
    print(f'{n} para Binário é: {bin(n)[2:]}')
elif c == 2:
    print(f'{n} para Octal é: {oct(n)[2:]}')
elif c == 3:
    print(f'{n} para Hexadecimal é: {hex(n)[2:]}')
else:
    print(sty.fg.red + 'Valor incorreto, tente novamente.')
