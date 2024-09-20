lista_pares_impares = [[], []]

for i in range(7):
    numero = int(input(f'Digite o {i + 1}° número: '))
    if numero % 2 == 0:
        lista_pares_impares[0].append(numero)
    else:
        lista_pares_impares[1].append(numero)


lista_pares_impares[1].sort()
lista_pares_impares[0].sort()
print(f'Os valores pares digitados foram {lista_pares_impares[0]}')
print(f'os valores impares digitados foram {lista_pares_impares[1]}')
