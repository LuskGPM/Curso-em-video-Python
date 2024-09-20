from random import randint
valores_sorteados = (
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
    randint(1, 9)
)
print('Os valores sorteados foram: ', end='')
for valores in valores_sorteados:
    print(valores, end=' ')
"""
print(f'\nO maior valor sorteado foi: {sorted(valores_sorteados)[-1]}')
print(f'O menor valor sorteado foi: {sorted(valores_sorteados)[0]}')
"""
print(f'\nO maior valor sorteado foi: {max(valores_sorteados)}')
print(f'O menor valor sorteado foi: {min(valores_sorteados)}')