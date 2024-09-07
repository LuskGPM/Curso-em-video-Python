from random import randint
nM = randint(0, 10)
print('Pensei em um número de 0 a 10\nConsegue adivinhar qual número eu pensei?')
nJ = int(input(''))
while nJ != nM:
    if nJ < nM:
        nJ = int(input('Mais um poquinho: '))
    else:
        nJ = int(input('Um pouco menos: '))
print('ACERTOOOOUUU')
