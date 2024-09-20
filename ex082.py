lista = [

]
lista_pares = [

]
listas_impares = [

]
for c in range(5):
    numero = int(input('Digite um valor: '))
    lista.append(numero)

for i, valor_lista in enumerate(lista):
    if valor_lista % 2 == 0:
        lista_pares.append(valor_lista)
    else:
        listas_impares.append(valor_lista)

print(f'''Valores digitados: {lista}
Valores pares: {lista_pares}
Valores impares: {listas_impares}''')
