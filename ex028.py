from sty import rs, fg
from random import randint
n = randint(0, 5)
print(fg.yellow + '-=' * 26 + fg.rs)
print(fg.li_blue + 'Pensei em um número entre 0 e 5, qual número pensei?' + fg.rs)
print(fg.yellow + "=-" * 26 + fg.rs)
n1 = int(input(fg.green + 'Número: ' + fg.rs))
if n1 == n:
    print(fg.li_blue + 'Você acertou, eu pensei em {} mesmo!'.format(n))
else:
    print(fg.li_blue + f'Você errou, eu pensei em {n}')
