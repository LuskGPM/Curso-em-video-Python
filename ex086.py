lista_valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor_horizontal = valor_vertical = 0

for i in range(3):
    for l in range(3):
        lista_valores[i][l] = int(input(f'Digite um valor para [{i}, {l}]: '))

for i in range(3):
    for l in range(3):
        print(f'[{lista_valores[i][l]: ^5}]', end=' ')
    print()
