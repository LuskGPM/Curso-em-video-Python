frase = input('Frase: ').strip().upper().split()
nf = len(''.join(frase))
inv = ''
for c in range(nf - 1 , -1, -1):
    inv += ''.join(frase)[c]
if inv == ''.join(frase):
    print('Palíndromo')
else:
    print('Não Palíndromo')
    