lista_valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

for i in range(3):
    for c in range(3):
        lista_valores[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))

print('='*30)
for i in range(3):
    for c in range(3):
        print(f'[{lista_valores[i][c]: ^5}]', end=' ')
        if c == 1 and lista_valores[i][c] > maior_segunda_linha:
            maior_segunda_linha = lista_valores[i][c]
        if i == 2:
            soma_terceira_coluna += lista_valores[i][c]
        if lista_valores[i][c] % 2 == 0:
            soma_pares += lista_valores[i][c]
    print()
print('='*30)

print(f'A soma dos valores pares digitados é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
