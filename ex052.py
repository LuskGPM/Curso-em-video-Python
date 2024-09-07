from sty import fg
n = int(input('Número: '))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(fg.green + f'{c}' + fg.rs, end=' ')
        count += 1
    else:
        print(fg.red + f'{c}' + fg.rs, end=' ')
if count > 2:
    en = "NÃO É PRIMO"
else:
    en = "É PRIMO"
print(f'\nO número {n} foi divisível {count} vezes.\nPor isso ele {en}.')
